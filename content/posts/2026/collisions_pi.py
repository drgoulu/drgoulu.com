#!/usr/bin/env python3
"""
Génère l'animation GIF 3D des collisions calculant Pi (billard de Galperin)
pour M = 8 (cube d'arête 2) et m = 1 (cube d'arête 1) -> 9 collisions.

Exécution :
    python3 content/posts/2026/collisions_pi.py
Sortie :
    content/posts/2026/images/collisions-pi-3d.gif
"""

import math
from pathlib import Path
import cairo
from PIL import Image

# ==============================================================================
# 1. SIMULATION PHYSIQUE EXACTE (M = 8, m = 1 -> 9 collisions)
# ==============================================================================
M = 8.0
m = 1.0
L_M = 2.0  # Arête du grand cube (M = 2^3 = 8)
L_m = 1.0  # Arête du petit cube (m = 1^3 = 1)

X_WALL = 12.2   # Position du mur de briques le long de la glissière
X_M_START = L_M  # Le cube 8 commence tout au début de la rampe (occupe [0, 2])


def simulate_collisions():
    """Calcule la liste exacte des événements (t, x_M, x_m, V, v, choc_num, type_choc).
    x_M : face avant (côté mur) du grand cube M=8 (occupe [x_M - L_M, x_M])
    x_m : face avant (côté mur) du petit cube m=1 (occupe [x_m - L_m, x_m])
    Contact entre les deux cubes : x_M == x_m - L_m
    Contact petit cube / mur     : x_m == X_WALL
    """
    d0 = 1.85              # Distance initiale entre le petit cube et le mur
    x_m = X_WALL - d0      # = 10.35 (occupe [9.35, 10.35])
    x_M = X_M_START        # = 2.00 (occupe [0.00, 2.00], tout au début de la rampe)
    V = 1.0                # Vitesse initiale de M vers le mur
    v = 0.0                # m initialement immobile
    t = 0.0
    choc = 0

    events = [(t, x_M, x_m, V, v, choc, None)]

    while True:
        dt_cc = ((x_m - L_m) - x_M) / (V - v) if V > v else float("inf")
        dt_cw = (X_WALL - x_m) / v if v > 0 else float("inf")

        if dt_cc == float("inf") and dt_cw == float("inf"):
            break

        if dt_cc <= dt_cw:
            t += dt_cc
            x_M += V * dt_cc
            x_m += v * dt_cc
            x_M = x_m - L_m
            V_new = ((M - m) * V + 2 * m * v) / (M + m)
            v_new = (2 * M * V + (m - M) * v) / (M + m)
            V, v = V_new, v_new
            choc += 1
            events.append((t, x_M, x_m, V, v, choc, "cubes"))
        else:
            t += dt_cw
            x_M += V * dt_cw
            x_m = X_WALL
            v = -v
            choc += 1
            events.append((t, x_M, x_m, V, v, choc, "wall"))

    # Prolongation après le 9e choc jusqu'au retour exact du cube 8 au début de la rampe (x_M = X_M_START)
    dt_outro = (X_M_START - x_M) / V  # V < 0 et x_M > X_M_START
    events.append((
        t + dt_outro,
        X_M_START,
        x_m + v * dt_outro,
        V,
        v,
        choc,
        None,
    ))
    return events


def state_at_time(events, t):
    """Évalue l'état physique exact à l'instant t (temps physique uniforme)."""
    for i in range(len(events) - 1):
        t0, xM0, xm0, V0, v0, c0, _ = events[i]
        t1, xM1, xm1, V1, v1, c1, _ = events[i + 1]
        if t <= t1 or i == len(events) - 2:
            dt = max(0.0, min(t - t0, t1 - t0))
            return {
                "t": t,
                "x_M": xM0 + V0 * dt,
                "x_m": xm0 + v0 * dt,
                "V": V0,
                "v": v0,
                "choc": c0,
                "flash": None,
            }
    t_end, xM_end, xm_end, V_end, v_end, c_end, _ = events[-1]
    return {
        "t": t_end,
        "x_M": xM_end,
        "x_m": xm_end,
        "V": V_end,
        "v": v_end,
        "choc": c_end,
        "flash": None,
    }


