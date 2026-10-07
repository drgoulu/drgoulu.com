#!/usr/bin/env python3
"""
scripts/archive_broken_links.py

Teste tous les liens externes des articles dans content/posts/ et remplace
les liens qui renvoient un code d'erreur (4xx, 5xx, timeout, DNS) ou un code
de redirection (3xx) par un lien vers https://web.archive.org à la date de
publication de l'article, en s'assurant que l'instantané retenu est le plus proche
mais bien antérieur (ou égal) à la date de rédaction.

Usage :
    python3 scripts/archive_broken_links.py [options]

Exemples :
    # Simulation sur un article précis en vérifiant l'antériorité de l'archive :
    python3 scripts/archive_broken_links.py --path content/posts/2012/dites-non-au-mouvement-perpetuel.md --dry-run

    # Traiter uniquement les articles de 2012 :
    python3 scripts/archive_broken_links.py --year 2012

    # Traiter en ignorant les simples passages de http à https si la page existe :
    python3 scripts/archive_broken_links.py --redirect-mode ignore-https --year 2012

    # Traiter l'ensemble du blog avec 20 threads parallèles :
    python3 scripts/archive_broken_links.py --workers 20
"""

import argparse
import atexit
import concurrent.futures
import html
import json
import os
import re
import sys
import threading
import time
import urllib.parse
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple

try:
    import requests
except ImportError:
    print("Erreur : le module 'requests' est requis. Installez-le avec : pip install requests")
    sys.exit(1)


# Domaines internes ou locaux à exclure des tests
INTERNAL_HOSTS = {
    "drgoulu.com",
    "www.drgoulu.com",
    "drgoulu.net",
    "www.drgoulu.net",
    "drgoulu.local",
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
}

# Domaines d'archives à ne pas tester ni ré-archiver
ARCHIVE_HOSTS = {
    "web.archive.org",
    "archive.org",
    "web-beta.archive.org",
    "archive.is",
    "archive.today",
    "archive.ph",
    "archive.li",
    "archive.vn",
    "archive.md",
}

# Domaines exclus à ne pas tester ni archiver (Quora, YouTube, etc.)
EXCLUDED_HOSTS = {
    "fr.quora.com",
    "quora.com",
    "www.quora.com",
    "www.youtube.com",
    "youtube.com",
    "m.youtube.com",
    "youtu.be",
}

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

DEFAULT_CACHE_FILE = ".link_cache.json"


def is_excluded_url(url: str) -> bool:
    """Détermine si l'URL doit être strictement ignorée (archives, Quora, YouTube)."""
    if not url:
        return True
    u_clean = url.strip()
    u_lower = u_clean.lower()

    # Vérification par préfixe ou motif textuel
    if (
        u_lower.startswith("https://web.archive.org")
        or u_lower.startswith("http://web.archive.org")
        or u_lower.startswith("https://archive.org")
        or u_lower.startswith("http://archive.org")
        or "web.archive.org" in u_lower
        or "archive.org/web" in u_lower
        or u_lower.startswith("https://fr.quora.com")
        or u_lower.startswith("http://fr.quora.com")
        or u_lower.startswith("https://www.quora.com")
        or u_lower.startswith("http://www.quora.com")
        or u_lower.startswith("https://quora.com")
        or u_lower.startswith("http://quora.com")
        or u_lower.startswith("https://www.youtube.com")
        or u_lower.startswith("http://www.youtube.com")
        or u_lower.startswith("https://youtube.com")
        or u_lower.startswith("http://youtube.com")
        or u_lower.startswith("https://youtu.be")
        or u_lower.startswith("http://youtu.be")
        or u_lower.startswith("https://m.youtube.com")
        or u_lower.startswith("http://m.youtube.com")
    ):
        return True

    try:
        parsed = urllib.parse.urlparse(u_lower)
        host = (parsed.hostname or "").lower()
        if not host:
            return True
        if host in INTERNAL_HOSTS:
            return True
        if any(host == ah or host.endswith("." + ah) for ah in ARCHIVE_HOSTS):
            return True
        if any(host == eh or host.endswith("." + eh) for eh in EXCLUDED_HOSTS):
            return True
    except Exception:
        return True

    return False


