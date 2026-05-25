#!/usr/bin/env python3
# Build script that assembles index.html from the data + templates below.
# Run once after editing TEMPLATES / STAMPS. Output: /home/user/DrawGame/index.html

import json, os, sys, textwrap

ROOT = '/home/user/DrawGame'

# ============================================================================
# 50 coloring templates (key, display name, category, svg-body)
# ============================================================================
# Categories: animal, ocean, fantasy, vehicle, nature, food, other
TEMPLATES = []  # filled by add() below

def add(key, name, cat, svg):
    TEMPLATES.append((key, name, cat, svg.strip()))

# Common stroke wrapper helper for readability in this file:
def W(inner):
    return '<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">\n' + textwrap.dedent(inner).strip() + '\n</g>'

# ============================================================================
# 30 stamps (key, display name, viewBox, svg-body)
# ============================================================================
STAMPS = []
def stamp(key, name, vb, svg, cat='thing'):
    STAMPS.append((key, name, vb, svg.strip(), cat))

# ============================================================================
# Categories
# ============================================================================
CATEGORIES = [
    ('animal',   '🐾 动物'),
    ('ocean',    '🌊 海洋'),
    ('bug',      '🐦 鸟和昆虫'),
    ('people',   '👦 小人'),
    ('fantasy',  '🦕 童话奇幻'),
    ('vehicle',  '🚗 交通工具'),
    ('building', '🏡 房屋建筑'),
    ('nature',   '🌸 自然'),
    ('food',     '🍰 食物'),
    ('other',    '🎉 节日和其他'),
]

STAMP_CATEGORIES = [
    ('people',  '👦 小人'),
    ('nature',  '🌳 自然'),
    ('animal',  '🐶 小动物'),
    ('thing',   '⭐ 装饰'),
    ('weather', '☀️ 天气'),
]