def build_timeline(events):
    """Échantillonne la trajectoire avec un pas de temps physique CONSTANT dt
    pour que les vitesses à l'écran soient strictement proportionnelles aux vitesses réelles,
    tout en calant la frame la plus proche de chaque choc sur le contact exact."""
    t_total = events[-1][0]
    n_frames = 150
    dt = t_total / float(n_frames - 1)

    frames_data = [state_at_time(events, k * dt) for k in range(n_frames)]

    # Pour chaque choc 1..9, caler la frame la plus proche sur l'instant exact du contact
    # afin que le rebond contre le mur ou contre le cube soit toujours visuellement net
    for idx_ev in range(1, 10):
        t_ev, xM_ev, xm_ev, V_ev, v_ev, choc_ev, kind_ev = events[idx_ev]
        k_best = round(t_ev / dt)
        k_best = max(0, min(n_frames - 1, k_best))
        flash_pos = xM_ev if kind_ev == "cubes" else X_WALL
        frames_data[k_best] = {
            "t": t_ev,
            "x_M": xM_ev,
            "x_m": xm_ev,
            "V": V_ev,
            "v": v_ev,
            "choc": choc_ev,
            "flash": (kind_ev, flash_pos, 1.0),
        }
        if k_best + 1 < n_frames and frames_data[k_best + 1]["flash"] is None:
            frames_data[k_best + 1]["flash"] = (kind_ev, flash_pos, 0.55)
            frames_data[k_best + 1]["choc"] = max(frames_data[k_best + 1]["choc"], choc_ev)

    # S'assurer que le compteur de chocs est monotone croissant
    max_c = 0
    for f in frames_data:
        if f["choc"] < max_c:
            f["choc"] = max_c
        else:
            max_c = f["choc"]

    return frames_data


# ==============================================================================
# 2. PROJECTION 3D PERSPECTIVE (fidèle à mathematics-08-00509-g002.png)
# ==============================================================================
WIDTH, HEIGHT = 900, 480


def project(x, y, z):
    """Projette un point 3D (x, y, z) en coordonnées écran (u, v)."""
    persp = 1.0 / (1.0 + 0.022 * x - 0.008 * y)
    scale = 51.5 * persp

    u0, v0 = 112.0, 412.0

    ux, vx = 0.90, -0.40  # Axe x : monte vers la droite
    uy, vy = 0.34, 0.15   # Axe y : transversal vers l'avant-droite
    uz, vz = 0.0, -0.96   # Axe z : vertical vers le haut

    u = u0 + scale * (ux * x + uy * y + uz * z)
    v = v0 + scale * (vx * x + vy * y + vz * z)
    return u, v


def draw_polygon(ctx, pts_3d, fill_rgb, stroke_rgb=(0.14, 0.12, 0.13), line_width=1.6):
    pts_2d = [project(px, py, pz) for (px, py, pz) in pts_3d]
    ctx.new_path()
    ctx.move_to(*pts_2d[0])
    for pt in pts_2d[1:]:
        ctx.line_to(*pt)
    ctx.close_path()
    if fill_rgb is not None:
        ctx.set_source_rgb(*fill_rgb)
        if stroke_rgb is not None:
            ctx.fill_preserve()
        else:
            ctx.fill()
    if stroke_rgb is not None:
        ctx.set_source_rgb(*stroke_rgb)
        ctx.set_line_width(line_width)
        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        ctx.stroke()


def draw_box(ctx, x0, x1, y0, y1, z0, z1, colors, stroke_rgb=(0.14, 0.12, 0.13), line_width=1.6):
    """Dessine un parallélépipède 3D [x0, x1] x [y0, y1] x [z0, z1]."""
    c_top, c_side, c_front = colors
    face_front = [(x0, y0, z0), (x0, y1, z0), (x0, y1, z1), (x0, y0, z1)]
    face_side = [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)]
    face_top = [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]

    draw_polygon(ctx, face_front, c_front, stroke_rgb, line_width)
    draw_polygon(ctx, face_side, c_side, stroke_rgb, line_width)
    draw_polygon(ctx, face_top, c_top, stroke_rgb, line_width)


# ==============================================================================
# 3. MUR DE BRIQUES, GLISSIÈRE 3D, CUBES ET ESPACE DE PHASE
# ==============================================================================
def draw_brick_wall(ctx):
    """Dessine le mur de briques en haut à droite, fidèle à mathematics-08-00509-g002.png."""
    brick_palette = [
        (0.73, 0.33, 0.14),
        (0.78, 0.38, 0.16),
        (0.62, 0.35, 0.23),
        (0.84, 0.55, 0.39),
        (0.75, 0.35, 0.15),
    ]
    rows = 5
    brick_h = 0.72
    brick_w = 2.75
    gap_y = 0.28
    gap_z = 0.14
    wall_x0 = X_WALL
    wall_x1 = X_WALL + 0.35

    for r in range(rows):
        z0 = -0.35 + r * (brick_h + gap_z)
        z1 = z0 + brick_h
        offset_y = 0.80 if (r % 2 == 1) else -0.45
        for c in range(3):
            y0 = -4.60 + offset_y + c * (brick_w + gap_y)
            y1 = y0 + brick_w
            if r == 0 and c == 0:
                continue
            base = brick_palette[(r * 3 + c) % len(brick_palette)]
            top_c = tuple(min(1.0, ch * 1.12) for ch in base)
            side_c = tuple(max(0.0, ch * 0.80) for ch in base)
            draw_box(
                ctx,
                wall_x0,
                wall_x1,
                y0,
                y1,
                z0,
                z1,
                (top_c, side_c, base),
                stroke_rgb=(0.52, 0.24, 0.10),
                line_width=1.0,
            )