class LinkChecker:
    def __init__(
        self,
        cache_path: str = DEFAULT_CACHE_FILE,
        workers: int = 15,
        timeout: int = 8,
        redirect_mode: str = "follow",
        verify_anterior: bool = True,
        use_cache: bool = True,
        verbose: bool = False,
    ):
        self.cache_path = cache_path
        self.workers = workers
        self.timeout = timeout
        self.redirect_mode = redirect_mode  # 'all', 'ignore-https', 'follow'
        self.verify_anterior = verify_anterior
        self.use_cache = use_cache
        self.verbose = verbose

        self.cache: Dict[str, dict] = {}
        self.archive_cache: Dict[str, dict] = {}
        self.cache_dirty = False
        self.lock = threading.Lock()

        self.archive_session = requests.Session()
        self.archive_session.headers.update({"User-Agent": USER_AGENT})

        if self.use_cache and os.path.exists(self.cache_path):
            try:
                with open(self.cache_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        if "url_checks" in data or "archive_resolutions" in data:
                            self.cache = data.get("url_checks", {})
                            self.archive_cache = data.get("archive_resolutions", {})
                        else:
                            # Format simple de migration
                            self.cache = data
                            self.archive_cache = {}
            except Exception as e:
                print(f"[!] Avertissement : impossible de charger le cache ({e})")
                self.cache = {}
                self.archive_cache = {}

        atexit.register(self.save_cache)

    def save_cache(self):
        """Sauvegarde atomique et thread-safe du cache JSON."""
        if not self.use_cache:
            return

        with self.lock:
            if not self.cache_dirty:
                return
            payload = {
                "url_checks": dict(self.cache),
                "archive_resolutions": dict(self.archive_cache),
            }
            self.cache_dirty = False

        temp_path = self.cache_path + ".tmp"
        try:
            with open(temp_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
            os.replace(temp_path, self.cache_path)
        except Exception as e:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except OSError:
                    pass
            print(f"[!] Erreur lors de la sauvegarde du cache : {e}")

    @staticmethod
    def is_external_url(url: str) -> bool:
        """
        Détermine si l'URL est une URL externe à vérifier.
        Exclut immédiatement tout lien commençant par https://web.archive.org,
        https://fr.quora.com, https://www.youtube.com, etc.
        """
        if not url:
            return False

        u_clean = url.strip()
        if not (u_clean.startswith("http://") or u_clean.startswith("https://")):
            return False

        return not is_excluded_url(u_clean)

    def probe_url(self, url: str) -> dict:
        """Effectue la requête réseau réelle et stocke les caractéristiques HTTP brutes."""
        test_url = html.unescape(url)
        headers = {
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "fr,fr-FR;q=0.9,en;q=0.8",
        }

        entry = {
            "status": 0,
            "location": None,
            "final_status": 0,
            "final_url": None,
            "error": None,
            "checked_at": datetime.now().isoformat(),
        }

        try:
            # 1. Tentative HEAD sans redirection
            resp = requests.head(
                test_url,
                headers=headers,
                timeout=self.timeout,
                allow_redirects=False,
            )
            status = resp.status_code

            # Si méthode HEAD refusée, bascule vers GET léger
            if status in (403, 405):
                resp = requests.get(
                    test_url,
                    headers=headers,
                    timeout=self.timeout,
                    allow_redirects=False,
                    stream=True,
                )
                status = resp.status_code

            entry["status"] = status

            # En cas de redirection 3xx
            if 300 <= status < 400:
                loc = resp.headers.get("Location")
                if loc:
                    resolved_loc = urllib.parse.urljoin(test_url, loc)
                    entry["location"] = resolved_loc

                    # Sonde la destination finale
                    try:
                        resp_final = requests.get(
                            test_url,
                            headers=headers,
                            timeout=self.timeout,
                            allow_redirects=True,
                            stream=True,
                        )
                        entry["final_status"] = resp_final.status_code
                        entry["final_url"] = resp_final.url
                    except Exception as e_final:
                        entry["final_status"] = 0
                        entry["final_error"] = type(e_final).__name__

        except requests.exceptions.RequestException as exc:
            entry["error"] = type(exc).__name__

        return entry

    def evaluate_entry(self, url: str, entry: dict) -> Tuple[bool, str, int]:
        """
        Évalue si une URL doit être remplacée en fonction du mode de redirection choisi.
        Retourne (is_broken, reason, status).
        """
        if entry.get("error"):
            return True, f"Erreur réseau ({entry['error']})", 0

        status = entry.get("status", 0)

        # Codes d'erreurs HTTP 4xx, 5xx
        if status >= 400 or status == 0:
            return True, f"Erreur HTTP {status}", status

        # Codes 2xx (Succès sans redirection)
        if 200 <= status < 300:
            return False, f"OK ({status})", status

        # Codes 3xx (Redirections)
        if 300 <= status < 400:
            location = entry.get("location") or "inconnue"
            final_status = entry.get("final_status", 0)

            if self.redirect_mode == "all":
                return True, f"Redirection ({status} -> {location})", status

            elif self.redirect_mode == "ignore-https":
                p_orig = urllib.parse.urlparse(url)
                p_dest = urllib.parse.urlparse(location)
                same_target = (
                    p_orig.scheme == "http"
                    and p_dest.scheme == "https"
                    and p_orig.hostname == p_dest.hostname
                    and (
                        p_orig.path.rstrip("/") == p_dest.path.rstrip("/")
                        or p_dest.path == p_orig.path + "/"
                    )
                )
                if same_target and (200 <= final_status < 400):
                    return False, f"OK (HTTPS upgrade {final_status})", final_status
                return True, f"Redirection ({status} -> {location})", status

            elif self.redirect_mode == "follow":
                if 200 <= final_status < 400:
                    return False, f"OK après redirection ({final_status})", final_status
                else:
                    return True, f"Erreur après redirection ({final_status})", final_status

        return False, f"Statut {status}", status

    def get_or_probe(self, url: str) -> dict:
        """Récupère l'entrée en cache ou effectue la requête réseau."""
        if self.use_cache:
            with self.lock:
                if url in self.cache:
                    return self.cache[url]

        entry = self.probe_url(url)

        if self.use_cache:
            with self.lock:
                self.cache[url] = entry
                self.cache_dirty = True

        return entry

    def check_url(self, url: str) -> Tuple[bool, str, int]:
        """Vérifie une URL unique (utilise le cache si disponible)."""
        entry = self.get_or_probe(url)
        return self.evaluate_entry(url, entry)

    def batch_check_urls(self, urls: Set[str]) -> Dict[str, Tuple[bool, str, int]]:
        """Vérifie un lot d'URLs en parallèle."""
        results = {}
        to_probe = []

        for u in urls:
            if self.use_cache and u in self.cache:
                results[u] = self.evaluate_entry(u, self.cache[u])
            else:
                to_probe.append(u)

        if to_probe:
            print(f"[*] Test de {len(to_probe)} URL(s) externe(s) ({self.workers} workers)...")
            completed = 0
            total = len(to_probe)

            with concurrent.futures.ThreadPoolExecutor(max_workers=self.workers) as executor:
                future_to_url = {executor.submit(self.get_or_probe, u): u for u in to_probe}
                for future in concurrent.futures.as_completed(future_to_url):
                    u = future_to_url[future]
                    try:
                        entry = future.result()
                    except Exception as exc:
                        entry = {"error": type(exc).__name__, "status": 0}
                    results[u] = self.evaluate_entry(u, entry)
                    completed += 1
                    if completed % 25 == 0 or completed == total:
                        print(f"    Progression tests URL : {completed}/{total} ({completed * 100 // total}%)")
                        self.save_cache()

        self.save_cache()
        return results

    def resolve_closest_anterior_snapshot(self, url: str, target_ts: str) -> Tuple[str, bool, str]:
        """
        Résout l'instantané Wayback Machine le plus proche mais antérieur (ou égal) à target_ts.
        target_ts : format 'YYYYMMDDHHMMSS' ou 'YYYYMMDD'.
        Retourne : (archive_url, is_anterior, note)
        """
        # Normalisation en 14 caractères (fin de journée si seule la date est connue)
        full_target_ts = target_ts if len(target_ts) == 14 else target_ts[:8] + "235959"
        cache_key = f"{url}@{full_target_ts}"

        if self.use_cache:
            with self.lock:
                if cache_key in self.archive_cache:
                    c = self.archive_cache[cache_key]
                    return c["archive_url"], c["is_anterior"], c["note"]

        if not self.verify_anterior:
            arch_url = f"https://web.archive.org/web/{full_target_ts[:8]}/{url}"
            return arch_url, True, "Génération standard (non vérifiée)"

        headers = {"User-Agent": USER_AGENT}
        probe_url = f"http://web.archive.org/web/{full_target_ts}/{url}"

        for attempt in range(3):
            try:
                time.sleep(0.3)
                r = self.archive_session.head(probe_url, allow_redirects=False, timeout=self.timeout)
                location = r.headers.get("Location")

                if not location and r.status_code == 404:
                    fallback = f"https://web.archive.org/web/{full_target_ts[:8]}/{url}"
                    res = (fallback, False, "Non archivé (404)")
                    if self.use_cache:
                        with self.lock:
                            self.archive_cache[cache_key] = {"archive_url": res[0], "is_anterior": res[1], "note": res[2]}
                            self.cache_dirty = True
                    return res

                if location:
                    m = re.search(r"/web/(\d{14})/", location)
                    if m:
                        found_ts = m.group(1)

                        # Cas 1 : L'instantané est déjà antérieur ou égal
                        if found_ts <= full_target_ts:
                            clean_url = f"https://web.archive.org/web/{found_ts}/{url}"
                            res = (clean_url, True, f"Instantané antérieur le plus proche ({found_ts} <= {full_target_ts})")
                            if self.use_cache:
                                with self.lock:
                                    self.archive_cache[cache_key] = {"archive_url": res[0], "is_anterior": res[1], "note": res[2]}
                                    self.cache_dirty = True
                            return res

                        # Cas 2 : L'instantané est POSTÉRIEUR -> consulter le TimeMap
                        timemap_url = f"http://web.archive.org/web/timemap/link/{url}"
                        try:
                            time.sleep(0.3)
                            tm_resp = self.archive_session.get(timemap_url, timeout=self.timeout)
                            if tm_resp.status_code == 200:
                                mementos = re.findall(
                                    r"<https?://web\.archive\.org/web/(\d{14})/[^>]+>;\s*rel=\"[^\"]*memento",
                                    tm_resp.text,
                                )
                                anterior = [ts for ts in mementos if ts <= full_target_ts]
                                if anterior:
                                    best_ts = anterior[-1]
                                    clean_url = f"https://web.archive.org/web/{best_ts}/{url}"
                                    res = (clean_url, True, f"Ajusté au snapshot antérieur le plus proche ({best_ts} <= {full_target_ts})")
                                    if self.use_cache:
                                        with self.lock:
                                            self.archive_cache[cache_key] = {"archive_url": res[0], "is_anterior": res[1], "note": res[2]}
                                            self.cache_dirty = True
                                    return res
                                else:
                                    clean_url = f"https://web.archive.org/web/{found_ts}/{url}"
                                    res = (clean_url, False, f"Aucun antérieur existant (premier connu le {found_ts})")
                                    if self.use_cache:
                                        with self.lock:
                                            self.archive_cache[cache_key] = {"archive_url": res[0], "is_anterior": res[1], "note": res[2]}
                                            self.cache_dirty = True
                                    return res
                        except Exception:
                            pass

                        clean_url = f"https://web.archive.org/web/{found_ts}/{url}"
                        res = (clean_url, False, f"Instantané postérieur ({found_ts} > {full_target_ts})")
                        if self.use_cache:
                            with self.lock:
                                self.archive_cache[cache_key] = {"archive_url": res[0], "is_anterior": res[1], "note": res[2]}
                                self.cache_dirty = True
                        return res

                break

            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as exc:
                if attempt < 2:
                    time.sleep(1.0 * (attempt + 1))
                else:
                    fallback = f"https://web.archive.org/web/{full_target_ts[:8]}/{url}"
                    return fallback, False, f"Erreur réseau Wayback ({type(exc).__name__})"

        fallback = f"https://web.archive.org/web/{full_target_ts[:8]}/{url}"
        res = (fallback, False, "Redirection standard")
        if self.use_cache:
            with self.lock:
                self.archive_cache[cache_key] = {"archive_url": res[0], "is_anterior": res[1], "note": res[2]}
                self.cache_dirty = True
        return res




def extract_post_date(content: str, filepath: str) -> str:
    """
    Extrait la date de rédaction au format YYYYMMDDHHMMSS (14 chiffres).
    Si l'heure n'est pas spécifiée, retourne YYYYMMDD235959 (fin de journée).
    """
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            # Date complète avec heure : date: 2012-05-27T17:54:00...
            m_full = re.search(
                r"^date:\s*['\"]?(\d{4})[-/]?(\d{2})[-/]?(\d{2})[T\s](\d{2}):(\d{2}):(\d{2})",
                fm,
                re.MULTILINE,
            )
            if m_full:
                return f"{m_full.group(1)}{m_full.group(2)}{m_full.group(3)}{m_full.group(4)}{m_full.group(5)}{m_full.group(6)}"

            # Date simple : date: 2012-05-27
            m_date = re.search(r"^date:\s*['\"]?(\d{4})[-/]?(\d{2})[-/]?(\d{2})", fm, re.MULTILINE)
            if m_date:
                return f"{m_date.group(1)}{m_date.group(2)}{m_date.group(3)}235959"

            # Année seule : date: 2012
            m_year = re.search(r"^date:\s*['\"]?(\d{4})", fm, re.MULTILINE)
            if m_year:
                return f"{m_year.group(1)}1231235959"

    filename = os.path.basename(filepath)
    m_file = re.match(r"^(\d{4})-(\d{2})-(\d{2})", filename)
    if m_file:
        return f"{m_file.group(1)}{m_file.group(2)}{m_file.group(3)}235959"

    m_dir = re.search(r"/posts/(\d{4})/", filepath.replace("\\", "/"))
    if m_dir:
        return f"{m_dir.group(1)}1231235959"

    return datetime.now().strftime("%Y%m%d%H%M%S")


def find_urls_in_post(content: str) -> List[str]:
    """Extrait toutes les URLs candidates d'un contenu Markdown."""
    urls = []

    def _should_include(raw_url: str) -> bool:
        if not raw_url:
            return False
        return not is_excluded_url(raw_url)

    # Liens Markdown : [texte](url) ou [texte](url "titre") (exclut les images ![alt](src))
    for m in re.finditer(
        r"(?<!!)\[[^\]]+\]\((https?://[^\s\)\"\']+)(?:\s+[\"\'].*?[\"\'])?\)",
        content,
    ):
        if _should_include(m.group(1)):
            urls.append(m.group(1))

    # Liens autolinks Markdown : <http://...>
    for m in re.finditer(r"<((?:https?)://[^>]+)>", content):
        if _should_include(m.group(1)):
            urls.append(m.group(1))

    # Liens HTML : <a href="...">
    for m in re.finditer(r"<a\b[^>]*?\bhref=[\"\'](https?://[^\"\'\s]+)[\"\']", content):
        if _should_include(m.group(1)):
            urls.append(m.group(1))

    # Liens shortcodes Hugo : {{< figure ... link="..." >}}
    for m in re.finditer(r"\blink=[\"\'](https?://[^\"\'\s]+)[\"\']", content):
        if _should_include(m.group(1)):
            urls.append(m.group(1))

    return urls


def replace_urls_in_post(content: str, replacements: Dict[str, str]) -> str:
    """Remplace les URLs ciblées dans le contenu Markdown de manière chirurgicale."""
    if not replacements:
        return content

    # 1. Liens Markdown : [texte](URL)
    pattern_md = re.compile(
        r"((?<!\!)\[[^\]]+\])\((https?://[^\s\)\"\']+)(\s+[\"\'].*?[\"\'])?\)"
    )

    def _replace_md(m):
        prefix = m.group(1)
        url = m.group(2)
        title = m.group(3) or ""
        if url in replacements:
            return f"{prefix}({replacements[url]}{title})"
        return m.group(0)

    content = pattern_md.sub(_replace_md, content)

    # 2. Autolinks Markdown : <URL>
    pattern_auto = re.compile(r"<((?:https?)://[^>]+)>")

    def _replace_auto(m):
        url = m.group(1)
        if url in replacements:
            return f"<{replacements[url]}>"
        return m.group(0)

    content = pattern_auto.sub(_replace_auto, content)

    # 3. Liens HTML : <a href="URL">
    pattern_html = re.compile(r"(<a\b[^>]*?\bhref=[\"\'])(https?://[^\"\'\s]+)([\"\'])")

    def _replace_html(m):
        url = m.group(2)
        if url in replacements:
            return f"{m.group(1)}{replacements[url]}{m.group(3)}"
        return m.group(0)

    content = pattern_html.sub(_replace_html, content)

    # 4. Shortcodes Hugo : link="URL"
    pattern_hugo = re.compile(r"(\blink=[\"\'])(https?://[^\"\'\s]+)([\"\'])")

    def _replace_hugo(m):
        url = m.group(2)
        if url in replacements:
            return f"{m.group(1)}{replacements[url]}{m.group(3)}"
        return m.group(0)

    content = pattern_hugo.sub(_replace_hugo, content)

    return content


def get_target_files(posts_dir: str, target_path: Optional[str], target_year: Optional[str]) -> List[str]:
    """Sélectionne les fichiers Markdown à analyser."""
    if target_path:
        if os.path.isfile(target_path):
            return [target_path]
        elif os.path.isdir(target_path):
            res = []
            for root, _, files in os.walk(target_path):
                for f in files:
                    if f.endswith(".md"):
                        res.append(os.path.join(root, f))
            return sorted(res)
        else:
            print(f"[!] Erreur : chemin introuvable : {target_path}")
            return []

    files_list = []
    for root, _, files in os.walk(posts_dir):
        if target_year:
            rel = os.path.relpath(root, posts_dir).replace("\\", "/")
            if not (rel == target_year or rel.startswith(f"{target_year}/")):
                continue

        for f in files:
            if f.endswith(".md"):
                files_list.append(os.path.join(root, f))

    return sorted(files_list)


def main():
    parser = argparse.ArgumentParser(
        description="Teste les liens externes des articles et remplace les liens brisés/redirigés par web.archive.org avec vérification d'antériorité.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--path",
        type=str,
        default=None,
        help="Chemin vers un fichier .md ou un répertoire précis à traiter",
    )
    parser.add_argument(
        "--year",
        type=str,
        default=None,
        help="Filtrer les articles par année (ex: 2012)",
    )
    parser.add_argument(
        "--redirect-mode",
        choices=["all", "ignore-https", "follow"],
        default="follow",
        help=(
            "Politique pour les redirections 3xx : "
            "'follow' (par défaut) = suit les redirections et ne remplace que si la destination finale est en erreur (tolère les passages http->https et redirections valides) ; "
            "'ignore-https' = conserve le lien uniquement si redirection http vers https valide 200, remplace les autres redirections ; "
            "'all' = toute redirection est considérée brisée et remplacée par l'archive."
        ),
    )
    parser.add_argument(
        "--no-verify-anterior",
        action="store_true",
        help="Désactive la vérification réseau que le snapshot Wayback est le plus proche et antérieur à l'article",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=15,
        help="Nombre de requêtes HTTP parallèles",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=8,
        help="Délai d'attente maximum par requête en secondes",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mode simulation : affiche les remplacements sans modifier les fichiers",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limiter l'analyse aux N premiers articles",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Désactiver l'utilisation du cache local",
    )
    parser.add_argument(
        "--cache-file",
        type=str,
        default=DEFAULT_CACHE_FILE,
        help="Fichier de cache JSON",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Affichage détaillé",
    )

    args = parser.parse_args()

    # Déterminer la racine du projet
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, ".."))
    posts_dir = os.path.join(repo_root, "content", "posts")

    cache_file_path = os.path.join(repo_root, args.cache_file)

    target_path = None
    if args.path:
        target_path = os.path.abspath(args.path)

    files = get_target_files(posts_dir, target_path, args.year)
    if args.limit:
        files = files[: args.limit]

    print(f"=== Vérificateur et Archiveur de Liens Externes ===")
    print(f"Articles ciblés          : {len(files)}")
    print(f"Mode de redirection      : {args.redirect_mode}")
    print(f"Vérification antériorité : {'NON' if args.no_verify_anterior else 'OUI (snapshot <= date article)'}")
    print(f"Workers parallèles       : {args.workers}")
    print(f"Délai d'expiration       : {args.timeout}s")
    print(f"Simulation (dry-run)     : {'OUI' if args.dry_run else 'NON'}")
    print(f"Cache activé             : {'NON' if args.no_cache else cache_file_path}")
    print("-----------------------------------------------------")

    if not files:
        print("[!] Aucun article trouvé pour les critères spécifiés.")
        return

    checker = LinkChecker(
        cache_path=cache_file_path,
        workers=args.workers,
        timeout=args.timeout,
        redirect_mode=args.redirect_mode,
        verify_anterior=not args.no_verify_anterior,
        use_cache=not args.no_cache,
        verbose=args.verbose,
    )

    # 1. Étape d'extraction de tous les liens externes
    post_links: Dict[str, Tuple[str, List[str], str]] = {}
    all_external_urls: Set[str] = set()

    for fpath in files:
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
                content = fp.read()
        except Exception as e:
            print(f"[!] Erreur de lecture pour {fpath} : {e}")
            continue

        date_ts = extract_post_date(content, fpath)
        found_urls = find_urls_in_post(content)
        ext_urls = [u for u in found_urls if checker.is_external_url(u)]

        if ext_urls:
            post_links[fpath] = (date_ts, ext_urls, content)
            all_external_urls.update(ext_urls)

    print(f"[*] Total d'URLs externes uniques à tester : {len(all_external_urls)}")
    print(f"[*] Articles contenant des liens à analyser : {len(post_links)}")

    # 2. Analyse, résolution et mise à jour progressive des articles
    total_modified_files = 0
    total_replaced_links = 0
    anterior_count = 0
    non_anterior_count = 0
    processed_count = 0
    total_posts = len(post_links)
    stats_lock = threading.Lock()

    print("\n[*] Analyse et mise à jour immédiate des articles au fil de l'eau...")

    def process_single_post(item):
        nonlocal total_modified_files, total_replaced_links, anterior_count, non_anterior_count, processed_count
        fpath, (date_ts, urls, content) = item

        replacements = {}
        for u in urls:
            is_broken, reason, _ = checker.check_url(u)
            if is_broken:
                arch_url, is_anterior, note = checker.resolve_closest_anterior_snapshot(u, date_ts)
                replacements[u] = arch_url
                with stats_lock:
                    if is_anterior:
                        anterior_count += 1
                    else:
                        non_anterior_count += 1

                if args.verbose or args.dry_run:
                    rel_path = os.path.relpath(fpath, repo_root)
                    stat_icon = "[✓ Antérieur]" if is_anterior else "[! Non-antérieur]"
                    print(f"  [{rel_path}] {stat_icon}")
                    print(f"    - URL originale : {u}")
                    print(f"    - Date article  : {date_ts[:4]}-{date_ts[4:6]}-{date_ts[6:8]}")
                    print(f"    - Archive cible : {arch_url}")
                    print(f"    - Motif / Note  : {reason} | {note}")

        if replacements:
            new_content = replace_urls_in_post(content, replacements)
            if not args.dry_run:
                try:
                    with open(fpath, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                except Exception as e:
                    print(f"[!] Erreur d'écriture sur {fpath} : {e}")

            with stats_lock:
                total_modified_files += 1
                total_replaced_links += len(replacements)
                rel_path = os.path.relpath(fpath, repo_root)
                print(f"[✓ Sauvegardé {total_modified_files}] {rel_path} ({len(replacements)} lien(s) remplacé(s))")

        with stats_lock:
            processed_count += 1
            if processed_count % 25 == 0 or processed_count == total_posts:
                print(f"    Progression : {processed_count}/{total_posts} articles ({processed_count * 100 // total_posts}%) - {total_modified_files} modifiés")
                checker.save_cache()

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        list(executor.map(process_single_post, post_links.items()))

    checker.save_cache()

    print("\n================== BILAN ==================")
    print(f"Articles analysés        : {len(files)}")
    print(f"Articles modifiés        : {total_modified_files}")
    print(f"Liens remplacés          : {total_replaced_links}")
    if checker.verify_anterior:
        print(f"  - Instantanés antérieurs confirmés : {anterior_count}")
        print(f"  - Sans capture antérieure trouvée  : {non_anterior_count}")
    if args.dry_run:
        print("[!] Mode simulation : AUCUN fichier n'a été modifié sur le disque.")
    else:
        print("[+] Modifications écrites au fil de l'eau avec succès dans les fichiers Markdown.")


if __name__ == "__main__":
    main()
