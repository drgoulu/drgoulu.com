#!/usr/bin/env python3
"""
delete_github_artifacts.py
Deletes all GitHub Actions artifacts for drgoulu/drgoulu.com via GitHub REST API.
"""

import sys
import os
import re
import json
import urllib.request
import urllib.error

REPO = "drgoulu/drgoulu.com"

def get_token():
    # 1. Environment variable
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        return token.strip()
    
    # 2. Check ~/.git-credentials
    git_cred = os.path.expanduser("~/.git-credentials")
    if os.path.exists(git_cred):
        with open(git_cred, "r", encoding="utf-8") as f:
            for line in f:
                if "github.com" in line:
                    # format: https://user:token@github.com
                    m = re.search(r'https?://[^:]+:([^@]+)@github\.com', line)
                    if m:
                        return m.group(1).strip()
    return None

def api_request(url, token, method="GET"):
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "GitHub-Artifact-Cleaner/1.0"
        },
        method=method
    )
    try:
        with urllib.request.urlopen(req) as resp:
            if method == "DELETE":
                return resp.status, None
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        return e.code, body

def main():
    import re
    token = sys.argv[1] if len(sys.argv) > 1 else get_token()
    if not token:
        print("Error: No GitHub token provided or found in environment / ~/.git-credentials.")
        print("Usage: python3 delete_github_artifacts.py <token>")
        sys.exit(1)

    print(f"Connecting to GitHub API for repository '{REPO}'...")
    total_deleted = 0

    while True:
        url = f"https://api.github.com/repos/{REPO}/actions/artifacts?per_page=100"
        status, data = api_request(url, token)

        if status != 200:
            print(f"Error {status} when listing artifacts:")
            print(data)
            sys.exit(1)

        artifacts = data.get("artifacts", [])
        total_count = data.get("total_count", 0)
        print(f"Found {total_count} artifact(s) on GitHub.")

        if not artifacts:
            break

        for art in artifacts:
            art_id = art["id"]
            art_name = art.get("name", "unnamed")
            art_size = art.get("size_in_bytes", 0)
            print(f"Deleting artifact {art_id} ('{art_name}', {art_size:,} bytes)...", end="", flush=True)

            del_url = f"https://api.github.com/repos/{REPO}/actions/artifacts/{art_id}"
            del_status, del_body = api_request(del_url, token, method="DELETE")

            if del_status in (204, 200):
                print(" OK")
                total_deleted += 1
            else:
                print(f" FAILED ({del_status}): {del_body}")

    print(f"\nDone. Successfully deleted {total_deleted} artifact(s).")

if __name__ == "__main__":
    main()