def draw_channel_back_and_floor(ctx):
    """Dessine la paroi arrière et le fond de la glissière 3D."""
    x_start, x_end = 0.0, X_WALL
    y_in = 1.02
    y_out = 1.26
    z_floor = 0.0
    z_under = -0.24
    z_back_rim = 0.72

    draw_box(
        ctx,
        x_start,
        x_end,
        -y_out,
        -y_in,
        z_under,
        z_back_rim,
        ((0.84, 0.79, 0.64), (0.69, 0.59, 0.46), (0.78, 0.73, 0.58)),
        stroke_rgb=(0.14, 0.12, 0.13),
        line_width=1.5,
    )
    inner_back = [
        (x_start, -y_in, z_floor),
        (x_end, -y_in, z_floor),
        (x_end, -y_in, z_back_rim),
        (x_start, -y_in, z_back_rim),
    ]
    draw_polygon(ctx, inner_back, (0.72, 0.63, 0.50), (0.14, 0.12, 0.13), 1.4)

    floor_poly = [
        (x_start, -y_in, z_floor),
        (x_end, -y_in, z_floor),
        (x_end, y_in, z_floor),
        (x_start, y_in, z_floor),
    ]
    draw_polygon(ctx, floor_poly, (0.81, 0.74, 0.60), (0.14, 0.12, 0.13), 1.4)

    under_front = [
        (x_start, -y_in, z_under),
        (x_start, y_in, z_under),
        (x_start, y_in, z_floor),
        (x_start, -y_in, z_floor),
    ]
    draw_polygon(ctx, under_front, (0.78, 0.73, 0.58), (0.14, 0.12, 0.13), 1.4)

    ctx.set_source_rgba(0.55, 0.47, 0.36, 0.40)
    ctx.set_line_width(1.0)
    for gx in range(1, 12):
        u1, v1 = project(gx, -y_in, 0.01)
        u2, v2 = project(gx, y_in, 0.01)
        ctx.move_to(u1, v1)
        ctx.line_to(u2, v2)
        ctx.stroke()


def draw_channel_front_rim(ctx):
    """Dessine le rebord avant bas de la glissière."""
    x_start, x_end = 0.0, X_WALL
    y_in = 1.02
    y_out = 1.26
    z_under = -0.24
    z_front_rim = 0.34

    draw_box(
        ctx,
        x_start,
        x_end,
        y_in,
        y_out,
        z_under,
        z_front_rim,
        ((0.85, 0.80, 0.65), (0.67, 0.57, 0.45), (0.78, 0.73, 0.58)),
        stroke_rgb=(0.14, 0.12, 0.13),
        line_width=1.5,
    )


def draw_velocity_arrow(ctx, x_start, y_pos, z_pos, vel, scale_v=0.85):
    """Dessine une flèche de vitesse 3D le long de l'axe x."""
    if abs(vel) < 0.04:
        return
    dx = math.copysign(max(0.45, min(1.80, abs(vel) * scale_v)), vel)
    x_end = x_start + dx

    u1, v1 = project(x_start, y_pos, z_pos)
    u2, v2 = project(x_end, y_pos, z_pos)

    ctx.set_source_rgba(1.0, 1.0, 1.0, 0.75)
    ctx.set_line_width(4.8)
    ctx.move_to(u1, v1)
    ctx.line_to(u2, v2)
    ctx.stroke()

    ctx.set_source_rgb(0.12, 0.12, 0.13)
    ctx.set_line_width(2.4)
    ctx.move_to(u1, v1)
    ctx.line_to(u2, v2)
    ctx.stroke()

    angle = math.atan2(v2 - v1, u2 - u1)
    head_len = 11.0
    head_ang = 0.42
    ctx.new_path()
    ctx.move_to(u2, v2)
    ctx.line_to(
        u2 - head_len * math.cos(angle - head_ang),
        v2 - head_len * math.sin(angle - head_ang),
    )
    ctx.line_to(
        u2 - 0.72 * head_len * math.cos(angle),
        v2 - 0.72 * head_len * math.sin(angle),
    )
    ctx.line_to(
        u2 - head_len * math.cos(angle + head_ang),
        v2 - head_len * math.sin(angle + head_ang),
    )
    ctx.close_path()
    ctx.fill()