# ============================================================================
# Fill patterns
# ============================================================================
# Each pattern is an SVG <pattern> definition. Filled with current accent color
# at fill time via a copy-and-recolor trick. We use placeholder __FG__ for the
# foreground color and __BG__ for background (transparent → white).
PATTERNS = [
    ('solid',     '纯色',   None),
    ('dots',      '小圆点', '<pattern id="pat-dots" patternUnits="userSpaceOnUse" width="14" height="14"><rect width="14" height="14" fill="__BG__"/><circle cx="7" cy="7" r="2.5" fill="__FG__"/></pattern>'),
    ('bigdots',   '大圆点', '<pattern id="pat-bigdots" patternUnits="userSpaceOnUse" width="20" height="20"><rect width="20" height="20" fill="__BG__"/><circle cx="10" cy="10" r="5" fill="__FG__"/></pattern>'),
    ('stripes',   '斜条纹', '<pattern id="pat-stripes" patternUnits="userSpaceOnUse" width="12" height="12" patternTransform="rotate(45)"><rect width="12" height="12" fill="__BG__"/><rect x="0" y="0" width="6" height="12" fill="__FG__"/></pattern>'),
    ('hstripes',  '横条纹', '<pattern id="pat-hstripes" patternUnits="userSpaceOnUse" width="10" height="10"><rect width="10" height="10" fill="__BG__"/><rect x="0" y="0" width="10" height="5" fill="__FG__"/></pattern>'),
    ('grid',      '网格',   '<pattern id="pat-grid" patternUnits="userSpaceOnUse" width="14" height="14"><rect width="14" height="14" fill="__BG__"/><path d="M0 0 H14 M0 0 V14" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
    ('plaid',     '格子',   '<pattern id="pat-plaid" patternUnits="userSpaceOnUse" width="20" height="20"><rect width="20" height="20" fill="__BG__"/><rect x="0" y="0" width="20" height="6" fill="__FG__" opacity="0.5"/><rect x="0" y="0" width="6" height="20" fill="__FG__" opacity="0.5"/></pattern>'),
    ('zigzag',    '锯齿',   '<pattern id="pat-zigzag" patternUnits="userSpaceOnUse" width="16" height="10"><rect width="16" height="10" fill="__BG__"/><path d="M0 8 L4 2 L8 8 L12 2 L16 8" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
    ('chevron',   'V 形',   '<pattern id="pat-chevron" patternUnits="userSpaceOnUse" width="20" height="10"><rect width="20" height="10" fill="__BG__"/><path d="M0 0 L10 8 L20 0" stroke="__FG__" stroke-width="2.5" fill="none"/></pattern>'),
    ('hearts',    '小爱心', '<pattern id="pat-hearts" patternUnits="userSpaceOnUse" width="18" height="18"><rect width="18" height="18" fill="__BG__"/><path d="M9 14 Q3 9 6 5 Q9 4 9 7 Q9 4 12 5 Q15 9 9 14 Z" fill="__FG__"/></pattern>'),
    ('stars',     '小星星', '<pattern id="pat-stars" patternUnits="userSpaceOnUse" width="20" height="20"><rect width="20" height="20" fill="__BG__"/><path d="M10 3 L12 8 L17 8 L13 11 L14 16 L10 13 L6 16 L7 11 L3 8 L8 8 Z" fill="__FG__"/></pattern>'),
    ('triangles', '三角形', '<pattern id="pat-triangles" patternUnits="userSpaceOnUse" width="16" height="14"><rect width="16" height="14" fill="__BG__"/><path d="M8 2 L14 12 L2 12 Z" fill="__FG__"/></pattern>'),
    ('bricks',    '砖块',   '<pattern id="pat-bricks" patternUnits="userSpaceOnUse" width="24" height="14"><rect width="24" height="14" fill="__BG__"/><rect x="0" y="0" width="11" height="6" fill="none" stroke="__FG__" stroke-width="1.5"/><rect x="13" y="0" width="11" height="6" fill="none" stroke="__FG__" stroke-width="1.5"/><rect x="6" y="8" width="11" height="6" fill="none" stroke="__FG__" stroke-width="1.5"/></pattern>'),
    ('cross',     '十字',   '<pattern id="pat-cross" patternUnits="userSpaceOnUse" width="16" height="16"><rect width="16" height="16" fill="__BG__"/><path d="M8 3 V13 M3 8 H13" stroke="__FG__" stroke-width="2.5"/></pattern>'),
    ('scales',    '鱼鳞',   '<pattern id="pat-scales" patternUnits="userSpaceOnUse" width="14" height="10"><rect width="14" height="10" fill="__BG__"/><path d="M-1 10 A8 8 0 0 1 15 10" stroke="__FG__" stroke-width="2" fill="none"/><path d="M7 10 A8 8 0 0 1 23 10" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
    ('waves',     '波浪',   '<pattern id="pat-waves" patternUnits="userSpaceOnUse" width="20" height="10"><rect width="20" height="10" fill="__BG__"/><path d="M0 5 Q5 0 10 5 Q15 10 20 5" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
    ('bubbles',   '泡泡',   '<pattern id="pat-bubbles" patternUnits="userSpaceOnUse" width="24" height="24"><rect width="24" height="24" fill="__BG__"/><circle cx="6" cy="6" r="3" fill="none" stroke="__FG__" stroke-width="1.5"/><circle cx="18" cy="10" r="4.5" fill="none" stroke="__FG__" stroke-width="1.5"/><circle cx="10" cy="20" r="2.5" fill="none" stroke="__FG__" stroke-width="1.5"/></pattern>'),
    ('flowers',   '小花',   '<pattern id="pat-flowers" patternUnits="userSpaceOnUse" width="22" height="22"><rect width="22" height="22" fill="__BG__"/><circle cx="11" cy="6" r="2.5" fill="__FG__"/><circle cx="16" cy="11" r="2.5" fill="__FG__"/><circle cx="11" cy="16" r="2.5" fill="__FG__"/><circle cx="6" cy="11" r="2.5" fill="__FG__"/><circle cx="11" cy="11" r="2" fill="__FG__"/></pattern>'),
    ('leopard',   '豹纹',   '<pattern id="pat-leopard" patternUnits="userSpaceOnUse" width="20" height="20"><rect width="20" height="20" fill="__BG__"/><ellipse cx="6" cy="6" rx="3" ry="2" fill="__FG__"/><ellipse cx="14" cy="14" rx="3" ry="2.5" fill="__FG__"/><circle cx="14" cy="5" r="1.5" fill="__FG__"/><circle cx="4" cy="15" r="1.5" fill="__FG__"/></pattern>'),
    ('arrows',    '箭头',   '<pattern id="pat-arrows" patternUnits="userSpaceOnUse" width="16" height="16"><rect width="16" height="16" fill="__BG__"/><path d="M3 8 L11 8 M8 5 L11 8 L8 11" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
]

# ============================================================================
# Color palette (kid-friendly)
# ============================================================================
PALETTE = [
    # Warm reds / pinks
    '#ff3b30','#e0153a','#ff2d92','#ffb6d9','#ff7eb9',
    # Oranges / browns
    '#ff9500','#ffd1a3','#cc7a00','#a0522d','#5a3a22',
    # Yellows / creams
    '#ffcc00','#fff3a0','#ffe66b','#f5e6cb','#d4a017',
    # Greens
    '#34c759','#b8e0a3','#2a9d3f','#185a2d','#7ed957',
    # Cyans / teals
    '#00c7be','#a5d8ff','#4ab3ff','#0a84ff','#2a6db0',
    # Purples / violets
    '#5856d6','#af52de','#d4b3ff','#7c3aed','#3d1e6d',
    # Neutrals
    '#ffffff','#e3e7ed','#8e8e93','#4a4a4a','#1a1a1a',
]

# Below this point: write_html() composes everything into the final file.
# All templates/stamps must be filled in before write_html() runs.

# =============================================================================
# Populate templates  (filled by separate edits below this block)
# =============================================================================

# Templates and stamps live in their own files for clarity.
import templates as _templates_mod
import stamps    as _stamps_mod
TEMPLATES.extend(_templates_mod.TEMPLATES)
STAMPS.extend(_stamps_mod.STAMPS)
assert len(TEMPLATES) == 100
assert len(STAMPS) == 30
# =============================================================================
# Populate stamps
# =============================================================================



# ============================================================================
# HTML / CSS / JS templates (Python strings, $-substituted later)
# ============================================================================

HTML_HEAD_CSS = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover" />
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
<title>卡通画图填色</title>
<style>
  :root {
    --accent: #5b8def;
    --accent-2: #b794f4;
    --accent-3: #ff9a76;
    --accent-dark: #2a5cb0;
    --bg-1: #fff5e1;
    --bg-2: #ffe7f0;
    --panel: #ffffff;
    --shadow: 0 6px 18px rgba(60,40,100,.10);
    --shadow-deep: 0 8px 24px rgba(60,40,100,.18);
    --radius: 22px;
    --hit: 56px;   /* min touch target */
    --grad-header: linear-gradient(135deg, #5b8def 0%, #b794f4 50%, #ff9a76 100%);
    --grad-button: linear-gradient(180deg, rgba(255,255,255,.28) 0%, rgba(255,255,255,.12) 100%);
  }
  * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  html, body {
    margin: 0; padding: 0; height: 100%;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Rounded", "PingFang SC", "Hiragino Sans GB", "Helvetica Neue", system-ui, sans-serif;
    background:
      radial-gradient(at 18% 12%, rgba(255,180,206,.45), transparent 40%),
      radial-gradient(at 82% 88%, rgba(170,210,255,.5), transparent 45%),
      linear-gradient(180deg, var(--bg-1), var(--bg-2));
    background-attachment: fixed;
    overscroll-behavior: none;
    touch-action: manipulation;
    user-select: none; -webkit-user-select: none;
    color: #2c2640;
  }
  body { display: flex; flex-direction: column; height: 100dvh; }

  /* Top bar — its background extends into the iPhone notch area */
  header {
    display: flex; align-items: center; gap: 8px;
    padding: calc(8px + env(safe-area-inset-top)) calc(12px + env(safe-area-inset-right)) 8px calc(12px + env(safe-area-inset-left));
    background: var(--grad-header);
    color: white;
    box-shadow: var(--shadow-deep);
    flex-shrink: 0;
    border-bottom-left-radius: 20px;
    border-bottom-right-radius: 20px;
    position: relative;
    overflow: hidden;
  }
  header::before {
    content: ''; position: absolute; inset: 0;
    background:
      radial-gradient(circle at 12% 30%, rgba(255,255,255,.18) 0, transparent 24%),
      radial-gradient(circle at 88% 70%, rgba(255,255,255,.14) 0, transparent 28%);
    pointer-events: none;
  }
  header > * { position: relative; z-index: 1; }
  header h1 {
    font-size: 20px; margin: 0; letter-spacing: 1.5px; flex-shrink: 0;
    font-weight: 800;
    text-shadow: 0 2px 4px rgba(0,0,0,.15);
  }
  .timer-chip {
    background: rgba(255,255,255,.22); padding: 6px 14px; border-radius: 999px;
    font-size: 15px; font-weight: 700; cursor: pointer; min-height: 48px;
    display: inline-flex; align-items: center; gap: 6px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.4), 0 2px 6px rgba(0,0,0,.08);
    transition: transform .15s ease;
  }
  .timer-chip:active { transform: scale(.94); }
  .timer-chip.warn  { background: rgba(255,200,90,.4); }
  .timer-chip.danger { background: rgba(255,90,110,.55); animation: blink 1s infinite; }
  @keyframes blink { 50% { opacity: .5; } }
  @keyframes pop   { 0%{transform:scale(1);} 40%{transform:scale(.93);} 100%{transform:scale(1);} }
  @keyframes modalIn { 0%{opacity:0; transform:translateY(20px) scale(.96);} 100%{opacity:1; transform:translateY(0) scale(1);} }
  @keyframes wiggle { 0%,100%{transform:rotate(0);} 25%{transform:rotate(-3deg);} 75%{transform:rotate(3deg);} }
  .header-spacer { flex: 1; }
  .header-btns { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
  .big-btn {
    background: var(--grad-button); border: none; color: white;
    padding: 10px 14px; border-radius: 14px;
    font-size: 15px; font-weight: 700;
    min-height: var(--hit); min-width: 64px;
    cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.45), 0 3px 8px rgba(0,0,0,.10);
    transition: transform .12s ease, box-shadow .12s ease;
  }
  .big-btn:active { transform: scale(.92); box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 1px 3px rgba(0,0,0,.12); }
  .big-btn.danger { background: linear-gradient(180deg, rgba(255,200,200,.45), rgba(255,180,180,.2)); }
  .big-btn.danger:active { background: linear-gradient(180deg, rgba(255,170,170,.6), rgba(255,150,150,.3)); }

  /* Main layout */
  main {
    flex: 1; display: flex; min-height: 0;
  }

  /* Color/pattern palette on the left */
  .palette {
    width: 200px; padding: 12px 10px 80px;
    background: var(--panel); box-shadow: var(--shadow);
    overflow-y: auto; flex-shrink: 0;
    display: flex; flex-direction: column; gap: 14px;
  }
  .palette h3 {
    margin: 0 0 6px; font-size: 12px; color: #666;
    text-transform: uppercase; letter-spacing: 1px;
  }
  .swatches {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;
  }
  .swatch {
    width: 100%; aspect-ratio: 1;
    border-radius: 50%;
    border: 3px solid #fff;
    box-shadow: 0 2px 6px rgba(0,0,0,.18);
    cursor: pointer;
    transition: transform .15s ease;
  }
  .swatch:hover { transform: scale(1.08); }
  .swatch:active { transform: scale(.9); }
  .swatch.active {
    outline: 4px solid var(--accent-2); outline-offset: 2px;
    box-shadow: 0 4px 12px rgba(183,148,244,.45);
  }
  .custom-color {
    display: flex; align-items: center; gap: 8px; margin-top: 6px;
  }
  .custom-color input[type=color] {
    width: 48px; height: 48px; border: none; background: none; padding: 0; cursor: pointer;
  }
  /* Compact palette buttons that open popups */
  .pop-btn {
    display: flex; align-items: center; gap: 10px;
    width: 100%; padding: 10px 12px;
    background: #f8fafc; border: 2px solid #e3e7ed; border-radius: 14px;
    cursor: pointer; min-height: 60px; text-align: left;
  }
  .pop-btn:active { background: #e6f3ff; border-color: var(--accent); }
  .pop-swatch {
    width: 38px; height: 38px; border-radius: 50%;
    background: #4ab3ff; border: 2px solid #fff;
    box-shadow: 0 1px 4px rgba(0,0,0,.2);
    flex-shrink: 0;
  }
  .pop-swatch-pat { border-radius: 10px; overflow: hidden; background: #fff; }
  .pop-swatch-pat svg { width: 100%; height: 100%; display: block; }
  .pop-label { font-size: 14px; font-weight: 600; color: #333; }
  .palette-section h3 {
    margin: 0 0 6px; font-size: 12px; color: #666;
    text-transform: uppercase; letter-spacing: 1px;
  }
  #colorPop .swatches {
    grid-template-columns: repeat(5, 1fr); gap: 8px;
  }
  #colorPop .swatch { width: 100%; aspect-ratio: 1; }
  .pattern-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;
  }
  .pattern-tile {
    aspect-ratio: 1; border-radius: 10px;
    border: 3px solid #e3e7ed; background: #fff;
    cursor: pointer; padding: 4px;
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; color: #555;
    flex-direction: column; gap: 2px;
    overflow: hidden;
  }
  .pattern-tile.active { border-color: var(--accent); background: #e6f3ff; }
  .pattern-tile svg { width: 100%; flex: 1; }
  .brush-row { display: flex; align-items: center; gap: 10px; }
  .brush-row input[type=range] {
    flex: 1; height: 32px;
  }
  .brush-preview {
    width: 44px; height: 44px;
    display: flex; align-items: center; justify-content: center;
  }
  .brush-dot { background: currentColor; border-radius: 50%; }

  /* Center stage */
  .stage-wrap {
    flex: 1; min-width: 0; position: relative;
    display: flex; align-items: center; justify-content: center;
    padding: 12px; overflow: hidden;
  }
  .stage {
    position: relative; background: white;
    box-shadow: var(--shadow); border-radius: var(--radius);
    overflow: hidden;
    aspect-ratio: 4 / 3;
    max-width: 100%; max-height: 100%;
    width: 100%;
  }
  .stage-inner {
    position: absolute; inset: 0;
    transform-origin: 0 0;
    transition: transform .12s ease-out;
  }
  .stage-inner.dragging { transition: none; }
  .stage-inner svg, .stage-inner canvas {
    position: absolute; inset: 0;
    width: 100%; height: 100%;
    display: block;
  }
  .stage-inner svg .fillable {
    cursor: pointer;
    transition: fill 0.15s ease;
  }
  .stage-inner svg .stamp-instance { cursor: pointer; }
  .stage-inner canvas { touch-action: none; pointer-events: none; }
  .stage-inner canvas.draw-mode { pointer-events: auto; cursor: crosshair; }

  /* Bottom toolbar with tools + zoom — lifts above iPhone home indicator */
  .bottom-bar {
    position: absolute;
    left: calc(12px + env(safe-area-inset-left));
    right: calc(12px + env(safe-area-inset-right));
    bottom: calc(12px + env(safe-area-inset-bottom));
    display: flex; align-items: center; justify-content: space-between;
    gap: 8px; pointer-events: none;
  }
  .tools, .zoom-tools {
    display: flex; gap: 6px;
    background: rgba(255,255,255,.96);
    padding: 6px; border-radius: 16px;
    box-shadow: var(--shadow);
    pointer-events: auto;
  }
  .tool {
    min-width: var(--hit); min-height: var(--hit);
    padding: 6px 10px;
    background: transparent; border: 3px solid transparent; border-radius: 12px;
    font-size: 12px; font-weight: 600; color: #333;
    cursor: pointer;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    gap: 2px;
  }
  .tool svg { width: 26px; height: 26px; }
  .tool.active { background: #e6f3ff; border-color: var(--accent); color: var(--accent-dark); }
  .zoom-tools .tool { min-width: 48px; }
  .zoom-tools .tool span { font-size: 18px; font-weight: 700; }

  /* Floating action: zoom-reset */
  .zoom-display {
    font-size: 12px; color: #555; padding: 0 6px;
    display: flex; align-items: center; font-variant-numeric: tabular-nums;
  }

  /* Modals */
  .modal {
    position: fixed; inset: 0;
    background: rgba(40,30,60,.5);
    backdrop-filter: blur(3px);
    -webkit-backdrop-filter: blur(3px);
    display: none; align-items: center; justify-content: center;
    z-index: 50; padding: 12px;
  }
  .modal.show { display: flex; }
  .modal.show .modal-box { animation: modalIn .26s cubic-bezier(.34,1.4,.5,1); }
  .modal-box {
    background: #fff; border-radius: 24px;
    width: 100%; max-width: 920px;
    max-height: 92vh; overflow: hidden;
    display: flex; flex-direction: column;
    box-shadow: 0 18px 50px rgba(40,30,80,.32), 0 2px 6px rgba(0,0,0,.08);
  }
  .modal-header {
    display: flex; align-items: center; gap: 10px;
    padding: 14px 18px; border-bottom: 1px solid #eef1f5;
    flex-shrink: 0;
  }
  .modal-header h2 { font-size: 20px; margin: 0; color: var(--accent-dark); flex: 1; }
  .modal-close-x {
    background: #f1f4f8; border: none; width: 44px; height: 44px;
    border-radius: 50%; font-size: 22px; cursor: pointer; color: #333;
  }
  .modal-body {
    overflow-y: auto; padding: 14px 18px;
  }
  .modal-footer {
    padding: 12px 18px;
    border-top: 1px solid #eef1f5;
    display: flex; justify-content: flex-end; gap: 8px;
    flex-shrink: 0;
  }
  .primary-btn {
    background: linear-gradient(135deg, #5b8def, #b794f4);
    color: #fff; border: none;
    padding: 12px 24px; border-radius: 14px; font-size: 16px; font-weight: 700;
    min-height: var(--hit); cursor: pointer;
    box-shadow: 0 4px 12px rgba(90,80,200,.25);
    transition: transform .12s ease;
  }
  .primary-btn:active { transform: scale(.94); }
  .secondary-btn {
    background: #f1f4f8; color: #333; border: none;
    padding: 12px 24px; border-radius: 14px; font-size: 16px; font-weight: 600;
    min-height: var(--hit); cursor: pointer;
    transition: transform .12s ease;
  }
  .secondary-btn:active { transform: scale(.94); background: #e3e7ed; }

  /* Picture / Stamp picker */
  .cat-tabs {
    display: flex; gap: 6px; padding-bottom: 10px; flex-wrap: wrap;
    position: sticky; top: 0; background: #fff; z-index: 2;
    border-bottom: 1px solid #eef1f5; margin-bottom: 10px;
  }
  .cat-tab {
    background: #f1f4f8; border: 2px solid transparent;
    padding: 10px 16px; border-radius: 999px;
    font-size: 14px; font-weight: 700; cursor: pointer;
    min-height: 44px; color: #555;
    transition: transform .12s ease, background .15s;
  }
  .cat-tab:active { transform: scale(.94); }
  .cat-tab.active {
    background: linear-gradient(135deg, #5b8def, #b794f4);
    color: #fff; border-color: transparent;
    box-shadow: 0 4px 10px rgba(90,80,200,.25);
  }
  .picker-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 12px;
  }
  .picker-card {
    background: #fff; border: 3px solid transparent;
    border-radius: 18px; padding: 8px; cursor: pointer;
    aspect-ratio: 4 / 3; position: relative;
    display: flex; flex-direction: column;
    box-shadow: 0 4px 12px rgba(90,80,150,.10);
    transition: transform .15s ease, box-shadow .15s ease;
  }
  .picker-card:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(90,80,150,.18); }
  .picker-card:active { transform: scale(.96); }
  .picker-card.active {
    border-color: var(--accent-2);
    background: #f6efff;
    box-shadow: 0 6px 16px rgba(183,148,244,.4);
  }
  .picker-card svg { width: 100%; flex: 1; }
  .picker-card .pc-label {
    font-size: 11px; color: #5e556d; text-align: center; padding-top: 4px;
    font-weight: 600;
  }
  .picker-card.custom::after {
    content: '×';
    position: absolute; top: 4px; right: 4px;
    width: 22px; height: 22px;
    background: rgba(0,0,0,.55); color: #fff;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; line-height: 1;
  }
  .picker-card.custom img { width: 100%; flex: 1; object-fit: contain; }

  .stamp-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(86px, 1fr));
    gap: 8px;
  }
  .stamp-card {
    background: #fff; border: 3px solid transparent;
    border-radius: 16px; padding: 6px; cursor: pointer;
    aspect-ratio: 1; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 3px 10px rgba(90,80,150,.10);
    transition: transform .15s ease;
  }
  .stamp-card:hover { transform: translateY(-3px) rotate(-2deg); }
  .stamp-card:active { transform: scale(.92); }
  .stamp-card.active {
    border-color: var(--accent-2);
    background: #f6efff;
    box-shadow: 0 5px 14px rgba(183,148,244,.4);
  }
  .stamp-card svg { width: 80%; height: 80%; }

  /* Search row in picture modal */
  .search-row {
    display: flex; gap: 6px; padding-bottom: 10px;
    border-bottom: 1px solid #eef1f5; margin-bottom: 10px;
    flex-wrap: wrap; align-items: center;
  }
  .search-row input[type=search] {
    flex: 1; min-width: 180px;
    padding: 10px 12px; font-size: 15px;
    border: 1px solid #dde3ea; border-radius: 10px;
    background: #fff;
  }
  .search-row .primary-btn { padding: 10px 18px; font-size: 14px; min-height: 44px; }
  .search-row .ghost-btn { padding: 10px 14px; font-size: 15px; min-height: 44px; }
  #searchResults:empty { display: none; }

  /* Upload section in picture modal */
  .upload-row {
    display: flex; gap: 8px; flex-wrap: wrap;
    padding: 0 0 12px;
    border-bottom: 1px solid #eef1f5; margin-bottom: 10px;
  }
  .upload-row .ghost-btn {
    background: #f1f4f8; border: 1px solid #dde3ea;
    border-radius: 10px; padding: 10px 14px; font-size: 14px; cursor: pointer;
    min-height: 44px; display: inline-flex; align-items: center; gap: 6px;
  }
  .upload-row input[type=url] {
    flex: 1; min-width: 160px;
    padding: 9px 10px; font-size: 14px;
    border: 1px solid #dde3ea; border-radius: 10px;
  }
  .hint { font-size: 12px; color: #888; padding-top: 6px; }

  /* Timer mode tabs */
  .mode-tab {
    flex: 1; padding: 10px 14px; font-size: 14px; font-weight: 600;
    background: #f1f4f8; border: 2px solid transparent; border-radius: 12px;
    cursor: pointer; min-height: 44px; color: #555;
  }
  .mode-tab.active { background: #e6f3ff; border-color: var(--accent); color: var(--accent-dark); }

  /* Timer settings */
  .timer-options {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px;
    margin: 6px 0;
  }
  .timer-options button {
    padding: 14px 4px; font-size: 16px; font-weight: 700;
    background: #f1f4f8; border: 3px solid transparent; border-radius: 12px;
    cursor: pointer; min-height: var(--hit);
  }
  .timer-options button.active { background: #e6f3ff; border-color: var(--accent); color: var(--accent-dark); }

  /* Help modal */
  .help-body h3 { margin: 14px 0 4px; font-size: 14px; color: #333; }
  .help-body p, .help-body li { font-size: 14px; line-height: 1.6; color: #444; }
  .help-body ul, .help-body ol { padding-left: 20px; margin: 4px 0; }

  /* Toast / autosave indicator */
  .toast {
    position: fixed; left: 50%; bottom: 80px; transform: translateX(-50%);
    background: linear-gradient(135deg, #5b8def, #b794f4);
    color: #fff;
    padding: 12px 22px; border-radius: 999px;
    font-size: 14px; font-weight: 700;
    box-shadow: 0 6px 18px rgba(90,80,200,.4);
    z-index: 60;
    opacity: 0; pointer-events: none;
    transition: opacity .25s, transform .25s;
  }
  .toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

  /* ===== Responsive ===== */

  /* Smaller laptops + iPad portrait */
  @media (max-width: 1024px) {
    .palette { width: 168px; padding: 10px 8px 70px; }
    header h1 { font-size: 16px; }
    .big-btn { padding: 8px 10px; font-size: 14px; min-width: 56px; }
  }

  /* iPad portrait edge */
  @media (max-width: 820px) {
    .palette { width: 150px; }
    .big-btn { padding: 7px 9px; font-size: 13px; min-width: 50px; min-height: 48px; gap: 4px; }
    .timer-chip { font-size: 14px; padding: 5px 10px; min-height: 48px; }
    header h1 { font-size: 15px; }
  }

  /* Phone portrait — column layout, palette is a top strip */
  @media (max-width: 640px) {
    :root { --hit: 44px; }
    body { font-size: 14px; }
    header {
      flex-wrap: wrap; padding: 6px 8px; gap: 6px;
    }
    header h1 { font-size: 14px; letter-spacing: 0; }
    .header-spacer { display: none; }
    .header-btns {
      flex: 1; justify-content: flex-end; gap: 4px; flex-wrap: nowrap;
    }
    .timer-chip { font-size: 13px; padding: 4px 10px; min-height: 40px; gap: 4px; }
    .big-btn {
      padding: 6px 8px; font-size: 12px; min-height: 40px; min-width: 40px;
      gap: 3px; border-radius: 10px;
    }

    main { flex-direction: column; }
    .palette {
      width: 100%; height: auto; flex-shrink: 0;
      padding: 8px 10px;
      flex-direction: row; overflow-x: auto; overflow-y: hidden;
      gap: 14px; max-height: none;
    }
    .palette > * { flex-shrink: 0; }
    .palette .pop-btn { min-width: 110px; padding: 6px 10px; min-height: 48px; }
    .palette .pop-swatch { width: 28px; height: 28px; }
    .palette .pop-label { font-size: 13px; }
    .palette-section { min-width: 140px; }
    .palette-section h3 { font-size: 10px; margin: 0 0 4px; }
    .brush-row { gap: 6px; }
    .brush-row input[type=range] { min-width: 70px; }
    .brush-preview { width: 30px; height: 30px; }
    /* Color popup on phones */
    #colorPop .swatches { grid-template-columns: repeat(6, 1fr); }
    .pattern-grid { grid-template-columns: repeat(4, 1fr); gap: 6px; }
    .pattern-tile { padding: 3px; font-size: 10px; }

    .stage-wrap { flex: 1; padding: 6px; min-height: 0; }
    .bottom-bar {
      left: 4px; right: 4px; bottom: 4px; gap: 4px;
      flex-wrap: wrap;
    }
    .tools, .zoom-tools { padding: 4px; gap: 3px; border-radius: 12px; }
    .tool {
      min-width: 44px; min-height: 44px; padding: 4px;
      font-size: 10px; border-width: 2px;
    }
    .tool svg { width: 20px; height: 20px; }
    .zoom-tools .tool { min-width: 38px; }
    .zoom-tools .tool span { font-size: 16px; }
    .zoom-display { font-size: 10px; padding: 0 4px; min-width: 30px; }

    /* Modals on phone: take full width */
    .modal { padding: 6px; align-items: stretch; }
    .modal-box {
      max-height: 100%; height: 100%; max-width: 100%;
      border-radius: 14px;
    }
    .modal-header { padding: 10px 12px; }
    .modal-header h2 { font-size: 16px; }
    .modal-close-x { width: 40px; height: 40px; font-size: 20px; }
    .modal-body { padding: 10px 12px; }
    .modal-footer { padding: 8px 12px; }
    .primary-btn, .secondary-btn {
      padding: 10px 16px; font-size: 14px; min-height: 44px;
    }
    .picker-grid { grid-template-columns: repeat(auto-fill, minmax(108px, 1fr)); gap: 8px; }
    .picker-card { padding: 4px; }
    .pc-label { font-size: 10px; }
    .stamp-grid { grid-template-columns: repeat(auto-fill, minmax(72px, 1fr)); gap: 6px; }
    .cat-tabs { gap: 4px; padding-bottom: 8px; margin-bottom: 8px; }
    .cat-tab { padding: 8px 12px; font-size: 13px; min-height: 40px; }
    .upload-row { flex-direction: column; align-items: stretch; gap: 6px; }
    .upload-row .ghost-btn { padding: 10px 12px; font-size: 14px; }
    .timer-options { grid-template-columns: repeat(3, 1fr); gap: 6px; }
    .timer-options button { padding: 12px 4px; font-size: 14px; min-height: 44px; }
  }

  /* Tiny phone (iPhone SE etc) */
  @media (max-width: 400px) {
    header h1 { display: none; }
    .big-btn .btn-label { display: none; }
    .big-btn .btn-icon { font-size: 18px; }
    .big-btn { min-width: 38px; min-height: 40px; padding: 4px 6px; }
    .timer-chip { font-size: 12px; padding: 3px 8px; gap: 3px; }
    .palette { gap: 10px; padding: 6px 8px; }
    .palette > * { min-width: 100px; }
    .palette .pop-label { font-size: 12px; }
    .picker-grid { grid-template-columns: repeat(auto-fill, minmax(96px, 1fr)); }
    .stamp-grid { grid-template-columns: repeat(auto-fill, minmax(64px, 1fr)); }
  }

  /* Phone landscape: header tighter so canvas keeps height */
  @media (max-width: 900px) and (orientation: landscape) and (max-height: 500px) {
    header { padding: 4px 8px; gap: 4px; }
    header h1 { display: none; }
    .timer-chip { font-size: 12px; min-height: 36px; padding: 3px 8px; }
    .big-btn { font-size: 12px; min-height: 36px; padding: 4px 8px; }
    .big-btn .btn-label { display: none; }
    .palette {
      padding: 4px 8px; gap: 10px; flex-direction: row;
    }
    .palette > * { min-width: 100px; }
    .palette .pop-btn { min-height: 40px; padding: 4px 8px; }
    .palette .pop-swatch { width: 24px; height: 24px; }
  }
</style>
</head>
"""

HTML_BODY = r"""<body>

<header>
  <h1>🎨 画图填色</h1>
  <div class="timer-chip" id="timerChip" title="点击设置倒计时">⏱ <span id="timerText">10:00</span></div>
  <div class="header-spacer"></div>
  <div class="header-btns">
    <button class="big-btn" id="pickPictureBtn"><span class="btn-icon">🖼️</span><span class="btn-label">选图</span></button>
    <button class="big-btn" id="undoBtn"><span class="btn-icon">↶</span><span class="btn-label">撤销</span></button>
    <button class="big-btn danger" id="clearBtn"><span class="btn-icon">🗑</span><span class="btn-label">清空</span></button>
    <button class="big-btn" id="saveBtn"><span class="btn-icon">💾</span><span class="btn-label">保存</span></button>
    <button class="big-btn" id="fullscreenBtn"><span class="btn-icon">⛶</span><span class="btn-label">全屏</span></button>
    <button class="big-btn" id="helpBtn">?</button>
  </div>
</header>

<main>
  <aside class="palette">
    <button class="pop-btn" id="openColorPop" title="颜色">
      <span class="pop-swatch" id="curColorSwatch"></span>
      <span class="pop-label">颜色</span>
    </button>
    <button class="pop-btn" id="openPatternPop" title="纹路">
      <span class="pop-swatch pop-swatch-pat"><svg viewBox="0 0 30 30" id="curPatternPreview"><rect width="30" height="30" fill="#4ab3ff"/></svg></span>
      <span class="pop-label" id="curPatternName">纯色</span>
    </button>
    <div class="palette-section">
      <h3>画笔粗细 <span id="brushSizeText" style="float:right;color:#555">10</span></h3>
      <div class="brush-row">
        <input type="range" id="brushSize" min="3" max="40" value="10" />
        <div class="brush-preview" id="brushPreview"><div class="brush-dot"></div></div>
      </div>
    </div>
    <div class="palette-section" id="stampSizeBox" style="display:none">
      <h3>贴纸大小 <span id="stampSizeText" style="float:right;color:#555">50</span></h3>
      <div class="brush-row">
        <input type="range" id="stampSize" min="20" max="160" value="50" />
      </div>
    </div>
  </aside>

  <div class="stage-wrap">
    <div class="stage" id="stage">
      <div class="stage-inner" id="stageInner">
        <svg id="coloringSvg" viewBox="0 0 400 300" preserveAspectRatio="xMidYMid meet"></svg>
        <canvas id="drawCanvas"></canvas>
      </div>
    </div>

    <div class="bottom-bar">
      <div class="tools" id="tools">
        <button class="tool active" data-tool="fill">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 3l9 9-7 7a3 3 0 01-4-4l2-2"/><path d="M19 14c0 2-2 4-2 4s-2-2-2-4a2 2 0 014 0z" fill="currentColor" stroke="none"/></svg>
          填色
        </button>
        <button class="tool" data-tool="brush">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21s4-1 6-3l9-9-3-3-9 9c-2 2-3 6-3 6z"/></svg>
          画笔
        </button>
        <button class="tool" data-tool="eraser">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 17l6 6h12M16 3l5 5L9 20H3v-6z"/></svg>
          橡皮
        </button>
        <button class="tool" data-tool="stamp">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l2.5 5 5.5.8-4 4 .9 5.5L12 16l-4.9 2.3.9-5.5-4-4 5.5-.8z"/></svg>
          贴纸
        </button>
      </div>

      <div class="zoom-tools">
        <button class="tool" id="zoomOut" title="缩小"><span>−</span></button>
        <div class="zoom-display" id="zoomDisplay">100%</div>
        <button class="tool" id="zoomIn" title="放大"><span>+</span></button>
        <button class="tool" id="zoomReset" title="复位 100%"><span style="font-size:11px;font-weight:700">复位</span></button>
      </div>
    </div>
  </div>
</main>

<!-- Picture picker modal -->
<div class="modal" id="pictureModal" role="dialog" aria-modal="true">
  <div class="modal-box">
    <div class="modal-header">
      <h2>🖼️ 选一张图</h2>
      <button class="modal-close-x" data-close="pictureModal">×</button>
    </div>
    <div class="modal-body">
      <!-- Search row: Google Custom Search API (user provides key/cx) -->
      <div class="search-row">
        <input id="searchInput" type="search" placeholder="🔍 搜图: 熊猫 / 汽车 / 公主 …" />
        <button class="ghost-btn primary-btn" id="searchBtn">搜图</button>
        <button class="ghost-btn" id="searchCfgBtn" title="设置 Google API key">⚙️</button>
      </div>
      <div id="searchResults" class="picker-grid" style="margin-bottom:10px"></div>

      <div class="upload-row">
        <label class="ghost-btn">📁 上传图片
          <input id="fileInput" type="file" accept="image/*" style="display:none" />
        </label>
        <button class="ghost-btn" id="googleBtn">🌐 在 Google 打开</button>
        <input id="urlInput" type="url" placeholder="或粘贴图片网址…" />
        <button class="ghost-btn" id="urlLoadBtn">载入</button>
      </div>
      <div class="cat-tabs" id="pictureCatTabs"></div>
      <div class="picker-grid" id="pictureGrid"></div>
    </div>
  </div>
</div>

<!-- Search settings modal (one-time Google API setup) -->
<div class="modal" id="searchCfgModal" role="dialog" aria-modal="true">
  <div class="modal-box" style="max-width:520px">
    <div class="modal-header">
      <h2>⚙️ Google 搜图设置</h2>
      <button class="modal-close-x" data-close="searchCfgModal">×</button>
    </div>
    <div class="modal-body">
      <p style="font-size:14px;line-height:1.6;color:#444">
        Google 图片本身没有公开 API。我们用 Google 的 <b>Programmable Search Engine</b>(每天 100 次免费)。
        一次性设置好,以后在上面框里输入关键词就能搜到图,点缩略图直接载入画板。
      </p>
      <ol style="font-size:14px;line-height:1.7;color:#444">
        <li>建一个 <b>Programmable Search Engine</b>:
          <a href="https://programmablesearchengine.google.com/" target="_blank" rel="noopener">programmablesearchengine.google.com</a>
          → "Add" → 把 "Search the entire web" 打开 → 在 Search settings 把 "Image search" 打开。
          创建后页面会显示 <b>Search engine ID(cx)</b>。
        </li>
        <li>申请一个 API key:
          <a href="https://console.cloud.google.com/apis/library/customsearch.googleapis.com" target="_blank" rel="noopener">Google Cloud Console</a>
          → "Enable" Custom Search API → 旁边 "Credentials" → "Create credentials" → "API key"。
        </li>
        <li>把两个值粘到这里(只存在你这台设备的浏览器里):</li>
      </ol>
      <div style="display:flex;flex-direction:column;gap:8px;margin-top:6px">
        <input id="gcsKeyInput" type="text" placeholder="API Key" autocomplete="off" style="padding:10px;border:1px solid #dde3ea;border-radius:8px;font-size:14px"/>
        <input id="gcsCxInput" type="text" placeholder="Search engine ID (cx)" autocomplete="off" style="padding:10px;border:1px solid #dde3ea;border-radius:8px;font-size:14px"/>
      </div>
    </div>
    <div class="modal-footer">
      <button class="secondary-btn" id="gcsClear">清空</button>
      <button class="primary-btn" id="gcsSave">保存</button>
    </div>
  </div>
</div>

<!-- Stamp picker modal -->
<div class="modal" id="stampModal" role="dialog" aria-modal="true">
  <div class="modal-box">
    <div class="modal-header">
      <h2>⭐ 选个贴纸,然后在画上点一下放上去</h2>
      <button class="modal-close-x" data-close="stampModal">×</button>
    </div>
    <div class="modal-body">
      <div class="cat-tabs" id="stampCatTabs"></div>
      <div class="stamp-grid" id="stampGrid"></div>
      <div class="hint">小贴士:再点一次同一个贴纸可以取消选中。贴纸用当前颜色着色。</div>
    </div>
  </div>
</div>

<!-- Color popup -->
<div class="modal" id="colorPop" role="dialog" aria-modal="true">
  <div class="modal-box" style="max-width:480px">
    <div class="modal-header">
      <h2>🎨 选颜色</h2>
      <button class="modal-close-x" data-close="colorPop">×</button>
    </div>
    <div class="modal-body">
      <div class="swatches" id="swatches"></div>
      <div class="custom-color" style="margin-top:14px;padding-top:14px;border-top:1px solid #eef1f5">
        <input type="color" id="customColor" value="#4ab3ff" />
        <span style="font-size:14px;color:#555">自选任意颜色 →</span>
      </div>
    </div>
  </div>
</div>

<!-- Pattern popup -->
<div class="modal" id="patternPop" role="dialog" aria-modal="true">
  <div class="modal-box" style="max-width:520px">
    <div class="modal-header">
      <h2>🎭 选纹路</h2>
      <button class="modal-close-x" data-close="patternPop">×</button>
    </div>
    <div class="modal-body">
      <div class="pattern-grid" id="patternGrid"></div>
    </div>
  </div>
</div>

<!-- Timer modal -->
<div class="modal" id="timerModal" role="dialog" aria-modal="true">
  <div class="modal-box" style="max-width:460px">
    <div class="modal-header">
      <h2>⏱ 倒计时</h2>
      <button class="modal-close-x" data-close="timerModal">×</button>
    </div>
    <div class="modal-body">
      <div style="display:flex;gap:6px;margin-bottom:14px">
        <button class="mode-tab active" data-mode="single">单人</button>
        <button class="mode-tab" data-mode="multi">多人轮流</button>
      </div>

      <div id="singleModeBox">
        <p style="margin:0 0 6px;color:#555">画多久?到时间会弹提示。</p>
        <div class="timer-options" id="timerOptions">
          <button data-min="1">1分钟</button>
          <button data-min="2">2分钟</button>
          <button data-min="3">3分钟</button>
          <button data-min="5">5分钟</button>
          <button data-min="10">10分钟</button>
          <button data-min="15">15分钟</button>
          <button data-min="0">关掉</button>
        </div>
      </div>

      <div id="multiModeBox" style="display:none">
        <p style="margin:0 0 6px;color:#555">每个人轮流画固定时间,时间一到提示换下一个人。</p>
        <h4 style="margin:10px 0 4px;font-size:13px;color:#333">几个人?</h4>
        <div class="timer-options" id="multiCountOpts">
          <button data-n="2">2 人</button>
          <button data-n="3">3 人</button>
          <button data-n="4">4 人</button>
          <button data-n="5">5 人</button>
        </div>
        <h4 style="margin:14px 0 4px;font-size:13px;color:#333">每人多长时间?</h4>
        <div class="timer-options" id="multiTurnOpts">
          <button data-min="1">1分钟</button>
          <button data-min="2">2分钟</button>
          <button data-min="3">3分钟</button>
          <button data-min="5">5分钟</button>
          <button data-min="10">10分钟</button>
          <button data-min="15">15分钟</button>
        </div>
        <h4 style="margin:14px 0 4px;font-size:13px;color:#333">玩几轮?(每人都画完算一轮)</h4>
        <div class="timer-options" id="multiRoundOpts">
          <button data-r="1">1 轮</button>
          <button data-r="2">2 轮</button>
          <button data-r="3">3 轮</button>
          <button data-r="5">5 轮</button>
          <button data-r="10">10 轮</button>
          <button data-r="0">不限</button>
        </div>
      </div>
    </div>
    <div class="modal-footer">
      <button class="secondary-btn" id="timerReset">↺ 重置</button>
      <button class="primary-btn" id="timerPauseResume">⏸ 暂停</button>
    </div>
  </div>
</div>

<!-- Timer-expired alert -->
<div class="modal" id="timerExpiredModal" role="dialog" aria-modal="true">
  <div class="modal-box" style="max-width:380px; text-align:center;">
    <div class="modal-body" style="padding:32px 24px">
      <div style="font-size:56px" id="timerExpiredIcon">⏰</div>
      <h2 style="font-size:24px; margin:8px 0; color:var(--accent-dark)" id="timerExpiredTitle">时间到啦!</h2>
      <p style="font-size:16px;color:#555;" id="timerExpiredSub">画得真棒 🎉</p>
    </div>
    <div class="modal-footer" style="justify-content:center;gap:10px" id="timerExpiredButtons">
      <button class="secondary-btn" id="timerExpired10More">再加 10 分钟</button>
      <button class="primary-btn" data-close="timerExpiredModal">好的</button>
    </div>
  </div>
</div>

<!-- Help modal -->
<div class="modal" id="helpModal" role="dialog" aria-modal="true">
  <div class="modal-box" style="max-width:560px">
    <div class="modal-header">
      <h2>怎么玩</h2>
      <button class="modal-close-x" data-close="helpModal">×</button>
    </div>
    <div class="modal-body help-body">
      <p>给小朋友的画图涂色游戏,在电脑/iPad/手机的浏览器里就能玩。</p>
      <h3>🖼️ 选图</h3>
      <p>点顶上 <b>选图</b> 按钮打开图库,有 50 张图按 🐾 动物 / 🌊 海洋 / 🦕 童话 / 🚗 交通 / 🌸 自然 / 🍰 食物 / 🎉 节日 分类。还可以上传你自己的图。</p>
      <h3>🎨 涂色</h3>
      <ul>
        <li><b>填色</b>:选颜色,点图里的一块区域,自动填满。</li>
        <li><b>纹路</b>:左边可以选小圆点、条纹、心形之类的纹路代替纯色。</li>
        <li><b>画笔</b>:自由涂鸦,可调粗细。</li>
        <li><b>橡皮</b>:擦掉画笔笔迹(不会擦掉填的颜色,要还原颜色用"撤销")。</li>
        <li><b>贴纸</b>:点顶上 <b>贴纸</b> 选一个,在画上点一下就贴一个,可以重复贴。</li>
      </ul>
      <h3>🔍 放大缩小</h3>
      <p>iPad 上两根手指捏合可放大缩小,捏住拖动可移动画面。电脑上用左下的 +/− 按钮,或滚轮 + Ctrl/Cmd。</p>
      <h3>💾 自动保存</h3>
      <p>每画一笔都自动存在浏览器里,关掉再打开,你画到一半的画会自动找回来。换图也会记住,不会丢。</p>
      <h3>⏱ 倒计时</h3>
      <p>顶上的 ⏱ 按钮设置画多久(默认 10 分钟),到时间会弹提示。</p>
      <h3>⛶ 全屏</h3>
      <p>点 ⛶ 按钮,浏览器进入全屏模式(iPad Safari 也可以从"分享 → 添加到主屏幕"装成 App)。</p>
    </div>
    <div class="modal-footer">
      <button class="primary-btn" data-close="helpModal">明白了!</button>
    </div>
  </div>
</div>

<!-- SVG patterns (defs, hidden) -->
<svg width="0" height="0" style="position:absolute" id="patternDefs">
  <defs id="patternDefsContent"></defs>
</svg>

<!-- Toast -->
<div class="toast" id="toast">已自动保存</div>
"""

JS = r"""<script>
'use strict';

/* =========================================================================
   Data injected at build time
   ========================================================================= */
const PALETTE = __PALETTE__;
const CATEGORIES = __CATEGORIES__;
const STAMP_CATEGORIES = __STAMP_CATEGORIES__;
const PATTERNS = __PATTERNS__;
const PAGES = __PAGES__;
const STAMPS = __STAMPS__;

/* =========================================================================
   State + persistence
   ========================================================================= */
const LS_KEY = 'cga_state_v1';
const state = {
  tool: 'fill',
  color: '#4ab3ff',
  pattern: 'solid',
  brushSize: 10,
  stampSize: 50,
  pageKey: 'panda',
  pictureCat: CATEGORIES[0][0],
  stampCat: STAMP_CATEGORIES[0][0],
  stampKey: null,
  view: { tx: 0, ty: 0, scale: 1 },
  firstPickDone: false,
  history: [],   // session-only undo stack
  timer: {
    durationSec: 600,
    startTs: Date.now(),
    elapsedBefore: 0,
    paused: false,
    fired: false,
  },
  customPages: {}, // key -> { name, dataUrl }
};

function debounce(fn, ms) {
  let t = null;
  return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
}

function loadPersisted() {
  try {
    const raw = localStorage.getItem(LS_KEY);
    if (!raw) return;
    const data = JSON.parse(raw);
    Object.assign(state, {
      tool: data.tool || state.tool,
      color: data.color || state.color,
      pattern: data.pattern || state.pattern,
      brushSize: data.brushSize || state.brushSize,
      stampSize: data.stampSize || state.stampSize,
      pageKey: data.pageKey || state.pageKey,
      pictureCat: data.pictureCat || state.pictureCat,
      stampCat: data.stampCat || state.stampCat,
      view: data.view || state.view,
      customPages: data.customPages || {},
      firstPickDone: !!data.firstPickDone,
    });
    if (data.timer) {
      Object.assign(state.timer, data.timer);
      state.timer.fired = !!data.timer.fired;
    }
    if (data.pageStates) state._pageStates = data.pageStates;
    // Restore custom pages into PAGES dict
    Object.entries(state.customPages).forEach(([k, v]) => {
      PAGES[k] = { name: v.name, category: 'custom', custom: true, dataUrl: v.dataUrl };
    });
  } catch (e) { console.warn('load failed', e); }
}

const savePersisted = debounce(() => {
  try {
    // Build pageStates from current SVG + canvas
    const pageStates = (state._pageStates || {});
    const cur = capturePageState();
    if (cur) pageStates[state.pageKey] = cur;
    state._pageStates = pageStates;
    const data = {
      tool: state.tool, color: state.color, pattern: state.pattern,
      brushSize: state.brushSize, stampSize: state.stampSize, pageKey: state.pageKey,
      pictureCat: state.pictureCat, stampCat: state.stampCat,
      view: state.view, customPages: state.customPages,
      timer: state.timer, pageStates,
      firstPickDone: state.firstPickDone,
    };
    localStorage.setItem(LS_KEY, JSON.stringify(data));
  } catch (e) {
    console.warn('save failed', e);
    if (e && e.name === 'QuotaExceededError') {
      showToast('存储已满,旧画作可能无法保存', 3000);
    }
  }
}, 350);

function capturePageState() {
  // Capture fill colors of fillable elements (by index) + canvas pixels (PNG)
  if (!svgEl) return null;
  const fills = [];
  svgEl.querySelectorAll('.fillable').forEach((el, i) => {
    const f = el.getAttribute('fill');
    if (!f || f === '#ffffff') return;
    // If it's a pattern url, look up the pattern def to extract (pattern,color)
    const m = f.match(/^url\(#([^)]+)\)$/);
    if (m) {
      const patEl = document.getElementById(m[1]);
      if (patEl) {
        const pkey = patEl.getAttribute('data-pkey');
        const pcolor = patEl.getAttribute('data-pcolor');
        if (pkey) { fills.push([i, { p: pkey, c: pcolor }]); return; }
      }
    }
    fills.push([i, f]);
  });
  // Capture stamps placed in SVG
  const stamps = [];
  svgEl.querySelectorAll('.stamp-instance').forEach(g => {
    stamps.push({
      key: g.dataset.stampKey,
      x: +g.dataset.x, y: +g.dataset.y,
      color: g.dataset.color,
      size: +g.dataset.size || 50,
      pattern: g.dataset.pattern || 'solid',
    });
  });
  // Capture canvas as PNG (only if there are strokes)
  let strokes = null;
  try {
    // Avoid serializing huge images: only save if non-empty
    if (canvasHasContent()) strokes = canvas.toDataURL('image/png');
  } catch (e) {}
  return { fills, stamps, strokes };
}

function canvasHasContent() {
  // Sample alpha channel to detect any pixel
  if (!canvas.width || !canvas.height) return false;
  try {
    const w = canvas.width, h = canvas.height;
    const step = Math.max(8, Math.floor(Math.min(w, h) / 40));
    const data = ctx.getImageData(0, 0, w, h).data;
    for (let i = 3; i < data.length; i += step * 4) {
      if (data[i] > 0) return true;
    }
  } catch (e) {}
  return false;
}

function applyPageState(s) {
  if (!s) return;
  if (Array.isArray(s.fills)) {
    const fillables = svgEl.querySelectorAll('.fillable');
    s.fills.forEach(([i, f]) => {
      if (!fillables[i]) return;
      if (f && typeof f === 'object' && f.p) {
        fillables[i].setAttribute('fill', patternInstanceFor(f.p, f.c));
      } else {
        fillables[i].setAttribute('fill', f);
      }
    });
  }
  if (Array.isArray(s.stamps)) {
    s.stamps.forEach(st => placeStamp(st.key, st.x, st.y, st.color, false, st.pattern, st.size));
  }
  if (s.strokes) {
    const img = new Image();
    img.onload = () => {
      // Make sure canvas is sized first
      ctx.save();
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      ctx.restore();
    };
    img.src = s.strokes;
  }
}

/* =========================================================================
   DOM refs
   ========================================================================= */
const svgEl = document.getElementById('coloringSvg');
const canvas = document.getElementById('drawCanvas');
const ctx = canvas.getContext('2d');
const stage = document.getElementById('stage');
const stageInner = document.getElementById('stageInner');
const swatchesBox = document.getElementById('swatches');
const customColor = document.getElementById('customColor');
const brushSizeInput = document.getElementById('brushSize');
const brushPreview = document.getElementById('brushPreview');
const brushDot = brushPreview.querySelector('.brush-dot');
const patternGrid = document.getElementById('patternGrid');
const toolsBox = document.getElementById('tools');
const zoomDisplay = document.getElementById('zoomDisplay');
const pictureGrid = document.getElementById('pictureGrid');
const pictureCatTabs = document.getElementById('pictureCatTabs');
const stampGrid = document.getElementById('stampGrid');
const stampCatTabs = document.getElementById('stampCatTabs');
const timerText = document.getElementById('timerText');
const timerChip = document.getElementById('timerChip');
const toast = document.getElementById('toast');
const patternDefsContent = document.getElementById('patternDefsContent');

let toastTimer = null;
function showToast(msg, ms = 1200) {
  toast.textContent = msg;
  toast.classList.add('show');
  if (toastTimer) clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('show'), ms);
}

/* =========================================================================
   Palette
   ========================================================================= */
function buildPalette() {
  swatchesBox.innerHTML = '';
  PALETTE.forEach(c => {
    const sw = document.createElement('div');
    sw.className = 'swatch' + (c === state.color ? ' active' : '');
    sw.style.background = c;
    sw.dataset.color = c;
    if (c === '#ffffff') sw.style.borderColor = '#ccc';
    sw.addEventListener('click', () => { selectColor(c); closeModal('colorPop'); });
    swatchesBox.appendChild(sw);
  });
}
function selectColor(c) {
  state.color = c;
  customColor.value = (c.length === 7 && c.startsWith('#')) ? c : '#000000';
  document.querySelectorAll('.swatch').forEach(s => s.classList.toggle('active', s.dataset.color === c));
  const curSw = document.getElementById('curColorSwatch');
  if (curSw) curSw.style.background = c;
  updateBrushPreview();
  updatePatternDefs();
  savePersisted();
}
customColor.addEventListener('input', e => {
  selectColor(e.target.value);
});

// Color popup button
document.getElementById('openColorPop').addEventListener('click', () => openModal('colorPop'));
// Closing the color popup on swatch selection
document.getElementById('swatches').addEventListener('click', (e) => {
  if (e.target.classList.contains('swatch')) closeModal('colorPop');
});

/* =========================================================================
   Patterns
   ========================================================================= */
function buildPatternTiles() {
  patternGrid.innerHTML = '';
  PATTERNS.forEach(([id, name, def]) => {
    const tile = document.createElement('div');
    tile.className = 'pattern-tile' + (id === state.pattern ? ' active' : '');
    tile.dataset.id = id;
    tile.title = name;
    if (id === 'solid') {
      tile.innerHTML = `<svg viewBox="0 0 30 30"><rect width="30" height="30" fill="${state.color}"/></svg><div>纯色</div>`;
    } else {
      const previewDef = def.replace(/__FG__/g, state.color).replace(/__BG__/g, '#ffffff');
      tile.innerHTML = `<svg viewBox="0 0 30 30"><defs>${previewDef}</defs><rect width="30" height="30" fill="url(#pat-${id})"/></svg><div>${name}</div>`;
    }
    tile.addEventListener('click', () => {
      state.pattern = id;
      buildPatternTiles();
      updateCurrentPatternPreview();
      closeModal('patternPop');
      savePersisted();
    });
    patternGrid.appendChild(tile);
  });
}
function updateCurrentPatternPreview() {
  const previewEl = document.getElementById('curPatternPreview');
  const nameEl = document.getElementById('curPatternName');
  if (!previewEl) return;
  const entry = PATTERNS.find(p => p[0] === state.pattern) || PATTERNS[0];
  const [id, name, def] = entry;
  if (!def) {
    previewEl.innerHTML = `<rect width="30" height="30" fill="${state.color}"/>`;
  } else {
    const previewDef = def.replace(/__FG__/g, state.color).replace(/__BG__/g, '#ffffff');
    previewEl.innerHTML = `<defs>${previewDef}</defs><rect width="30" height="30" fill="url(#pat-${id})"/>`;
  }
  if (nameEl) nameEl.textContent = name;
}
document.getElementById('openPatternPop').addEventListener('click', () => openModal('patternPop'));
// Pattern instances are created once per (pattern, color) pair and cached
// so previously-filled regions are NEVER recolored when the user picks a
// different palette color.
let patternInstanceCounter = 0;
const patternInstanceCache = {};
function patternInstanceFor(patternKey, color) {
  if (!patternKey || patternKey === 'solid') return color;
  const cacheKey = patternKey + '|' + color;
  if (patternInstanceCache[cacheKey]) return patternInstanceCache[cacheKey];
  const def = PATTERNS.find(p => p[0] === patternKey);
  if (!def || !def[2]) { patternInstanceCache[cacheKey] = color; return color; }
  const newId = `pi-${++patternInstanceCounter}`;
  const xml = def[2]
    .replace('id="pat-' + patternKey + '"', `id="${newId}" data-pkey="${patternKey}" data-pcolor="${color}"`)
    .replace(/__FG__/g, color)
    .replace(/__BG__/g, '#ffffff');
  patternDefsContent.insertAdjacentHTML('beforeend', xml);
  const url = `url(#${newId})`;
  patternInstanceCache[cacheKey] = url;
  return url;
}

function updatePatternDefs() {
  // Only refresh the palette TILE previews — leave the actual filled defs alone.
  buildPatternTiles();
  updateCurrentPatternPreview();
}

function currentFillValue() {
  return patternInstanceFor(state.pattern, state.color);
}

/* =========================================================================
   Brush size
   ========================================================================= */
function updateBrushPreview() {
  const s = Math.max(4, Math.min(32, state.brushSize));
  brushDot.style.width = s + 'px';
  brushDot.style.height = s + 'px';
  brushPreview.style.color = state.color;
  const bst = document.getElementById('brushSizeText');
  if (bst) bst.textContent = state.brushSize;
}
brushSizeInput.addEventListener('input', e => {
  state.brushSize = +e.target.value;
  updateBrushPreview();
  savePersisted();
});

// Stamp size slider
const stampSizeInput = document.getElementById('stampSize');
const stampSizeText = document.getElementById('stampSizeText');
const stampSizeBox = document.getElementById('stampSizeBox');
stampSizeInput.addEventListener('input', e => {
  state.stampSize = +e.target.value;
  stampSizeText.textContent = e.target.value;
  savePersisted();
});

/* =========================================================================
   Tools
   ========================================================================= */
toolsBox.addEventListener('click', e => {
  const t = e.target.closest('.tool');
  if (!t || !t.dataset.tool) return;
  setTool(t.dataset.tool);
});
function setTool(t, openStampPicker = true) {
  const prev = state.tool;
  state.tool = t;
  document.querySelectorAll('#tools .tool').forEach(b => b.classList.toggle('active', b.dataset.tool === t));
  if (t === 'brush' || t === 'eraser') {
    canvas.classList.add('draw-mode');
  } else {
    canvas.classList.remove('draw-mode');
  }
  if (t !== 'stamp') state.stampKey = null;
  if (stampSizeBox) stampSizeBox.style.display = (t === 'stamp') ? '' : 'none';
  // When user picks stamp tool from the bottom bar, auto-open the stamp picker
  if (t === 'stamp' && openStampPicker && prev !== 'stamp') {
    buildStampCatTabs(); buildStampGrid(); openModal('stampModal');
  }
  savePersisted();
}

/* =========================================================================
   Pages (load / fill bindings)
   ========================================================================= */
function loadPage(key, restoreState = true) {
  const page = PAGES[key];
  if (!page) return;
  // Save current page state before switching
  // Snapshot current page state into _pageStates before switching
  if (svgEl.innerHTML) {
    state._pageStates = state._pageStates || {};
    const snap = capturePageState();
    if (snap) state._pageStates[state.pageKey] = snap;
  }
  state.pageKey = key;
  state.history = [];

  if (page.custom && page.dataUrl) {
    svgEl.innerHTML =
      `<image href="${page.dataUrl}" x="0" y="0" width="400" height="300" preserveAspectRatio="xMidYMid meet"/>`;
  } else {
    svgEl.innerHTML = page.svg;
  }
  bindFillable();
  clearCanvas(false);
  resetView();
  // Restore saved state for this page if any
  if (restoreState && state._pageStates && state._pageStates[key]) {
    applyPageState(state._pageStates[key]);
  }
  syncCanvasSize();
  buildPictureGrid();
  savePersisted();
}

function bindFillable() {
  // Direct SVG handlers only fire when canvas isn't catching clicks
  // (i.e. only in fill / stamp tool modes). Eraser is handled via the
  // canvas pointer flow with hit-testing — see eraserTapHitTest above.
  svgEl.querySelectorAll('.fillable').forEach(el => {
    const handler = (e) => {
      if (state.tool !== 'fill') return;
      e.preventDefault();
      const prev = el.getAttribute('fill') || '#ffffff';
      const next = currentFillValue();
      if (prev === next) return;
      state.history.push({ kind: 'fill', el, prevColor: prev });
      el.setAttribute('fill', next);
      savePersisted();
    };
    el.addEventListener('click', handler);
    el.addEventListener('touchstart', handler, { passive: false });
  });
}
// Delegated SVG click handler, bound exactly once for stamp placement
function svgStampClick(e) {
  if (state.tool !== 'stamp' || !state.stampKey) return;
  if (e.target.closest('.stamp-instance')) return;
  const pt = svgEventToPoint(e);
  if (!pt) return;
  placeStamp(state.stampKey, pt.x, pt.y, state.color, true, state.pattern, state.stampSize);
}
svgEl.addEventListener('click', svgStampClick);
svgEl.addEventListener('touchend', (e) => {
  // Some browsers fire only touchend (not click) on SVG. Forward as needed.
  if (state.tool === 'stamp' && state.stampKey) svgStampClick(e);
}, { passive: true });
function svgEventToPoint(e) {
  const rect = svgEl.getBoundingClientRect();
  const cx = (e.touches ? e.touches[0].clientX : e.clientX) - rect.left;
  const cy = (e.touches ? e.touches[0].clientY : e.clientY) - rect.top;
  const x = (cx / rect.width) * 400;
  const y = (cy / rect.height) * 300;
  return { x, y };
}
/* =========================================================================
   Stamps
   ========================================================================= */
function placeStamp(key, x, y, color, addHistory, patternKey, size) {
  const stamp = STAMPS.find(s => s[0] === key);
  if (!stamp) return;
  const [, , vb, body] = stamp;
  const SIZE = size || state.stampSize || 50;
  const fillVal = patternInstanceFor(patternKey || 'solid', color);
  const halfSize = SIZE / 2;
  const ns = 'http://www.w3.org/2000/svg';
  const g = document.createElementNS(ns, 'g');
  g.setAttribute('class', 'stamp-instance');
  g.setAttribute('transform', `translate(${x - halfSize} ${y - halfSize}) scale(${SIZE / vb})`);
  g.setAttribute('data-stamp-key', key);
  g.setAttribute('data-x', x);
  g.setAttribute('data-y', y);
  g.setAttribute('data-color', color);
  g.setAttribute('data-size', SIZE);
  g.setAttribute('data-pattern', patternKey || 'solid');
  g.innerHTML = body.replace(/__C__/g, fillVal);
  svgEl.appendChild(g);
  if (addHistory) {
    state.history.push({ kind: 'stamp', el: g });
    savePersisted();
  }
}

/* =========================================================================
   Canvas drawing with pan/zoom-aware coordinates
   ========================================================================= */
function syncCanvasSize() {
  const rect = stage.getBoundingClientRect();
  const prev = document.createElement('canvas');
  prev.width = canvas.width; prev.height = canvas.height;
  if (canvas.width && canvas.height) prev.getContext('2d').drawImage(canvas, 0, 0);
  const dpr = window.devicePixelRatio || 1;
  canvas.width = Math.round(rect.width * dpr);
  canvas.height = Math.round(rect.height * dpr);
  canvas.style.width = rect.width + 'px';
  canvas.style.height = rect.height + 'px';
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.lineCap = 'round'; ctx.lineJoin = 'round';
  if (prev.width) {
    ctx.drawImage(prev, 0, 0, prev.width / dpr, prev.height / dpr);
  }
}
window.addEventListener('resize', () => { syncCanvasSize(); });

// Track pointers for pan/zoom & drawing
const pointers = new Map();
let drawing = false;
let lastX = 0, lastY = 0;
let strokeSnapshot = null;
let pinchStart = null;

function canvasEventToLocal(e) {
  const rect = canvas.getBoundingClientRect();
  return { x: e.clientX - rect.left, y: e.clientY - rect.top };
}

function startStroke(x, y) {
  strokeSnapshot = ctx.getImageData(0, 0, canvas.width, canvas.height);
  drawing = true;
  lastX = x; lastY = y;
  drawSegment(x, y, x, y);
}
function continueStroke(x, y) {
  if (!drawing) return;
  drawSegment(lastX, lastY, x, y);
  lastX = x; lastY = y;
}
function endStroke() {
  if (!drawing) return;
  drawing = false;
  if (strokeSnapshot) {
    state.history.push({ kind: 'stroke', imageData: strokeSnapshot });
    strokeSnapshot = null;
    savePersisted();
  }
}
function drawSegment(x1, y1, x2, y2) {
  ctx.lineWidth = state.brushSize;
  if (state.tool === 'eraser') {
    ctx.globalCompositeOperation = 'destination-out';
    ctx.strokeStyle = 'rgba(0,0,0,1)';
  } else {
    ctx.globalCompositeOperation = 'source-over';
    ctx.strokeStyle = state.color;
  }
  ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
}

// Eraser tap-vs-drag tracking: brush always starts a stroke on pointerdown,
// but eraser defers — if user drags > 8px we treat it as canvas erasing;
// if they just tap, we hit-test the SVG to reset a fill or remove a stamp.
let eraserPending = null; // { x, y, clientX, clientY }

canvas.addEventListener('pointerdown', (e) => {
  canvas.setPointerCapture?.(e.pointerId);
  pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
  if (pointers.size === 2) {
    drawing = false; strokeSnapshot = null; eraserPending = null;
    const pts = [...pointers.values()];
    pinchStart = {
      dist: Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y),
      mid: { x: (pts[0].x + pts[1].x) / 2, y: (pts[0].y + pts[1].y) / 2 },
      view: { ...state.view },
    };
    stageInner.classList.add('dragging');
    return;
  }
  if (pointers.size !== 1) return;
  if (state.tool === 'brush') {
    e.preventDefault();
    const p = canvasEventToLocal(e);
    startStroke(p.x, p.y);
  } else if (state.tool === 'eraser') {
    e.preventDefault();
    const p = canvasEventToLocal(e);
    eraserPending = { x: p.x, y: p.y, clientX: e.clientX, clientY: e.clientY };
  }
});
canvas.addEventListener('pointermove', (e) => {
  if (!pointers.has(e.pointerId)) return;
  pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
  if (pointers.size === 2 && pinchStart) {
    const pts = [...pointers.values()];
    const dist = Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y);
    const mid = { x: (pts[0].x + pts[1].x) / 2, y: (pts[0].y + pts[1].y) / 2 };
    const ratio = dist / pinchStart.dist;
    const newScale = Math.max(1, Math.min(5, pinchStart.view.scale * ratio));
    setView(pinchStart.view.tx + (mid.x - pinchStart.mid.x), pinchStart.view.ty + (mid.y - pinchStart.mid.y), newScale);
    return;
  }
  if (pointers.size !== 1) return;
  // Eraser drag detection: if pointer moved enough, promote pending tap → canvas stroke
  if (eraserPending) {
    const dx = e.clientX - eraserPending.clientX;
    const dy = e.clientY - eraserPending.clientY;
    if (dx * dx + dy * dy > 256) {  // > 16px → treat as drag (canvas erase)
      startStroke(eraserPending.x, eraserPending.y);
      eraserPending = null;
    }
  }
  if (drawing) {
    e.preventDefault();
    const p = canvasEventToLocal(e);
    continueStroke(p.x, p.y);
  }
});
function setView(tx, ty, newScale) {
  state.view.tx = tx;
  state.view.ty = ty;
  state.view.scale = newScale;
  applyView();
}

// Eraser tap on SVG: reset a fill, or remove a stamp
function eraserTapHitTest(clientX, clientY) {
  const orig = canvas.style.pointerEvents;
  canvas.style.pointerEvents = 'none';
  const target = document.elementFromPoint(clientX, clientY);
  canvas.style.pointerEvents = orig;
  if (!target) return;
  if (target.classList && target.classList.contains('fillable')) {
    const prev = target.getAttribute('fill') || '#ffffff';
    if (prev !== '#ffffff') {
      state.history.push({ kind: 'fill', el: target, prevColor: prev });
      target.setAttribute('fill', '#ffffff');
      savePersisted();
    }
    return;
  }
  const stampInst = target.closest && target.closest('.stamp-instance');
  if (stampInst && stampInst.parentNode === svgEl) {
    state.history.push({
      kind: 'stamp-removed',
      key: stampInst.dataset.stampKey,
      x: +stampInst.dataset.x, y: +stampInst.dataset.y,
      color: stampInst.dataset.color,
      size: +stampInst.dataset.size || 50,
      pattern: stampInst.dataset.pattern || 'solid',
    });
    stampInst.parentNode.removeChild(stampInst);
    savePersisted();
  }
}

function pointerEnd(e) {
  pointers.delete(e.pointerId);
  if (pointers.size < 2) { pinchStart = null; stageInner.classList.remove('dragging'); }
  if (pointers.size === 0) {
    if (eraserPending && state.tool === 'eraser') {
      const { clientX, clientY } = eraserPending;
      eraserPending = null;
      eraserTapHitTest(clientX, clientY);
    }
    endStroke();
  }
}
canvas.addEventListener('pointerup', pointerEnd);
canvas.addEventListener('pointercancel', pointerEnd);
canvas.addEventListener('pointerleave', pointerEnd);

// Wheel-zoom
stage.addEventListener('wheel', (e) => {
  if (!(e.ctrlKey || e.metaKey)) return;
  e.preventDefault();
  const rect = stage.getBoundingClientRect();
  const cx = e.clientX - rect.left;
  const cy = e.clientY - rect.top;
  const newScale = Math.max(1, Math.min(5, state.view.scale * (e.deltaY < 0 ? 1.12 : 0.88)));
  zoomAround(cx, cy, newScale);
}, { passive: false });

function zoomAround(cx, cy, newScale) {
  // Keep the point (cx, cy) under the cursor invariant.
  const v = state.view;
  const localX = (cx - v.tx) / v.scale;
  const localY = (cy - v.ty) / v.scale;
  v.scale = newScale;
  v.tx = cx - localX * newScale;
  v.ty = cy - localY * newScale;
  applyView();
}
// (setView defined above)
function applyView() {
  const v = state.view;
  stageInner.style.transform = `translate(${v.tx}px, ${v.ty}px) scale(${v.scale})`;
  zoomDisplay.textContent = Math.round(v.scale * 100) + '%';
  savePersisted();
}
function resetView() {
  state.view = { tx: 0, ty: 0, scale: 1 };
  applyView();
}
document.getElementById('zoomIn').addEventListener('click', () => {
  const rect = stage.getBoundingClientRect();
  zoomAround(rect.width / 2, rect.height / 2, Math.min(5, state.view.scale * 1.25));
});
document.getElementById('zoomOut').addEventListener('click', () => {
  const rect = stage.getBoundingClientRect();
  zoomAround(rect.width / 2, rect.height / 2, Math.max(1, state.view.scale * 0.8));
});
document.getElementById('zoomReset').addEventListener('click', resetView);

/* =========================================================================
   Undo / Clear / Save (top)
   ========================================================================= */
document.getElementById('undoBtn').addEventListener('click', () => {
  const last = state.history.pop();
  if (!last) { showToast('没有可以撤销的'); return; }
  if (last.kind === 'fill') last.el.setAttribute('fill', last.prevColor);
  else if (last.kind === 'stroke') ctx.putImageData(last.imageData, 0, 0);
  else if (last.kind === 'stamp' && last.el && last.el.parentNode) last.el.parentNode.removeChild(last.el);
  else if (last.kind === 'stamp-removed') placeStamp(last.key, last.x, last.y, last.color, false, last.pattern, last.size);
  savePersisted();
});

document.getElementById('clearBtn').addEventListener('click', () => {
  if (!confirm('要清空当前这张画吗?(撤销键可以恢复之前的状态)')) return;
  // Clear fills + canvas + stamps for current page
  if (state._pageStates) delete state._pageStates[state.pageKey];
  loadPage(state.pageKey, false);
  showToast('已清空');
});

function clearCanvas(addHistory = true) {
  if (addHistory && canvas.width && canvas.height) {
    state.history.push({ kind: 'stroke', imageData: ctx.getImageData(0, 0, canvas.width, canvas.height) });
  }
  ctx.save();
  ctx.setTransform(1, 0, 0, 1, 0, 0);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.restore();
}

document.getElementById('saveBtn').addEventListener('click', async () => {
  // Render at stage (unscaled) size into a clean offscreen canvas
  const rect = stage.getBoundingClientRect();
  const w = Math.round(rect.width), h = Math.round(rect.height);
  const out = document.createElement('canvas');
  out.width = w * 2; out.height = h * 2;
  const octx = out.getContext('2d');
  octx.scale(2, 2);
  octx.fillStyle = '#ffffff';
  octx.fillRect(0, 0, w, h);

  // Inline patterns into the SVG so the exported PNG keeps them
  const cloned = svgEl.cloneNode(true);
  cloned.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
  cloned.setAttribute('width', w);
  cloned.setAttribute('height', h);
  // Embed pattern defs into the cloned SVG
  const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
  defs.innerHTML = patternDefsContent.innerHTML;
  cloned.insertBefore(defs, cloned.firstChild);

  const svgStr = new XMLSerializer().serializeToString(cloned);
  const svgBlob = new Blob([svgStr], { type: 'image/svg+xml;charset=utf-8' });
  const url = URL.createObjectURL(svgBlob);
  const img = new Image();
  img.onload = () => {
    octx.drawImage(img, 0, 0, w, h);
    octx.drawImage(canvas, 0, 0, w, h);
    URL.revokeObjectURL(url);
    out.toBlob(blob => {
      const a = document.createElement('a');
      a.download = `coloring-${state.pageKey}-${Date.now()}.png`;
      a.href = URL.createObjectURL(blob);
      a.click();
      setTimeout(() => URL.revokeObjectURL(a.href), 1000);
      showToast('已下载 PNG');
    }, 'image/png');
  };
  img.onerror = () => showToast('保存失败,请重试');
  img.src = url;
});

/* =========================================================================
   Picture picker modal
   ========================================================================= */
function openModal(id) { document.getElementById(id).classList.add('show'); }
function closeModal(id) { document.getElementById(id).classList.remove('show'); }
document.querySelectorAll('[data-close]').forEach(b => {
  b.addEventListener('click', () => closeModal(b.dataset.close));
});
document.querySelectorAll('.modal').forEach(m => {
  m.addEventListener('click', (e) => { if (e.target === m) m.classList.remove('show'); });
});
document.getElementById('pickPictureBtn').addEventListener('click', () => {
  buildPictureCatTabs(); buildPictureGrid(); openModal('pictureModal');
});

function buildPictureCatTabs() {
  pictureCatTabs.innerHTML = '';
  const cats = [...CATEGORIES];
  if (Object.keys(state.customPages).length) cats.push(['custom', '📁 我的图']);
  cats.forEach(([id, name]) => {
    const b = document.createElement('button');
    b.className = 'cat-tab' + (id === state.pictureCat ? ' active' : '');
    b.textContent = name;
    b.addEventListener('click', () => {
      state.pictureCat = id; savePersisted();
      buildPictureCatTabs(); buildPictureGrid();
    });
    pictureCatTabs.appendChild(b);
  });
}
function buildPictureGrid() {
  pictureGrid.innerHTML = '';
  Object.keys(PAGES).forEach(key => {
    const page = PAGES[key];
    const cat = page.custom ? 'custom' : page.category;
    if (cat !== state.pictureCat) return;
    const card = document.createElement('div');
    card.className = 'picker-card' + (key === state.pageKey ? ' active' : '') + (page.custom ? ' custom' : '');
    card.dataset.key = key;
    if (page.custom && page.dataUrl) {
      card.innerHTML = `<img src="${page.dataUrl}" alt="${page.name}"/><div class="pc-label">${page.name}</div>`;
    } else {
      card.innerHTML = `<svg viewBox="0 0 400 300">${page.svg}</svg><div class="pc-label">${page.name}</div>`;
    }
    card.addEventListener('click', (e) => {
      if (page.custom) {
        const r = card.getBoundingClientRect();
        const x = e.clientX - r.left, y = e.clientY - r.top;
        if (x > r.width - 30 && y < 30) {
          delete PAGES[key]; delete state.customPages[key];
          if (state.pageKey === key) { state.pageKey = 'blank'; loadPage('blank'); }
          savePersisted(); buildPictureCatTabs(); buildPictureGrid();
          return;
        }
      }
      loadPage(key);
      closeModal('pictureModal');
      markFirstPickDone();
    });
    pictureGrid.appendChild(card);
  });
}

// Called when the user first picks any picture — flips the firstPickDone
// flag and (re)starts the timer so the initial picker doesn't count as
// drawing time. No-op for every pick after the first.
function markFirstPickDone() {
  if (state.firstPickDone) return;
  state.firstPickDone = true;
  state.timer.elapsedBefore = 0;
  state.timer.startTs = Date.now();
  state.timer.paused = false;
  state.timer.fired = false;
  if (state.timer.mode === 'multi') {
    state.timer.currentPlayer = 1;
    state.timer.currentRound = 1;
    state.timer.done = false;
  }
  tickTimer();
  savePersisted();
}

/* =========================================================================
   Custom image upload / URL / Google
   ========================================================================= */
let customCounter = 0;
function addCustomPage(dataUrl, label) {
  customCounter++;
  const key = 'custom_' + Date.now() + '_' + customCounter;
  const name = label || ('我的图 ' + customCounter);
  PAGES[key] = { name, category: 'custom', custom: true, dataUrl };
  state.customPages[key] = { name, dataUrl };
  state.pictureCat = 'custom';
  savePersisted();
  loadPage(key);
  closeModal('pictureModal');
  markFirstPickDone();
}
document.getElementById('fileInput').addEventListener('change', (e) => {
  const f = e.target.files && e.target.files[0];
  if (!f) return;
  const reader = new FileReader();
  reader.onload = () => addCustomPage(reader.result, f.name.replace(/\.[^.]+$/, ''));
  reader.readAsDataURL(f);
  e.target.value = '';
});
document.getElementById('googleBtn').addEventListener('click', () => {
  const q = encodeURIComponent((document.getElementById('searchInput').value || 'cute coloring page for kids') + ' coloring');
  window.open('https://www.google.com/search?tbm=isch&q=' + q, '_blank', 'noopener');
});

/* ========== Google Custom Search ========== */
const GCS_KEY_LS = 'cga_gcs_key';
const GCS_CX_LS  = 'cga_gcs_cx';
const searchInput   = document.getElementById('searchInput');
const searchBtn     = document.getElementById('searchBtn');
const searchResults = document.getElementById('searchResults');
const searchCfgBtn  = document.getElementById('searchCfgBtn');
const gcsKeyInput   = document.getElementById('gcsKeyInput');
const gcsCxInput    = document.getElementById('gcsCxInput');

searchCfgBtn.addEventListener('click', () => {
  gcsKeyInput.value = localStorage.getItem(GCS_KEY_LS) || '';
  gcsCxInput.value  = localStorage.getItem(GCS_CX_LS)  || '';
  openModal('searchCfgModal');
});
document.getElementById('gcsSave').addEventListener('click', () => {
  const k = (gcsKeyInput.value || '').trim();
  const c = (gcsCxInput.value  || '').trim();
  if (k) localStorage.setItem(GCS_KEY_LS, k); else localStorage.removeItem(GCS_KEY_LS);
  if (c) localStorage.setItem(GCS_CX_LS, c);  else localStorage.removeItem(GCS_CX_LS);
  closeModal('searchCfgModal');
  showToast(k && c ? '搜图设置已保存' : '已清空设置');
});
document.getElementById('gcsClear').addEventListener('click', () => {
  gcsKeyInput.value = '';
  gcsCxInput.value = '';
});

async function doGoogleSearch() {
  const q = (searchInput.value || '').trim();
  if (!q) { searchInput.focus(); return; }
  const key = localStorage.getItem(GCS_KEY_LS);
  const cx  = localStorage.getItem(GCS_CX_LS);
  if (!key || !cx) {
    if (confirm('还没设置 Google API key 和 CSE ID。要现在设置吗?')) openModal('searchCfgModal');
    return;
  }
  searchResults.innerHTML = '<div style="grid-column:1/-1;text-align:center;padding:14px;color:#666;font-size:14px">正在搜图…</div>';
  try {
    const url = `https://www.googleapis.com/customsearch/v1?key=${encodeURIComponent(key)}&cx=${encodeURIComponent(cx)}&searchType=image&safe=active&num=10&q=${encodeURIComponent(q + ' coloring page')}`;
    const res = await fetch(url);
    const data = await res.json();
    if (data.error) throw new Error((data.error.message || '搜图失败') + ' (检查 API key / cx 是否正确,以及今日额度)');
    const items = data.items || [];
    if (!items.length) { searchResults.innerHTML = '<div style="grid-column:1/-1;padding:14px;color:#666;text-align:center">没找到结果,换个词试试</div>'; return; }
    renderSearchResults(items);
  } catch (e) {
    searchResults.innerHTML = `<div style="grid-column:1/-1;padding:14px;color:#c33;text-align:center;font-size:13px">搜图失败:${e.message}</div>`;
  }
}
function renderSearchResults(items) {
  searchResults.innerHTML = '';
  items.forEach(it => {
    const card = document.createElement('div');
    card.className = 'picker-card';
    const thumb = (it.image && it.image.thumbnailLink) ? it.image.thumbnailLink : it.link;
    card.innerHTML = `<img src="${thumb}" alt="${(it.title||'').replace(/"/g,'&quot;')}" style="width:100%;flex:1;object-fit:contain"/><div class="pc-label">点这里载入</div>`;
    card.addEventListener('click', async () => {
      card.querySelector('.pc-label').textContent = '正在载入…';
      try {
        const res = await fetch(it.link, { mode: 'cors' });
        if (!res.ok) throw new Error('HTTP ' + res.status);
        const blob = await res.blob();
        const reader = new FileReader();
        reader.onload = () => addCustomPage(reader.result, it.title ? it.title.slice(0, 24) : '搜到的图');
        reader.readAsDataURL(blob);
      } catch (e) {
        // CORS blocked — fall back to embedding the URL directly. Save may fail.
        addCustomPage(it.link, it.title ? it.title.slice(0, 24) : '搜到的图');
      }
    });
    searchResults.appendChild(card);
  });
}
searchBtn.addEventListener('click', doGoogleSearch);
searchInput.addEventListener('keydown', e => { if (e.key === 'Enter') doGoogleSearch(); });
document.getElementById('urlLoadBtn').addEventListener('click', async () => {
  const input = document.getElementById('urlInput');
  const url = (input.value || '').trim();
  if (!url) return;
  try {
    const res = await fetch(url, { mode: 'cors' });
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const blob = await res.blob();
    const reader = new FileReader();
    reader.onload = () => { addCustomPage(reader.result, '网络图'); input.value = ''; };
    reader.readAsDataURL(blob);
  } catch (err) {
    if (confirm('这张图禁止跨站加载,只能预览/上色但保存 PNG 可能失败。继续吗?')) {
      addCustomPage(url, '网络图');
      input.value = '';
    }
  }
});

/* =========================================================================
   Stamp picker modal — opened automatically by setTool('stamp')
   ========================================================================= */
function buildStampCatTabs() {
  stampCatTabs.innerHTML = '';
  STAMP_CATEGORIES.forEach(([id, name]) => {
    const b = document.createElement('button');
    b.className = 'cat-tab' + (id === state.stampCat ? ' active' : '');
    b.textContent = name;
    b.addEventListener('click', () => {
      state.stampCat = id; savePersisted();
      buildStampCatTabs(); buildStampGrid();
    });
    stampCatTabs.appendChild(b);
  });
}
function buildStampGrid() {
  stampGrid.innerHTML = '';
  STAMPS.forEach(([key, name, vb, body, cat]) => {
    if (cat !== state.stampCat) return;
    const card = document.createElement('div');
    card.className = 'stamp-card' + (key === state.stampKey ? ' active' : '');
    card.title = name;
    card.innerHTML = `<svg viewBox="0 0 ${vb} ${vb}">${body.replace(/__C__/g, state.color)}</svg>`;
    card.addEventListener('click', () => {
      state.stampKey = (state.stampKey === key) ? null : key;
      setTool('stamp');
      buildStampGrid();
      closeModal('stampModal');
      showToast(state.stampKey ? '在画上点一下放贴纸' : '取消贴纸', 1500);
    });
    stampGrid.appendChild(card);
  });
}

/* =========================================================================
   Timer (single + multi-player turn timing with round limit)
   ========================================================================= */
// state.timer extended: {
//   mode: 'single'|'multi',
//   durationSec, startTs, elapsedBefore, paused, fired,
//   playerCount, currentPlayer,            // multi only
//   totalRounds, currentRound, done        // multi only
// }
const T = state.timer;
if (!T.mode) T.mode = 'single';
if (!T.playerCount) T.playerCount = 2;
if (!T.currentPlayer) T.currentPlayer = 1;
if (T.totalRounds == null) T.totalRounds = 3;
if (!T.currentRound) T.currentRound = 1;
if (T.done == null) T.done = false;
// Backwards-compat: previously the single-mode options went up to 60 minutes.
// We capped the max at 15 minutes — clamp old saved values to fit.
if (T.mode === 'single' && T.durationSec > 900) T.durationSec = 600;

function fmtMs(ms) {
  const s = Math.max(0, Math.floor(ms / 1000));
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
}
function tickTimer() {
  const t = state.timer;
  if (t.done) {
    timerText.textContent = '🎉 完成';
    timerChip.className = 'timer-chip';
    return;
  }
  // Before the user has picked their first picture, freeze the timer on the
  // full duration so the initial picker isn't counted as drawing time.
  if (!state.firstPickDone) {
    timerText.textContent = t.durationSec > 0 ? '等开始 ' + fmtMs(t.durationSec * 1000) : '关';
    timerChip.className = 'timer-chip';
    return;
  }
  if (t.durationSec <= 0) {
    timerText.textContent = '关';
    timerChip.className = 'timer-chip';
    return;
  }
  const elapsed = t.paused ? t.elapsedBefore : t.elapsedBefore + (Date.now() - t.startTs);
  const remaining = t.durationSec * 1000 - elapsed;
  let label;
  if (t.mode === 'multi') {
    const r = t.totalRounds > 0 ? `R${t.currentRound}/${t.totalRounds}` : `R${t.currentRound}`;
    label = `P${t.currentPlayer}/${t.playerCount} ${r} ${fmtMs(remaining)}`;
  } else {
    label = fmtMs(remaining);
  }
  timerText.textContent = label;
  timerChip.classList.remove('warn', 'danger');
  if (remaining <= 60_000 && remaining > 0) timerChip.classList.add('warn');
  if (remaining <= 10_000 && remaining > 0) timerChip.classList.add('danger');
  if (remaining <= 0 && !t.fired) {
    t.fired = true;
    showTimerExpired();
    savePersisted();
  }
}
setInterval(tickTimer, 500);

// Advance to next player in multi mode. Returns true if more turns remain.
function advanceToNextPlayer() {
  const t = state.timer;
  let nextPlayer = (t.currentPlayer % t.playerCount) + 1;
  let nextRound = t.currentRound + (nextPlayer === 1 ? 1 : 0);
  if (t.totalRounds > 0 && nextRound > t.totalRounds) {
    t.done = true;
    return false;
  }
  t.currentPlayer = nextPlayer;
  t.currentRound = nextRound;
  t.elapsedBefore = 0;
  t.startTs = Date.now();
  t.paused = false;
  t.fired = false;
  return true;
}

function showTimerExpired() {
  const t = state.timer;
  const icon = document.getElementById('timerExpiredIcon');
  const title = document.getElementById('timerExpiredTitle');
  const sub = document.getElementById('timerExpiredSub');
  const btns = document.getElementById('timerExpiredButtons');
  if (t.mode === 'multi') {
    // Peek at what comes next (without mutating state)
    const nextPlayer = (t.currentPlayer % t.playerCount) + 1;
    const nextRound = t.currentRound + (nextPlayer === 1 ? 1 : 0);
    const isLast = t.totalRounds > 0 && nextRound > t.totalRounds;
    if (isLast) {
      // Last turn — game over
      icon.textContent = '🎉';
      title.textContent = '都画完啦!';
      sub.textContent = `${t.playerCount} 个小朋友各画了 ${t.totalRounds} 轮 ✨`;
      btns.innerHTML = `<button class="secondary-btn" id="timerPlayAgain">再玩一局</button>
                        <button class="primary-btn"   id="timerDone">完成</button>`;
      document.getElementById('timerPlayAgain').addEventListener('click', () => {
        t.currentPlayer = 1; t.currentRound = 1; t.done = false;
        t.elapsedBefore = 0; t.startTs = Date.now();
        t.paused = false; t.fired = false;
        closeModal('timerExpiredModal'); tickTimer(); savePersisted();
      });
      document.getElementById('timerDone').addEventListener('click', () => {
        t.done = true;
        closeModal('timerExpiredModal'); tickTimer(); savePersisted();
      });
    } else {
      icon.textContent = '🔁';
      title.textContent = '换人啦!';
      sub.textContent = `玩家 ${t.currentPlayer} 时间到 — 轮到 玩家 ${nextPlayer} ${nextPlayer === 1 ? `(第 ${nextRound} 轮)` : ''} 🎨`;
      btns.innerHTML = `<button class="primary-btn" id="timerNextPlayer">让玩家 ${nextPlayer} 开始 ▶</button>`;
      document.getElementById('timerNextPlayer').addEventListener('click', () => {
        advanceToNextPlayer();
        closeModal('timerExpiredModal'); tickTimer(); savePersisted();
      });
    }
  } else {
    icon.textContent = '⏰';
    title.textContent = '时间到啦!';
    sub.textContent = '画得真棒 🎉';
    btns.innerHTML = `<button class="secondary-btn" id="timerExpired10More">再加 10 分钟</button>
                      <button class="primary-btn"   id="timerExpired1More">再加 1 分钟</button>
                      <button class="primary-btn"   data-close="timerExpiredModal">好的</button>`;
    document.getElementById('timerExpired10More').addEventListener('click', () => {
      t.durationSec += 600; t.fired = false;
      closeModal('timerExpiredModal'); savePersisted();
    });
    document.getElementById('timerExpired1More').addEventListener('click', () => {
      t.durationSec += 60; t.fired = false;
      closeModal('timerExpiredModal'); savePersisted();
    });
    document.querySelector('#timerExpiredButtons [data-close]')
      .addEventListener('click', () => closeModal('timerExpiredModal'));
  }
  openModal('timerExpiredModal');
}

// If user dismisses the expired modal without clicking a button (taps backdrop
// or hits ×), in multi-mode auto-advance so the game doesn't get stuck.
const expiredModal = document.getElementById('timerExpiredModal');
new MutationObserver(() => {
  if (!expiredModal.classList.contains('show') && state.timer.fired && state.timer.mode === 'multi' && !state.timer.done) {
    advanceToNextPlayer();
    tickTimer();
    savePersisted();
  }
}).observe(expiredModal, { attributes: true, attributeFilter: ['class'] });

function refreshTimerModalSelections() {
  const t = state.timer;
  document.querySelectorAll('.mode-tab').forEach(b =>
    b.classList.toggle('active', b.dataset.mode === t.mode)
  );
  document.getElementById('singleModeBox').style.display = (t.mode === 'single') ? '' : 'none';
  document.getElementById('multiModeBox').style.display  = (t.mode === 'multi')  ? '' : 'none';
  document.querySelectorAll('#timerOptions button').forEach(b => {
    b.classList.toggle('active', t.mode === 'single' && +b.dataset.min === t.durationSec / 60);
  });
  document.querySelectorAll('#multiCountOpts button').forEach(b => {
    b.classList.toggle('active', t.mode === 'multi' && +b.dataset.n === t.playerCount);
  });
  document.querySelectorAll('#multiTurnOpts button').forEach(b => {
    b.classList.toggle('active', t.mode === 'multi' && +b.dataset.min === t.durationSec / 60);
  });
  document.querySelectorAll('#multiRoundOpts button').forEach(b => {
    b.classList.toggle('active', t.mode === 'multi' && +b.dataset.r === t.totalRounds);
  });
  document.getElementById('timerPauseResume').textContent = t.paused ? '▶ 继续' : '⏸ 暂停';
}

timerChip.addEventListener('click', () => {
  refreshTimerModalSelections();
  openModal('timerModal');
});
document.querySelectorAll('.mode-tab').forEach(b => {
  b.addEventListener('click', () => {
    const t = state.timer;
    t.mode = b.dataset.mode;
    if (t.mode === 'multi') {
      // Switching INTO multi mode: pick a sensible per-turn default
      if (t.durationSec === 0 || t.durationSec > 1800) t.durationSec = 60;
      t.currentPlayer = 1;
      t.currentRound = 1;
      t.done = false;
    } else {
      // Switching back to single — keep durationSec if it's reasonable
      if (t.durationSec < 60) t.durationSec = 600;
    }
    t.elapsedBefore = 0;
    t.startTs = Date.now();
    t.paused = false;
    t.fired = false;
    refreshTimerModalSelections();
    tickTimer();
    savePersisted();
  });
});
document.getElementById('timerOptions').addEventListener('click', (e) => {
  const b = e.target.closest('button'); if (!b) return;
  state.timer.mode = 'single';
  setTimerDuration(+b.dataset.min * 60);
  refreshTimerModalSelections();
});
document.getElementById('multiCountOpts').addEventListener('click', (e) => {
  const b = e.target.closest('button'); if (!b) return;
  const t = state.timer;
  t.mode = 'multi';
  t.playerCount = +b.dataset.n;
  t.currentPlayer = 1;
  t.currentRound = 1;
  t.done = false;
  t.elapsedBefore = 0;
  t.startTs = Date.now();
  t.paused = false;
  t.fired = false;
  refreshTimerModalSelections();
  tickTimer();
  savePersisted();
});
document.getElementById('multiTurnOpts').addEventListener('click', (e) => {
  const b = e.target.closest('button'); if (!b) return;
  state.timer.mode = 'multi';
  state.timer.currentRound = 1;
  state.timer.currentPlayer = 1;
  state.timer.done = false;
  setTimerDuration(+b.dataset.min * 60);
  refreshTimerModalSelections();
});
document.getElementById('multiRoundOpts').addEventListener('click', (e) => {
  const b = e.target.closest('button'); if (!b) return;
  const t = state.timer;
  t.mode = 'multi';
  t.totalRounds = +b.dataset.r;
  t.currentPlayer = 1;
  t.currentRound = 1;
  t.done = false;
  t.elapsedBefore = 0;
  t.startTs = Date.now();
  t.paused = false;
  t.fired = false;
  refreshTimerModalSelections();
  tickTimer();
  savePersisted();
});
function setTimerDuration(sec) {
  state.timer.durationSec = sec;
  state.timer.elapsedBefore = 0;
  state.timer.startTs = Date.now();
  state.timer.paused = false;
  state.timer.fired = false;
  state.timer.done = false;
  tickTimer();
  savePersisted();
}
document.getElementById('timerReset').addEventListener('click', () => {
  const t = state.timer;
  if (t.mode === 'multi') { t.currentPlayer = 1; t.currentRound = 1; }
  t.done = false;
  setTimerDuration(t.durationSec);
  refreshTimerModalSelections();
  showToast('倒计时已重置');
});
document.getElementById('timerPauseResume').addEventListener('click', () => {
  const t = state.timer;
  if (t.paused) {
    t.paused = false;
    t.startTs = Date.now();
  } else {
    t.paused = true;
    t.elapsedBefore = t.elapsedBefore + (Date.now() - t.startTs);
  }
  refreshTimerModalSelections();
  savePersisted();
});

/* =========================================================================
   Fullscreen
   ========================================================================= */
document.getElementById('fullscreenBtn').addEventListener('click', async () => {
  try {
    if (document.fullscreenElement) await document.exitFullscreen();
    else if (document.documentElement.requestFullscreen) await document.documentElement.requestFullscreen();
    else if (document.documentElement.webkitRequestFullscreen) document.documentElement.webkitRequestFullscreen();
    else showToast('当前浏览器不支持全屏 — iPad Safari 请用"分享 → 添加到主屏幕"', 3000);
  } catch (e) { showToast('无法进入全屏: ' + e.message, 2500); }
});

/* =========================================================================
   Help
   ========================================================================= */
document.getElementById('helpBtn').addEventListener('click', () => openModal('helpModal'));

/* =========================================================================
   Boot
   ========================================================================= */
loadPersisted();
buildPalette();
selectColor(state.color);
buildPatternTiles();
updatePatternDefs();
updateBrushPreview();
brushSizeInput.value = state.brushSize;
stampSizeInput.value = state.stampSize;
stampSizeText.textContent = state.stampSize;
setTool(state.tool);
loadPage(state.pageKey);
applyView();
tickTimer();

// Auto-open the picture picker as the first screen (after help on first visit).
function openPickerAfterBoot() {
  buildPictureCatTabs();
  buildPictureGrid();
  openModal('pictureModal');
}
// First-run: help, then picker. Returning visit: jump straight to picker.
try {
  if (!localStorage.getItem('cga_help_seen')) {
    openModal('helpModal');
    localStorage.setItem('cga_help_seen', '1');
    // When user closes help, open picker
    const helpModal = document.getElementById('helpModal');
    const obs = new MutationObserver(() => {
      if (!helpModal.classList.contains('show')) {
        obs.disconnect();
        setTimeout(openPickerAfterBoot, 250);
      }
    });
    obs.observe(helpModal, { attributes: true, attributeFilter: ['class'] });
  } else {
    setTimeout(openPickerAfterBoot, 100);
  }
} catch (_) { openPickerAfterBoot(); }

</script>
</body>
</html>
"""

# ============================================================================
# Compose final HTML
# ============================================================================
def js_template_literal(svg):
    # Escape backticks and ${
    return svg.replace('\\', '\\\\').replace('`', '\\`').replace('${', '\\${')

def write_html():
    # Build PAGES JS dict
    page_entries = []
    for key, name, cat, svg in TEMPLATES:
        svg_esc = js_template_literal(svg)
        page_entries.append(f"  {key}: {{ name: {json.dumps(name, ensure_ascii=False)}, category: {json.dumps(cat)}, svg: `{svg_esc}` }}")
    pages_js = '{\n' + ',\n'.join(page_entries) + '\n}'

    # Build STAMPS JS array
    stamp_entries = []
    for key, name, vb, body, cat in STAMPS:
        body_esc = js_template_literal(body)
        stamp_entries.append(f"  [{json.dumps(key)}, {json.dumps(name, ensure_ascii=False)}, {vb}, `{body_esc}`, {json.dumps(cat)}]")
    stamps_js = '[\n' + ',\n'.join(stamp_entries) + '\n]'

    js = JS \
        .replace('__PALETTE__', json.dumps(PALETTE)) \
        .replace('__CATEGORIES__', json.dumps(CATEGORIES, ensure_ascii=False)) \
        .replace('__STAMP_CATEGORIES__', json.dumps(STAMP_CATEGORIES, ensure_ascii=False)) \
        .replace('__PATTERNS__', json.dumps(PATTERNS, ensure_ascii=False)) \
        .replace('__PAGES__', pages_js) \
        .replace('__STAMPS__', stamps_js)

    html = HTML_HEAD_CSS + HTML_BODY + js
    out = os.path.join(ROOT, 'index.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'wrote {out}, {len(html)} bytes, {len(TEMPLATES)} templates, {len(STAMPS)} stamps')

if __name__ == '__main__':
    # Templates and stamps will be filled in by separate edits to this file.
    # Sanity: if no templates yet, still write to test framework.
    if not TEMPLATES:
        # placeholder so file loads
        add('blank', '空白画板', 'other', '<g><rect class="fillable" fill="#ffffff" x="0" y="0" width="400" height="300"/></g>')
    write_html()