def draw_cubes(ctx, state):
    """Dessine le petit cube (m=1) et le grand cube (M=8) sans légendes textuelles au-dessus."""
    x_M = state["x_M"]
    x_m = state["x_m"]
    V = state["V"]
    v = state["v"]

    shadow_m = [
        (x_m - L_m, 0.0, 0.01),
        (x_m, 0.0, 0.01),
        (x_m, 1.0, 0.01),
        (x_m - L_m, 1.0, 0.01),
    ]
    draw_polygon(ctx, shadow_m, (0.64, 0.57, 0.45), None)

    shadow_M = [
        (x_M - L_M, -1.0, 0.01),
        (x_M, -1.0, 0.01),
        (x_M, 1.0, 0.01),
        (x_M - L_M, 1.0, 0.01),
    ]
    draw_polygon(ctx, shadow_M, (0.64, 0.57, 0.45), None)

    # 1. Petit cube m = 1 (arête 1.0, y in [0.0, 1.0])
    draw_box(
        ctx,
        x_m - L_m,
        x_m,
        0.0,
        1.0,
        0.0,
        L_m,
        ((0.99, 0.99, 1.0), (0.86, 0.90, 0.95), (0.93, 0.96, 0.99)),
        stroke_rgb=(0.14, 0.12, 0.13),
        line_width=1.8,
    )
    um_face, vm_face = project(x_m - 0.5 * L_m, 1.0, 0.54 * L_m)
    ctx.select_font_face("Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(16)
    ctx.set_source_rgb(0.18, 0.23, 0.30)
    ext = ctx.text_extents("1")
    ctx.move_to(um_face - ext.width / 2, vm_face + ext.height / 2)
    ctx.show_text("1")

    # 2. Grand cube M = 8 (arête 2.0, y in [-1.0, 1.0])
    draw_box(
        ctx,
        x_M - L_M,
        x_M,
        -1.0,
        1.0,
        0.0,
        L_M,
        ((0.74, 0.76, 0.79), (0.50, 0.53, 0.57), (0.61, 0.64, 0.68)),
        stroke_rgb=(0.14, 0.12, 0.13),
        line_width=2.0,
    )
    uM_face, vM_face = project(x_M - 0.5 * L_M, 1.0, 0.52 * L_M)
    ctx.select_font_face("Serif", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(27)
    ctx.set_source_rgb(0.96, 0.97, 0.99)
    ext = ctx.text_extents("8")
    ctx.move_to(uM_face - ext.width / 2, vM_face + ext.height / 2)
    ctx.show_text("8")

    # Flash d'impact sur l'arête de contact
    if state["flash"] is not None:
        kind, fx, intensity = state["flash"]
        uf, vf = project(fx, 1.0 if kind == "cubes" else 0.5, 0.65)
        rad = 22.0 * (1.25 - 0.4 * intensity)
        pat = cairo.RadialGradient(uf, vf, 2.0, uf, vf, rad)
        pat.add_color_stop_rgba(0.0, 1.0, 0.96, 0.35, 0.95 * intensity)
        pat.add_color_stop_rgba(0.55, 1.0, 0.48, 0.05, 0.75 * intensity)
        pat.add_color_stop_rgba(1.0, 1.0, 0.2, 0.0, 0.0)
        ctx.new_path()
        ctx.set_source(pat)
        ctx.arc(uf, vf, rad, 0, 2 * math.pi)
        ctx.fill()

    # Flèches de vitesse au-dessus des cubes (sans texte M=8,V ni m=1,v)
    draw_velocity_arrow(ctx, x_M - 0.5 * L_M, 0.0, L_M + 0.25, V, scale_v=0.95)
    draw_velocity_arrow(ctx, x_m - 0.5 * L_m, 0.5, L_m + 0.25, v, scale_v=0.55)


def draw_hud_and_phase_circle(ctx, state, events):
    """Affiche en haut à gauche le compteur de chocs et le diagramme dans l'espace de phase."""
    choc = state["choc"]

    # 1. Compteur de collisions
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(24)
    ctx.set_source_rgb(0.15, 0.18, 0.24)
    ctx.move_to(28, 40)
    ctx.show_text(f"Collisions : {choc} / 9")

    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(13.5)
    ctx.set_source_rgb(0.38, 0.42, 0.48)
    ctx.move_to(28, 61)
    ctx.show_text("M = 8 (cube 2×2×2),  m = 1 (cube 1×1×1)")

    # 2. Cercle de conservation d'énergie dans l'espace des phases (W = √M·V, w = √m·v)
    cx, cy = 112.0, 152.0
    radius = 62.0
    r_energy = math.sqrt(M) * 1.0

    # Axes W et w
    ctx.set_source_rgb(0.25, 0.25, 0.28)
    ctx.set_line_width(1.3)
    ctx.move_to(cx - radius - 16, cy)
    ctx.line_to(cx + radius + 18, cy)
    ctx.move_to(cx, cy + radius + 14)
    ctx.line_to(cx, cy - radius - 16)
    ctx.stroke()

    # Légendes des axes avec le symbole racine carrée (police DejaVu Sans)
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_OBLIQUE, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(12.5)
    ctx.move_to(cx + radius + 5, cy + 14)
    ctx.show_text("√M·V")
    ctx.move_to(cx + 6, cy - radius - 5)
    ctx.show_text("√m·v")

    # Cercle d'énergie cinétique constante
    ctx.new_path()
    ctx.set_source_rgba(0.20, 0.35, 0.85, 0.28)
    ctx.set_line_width(1.5)
    ctx.arc(cx, cy, radius, 0, 2 * math.pi)
    ctx.stroke()

    # Coordonnées des états 0..9 sur le cercle
    pts_circle = []
    for k in range(10):
        _, _, _, Vk, vk, _, _ = events[k]
        px = cx + (math.sqrt(M) * Vk / r_energy) * radius
        py = cy - (math.sqrt(m) * vk / r_energy) * radius
        pts_circle.append((px, py))

    # Cordes bleues des rebonds effectués
    if choc >= 1:
        ctx.set_source_rgb(0.05, 0.18, 0.92)
        ctx.set_line_width(1.9)
        ctx.move_to(*pts_circle[0])
        for k in range(1, choc + 1):
            ctx.line_to(*pts_circle[k])
        ctx.stroke()

    # Points 0..choc sur le cercle
    ctx.select_font_face("DejaVu Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    ctx.set_font_size(11.5)
    for k in range(choc + 1):
        px, py = pts_circle[k]
        r_dot = 5.2 if k == choc else 3.8
        ctx.new_path()
        ctx.set_source_rgb(0.95, 0.12, 0.08)
        ctx.arc(px, py, r_dot, 0, 2 * math.pi)
        ctx.fill()
        ctx.new_path()
        ctx.set_source_rgb(1.0, 0.85, 0.85)
        ctx.arc(px - 1.2, py - 1.2, r_dot * 0.35, 0, 2 * math.pi)
        ctx.fill()

        ang = math.atan2(py - cy, px - cx)
        lx = cx + (radius + 13) * math.cos(ang) - 4
        ly = cy + (radius + 13) * math.sin(ang) + 4
        ctx.set_source_rgb(0.05, 0.18, 0.88)
        ctx.move_to(lx, ly)
        ctx.show_text(str(k))


def render_frame(state, events):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.set_source_rgb(1.0, 1.0, 1.0)
    ctx.paint()

    draw_brick_wall(ctx)
    draw_channel_back_and_floor(ctx)
    draw_cubes(ctx, state)
    draw_channel_front_rim(ctx)
    draw_hud_and_phase_circle(ctx, state, events)

    buf = surface.get_data()
    img = Image.frombuffer("RGBA", (WIDTH, HEIGHT), buf, "raw", "BGRA", 0, 1).convert("RGB")
    return img


def main():
    events = simulate_collisions()
    frames_data = build_timeline(events)

    pil_frames = [render_frame(state, events) for state in frames_data]

    out_dir = Path(__file__).resolve().parent / "images"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_gif = out_dir / "collisions-pi-3d.gif"

    # Palette globale unique pour permettre l'optimisation delta inter-trames du GIF
    master_pal = pil_frames[len(pil_frames) // 2].quantize(
        colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE
    )
    quantized = [
        im.quantize(palette=master_pal, dither=Image.Dither.NONE) for im in pil_frames
    ]
    quantized[0].save(
        out_gif,
        save_all=True,
        append_images=quantized[1:],
        duration=45,  # ~22 fps
        loop=0,
        optimize=True,
    )
    print(f"GIF généré : {out_gif} ({len(pil_frames)} frames, {out_gif.stat().st_size / 1024:.1f} Ko)")


if __name__ == "__main__":
    main()
