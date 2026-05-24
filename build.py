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
    ('animal',  '🐾 动物'),
    ('ocean',   '🌊 海洋'),
    ('fantasy', '🦕 童话奇幻'),
    ('vehicle', '🚗 交通工具'),
    ('nature',  '🌸 自然'),
    ('food',    '🍰 食物'),
    ('other',   '🎉 节日和其他'),
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
    ('solid',   '纯色',   None),  # special: solid is the default mode
    ('dots',    '圆点',   '<pattern id="pat-dots" patternUnits="userSpaceOnUse" width="14" height="14"><rect width="14" height="14" fill="__BG__"/><circle cx="7" cy="7" r="2.5" fill="__FG__"/></pattern>'),
    ('stripes', '斜条纹', '<pattern id="pat-stripes" patternUnits="userSpaceOnUse" width="12" height="12" patternTransform="rotate(45)"><rect width="12" height="12" fill="__BG__"/><rect x="0" y="0" width="6" height="12" fill="__FG__"/></pattern>'),
    ('grid',    '网格',   '<pattern id="pat-grid" patternUnits="userSpaceOnUse" width="14" height="14"><rect width="14" height="14" fill="__BG__"/><path d="M0 0 H14 M0 0 V14" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
    ('zigzag',  '锯齿',   '<pattern id="pat-zigzag" patternUnits="userSpaceOnUse" width="16" height="10"><rect width="16" height="10" fill="__BG__"/><path d="M0 8 L4 2 L8 8 L12 2 L16 8" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
    ('hearts',  '小爱心', '<pattern id="pat-hearts" patternUnits="userSpaceOnUse" width="18" height="18"><rect width="18" height="18" fill="__BG__"/><path d="M9 14 Q3 9 6 5 Q9 4 9 7 Q9 4 12 5 Q15 9 9 14 Z" fill="__FG__"/></pattern>'),
    ('stars',   '小星星', '<pattern id="pat-stars" patternUnits="userSpaceOnUse" width="20" height="20"><rect width="20" height="20" fill="__BG__"/><path d="M10 3 L12 8 L17 8 L13 11 L14 16 L10 13 L6 16 L7 11 L3 8 L8 8 Z" fill="__FG__"/></pattern>'),
    ('scales',  '鱼鳞',   '<pattern id="pat-scales" patternUnits="userSpaceOnUse" width="14" height="10"><rect width="14" height="10" fill="__BG__"/><path d="M-1 10 A8 8 0 0 1 15 10" stroke="__FG__" stroke-width="2" fill="none"/><path d="M7 10 A8 8 0 0 1 23 10" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
    ('waves',   '波浪',   '<pattern id="pat-waves" patternUnits="userSpaceOnUse" width="20" height="10"><rect width="20" height="10" fill="__BG__"/><path d="M0 5 Q5 0 10 5 Q15 10 20 5" stroke="__FG__" stroke-width="2" fill="none"/></pattern>'),
]

# ============================================================================
# Color palette (kid-friendly)
# ============================================================================
PALETTE = [
    '#ff3b30','#ff9500','#ffcc00','#34c759','#00c7be',
    '#4ab3ff','#5856d6','#af52de','#ff2d92','#a0522d',
    '#1a1a1a','#8e8e93','#ffffff','#f5e6cb','#ffd1a3',
    '#ffb6d9','#a5d8ff','#b8e0a3','#fff3a0','#d4b3ff',
]

# Below this point: write_html() composes everything into the final file.
# All templates/stamps must be filled in before write_html() runs.

# =============================================================================
# Populate templates  (filled by separate edits below this block)
# =============================================================================

# --- Animals (10) ---
add('panda', '🐼 熊猫吃竹子', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <g stroke-width="2"><line x1="55" y1="20" x2="55" y2="26"/><line x1="55" y1="74" x2="55" y2="80"/><line x1="25" y1="50" x2="31" y2="50"/><line x1="79" y1="50" x2="85" y2="50"/><line x1="32" y1="27" x2="36" y2="32"/><line x1="74" y1="68" x2="78" y2="73"/><line x1="78" y1="27" x2="74" y2="32"/><line x1="36" y1="68" x2="32" y2="73"/></g>
  <path class="fillable" fill="#ffffff" d="M285 60 Q300 45 320 50 Q340 40 355 55 Q365 60 360 70 L285 70 Q275 65 285 60 Z"/>
  <rect class="fillable" fill="#ffffff" x="20" y="160" width="14" height="120"/>
  <g stroke-width="1.5" fill="none"><line x1="20" y1="190" x2="34" y2="190"/><line x1="20" y1="225" x2="34" y2="225"/><line x1="20" y1="260" x2="34" y2="260"/></g>
  <path class="fillable" fill="#ffffff" d="M34 175 Q52 168 62 178 Q48 184 34 182 Z"/>
  <path class="fillable" fill="#ffffff" d="M34 215 Q52 208 62 218 Q48 224 34 222 Z"/>
  <rect class="fillable" fill="#ffffff" x="366" y="140" width="14" height="140"/>
  <g stroke-width="1.5" fill="none"><line x1="366" y1="175" x2="380" y2="175"/><line x1="366" y1="210" x2="380" y2="210"/><line x1="366" y1="245" x2="380" y2="245"/></g>
  <path class="fillable" fill="#ffffff" d="M366 155 Q348 148 338 158 Q352 164 366 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M366 195 Q348 188 338 198 Q352 204 366 202 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="220" rx="78" ry="52"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="230" rx="42" ry="28"/>
  <circle class="fillable" fill="#ffffff" cx="218" cy="218" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="185" cy="225" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="205" cy="240" r="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="145" cy="205" rx="26" ry="17"/>
  <ellipse class="fillable" fill="#ffffff" cx="255" cy="205" rx="26" ry="17"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="266" rx="22" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="230" cy="266" rx="22" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="268" rx="13" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="230" cy="268" rx="13" ry="8"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="130" r="64"/>
  <circle class="fillable" fill="#ffffff" cx="150" cy="84" r="20"/>
  <circle class="fillable" fill="#ffffff" cx="250" cy="84" r="20"/>
  <ellipse class="fillable" fill="#ffffff" cx="173" cy="123" rx="12" ry="16" transform="rotate(-15 173 123)"/>
  <ellipse class="fillable" fill="#ffffff" cx="227" cy="123" rx="12" ry="16" transform="rotate(15 227 123)"/>
  <circle class="fillable" fill="#ffffff" cx="175" cy="120" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="120" r="5"/>
  <circle fill="#1a1a1a" cx="176" cy="122" r="2.5"/>
  <circle fill="#1a1a1a" cx="224" cy="122" r="2.5"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="148" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="148" r="6"/>
  <path class="fillable" fill="#ffffff" d="M193 146 Q200 154 207 146 Q204 141 200 141 Q196 141 193 146 Z"/>
  <line x1="200" y1="154" x2="200" y2="161"/>
  <path fill="none" d="M200 161 Q192 168 187 164"/>
  <path fill="none" d="M200 161 Q208 168 213 164"/>
  <rect class="fillable" fill="#ffffff" x="178" y="195" width="44" height="12"/>
  <g stroke-width="1.5" fill="none"><line x1="195" y1="195" x2="195" y2="207"/><line x1="208" y1="195" x2="208" y2="207"/></g>
  <path class="fillable" fill="#ffffff" d="M222 195 Q235 185 245 195 Q235 205 222 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M222 207 Q235 215 245 207 Q235 200 222 205 Z"/>
</g>
''')

add('lion', '🦁 小狮子', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="50" r="20"/>
  <g stroke-width="2"><line x1="345" y1="20" x2="345" y2="26"/><line x1="345" y1="74" x2="345" y2="80"/><line x1="315" y1="50" x2="321" y2="50"/><line x1="369" y1="50" x2="375" y2="50"/></g>
  <path class="fillable" fill="#ffffff" d="M50 55 Q65 40 85 45 Q105 35 120 55 Q135 55 130 70 L50 70 Q40 65 50 55 Z"/>
  <g stroke-width="2" fill="none"><path d="M20 280 Q25 270 30 280"/><path d="M40 285 Q45 270 50 285"/><path d="M340 285 Q345 270 350 285"/><path d="M370 280 Q375 270 380 280"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="222" rx="78" ry="48"/>
  <path class="fillable" fill="#ffffff" d="M275 218 Q310 198 320 178 Q315 200 295 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M315 180 Q325 164 322 154 Q310 164 313 177 Z"/>
  <path class="fillable" fill="#ffffff" d="M152 252 L148 280 L172 280 L178 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M222 254 L228 280 L252 280 L246 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M128 130 L108 122 L120 138 L102 144 L122 152 L102 158 L122 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 70 L122 58 L142 62 L132 42 L156 55 L150 36 L168 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 52 L168 35 L188 42 L195 28 L205 28 L212 42 L232 35 L220 52 Z"/>
  <path class="fillable" fill="#ffffff" d="M260 70 L278 58 L258 62 L268 42 L244 55 L250 36 L232 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M272 130 L292 122 L280 138 L298 144 L278 152 L298 158 L278 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M260 188 L278 195 L258 195 L278 208 L260 203 L270 218 L250 202 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 188 L122 195 L142 195 L122 208 L140 203 L130 218 L150 202 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="135" r="42"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="155" rx="22" ry="16"/>
  <circle class="fillable" fill="#ffffff" cx="183" cy="125" r="7"/>
  <circle class="fillable" fill="#ffffff" cx="217" cy="125" r="7"/>
  <circle fill="#1a1a1a" cx="185" cy="127" r="3"/>
  <circle fill="#1a1a1a" cx="215" cy="127" r="3"/>
  <path fill="none" d="M175 113 Q183 108 191 113"/>
  <path fill="none" d="M209 113 Q217 108 225 113"/>
  <path class="fillable" fill="#ffffff" d="M193 148 Q200 156 207 148 Q204 144 200 144 Q196 144 193 148 Z"/>
  <line x1="200" y1="156" x2="200" y2="164"/>
  <path fill="none" d="M200 164 Q190 172 185 166"/>
  <path fill="none" d="M200 164 Q210 172 215 166"/>
  <g stroke-width="1.5" fill="none"><line x1="180" y1="152" x2="160" y2="148"/><line x1="180" y1="158" x2="158" y2="160"/><line x1="220" y1="152" x2="240" y2="148"/><line x1="220" y1="158" x2="242" y2="160"/></g>
  <path class="fillable" fill="#ffffff" d="M165 92 Q160 78 178 82 Q175 95 170 95 Z"/>
  <path class="fillable" fill="#ffffff" d="M235 92 Q240 78 222 82 Q225 95 230 95 Z"/>
</g>
''')

add('tiger', '🐯 老虎', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <g stroke-width="2" fill="none"><path d="M15 285 Q22 273 28 285"/><path d="M40 285 Q47 273 53 285"/><path d="M350 285 Q357 273 363 285"/><path d="M375 285 Q382 273 388 285"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="220" rx="80" ry="50"/>
  <path class="fillable" fill="#ffffff" d="M280 220 Q310 205 322 180 Q325 200 305 222 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 252 L146 282 L172 282 L178 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M222 254 L228 282 L254 282 L250 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 196 Q138 200 130 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 192 Q160 200 152 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 190 Q190 200 182 225 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 192 Q220 200 212 225 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 190 Q250 200 242 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M270 192 Q278 200 272 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M310 195 L316 210 L308 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M298 215 L304 222 L298 228 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="135" r="62"/>
  <path class="fillable" fill="#ffffff" d="M138 95 L130 75 L155 80 Z"/>
  <path class="fillable" fill="#ffffff" d="M262 95 L270 75 L245 80 Z"/>
  <circle class="fillable" fill="#ffffff" cx="140" cy="90" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="260" cy="90" r="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="155" rx="36" ry="22"/>
  <path class="fillable" fill="#ffffff" d="M148 110 L158 122 L148 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M252 110 L242 122 L252 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 145 L162 152 L150 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 145 L238 152 L250 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 92 L200 105 L205 92 Z"/>
  <circle class="fillable" fill="#ffffff" cx="183" cy="130" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="217" cy="130" r="8"/>
  <circle fill="#1a1a1a" cx="184" cy="132" r="3"/>
  <circle fill="#1a1a1a" cx="216" cy="132" r="3"/>
  <path class="fillable" fill="#ffffff" d="M192 152 Q200 160 208 152 Q204 147 200 147 Q196 147 192 152 Z"/>
  <line x1="200" y1="160" x2="200" y2="168"/>
  <path fill="none" d="M200 168 Q190 175 184 170"/>
  <path fill="none" d="M200 168 Q210 175 216 170"/>
  <g stroke-width="1.5" fill="none"><line x1="178" y1="155" x2="155" y2="150"/><line x1="178" y1="160" x2="155" y2="163"/><line x1="222" y1="155" x2="245" y2="150"/><line x1="222" y1="160" x2="245" y2="163"/></g>
</g>
''')

add('penguin', '🐧 小企鹅', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="60" cy="50" r="20"/>
  <g stroke-width="1.5">
    <g transform="translate(120 50)" fill="none"><line x1="0" y1="-6" x2="0" y2="6"/><line x1="-6" y1="0" x2="6" y2="0"/><line x1="-4" y1="-4" x2="4" y2="4"/><line x1="-4" y1="4" x2="4" y2="-4"/></g>
    <g transform="translate(290 70)" fill="none"><line x1="0" y1="-6" x2="0" y2="6"/><line x1="-6" y1="0" x2="6" y2="0"/><line x1="-4" y1="-4" x2="4" y2="4"/><line x1="-4" y1="4" x2="4" y2="-4"/></g>
    <g transform="translate(340 130)" fill="none"><line x1="0" y1="-5" x2="0" y2="5"/><line x1="-5" y1="0" x2="5" y2="0"/></g>
    <g transform="translate(60 140)" fill="none"><line x1="0" y1="-5" x2="0" y2="5"/><line x1="-5" y1="0" x2="5" y2="0"/></g>
    <g transform="translate(180 95)" fill="none"><line x1="0" y1="-5" x2="0" y2="5"/><line x1="-5" y1="0" x2="5" y2="0"/></g>
    <g transform="translate(230 50)" fill="none"><line x1="0" y1="-5" x2="0" y2="5"/><line x1="-5" y1="0" x2="5" y2="0"/></g>
  </g>
  <path class="fillable" fill="#ffffff" d="M0 200 Q40 195 80 200 Q120 205 160 200 Q200 195 240 200 Q280 205 320 200 Q360 195 400 200 L400 245 L0 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M270 200 L305 145 L340 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M280 200 L305 175 L320 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M30 250 Q60 240 90 250 L90 270 L30 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M310 248 Q340 240 370 248 L370 268 L310 268 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="195" rx="62" ry="75"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="205" rx="40" ry="58"/>
  <path class="fillable" fill="#ffffff" d="M145 180 Q122 200 128 240 Q145 225 158 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M255 180 Q278 200 272 240 Q255 225 242 200 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="115" rx="46" ry="48"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="125" rx="30" ry="30"/>
  <circle class="fillable" fill="#ffffff" cx="185" cy="113" r="7"/>
  <circle class="fillable" fill="#ffffff" cx="215" cy="113" r="7"/>
  <circle fill="#1a1a1a" cx="187" cy="115" r="3"/>
  <circle fill="#1a1a1a" cx="213" cy="115" r="3"/>
  <path class="fillable" fill="#ffffff" d="M192 132 L208 132 L200 150 Z"/>
  <circle class="fillable" fill="#ffffff" cx="174" cy="135" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="226" cy="135" r="6"/>
  <path class="fillable" fill="#ffffff" d="M168 268 Q158 278 163 285 L195 285 Q200 278 195 268 Z"/>
  <path class="fillable" fill="#ffffff" d="M205 268 Q200 278 205 285 L237 285 Q242 278 232 268 Z"/>
  <path class="fillable" fill="#ffffff" d="M162 165 Q170 175 200 175 Q230 175 238 165 L238 180 Q200 190 162 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 180 L218 205 L232 205 L222 180 Z"/>
</g>
''')

add('cat', '🐱 小猫和毛线球', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="55" r="20"/>
  <g stroke-width="2"><line x1="345" y1="25" x2="345" y2="31"/><line x1="345" y1="79" x2="345" y2="85"/><line x1="315" y1="55" x2="321" y2="55"/><line x1="369" y1="55" x2="375" y2="55"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="220" rx="80" ry="42"/>
  <path class="fillable" fill="#ffffff" d="M120 230 Q90 195 95 165 Q100 185 115 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 254 L150 280 L172 280 L178 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M194 256 L189 280 L211 280 L216 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M230 256 L228 280 L250 280 L252 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 198 L155 198 L150 215 L145 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 200 L185 200 L180 215 L175 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 200 L215 200 L210 215 L205 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M230 200 L245 200 L240 215 L235 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M260 200 L275 200 L265 215 L260 215 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="145" r="55"/>
  <path class="fillable" fill="#ffffff" d="M155 105 L165 75 L188 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M245 105 L235 75 L212 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 100 L170 90 L180 95 Z"/>
  <path class="fillable" fill="#ffffff" d="M242 100 L230 90 L220 95 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="140" rx="8" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="140" rx="8" ry="10"/>
  <ellipse fill="#1a1a1a" cx="180" cy="142" rx="2.5" ry="6"/>
  <ellipse fill="#1a1a1a" cx="220" cy="142" rx="2.5" ry="6"/>
  <path class="fillable" fill="#ffffff" d="M195 158 L205 158 L200 167 Z"/>
  <line x1="200" y1="167" x2="200" y2="173"/>
  <path fill="none" d="M200 173 Q193 178 188 175"/>
  <path fill="none" d="M200 173 Q207 178 212 175"/>
  <g stroke-width="1.5" fill="none"><line x1="190" y1="163" x2="170" y2="160"/><line x1="190" y1="168" x2="170" y2="170"/><line x1="210" y1="163" x2="230" y2="160"/><line x1="210" y1="168" x2="230" y2="170"/></g>
  <circle class="fillable" fill="#ffffff" cx="320" cy="240" r="28"/>
  <g stroke-width="1.5" fill="none"><path d="M295 230 Q320 220 345 234"/><path d="M295 240 Q320 232 345 245"/><path d="M295 250 Q320 244 345 255"/><path d="M310 218 Q325 245 340 260"/><path d="M308 222 Q330 232 335 258"/></g>
  <path fill="none" d="M348 240 Q380 235 390 260"/>
</g>
''')

add('dog', '🐶 小狗和骨头', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="60" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 60 Q295 45 315 50 Q335 40 350 55 Q365 60 360 70 L280 70 Q270 65 280 60 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="220" rx="80" ry="48"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="235" rx="48" ry="28"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="208" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="218" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="155" cy="240" r="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="260" cy="225" rx="8" ry="14" transform="rotate(-30 260 225)"/>
  <path class="fillable" fill="#ffffff" d="M278 205 Q300 188 305 168 Q298 188 280 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 256 L150 280 L175 280 L180 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M212 258 L210 280 L235 280 L237 256 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="145" r="58"/>
  <path class="fillable" fill="#ffffff" d="M148 130 Q125 145 132 175 Q150 168 158 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M252 130 Q275 145 268 175 Q250 168 242 145 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="165" rx="28" ry="20"/>
  <circle class="fillable" fill="#ffffff" cx="183" cy="135" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="217" cy="135" r="8"/>
  <circle fill="#1a1a1a" cx="184" cy="137" r="3"/>
  <circle fill="#1a1a1a" cx="216" cy="137" r="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="160" rx="8" ry="6"/>
  <path class="fillable" fill="#ffffff" d="M192 174 Q200 200 208 174 Q210 184 200 188 Q190 184 192 174 Z"/>
  <path fill="none" d="M192 174 Q200 180 208 174"/>
  <path class="fillable" fill="#ffffff" d="M70 230 Q60 222 65 215 Q75 215 78 222 L100 222 Q103 215 113 215 Q118 222 108 230 Q118 238 113 245 Q103 245 100 238 L78 238 Q75 245 65 245 Q60 238 70 230 Z"/>
</g>
''')

add('rabbit', '🐰 小兔子和胡萝卜', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M50 60 Q65 45 85 50 Q105 40 120 55 Q135 60 130 70 L50 70 Q40 65 50 60 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="225" rx="68" ry="48"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="238" rx="38" ry="25"/>
  <path class="fillable" fill="#ffffff" d="M155 258 L150 282 L172 282 L178 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M212 260 L210 282 L232 282 L237 258 Z"/>
  <circle class="fillable" fill="#ffffff" cx="252" cy="218" r="13"/>
  <circle class="fillable" fill="#ffffff" cx="195" cy="150" r="50"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="80" rx="13" ry="38"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="80" rx="13" ry="38"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="85" rx="7" ry="28"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="85" rx="7" ry="28"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="140" r="7"/>
  <circle class="fillable" fill="#ffffff" cx="210" cy="140" r="7"/>
  <circle fill="#1a1a1a" cx="181" cy="142" r="3"/>
  <circle fill="#1a1a1a" cx="211" cy="142" r="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="160" rx="5" ry="4"/>
  <line x1="195" y1="164" x2="195" y2="172"/>
  <path fill="none" d="M195 172 Q188 178 183 173"/>
  <path fill="none" d="M195 172 Q202 178 207 173"/>
  <g stroke-width="1.5" fill="none"><line x1="187" y1="160" x2="168" y2="158"/><line x1="187" y1="165" x2="167" y2="170"/><line x1="203" y1="160" x2="222" y2="158"/><line x1="203" y1="165" x2="223" y2="170"/></g>
  <circle class="fillable" fill="#ffffff" cx="178" cy="155" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="212" cy="155" r="5"/>
  <path class="fillable" fill="#ffffff" d="M285 250 L325 230 L335 260 L295 280 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="293" y1="248" x2="324" y2="232"/><line x1="298" y1="258" x2="328" y2="240"/><line x1="304" y1="268" x2="333" y2="252"/></g>
  <path class="fillable" fill="#ffffff" d="M323 232 Q335 215 350 222 Q345 230 335 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M328 228 Q336 210 348 213 Q344 222 338 230 Z"/>
</g>
''')

add('fox', '🦊 小狐狸', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 60 Q295 45 315 50 Q335 40 350 55 Q365 60 360 70 L280 70 Q270 65 280 60 Z"/>
  <g stroke-width="2" fill="none"><path d="M25 285 Q30 275 35 285"/><path d="M45 285 Q50 273 55 285"/><path d="M345 285 Q350 275 355 285"/><path d="M365 285 Q370 273 375 285"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="218" rx="74" ry="42"/>
  <path class="fillable" fill="#ffffff" d="M170 200 Q195 210 220 200 L220 245 Q195 250 170 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 248 L150 282 L172 282 L178 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M212 250 L210 282 L232 282 L237 248 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 220 Q310 195 325 158 Q318 180 308 205 Q318 222 305 240 Q288 240 270 232 Z"/>
  <path class="fillable" fill="#ffffff" d="M315 162 Q322 155 326 158 Q325 175 320 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 100 Q160 130 165 165 Q175 155 195 152 Q215 155 225 165 Q230 130 195 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 100 L170 78 L178 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 100 L220 78 L212 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 92 L182 80 L188 92 Z"/>
  <path class="fillable" fill="#ffffff" d="M212 92 L208 80 L202 92 Z"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="135" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="210" cy="135" r="6"/>
  <circle fill="#1a1a1a" cx="181" cy="137" r="2.5"/>
  <circle fill="#1a1a1a" cx="211" cy="137" r="2.5"/>
  <path class="fillable" fill="#ffffff" d="M188 158 L202 158 L195 168 Z"/>
  <line x1="195" y1="168" x2="195" y2="175"/>
  <path fill="none" d="M195 175 Q190 180 185 177"/>
  <path fill="none" d="M195 175 Q200 180 205 177"/>
  <path class="fillable" fill="#ffffff" d="M170 150 Q180 152 188 158 L188 160 Q175 156 170 154 Z"/>
  <path class="fillable" fill="#ffffff" d="M220 150 Q210 152 202 158 L202 160 Q215 156 220 154 Z"/>
</g>
''')

add('elephant', '🐘 大象洗澡', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 55 Q295 40 315 45 Q335 35 350 50 Q365 55 360 65 L280 65 Q270 60 280 55 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="200" rx="90" ry="55"/>
  <path class="fillable" fill="#ffffff" d="M135 195 L130 270 L170 270 L172 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 215 L178 270 L210 270 L210 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M220 215 L222 270 L252 270 L250 215 Z"/>
  <g stroke-width="1.5" fill="none">
    <line x1="138" y1="266" x2="142" y2="270"/><line x1="148" y1="266" x2="152" y2="270"/><line x1="158" y1="266" x2="162" y2="270"/>
    <line x1="184" y1="266" x2="188" y2="270"/><line x1="194" y1="266" x2="198" y2="270"/><line x1="204" y1="266" x2="208" y2="270"/>
    <line x1="226" y1="266" x2="230" y2="270"/><line x1="236" y1="266" x2="240" y2="270"/><line x1="246" y1="266" x2="250" y2="270"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M285 180 Q310 180 305 220 L290 220 Q288 200 280 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 165 Q70 165 65 215 Q100 195 115 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 165 Q90 145 100 175 Q110 175 118 175 Z"/>
  <circle class="fillable" fill="#ffffff" cx="155" cy="170" r="6"/>
  <circle fill="#1a1a1a" cx="155" cy="172" r="2.5"/>
  <path class="fillable" fill="#ffffff" d="M140 200 Q150 205 145 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 200 Q175 205 170 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 188 Q100 200 95 220 Q105 230 115 218 Q125 225 130 215 Q120 205 115 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M118 218 Q108 232 110 245 Q120 240 125 228 Z"/>
  <g>
    <circle class="fillable" fill="#ffffff" cx="80" cy="170" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="65" cy="155" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="55" cy="140" r="3"/>
    <circle class="fillable" fill="#ffffff" cx="85" cy="140" r="3"/>
    <circle class="fillable" fill="#ffffff" cx="50" cy="120" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="70" cy="115" r="3"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M260 230 Q280 235 280 250 Q260 250 258 240 Z"/>
</g>
''')

add('owl', '🦉 猫头鹰', 'animal', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5">
    <path class="fillable" fill="#ffffff" d="M50 45 L52 52 L60 52 L54 56 L56 64 L50 60 L44 64 L46 56 L40 52 L48 52 Z"/>
    <path class="fillable" fill="#ffffff" d="M340 50 L342 57 L350 57 L344 61 L346 69 L340 65 L334 69 L336 61 L330 57 L338 57 Z"/>
    <path class="fillable" fill="#ffffff" d="M70 130 L72 137 L80 137 L74 141 L76 149 L70 145 L64 149 L66 141 L60 137 L68 137 Z"/>
    <circle class="fillable" fill="#ffffff" cx="350" cy="135" r="3"/>
    <circle class="fillable" fill="#ffffff" cx="40" cy="200" r="2.5"/>
    <circle class="fillable" fill="#ffffff" cx="370" cy="220" r="2.5"/>
  </g>
  <circle class="fillable" fill="#ffffff" cx="345" cy="60" r="20"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="175" rx="68" ry="80"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="200" rx="40" ry="55"/>
  <path class="fillable" fill="#ffffff" d="M132 175 Q120 200 130 240 Q142 220 152 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 175 Q280 200 270 240 Q258 220 248 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M135 105 L150 120 L142 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M265 105 L250 120 L258 130 Z"/>
  <circle class="fillable" fill="#ffffff" cx="175" cy="140" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="140" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="175" cy="140" r="14"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="140" r="14"/>
  <circle fill="#1a1a1a" cx="175" cy="142" r="7"/>
  <circle fill="#1a1a1a" cx="225" cy="142" r="7"/>
  <circle fill="#ffffff" cx="172" cy="139" r="2"/>
  <circle fill="#ffffff" cx="222" cy="139" r="2"/>
  <path class="fillable" fill="#ffffff" d="M193 162 L207 162 L200 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 215 Q200 220 235 215 Q230 235 200 240 Q170 235 165 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 240 Q200 245 222 240 Q218 252 200 255 Q182 252 178 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 255 L175 268 L188 268 L192 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M220 255 L225 268 L212 268 L208 258 Z"/>
  <rect class="fillable" fill="#ffffff" x="80" y="265" width="240" height="14" rx="4"/>
  <g stroke-width="1.5" fill="none"><line x1="100" y1="265" x2="105" y2="279"/><line x1="140" y1="265" x2="145" y2="279"/><line x1="180" y1="265" x2="185" y2="279"/><line x1="220" y1="265" x2="225" y2="279"/><line x1="260" y1="265" x2="265" y2="279"/><line x1="300" y1="265" x2="305" y2="279"/></g>
</g>
''')

# --- Ocean (6) ---
add('ocean', '🐠 海底世界', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke="#9bd0ff" stroke-width="2" stroke-dasharray="6 6" fill="none"><line x1="60" y1="0" x2="80" y2="80"/><line x1="180" y1="0" x2="160" y2="100"/><line x1="320" y1="0" x2="340" y2="90"/></g>
  <path class="fillable" fill="#ffffff" d="M0 250 Q80 235 160 245 Q240 258 320 240 Q380 245 400 252 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M55 248 Q48 220 60 200 Q70 215 78 220 Q82 200 88 218 Q95 205 95 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M325 248 Q318 232 330 222 Q340 215 350 228 Q360 220 368 235 Q375 240 365 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M125 248 Q118 220 128 195 Q120 175 132 155 Q126 138 138 125 Q145 130 140 148 Q148 172 138 195 Q148 220 138 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M275 248 Q280 220 270 195 Q280 170 268 145 L272 145 Q282 170 274 195 Q283 220 278 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 150 Q240 100 170 105 Q110 115 110 150 Q110 185 170 195 Q240 200 250 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 150 Q295 110 320 105 Q310 150 320 195 Q295 190 250 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 110 Q180 80 200 82 Q215 95 218 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M175 190 Q185 220 200 217 Q215 207 218 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 110 Q170 150 165 192 L185 190 Q190 150 185 112 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 113 Q215 150 210 188 L228 185 Q233 150 228 115 Z"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="140" r="11"/>
  <circle fill="#1a1a1a" cx="135" cy="143" r="4"/>
  <path fill="none" d="M112 152 Q105 156 112 160"/>
  <ellipse class="fillable" fill="#ffffff" cx="60" cy="100" rx="32" ry="28"/>
  <path class="fillable" fill="#ffffff" d="M30 115 Q14 145 26 170 Q18 145 32 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M45 128 Q40 160 56 175 Q44 150 52 132 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 132 Q60 168 72 182 Q60 158 65 132 Z"/>
  <path class="fillable" fill="#ffffff" d="M75 130 Q88 158 74 178 Q82 155 80 132 Z"/>
  <path class="fillable" fill="#ffffff" d="M88 120 Q108 142 100 168 Q102 145 92 130 Z"/>
  <circle class="fillable" fill="#ffffff" cx="50" cy="95" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="70" cy="95" r="5"/>
  <circle fill="#1a1a1a" cx="50" cy="96" r="2.5"/>
  <circle fill="#1a1a1a" cx="70" cy="96" r="2.5"/>
  <path class="fillable" fill="#ffffff" d="M340 65 Q335 50 320 50 Q305 55 305 65 Q305 78 320 82 Q335 80 340 65 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 65 Q352 55 362 53 Q357 65 362 80 Q352 78 340 65 Z"/>
  <circle fill="#1a1a1a" cx="313" cy="63" r="2"/>
  <path class="fillable" fill="#ffffff" d="M200 258 L208 244 L224 244 L211 254 L218 270 L200 260 L182 270 L189 254 L176 244 L192 244 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="105" cy="45" r="8"/><circle class="fillable" fill="#ffffff" cx="122" cy="25" r="5"/><circle class="fillable" fill="#ffffff" cx="98" cy="20" r="4"/><circle class="fillable" fill="#ffffff" cx="260" cy="40" r="6"/><circle class="fillable" fill="#ffffff" cx="245" cy="20" r="4"/></g>
</g>
''')

add('whale', '🐋 鲸鱼', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 55 Q295 40 315 45 Q335 35 350 50 Q365 55 360 65 L280 65 Q270 60 280 55 Z"/>
  <path class="fillable" fill="#ffffff" d="M40 220 Q90 225 140 220 Q190 215 240 220 Q290 225 360 220 L360 240 L40 240 Z"/>
  <g stroke-width="2" fill="none"><path d="M40 245 Q90 250 140 245 Q190 240 240 245 Q290 250 360 245"/><path d="M40 265 Q90 270 140 265 Q190 260 240 265 Q290 270 360 265"/><path d="M40 285 Q90 290 140 285 Q190 280 240 285 Q290 290 360 285"/></g>
  <path class="fillable" fill="#ffffff" d="M65 200 Q40 130 130 110 Q230 100 295 150 Q330 165 335 195 Q330 215 280 215 L80 215 Q55 215 65 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M335 195 Q360 175 370 145 Q360 185 350 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M335 195 Q360 215 370 245 Q358 210 348 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M225 215 Q235 235 250 230 Q260 220 255 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M85 215 L95 225 L90 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M115 215 L125 225 L120 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M145 215 L155 225 L150 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M175 215 L185 225 L180 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M205 215 L215 225 L210 215 Z"/>
  <circle class="fillable" fill="#ffffff" cx="105" cy="160" r="7"/>
  <circle fill="#1a1a1a" cx="106" cy="162" r="3"/>
  <path fill="none" d="M70 175 Q60 180 65 188"/>
  <path class="fillable" fill="#ffffff" d="M155 130 Q160 100 165 90 Q170 100 175 130 Z"/>
  <circle class="fillable" fill="#ffffff" cx="155" cy="80" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="65" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="50" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="195" cy="40" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="145" cy="55" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="35" r="4"/>
</g>
''')

add('octopus', '🐙 章鱼', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke="#9bd0ff" stroke-width="2" stroke-dasharray="6 6" fill="none"><line x1="100" y1="0" x2="120" y2="80"/><line x1="300" y1="0" x2="280" y2="90"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="130" rx="80" ry="68"/>
  <path class="fillable" fill="#ffffff" d="M165 50 L170 25 L195 35 Q198 30 210 32 L222 22 L228 48 Q235 38 245 45 L242 65 Q235 55 225 60 L210 50 L200 60 L185 50 L172 58 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="118" rx="14" ry="16"/>
  <ellipse class="fillable" fill="#ffffff" cx="228" cy="118" rx="14" ry="16"/>
  <circle class="fillable" fill="#ffffff" cx="172" cy="122" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="228" cy="122" r="6"/>
  <circle fill="#1a1a1a" cx="172" cy="124" r="3"/>
  <circle fill="#1a1a1a" cx="228" cy="124" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="155" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="155" r="6"/>
  <path fill="none" d="M188 165 Q200 175 212 165"/>
  <path class="fillable" fill="#ffffff" d="M125 175 Q90 200 100 240 Q120 220 130 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M148 188 Q130 230 150 270 Q156 235 165 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M175 195 Q170 240 195 280 Q188 240 188 205 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 198 Q200 245 220 280 Q215 240 215 205 Z"/>
  <path class="fillable" fill="#ffffff" d="M225 195 Q230 240 245 270 Q244 235 238 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M252 188 Q270 230 250 270 Q244 235 235 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M275 175 Q310 200 300 240 Q280 220 270 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 178 Q140 165 130 175 Q145 185 158 188 Z"/>
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="125" cy="220" r="3"/><circle class="fillable" fill="#ffffff" cx="155" cy="245" r="3"/><circle class="fillable" fill="#ffffff" cx="180" cy="260" r="3"/><circle class="fillable" fill="#ffffff" cx="215" cy="260" r="3"/><circle class="fillable" fill="#ffffff" cx="240" cy="250" r="3"/><circle class="fillable" fill="#ffffff" cx="285" cy="225" r="3"/></g>
  <g><circle class="fillable" fill="#ffffff" cx="320" cy="80" r="6"/><circle class="fillable" fill="#ffffff" cx="335" cy="55" r="4"/><circle class="fillable" fill="#ffffff" cx="60" cy="90" r="5"/><circle class="fillable" fill="#ffffff" cx="50" cy="65" r="3"/></g>
</g>
''')

add('dolphin', '🐬 海豚跳跃', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="50" r="20"/>
  <path class="fillable" fill="#ffffff" d="M50 60 Q65 45 85 50 Q105 40 120 55 Q135 60 130 70 L50 70 Q40 65 50 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 230 Q40 220 80 230 Q120 240 160 230 Q200 220 240 230 Q280 240 320 230 Q360 220 400 230 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 250 Q40 240 80 250 Q120 260 160 250 Q200 240 240 250 Q280 260 320 250 Q360 240 400 250"/><path d="M0 275 Q40 265 80 275 Q120 285 160 275 Q200 265 240 275 Q280 285 320 275 Q360 265 400 275"/></g>
  <path class="fillable" fill="#ffffff" d="M80 200 Q60 120 150 100 Q250 95 300 150 Q330 180 320 210 Q280 230 220 215 Q200 220 180 220 Q120 230 90 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M80 200 Q60 120 130 130 Q200 175 220 215 Q190 220 165 215 Q120 230 90 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 100 L185 70 L200 95 Z"/>
  <path class="fillable" fill="#ffffff" d="M280 195 Q295 180 295 165 Q310 175 315 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M320 210 Q345 195 355 175 Q345 220 320 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M320 210 Q345 230 360 240 Q340 240 320 230 Z"/>
  <circle class="fillable" fill="#ffffff" cx="120" cy="155" r="7"/>
  <circle fill="#1a1a1a" cx="121" cy="157" r="3"/>
  <path fill="none" d="M85 175 Q70 180 75 190"/>
  <path fill="none" d="M85 175 Q70 178 78 168"/>
  <g><circle class="fillable" fill="#ffffff" cx="60" cy="225" r="6"/><circle class="fillable" fill="#ffffff" cx="70" cy="210" r="4"/><circle class="fillable" fill="#ffffff" cx="350" cy="220" r="5"/><circle class="fillable" fill="#ffffff" cx="340" cy="205" r="3"/></g>
</g>
''')

add('crab', '🦀 螃蟹', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 230 Q60 220 120 230 Q180 240 240 230 Q300 220 400 230 L400 300 L0 300 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="70" cy="270" r="4"/><circle class="fillable" fill="#ffffff" cx="320" cy="265" r="3"/><circle class="fillable" fill="#ffffff" cx="350" cy="280" r="4"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="180" rx="92" ry="55"/>
  <path class="fillable" fill="#ffffff" d="M115 170 Q90 150 85 130 Q100 145 115 158 Z"/>
  <path class="fillable" fill="#ffffff" d="M285 170 Q310 150 315 130 Q300 145 285 158 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="80" cy="120" rx="20" ry="16" transform="rotate(-30 80 120)"/>
  <ellipse class="fillable" fill="#ffffff" cx="320" cy="120" rx="20" ry="16" transform="rotate(30 320 120)"/>
  <path fill="none" d="M70 110 Q75 130 90 125"/>
  <path fill="none" d="M330 110 Q325 130 310 125"/>
  <path class="fillable" fill="#ffffff" d="M120 200 L80 215 L88 235 L130 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 220 L100 250 L115 265 L150 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 230 L160 270 L180 270 L185 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M215 230 L220 270 L240 270 L235 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 230 L285 265 L300 250 L270 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M280 200 L320 215 L312 235 L270 215 Z"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="135" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="230" cy="135" r="6"/>
  <line x1="170" y1="141" x2="170" y2="165"/>
  <line x1="230" y1="141" x2="230" y2="165"/>
  <circle fill="#1a1a1a" cx="170" cy="135" r="2.5"/>
  <circle fill="#1a1a1a" cx="230" cy="135" r="2.5"/>
  <path fill="none" d="M185 200 Q200 210 215 200"/>
  <g stroke-width="1.5" fill="none"><line x1="150" y1="180" x2="160" y2="195"/><line x1="180" y1="178" x2="185" y2="195"/><line x1="220" y1="178" x2="215" y2="195"/><line x1="250" y1="180" x2="240" y2="195"/></g>
  <g><circle class="fillable" fill="#ffffff" cx="170" cy="195" r="2"/><circle class="fillable" fill="#ffffff" cx="200" cy="190" r="2"/><circle class="fillable" fill="#ffffff" cx="230" cy="195" r="2"/></g>
</g>
''')

add('jellyfish', '🪼 水母', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke="#9bd0ff" stroke-width="2" stroke-dasharray="6 6" fill="none"><line x1="60" y1="0" x2="60" y2="40"/><line x1="180" y1="0" x2="180" y2="35"/><line x1="320" y1="0" x2="320" y2="40"/></g>
  <path class="fillable" fill="#ffffff" d="M110 145 Q110 65 200 60 Q290 65 290 145 Q280 160 200 160 Q120 160 110 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 155 Q125 145 145 145 Q150 158 138 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 155 Q160 145 180 145 Q183 158 170 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 158 Q193 148 213 148 Q216 160 203 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M222 158 Q227 148 247 148 Q250 160 237 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M255 155 Q260 145 280 145 Q283 158 270 162 Z"/>
  <g>
    <circle class="fillable" fill="#ffffff" cx="155" cy="100" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="185" cy="110" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="215" cy="105" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="245" cy="115" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="200" cy="85" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="170" cy="125" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="230" cy="125" r="4"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M130 160 Q120 200 130 240 Q140 280 130 290 Q125 270 122 235 Q118 195 126 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 162 Q150 200 165 235 Q155 270 162 285 Q170 260 168 230 Q170 195 164 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M185 165 Q180 210 195 250 Q185 280 192 290 Q200 265 198 232 Q200 195 194 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M212 165 Q215 210 205 250 Q215 280 208 290 Q200 265 202 232 Q200 195 206 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M238 162 Q245 200 230 235 Q240 270 235 285 Q225 260 230 230 Q230 195 232 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 160 Q275 200 268 240 Q258 280 270 290 Q275 270 280 235 Q282 195 274 160 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="80" cy="60" r="6"/><circle class="fillable" fill="#ffffff" cx="100" cy="40" r="4"/><circle class="fillable" fill="#ffffff" cx="330" cy="50" r="5"/><circle class="fillable" fill="#ffffff" cx="345" cy="30" r="3"/></g>
</g>
''')

# --- Fantasy (7) ---
add('dinosaur', '🦖 霸王龙', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 240 L330 130 Q335 125 340 125 L345 130 L395 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M325 132 Q335 142 345 132 Q345 148 335 148 Q325 148 325 132 Z"/>
  <path class="fillable" fill="#ffffff" d="M328 148 Q335 158 342 148 L342 175 Q335 180 328 175 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="335" cy="105" rx="18" ry="12"/>
  <ellipse class="fillable" fill="#ffffff" cx="350" cy="80" rx="22" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="318" cy="62" rx="16" ry="10"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 232 200 240 Q300 250 400 235 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M35 240 Q30 200 35 170 Q40 165 50 170 Q55 200 50 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M42 170 Q15 158 5 132 Q22 148 38 162 Q18 132 28 105 Q38 128 44 158 Q60 130 82 130 Q62 145 50 165 Q75 145 95 152 Q72 162 50 168 Z"/>
  <g>
    <path class="fillable" fill="#ffffff" d="M260 50 Q280 42 295 48 Q302 42 305 50 Q295 58 285 60 L272 56 Z"/>
    <path class="fillable" fill="#ffffff" d="M272 56 Q280 64 290 64 L294 58 L286 54 Z"/>
    <circle fill="#1a1a1a" cx="297" cy="50" r="1.5"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M100 235 Q92 200 112 175 Q140 155 180 165 Q220 175 230 200 Q235 218 220 232 Z"/>
  <g>
    <path class="fillable" fill="#ffffff" d="M115 175 Q120 165 125 175 Q120 180 115 175 Z"/>
    <path class="fillable" fill="#ffffff" d="M135 168 Q140 158 145 168 Q140 173 135 168 Z"/>
    <path class="fillable" fill="#ffffff" d="M155 163 Q160 153 165 163 Q160 168 155 163 Z"/>
    <path class="fillable" fill="#ffffff" d="M175 162 Q180 152 185 162 Q180 167 175 162 Z"/>
    <path class="fillable" fill="#ffffff" d="M195 168 Q200 158 205 168 Q200 173 195 168 Z"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M90 195 Q40 192 10 215 Q35 210 60 212 Q85 212 102 212 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 188 Q220 145 270 142 Q310 148 320 175 L320 200 Q315 215 295 215 L240 215 Q220 215 212 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M258 198 Q295 198 322 192 L325 205 Q295 215 258 210 Z"/>
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M270 198 L274 210 L278 198 Z"/><path class="fillable" fill="#ffffff" d="M286 198 L290 210 L294 198 Z"/><path class="fillable" fill="#ffffff" d="M302 198 L306 210 L310 198 Z"/></g>
  <circle class="fillable" fill="#ffffff" cx="290" cy="170" r="6"/>
  <circle fill="#1a1a1a" cx="292" cy="171" r="2.5"/>
  <circle fill="#1a1a1a" cx="313" cy="175" r="1.5"/>
  <path class="fillable" fill="#ffffff" d="M195 215 Q190 225 192 235 L200 235 Q200 225 203 218 Z"/>
  <path class="fillable" fill="#ffffff" d="M138 232 Q133 252 128 270 L150 270 Q155 255 155 234 Z"/>
  <path class="fillable" fill="#ffffff" d="M185 235 Q180 255 175 270 L195 270 Q200 255 200 240 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="280" cy="270" rx="14" ry="18"/>
  <ellipse class="fillable" fill="#ffffff" cx="310" cy="275" rx="14" ry="18"/>
</g>
''')

add('dragon', '🐲 飞龙', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <g><circle class="fillable" fill="#ffffff" cx="350" cy="50" r="4"/><circle class="fillable" fill="#ffffff" cx="120" cy="40" r="3"/><circle class="fillable" fill="#ffffff" cx="280" cy="35" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M100 260 Q90 220 120 195 Q160 175 200 185 Q240 195 250 220 Q255 245 240 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 220 Q295 215 320 240 Q300 255 270 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M320 240 L345 230 L350 248 L335 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M335 252 L355 268 L348 275 L332 263 Z"/>
  <path class="fillable" fill="#ffffff" d="M115 195 Q90 160 95 130 Q75 155 80 195 Q70 230 90 240 Q92 215 115 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M105 175 L115 145 L125 165 L138 140 L142 168 L160 145 L160 178 Q142 180 130 184 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 175 L175 155 L185 168 L195 150 L200 168 L210 155 L218 170 L228 158 L232 175 L240 165 L240 188 Q205 195 175 192 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="160" cy="220" rx="35" ry="22"/>
  <path class="fillable" fill="#ffffff" d="M125 215 L150 195 L155 215 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="225" rx="32" ry="20"/>
  <path class="fillable" fill="#ffffff" d="M115 250 L122 270 L132 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M145 255 L152 275 L162 255 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 258 L202 278 L212 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M225 255 L232 275 L242 255 Z"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="208" r="5"/>
  <circle fill="#1a1a1a" cx="100" cy="209" r="2.5"/>
  <path fill="none" d="M85 215 Q80 220 85 225"/>
  <path class="fillable" fill="#ffffff" d="M88 192 L85 178 L95 190 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 188 L108 174 L118 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M55 220 Q40 215 30 220 Q35 235 50 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M40 230 Q25 232 20 245 Q35 250 45 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M55 245 Q40 250 32 262 Q50 268 60 255 Z"/>
</g>
''')

add('unicorn', '🦄 彩虹独角兽', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M60 40 L63 50 L73 50 L65 56 L68 66 L60 60 L52 66 L55 56 L47 50 L57 50 Z"/><path class="fillable" fill="#ffffff" d="M345 45 L348 55 L358 55 L350 61 L353 71 L345 65 L337 71 L340 61 L332 55 L342 55 Z"/><path class="fillable" fill="#ffffff" d="M30 130 L32 137 L40 137 L34 142 L36 149 L30 145 L24 149 L26 142 L20 137 L28 137 Z"/><path class="fillable" fill="#ffffff" d="M370 150 L372 157 L380 157 L374 162 L376 169 L370 165 L364 169 L366 162 L360 157 L368 157 Z"/></g>
  <path class="fillable" fill="#ffffff" d="M40 250 A155 155 0 0 1 360 250 L345 250 A140 140 0 0 0 55 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M55 250 A140 140 0 0 1 345 250 L330 250 A125 125 0 0 0 70 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M70 250 A125 125 0 0 1 330 250 L315 250 A110 110 0 0 0 85 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M85 250 A110 110 0 0 1 315 250 L300 250 A95 95 0 0 0 100 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M100 250 A95 95 0 0 1 300 250 L285 250 A80 80 0 0 0 115 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M115 250 A80 80 0 0 1 285 250 L270 250 A65 65 0 0 0 130 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M28 250 Q18 232 33 226 Q40 212 60 218 Q72 208 88 222 Q105 222 100 245 L92 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M308 250 Q302 228 318 222 Q330 210 348 220 Q368 218 365 240 Q372 250 360 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 270 Q100 260 200 270 Q300 280 400 265 L400 300 L0 300 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="205" rx="62" ry="35"/>
  <path class="fillable" fill="#ffffff" d="M245 198 Q258 178 268 158 Q280 148 292 158 Q296 168 290 178 L260 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M258 165 Q258 132 290 128 Q322 130 328 145 Q332 160 322 170 Q312 178 290 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M284 130 L290 108 L300 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M302 128 L308 95 L318 125 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="305" y1="118" x2="313" y2="118"/><line x1="306" y1="110" x2="312" y2="110"/></g>
  <circle fill="#1a1a1a" cx="305" cy="150" r="3"/>
  <circle fill="#1a1a1a" cx="324" cy="158" r="1.5"/>
  <path fill="none" d="M315 165 Q322 170 326 165"/>
  <path class="fillable" fill="#ffffff" d="M275 145 Q252 130 240 145 Q258 152 270 158 Z"/>
  <path class="fillable" fill="#ffffff" d="M258 165 Q232 168 230 182 Q252 178 263 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M248 182 Q220 188 220 205 Q243 200 253 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M242 200 Q215 208 220 220 Q240 215 250 208 Z"/>
  <path class="fillable" fill="#ffffff" d="M276 130 Q282 115 296 115 Q290 125 285 135 Z"/>
  <path class="fillable" fill="#ffffff" d="M148 200 Q126 184 128 168 Q140 178 154 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 212 Q120 208 115 222 Q135 222 154 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 222 Q128 232 124 246 Q146 240 160 228 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 233 L165 268 L182 268 L188 234 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 233 L195 268 L212 268 L218 234 Z"/>
  <path class="fillable" fill="#ffffff" d="M228 233 L226 268 L243 268 L246 234 Z"/>
  <path class="fillable" fill="#ffffff" d="M248 233 L253 268 L268 268 L264 234 Z"/>
  <rect class="fillable" fill="#ffffff" x="163" y="264" width="22" height="8"/>
  <rect class="fillable" fill="#ffffff" x="193" y="264" width="22" height="8"/>
  <rect class="fillable" fill="#ffffff" x="223" y="264" width="22" height="8"/>
  <rect class="fillable" fill="#ffffff" x="251" y="264" width="22" height="8"/>
</g>
''')

add('mermaid', '🧜‍♀️ 美人鱼', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke="#9bd0ff" stroke-width="2" stroke-dasharray="6 6" fill="none"><line x1="80" y1="0" x2="80" y2="60"/><line x1="320" y1="0" x2="320" y2="60"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="290" rx="180" ry="15"/>
  <path class="fillable" fill="#ffffff" d="M140 80 Q145 50 175 45 L195 35 L205 35 L225 45 Q255 50 260 80 Q260 110 240 130 Q200 140 160 130 Q140 110 140 80 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 130 Q150 165 145 200 Q155 180 175 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M235 130 Q250 165 255 200 Q245 180 225 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 25 Q140 12 130 25 Q145 32 158 30 Z"/>
  <path class="fillable" fill="#ffffff" d="M245 25 Q260 12 270 25 Q255 32 242 30 Z"/>
  <circle class="fillable" fill="#ffffff" cx="183" cy="80" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="217" cy="80" r="6"/>
  <circle fill="#1a1a1a" cx="184" cy="82" r="2.5"/>
  <circle fill="#1a1a1a" cx="216" cy="82" r="2.5"/>
  <path fill="none" d="M190 102 Q200 110 210 102"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="95" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="230" cy="95" r="4"/>
  <path class="fillable" fill="#ffffff" d="M170 140 Q160 165 158 195 Q175 175 180 152 Z"/>
  <path class="fillable" fill="#ffffff" d="M230 140 Q240 165 242 195 Q225 175 220 152 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 145 Q175 175 200 178 Q225 175 220 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 178 Q175 200 178 220 Q220 220 222 178 Q220 195 200 200 Q180 195 180 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 220 Q160 250 165 280 Q200 280 235 280 Q240 250 222 220 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="190" cy="232" r="6"/><circle class="fillable" fill="#ffffff" cx="210" cy="232" r="6"/><circle class="fillable" fill="#ffffff" cx="185" cy="250" r="6"/><circle class="fillable" fill="#ffffff" cx="200" cy="250" r="6"/><circle class="fillable" fill="#ffffff" cx="215" cy="250" r="6"/><circle class="fillable" fill="#ffffff" cx="180" cy="268" r="6"/><circle class="fillable" fill="#ffffff" cx="195" cy="268" r="6"/><circle class="fillable" fill="#ffffff" cx="210" cy="268" r="6"/><circle class="fillable" fill="#ffffff" cx="225" cy="268" r="6"/></g>
  <path class="fillable" fill="#ffffff" d="M163 282 Q130 270 110 285 Q140 295 168 290 Z"/>
  <path class="fillable" fill="#ffffff" d="M237 282 Q270 270 290 285 Q260 295 232 290 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="65" cy="80" r="5"/><circle class="fillable" fill="#ffffff" cx="335" cy="100" r="5"/><circle class="fillable" fill="#ffffff" cx="75" cy="60" r="3"/></g>
</g>
''')

add('castle', '🏰 城堡', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 45 Q295 30 315 35 Q335 25 350 45 Q365 45 360 60 L280 60 Q270 55 280 45 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 220 200 235 Q300 250 400 225 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="85" y="120" width="42" height="120"/>
  <rect class="fillable" fill="#ffffff" x="273" y="120" width="42" height="120"/>
  <rect class="fillable" fill="#ffffff" x="178" y="85" width="44" height="60"/>
  <rect class="fillable" fill="#ffffff" x="120" y="140" width="160" height="100"/>
  <path class="fillable" fill="#ffffff" d="M80 120 L106 75 L132 120 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 120 L294 75 L320 120 Z"/>
  <path class="fillable" fill="#ffffff" d="M173 85 L200 45 L227 85 Z"/>
  <line x1="106" y1="75" x2="106" y2="55"/>
  <path class="fillable" fill="#ffffff" d="M106 55 L122 60 L106 65 Z"/>
  <line x1="294" y1="75" x2="294" y2="55"/>
  <path class="fillable" fill="#ffffff" d="M294 55 L310 60 L294 65 Z"/>
  <line x1="200" y1="45" x2="200" y2="25"/>
  <path class="fillable" fill="#ffffff" d="M200 25 L220 32 L200 40 Z"/>
  <rect class="fillable" fill="#ffffff" x="128" y="132" width="14" height="10"/>
  <rect class="fillable" fill="#ffffff" x="150" y="132" width="14" height="10"/>
  <rect class="fillable" fill="#ffffff" x="172" y="132" width="14" height="10"/>
  <rect class="fillable" fill="#ffffff" x="214" y="132" width="14" height="10"/>
  <rect class="fillable" fill="#ffffff" x="236" y="132" width="14" height="10"/>
  <rect class="fillable" fill="#ffffff" x="258" y="132" width="14" height="10"/>
  <path class="fillable" fill="#ffffff" d="M180 240 L180 200 Q180 178 200 178 Q220 178 220 200 L220 240 Z"/>
  <rect class="fillable" fill="#ffffff" x="98" y="150" width="16" height="22"/>
  <rect class="fillable" fill="#ffffff" x="286" y="150" width="16" height="22"/>
  <rect class="fillable" fill="#ffffff" x="138" y="158" width="14" height="20"/>
  <rect class="fillable" fill="#ffffff" x="248" y="158" width="14" height="20"/>
  <rect class="fillable" fill="#ffffff" x="192" y="100" width="16" height="22"/>
  <rect class="fillable" fill="#ffffff" x="98" y="180" width="16" height="22"/>
  <rect class="fillable" fill="#ffffff" x="286" y="180" width="16" height="22"/>
  <g stroke-width="1.5" fill="none"><line x1="120" y1="200" x2="280" y2="200"/><line x1="120" y1="220" x2="280" y2="220"/><line x1="140" y1="190" x2="140" y2="200"/><line x1="160" y1="200" x2="160" y2="220"/><line x1="180" y1="190" x2="180" y2="200"/><line x1="220" y1="200" x2="220" y2="220"/><line x1="240" y1="190" x2="240" y2="200"/><line x1="260" y1="200" x2="260" y2="220"/></g>
</g>
''')

add('princess', '👸 公主', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M60 50 L63 60 L73 60 L65 66 L68 76 L60 70 L52 76 L55 66 L47 60 L57 60 Z"/><path class="fillable" fill="#ffffff" d="M340 50 L343 60 L353 60 L345 66 L348 76 L340 70 L332 76 L335 66 L327 60 L337 60 Z"/></g>
  <circle class="fillable" fill="#ffffff" cx="200" cy="115" r="42"/>
  <path class="fillable" fill="#ffffff" d="M160 90 Q170 60 200 50 Q230 60 240 90 L235 110 Q200 95 165 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 80 L165 50 L175 80 L185 45 L195 80 L205 45 L215 80 L225 45 L235 80 L250 50 L240 90 Z"/>
  <circle class="fillable" fill="#ffffff" cx="167" cy="60" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="183" cy="55" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="50" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="217" cy="55" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="233" cy="60" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="183" cy="110" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="217" cy="110" r="6"/>
  <circle fill="#1a1a1a" cx="184" cy="112" r="2.5"/>
  <circle fill="#1a1a1a" cx="216" cy="112" r="2.5"/>
  <path fill="none" d="M190 130 Q200 138 210 130"/>
  <circle class="fillable" fill="#ffffff" cx="172" cy="125" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="228" cy="125" r="3"/>
  <path class="fillable" fill="#ffffff" d="M165 145 Q200 158 235 145 L235 175 Q200 185 165 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M125 175 L165 165 L165 240 L125 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M275 175 L235 165 L235 240 L275 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 175 Q155 240 130 285 Q160 290 200 290 Q240 290 270 285 Q245 240 245 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 200 Q200 205 235 200 L235 220 Q200 225 165 220 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="180" cy="240" r="5"/><circle class="fillable" fill="#ffffff" cx="200" cy="248" r="5"/><circle class="fillable" fill="#ffffff" cx="220" cy="240" r="5"/><circle class="fillable" fill="#ffffff" cx="170" cy="265" r="5"/><circle class="fillable" fill="#ffffff" cx="190" cy="272" r="5"/><circle class="fillable" fill="#ffffff" cx="210" cy="272" r="5"/><circle class="fillable" fill="#ffffff" cx="230" cy="265" r="5"/></g>
  <circle class="fillable" fill="#ffffff" cx="138" cy="245" r="6"/>
  <line x1="138" y1="245" x2="138" y2="285"/>
  <path class="fillable" fill="#ffffff" d="M132 220 L138 200 L144 220 L138 235 Z"/>
</g>
''')

add('robot', '🤖 机器人', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="50" cy="40" r="3"/><circle class="fillable" fill="#ffffff" cx="350" cy="50" r="3"/><circle class="fillable" fill="#ffffff" cx="80" cy="60" r="2"/></g>
  <line x1="200" y1="55" x2="200" y2="35"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="32" r="6"/>
  <rect class="fillable" fill="#ffffff" x="150" y="55" width="100" height="80" rx="8"/>
  <rect class="fillable" fill="#ffffff" x="165" y="75" width="22" height="22" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="213" y="75" width="22" height="22" rx="3"/>
  <circle fill="#1a1a1a" cx="176" cy="86" r="4"/>
  <circle fill="#1a1a1a" cx="224" cy="86" r="4"/>
  <rect class="fillable" fill="#ffffff" x="170" y="110" width="60" height="14" rx="2"/>
  <g stroke-width="1.5" fill="none"><line x1="180" y1="110" x2="180" y2="124"/><line x1="190" y1="110" x2="190" y2="124"/><line x1="200" y1="110" x2="200" y2="124"/><line x1="210" y1="110" x2="210" y2="124"/><line x1="220" y1="110" x2="220" y2="124"/></g>
  <rect class="fillable" fill="#ffffff" x="120" y="140" width="160" height="110" rx="10"/>
  <rect class="fillable" fill="#ffffff" x="140" y="160" width="120" height="40" rx="4"/>
  <g stroke-width="1.5" fill="none"><path d="M150 180 L160 170 L170 185 L180 168 L190 180 L200 172 L210 180 L220 168 L230 185 L240 170 L250 180"/></g>
  <circle class="fillable" fill="#ffffff" cx="145" cy="220" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="220" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="215" cy="220" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="255" cy="220" r="10"/>
  <path class="fillable" fill="#ffffff" d="M85 145 L115 145 L115 220 L85 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M285 145 L315 145 L315 220 L285 220 Z"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="235" r="14"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="235" r="14"/>
  <rect class="fillable" fill="#ffffff" x="130" y="250" width="40" height="35" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="230" y="250" width="40" height="35" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="125" y="285" width="50" height="10" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="225" y="285" width="50" height="10" rx="3"/>
</g>
''')

# --- Vehicles (7) ---
add('car', '🚗 小汽车', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 55 Q295 40 315 45 Q335 35 350 50 Q365 55 360 65 L280 65 Q270 60 280 55 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 L400 250 L400 285 L0 285 Z"/>
  <g stroke="#1a1a1a" stroke-width="3" stroke-dasharray="14 14" fill="none"><line x1="0" y1="268" x2="400" y2="268"/></g>
  <path class="fillable" fill="#ffffff" d="M60 230 L60 175 Q60 165 70 165 L120 165 L150 120 Q160 110 175 110 L260 110 Q275 110 285 120 L320 165 L340 165 Q350 165 350 175 L350 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 160 L180 125 Q185 120 195 120 L205 120 L205 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M215 120 L260 120 Q270 120 275 125 L295 160 L215 160 Z"/>
  <line x1="210" y1="165" x2="210" y2="230"/>
  <rect class="fillable" fill="#ffffff" x="158" y="190" width="44" height="35" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="218" y="190" width="44" height="35" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="62" y="200" width="20" height="6" rx="2"/>
  <rect class="fillable" fill="#ffffff" x="318" y="200" width="20" height="6" rx="2"/>
  <circle class="fillable" fill="#ffffff" cx="115" cy="240" r="28"/>
  <circle class="fillable" fill="#ffffff" cx="285" cy="240" r="28"/>
  <circle class="fillable" fill="#ffffff" cx="115" cy="240" r="16"/>
  <circle class="fillable" fill="#ffffff" cx="285" cy="240" r="16"/>
  <circle class="fillable" fill="#ffffff" cx="115" cy="240" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="285" cy="240" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="332" cy="195" r="7"/>
  <circle class="fillable" fill="#ffffff" cx="68" cy="195" r="7"/>
  <rect class="fillable" fill="#ffffff" x="55" y="208" width="14" height="6" rx="2"/>
</g>
''')

add('train', '🚂 小火车', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="40" r="18"/>
  <g stroke-width="2" fill="none"><path d="M120 280 L380 280"/></g>
  <g stroke-width="2"><line x1="130" y1="278" x2="130" y2="288"/><line x1="160" y1="278" x2="160" y2="288"/><line x1="190" y1="278" x2="190" y2="288"/><line x1="220" y1="278" x2="220" y2="288"/><line x1="250" y1="278" x2="250" y2="288"/><line x1="280" y1="278" x2="280" y2="288"/><line x1="310" y1="278" x2="310" y2="288"/><line x1="340" y1="278" x2="340" y2="288"/><line x1="370" y1="278" x2="370" y2="288"/></g>
  <path class="fillable" fill="#ffffff" d="M75 270 L75 200 L150 200 L150 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M85 200 L85 150 L130 150 L130 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M105 150 L105 110 L125 110 L125 150 Z"/>
  <rect class="fillable" fill="#ffffff" x="95" y="160" width="26" height="22" rx="3"/>
  <circle class="fillable" fill="#ffffff" cx="75" cy="220" r="6"/>
  <g><circle class="fillable" fill="#ffffff" cx="100" cy="100" r="6"/><circle class="fillable" fill="#ffffff" cx="90" cy="80" r="8"/><circle class="fillable" fill="#ffffff" cx="105" cy="55" r="10"/><circle class="fillable" fill="#ffffff" cx="125" cy="40" r="7"/></g>
  <circle class="fillable" fill="#ffffff" cx="95" cy="275" r="16"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="275" r="16"/>
  <circle class="fillable" fill="#ffffff" cx="95" cy="275" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="275" r="6"/>
  <line x1="150" y1="240" x2="170" y2="240"/>
  <path class="fillable" fill="#ffffff" d="M170 270 L170 210 L260 210 L260 270 Z"/>
  <rect class="fillable" fill="#ffffff" x="180" y="222" width="20" height="20" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="210" y="222" width="20" height="20" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="240" y="222" width="14" height="20" rx="3"/>
  <circle class="fillable" fill="#ffffff" cx="190" cy="275" r="16"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="275" r="16"/>
  <circle class="fillable" fill="#ffffff" cx="190" cy="275" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="275" r="6"/>
  <line x1="260" y1="240" x2="280" y2="240"/>
  <path class="fillable" fill="#ffffff" d="M280 270 L280 215 L370 215 L370 270 Z"/>
  <rect class="fillable" fill="#ffffff" x="290" y="225" width="22" height="22" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="322" y="225" width="22" height="22" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="350" y="225" width="14" height="22" rx="3"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="275" r="16"/>
  <circle class="fillable" fill="#ffffff" cx="350" cy="275" r="16"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="275" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="350" cy="275" r="6"/>
</g>
''')

add('airplane', '✈️ 飞机', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M260 60 Q280 40 305 50 Q330 35 350 55 Q365 60 360 75 L260 75 Q250 65 260 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 200 Q90 195 130 200 Q170 205 200 200 L260 195 Q300 192 340 195 Q365 190 360 175 Q330 165 290 168 Q230 160 200 160 L130 155 Q90 150 60 165 Q50 180 60 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 195 L390 175 L375 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 165 L390 155 Q370 175 350 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 200 L165 250 L185 250 L175 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 160 L160 110 L180 110 L175 158 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 200 L222 245 L240 245 L235 200 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="100" cy="178" rx="12" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="140" cy="180" rx="10" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="175" cy="182" rx="10" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="210" cy="182" rx="10" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="245" cy="180" rx="10" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="280" cy="178" rx="10" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="315" cy="178" rx="9" ry="12"/>
  <g><circle class="fillable" fill="#ffffff" cx="40" cy="100" r="4"/><circle class="fillable" fill="#ffffff" cx="60" cy="85" r="3"/><circle class="fillable" fill="#ffffff" cx="80" cy="105" r="3"/></g>
  <g><circle class="fillable" fill="#ffffff" cx="370" cy="240" r="4"/><circle class="fillable" fill="#ffffff" cx="350" cy="265" r="3"/></g>
</g>
''')

add('rocket', '🚀 太空火箭', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M50 50 L53 60 L63 60 L55 66 L58 76 L50 70 L42 76 L45 66 L37 60 L47 60 Z"/><path class="fillable" fill="#ffffff" d="M340 60 L343 70 L353 70 L345 76 L348 86 L340 80 L332 86 L335 76 L327 70 L337 70 Z"/><path class="fillable" fill="#ffffff" d="M80 230 L83 240 L93 240 L85 246 L88 256 L80 250 L72 256 L75 246 L67 240 L77 240 Z"/><path class="fillable" fill="#ffffff" d="M320 250 L323 260 L333 260 L325 266 L328 276 L320 270 L312 276 L315 266 L307 260 L317 260 Z"/><circle class="fillable" fill="#ffffff" cx="30" cy="120" r="3"/><circle class="fillable" fill="#ffffff" cx="100" cy="160" r="2.5"/><circle class="fillable" fill="#ffffff" cx="370" cy="130" r="3"/><circle class="fillable" fill="#ffffff" cx="50" cy="200" r="2.5"/><circle class="fillable" fill="#ffffff" cx="280" cy="190" r="2.5"/><circle class="fillable" fill="#ffffff" cx="125" cy="80" r="2"/><circle class="fillable" fill="#ffffff" cx="265" cy="60" r="2"/></g>
  <circle class="fillable" fill="#ffffff" cx="335" cy="105" r="24"/>
  <ellipse fill="none" cx="335" cy="105" rx="40" ry="9"/>
  <circle class="fillable" fill="#ffffff" cx="60" cy="180" r="20"/>
  <circle class="fillable" fill="#ffffff" cx="54" cy="175" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="66" cy="186" r="2.5"/>
  <circle class="fillable" fill="#ffffff" cx="68" cy="172" r="2"/>
  <path class="fillable" fill="#ffffff" d="M170 80 L170 220 Q170 235 200 235 Q230 235 230 220 L230 80 Q220 50 200 50 Q180 50 170 80 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 60 Q200 25 220 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 130 L230 130 L230 148 L170 148 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 160 L230 160 L230 175 L170 175 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="100" r="18"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="103" r="10"/>
  <circle fill="#1a1a1a" cx="196" cy="102" r="1.5"/>
  <circle fill="#1a1a1a" cx="204" cy="102" r="1.5"/>
  <path fill="none" d="M196 108 Q200 111 204 108"/>
  <path class="fillable" fill="#ffffff" d="M170 200 L138 250 L170 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M230 200 L262 250 L230 245 Z"/>
  <rect class="fillable" fill="#ffffff" x="175" y="230" width="50" height="18"/>
  <path class="fillable" fill="#ffffff" d="M180 248 Q174 278 188 290 Q190 270 186 248 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 250 Q189 290 200 298 Q211 290 205 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M214 248 Q220 278 212 290 Q210 270 214 248 Z"/>
</g>
''')

add('pirate', '🏴‍☠️ 海盗船', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 50 Q295 35 315 40 Q335 30 350 50 Q365 50 360 65 L280 65 Q270 60 280 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 200 Q40 195 80 200 Q120 205 160 200 Q200 195 240 200 Q280 205 320 200 Q360 195 400 200 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 215 Q40 210 80 215 Q120 220 160 215 Q200 210 240 215 Q280 220 320 215 Q360 210 400 215"/><path d="M0 240 Q40 235 80 240 Q120 245 160 240 Q200 235 240 240 Q280 245 320 240 Q360 235 400 240"/><path d="M0 270 Q40 265 80 270 Q120 275 160 270 Q200 265 240 270 Q280 275 320 270 Q360 265 400 270"/></g>
  <path class="fillable" fill="#ffffff" d="M80 215 L320 215 L300 270 L100 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M85 220 L160 220 L150 265 L95 265 Z"/>
  <path class="fillable" fill="#ffffff" d="M245 220 L315 220 L305 265 L255 265 Z"/>
  <circle class="fillable" fill="#ffffff" cx="125" cy="245" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="245" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="245" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="230" cy="245" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="275" cy="245" r="6"/>
  <line x1="200" y1="215" x2="200" y2="80"/>
  <path class="fillable" fill="#ffffff" d="M150 100 L200 88 L250 100 L240 175 L160 175 Z"/>
  <line x1="150" y1="100" x2="250" y2="100"/>
  <line x1="160" y1="175" x2="240" y2="175"/>
  <g stroke-width="1.5" fill="none"><line x1="175" y1="100" x2="172" y2="175"/><line x1="200" y1="100" x2="200" y2="175"/><line x1="225" y1="100" x2="228" y2="175"/><line x1="150" y1="130" x2="250" y2="130"/><line x1="155" y1="155" x2="245" y2="155"/></g>
  <line x1="200" y1="80" x2="200" y2="55"/>
  <rect class="fillable" fill="#ffffff" x="200" y="55" width="40" height="22"/>
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="215" cy="64" r="4"/><line x1="211" y1="60" x2="219" y2="68"/><line x1="219" y1="60" x2="211" y2="68"/><path fill="none" d="M210 72 Q215 76 220 72"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="80" rx="12" ry="5"/>
  <path class="fillable" fill="#ffffff" d="M188 215 L188 200 Q188 195 200 195 Q212 195 212 200 L212 215 Z"/>
  <rect class="fillable" fill="#ffffff" x="60" y="245" width="22" height="20"/>
  <g stroke-width="1.5" fill="none"><line x1="60" y1="252" x2="82" y2="252"/><line x1="60" y1="258" x2="82" y2="258"/></g>
</g>
''')

add('fire_truck', '🚒 消防车', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 L400 250 L400 285 L0 285 Z"/>
  <g stroke="#1a1a1a" stroke-width="3" stroke-dasharray="14 14" fill="none"><line x1="0" y1="268" x2="400" y2="268"/></g>
  <rect class="fillable" fill="#ffffff" x="45" y="160" width="305" height="100" rx="6"/>
  <rect class="fillable" fill="#ffffff" x="45" y="160" width="80" height="100" rx="6"/>
  <rect class="fillable" fill="#ffffff" x="55" y="175" width="58" height="30" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="60" y="230" width="22" height="22" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="135" y="180" width="60" height="68" rx="4"/>
  <g stroke-width="1.5" fill="none"><line x1="135" y1="200" x2="195" y2="200"/><line x1="135" y1="220" x2="195" y2="220"/></g>
  <rect class="fillable" fill="#ffffff" x="210" y="180" width="60" height="68" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="285" y="180" width="55" height="68" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="100" y="140" width="20" height="22" rx="3"/>
  <circle class="fillable" fill="#ffffff" cx="110" cy="135" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="155" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="155" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="310" cy="155" r="6"/>
  <path class="fillable" fill="#ffffff" d="M180 165 L250 80 L260 90 L195 175 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="195" y1="155" x2="220" y2="130"/><line x1="205" y1="145" x2="230" y2="120"/><line x1="215" y1="135" x2="240" y2="110"/><line x1="225" y1="125" x2="250" y2="100"/></g>
  <path class="fillable" fill="#ffffff" d="M330 200 Q360 195 360 220 Q345 222 335 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M335 215 Q380 220 370 250 Q355 245 348 230 Z"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="270" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="270" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="270" cy="270" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="320" cy="270" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="270" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="270" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="270" cy="270" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="320" cy="270" r="10"/>
</g>
''')

add('balloon', '🎈 热气球', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 50 Q295 35 315 40 Q335 30 350 50 Q365 50 360 65 L280 65 Q270 60 280 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 280 Q60 260 120 270 Q180 280 240 270 Q300 260 400 275 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 150 Q120 80 200 80 Q280 80 280 150 Q280 195 200 220 Q120 195 120 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 140 L155 100 L185 95 L185 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M185 95 L185 175 L215 175 L215 95 Z"/>
  <path class="fillable" fill="#ffffff" d="M215 95 L215 175 L245 100 L245 140 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 140 L130 155 L130 175 L155 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M245 140 L270 155 L270 175 L245 165 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="155" y1="170" x2="155" y2="205"/><line x1="200" y1="178" x2="200" y2="218"/><line x1="245" y1="170" x2="245" y2="205"/><line x1="170" y1="175" x2="170" y2="210"/><line x1="230" y1="175" x2="230" y2="210"/></g>
  <rect class="fillable" fill="#ffffff" x="160" y="220" width="80" height="45" rx="3"/>
  <g stroke-width="1.5" fill="none"><line x1="170" y1="220" x2="170" y2="265"/><line x1="185" y1="220" x2="185" y2="265"/><line x1="200" y1="220" x2="200" y2="265"/><line x1="215" y1="220" x2="215" y2="265"/><line x1="230" y1="220" x2="230" y2="265"/></g>
  <circle class="fillable" fill="#ffffff" cx="180" cy="270" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="272" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="220" cy="270" r="5"/>
</g>
''')

# --- Nature (7) ---
add('garden', '🌻 花园', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="22"/>
  <g stroke-width="2"><line x1="55" y1="20" x2="55" y2="27"/><line x1="55" y1="83" x2="55" y2="90"/><line x1="22" y1="55" x2="30" y2="55"/><line x1="80" y1="55" x2="88" y2="55"/></g>
  <path class="fillable" fill="#ffffff" d="M250 45 Q265 30 285 35 Q305 25 320 45 Q335 45 330 60 L250 60 Q240 55 250 45 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 220 Q100 210 200 220 Q300 230 400 215 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M70 200 Q60 178 75 165 Q82 158 88 168 Q92 178 86 188 Q88 198 78 202 Z"/>
  <path fill="none" d="M78 202 Q76 240 80 285"/>
  <path class="fillable" fill="#ffffff" d="M78 240 Q60 228 50 240 Q65 250 78 248 Z"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="170" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="160" cy="152" rx="6" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="160" cy="188" rx="6" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="142" cy="170" rx="11" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="178" cy="170" rx="11" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="147" cy="157" rx="10" ry="6" transform="rotate(-45 147 157)"/>
  <ellipse class="fillable" fill="#ffffff" cx="173" cy="157" rx="10" ry="6" transform="rotate(45 173 157)"/>
  <ellipse class="fillable" fill="#ffffff" cx="147" cy="183" rx="10" ry="6" transform="rotate(45 147 183)"/>
  <ellipse class="fillable" fill="#ffffff" cx="173" cy="183" rx="10" ry="6" transform="rotate(-45 173 183)"/>
  <path fill="none" d="M160 180 Q160 240 158 285"/>
  <path class="fillable" fill="#ffffff" d="M160 240 Q176 230 190 240 Q175 250 160 248 Z"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="150" r="18"/>
  <ellipse class="fillable" fill="#ffffff" cx="240" cy="123" rx="8" ry="15"/>
  <ellipse class="fillable" fill="#ffffff" cx="240" cy="177" rx="8" ry="15"/>
  <ellipse class="fillable" fill="#ffffff" cx="213" cy="150" rx="15" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="267" cy="150" rx="15" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="219" cy="131" rx="13" ry="7" transform="rotate(-45 219 131)"/>
  <ellipse class="fillable" fill="#ffffff" cx="261" cy="131" rx="13" ry="7" transform="rotate(45 261 131)"/>
  <ellipse class="fillable" fill="#ffffff" cx="219" cy="169" rx="13" ry="7" transform="rotate(45 219 169)"/>
  <ellipse class="fillable" fill="#ffffff" cx="261" cy="169" rx="13" ry="7" transform="rotate(-45 261 169)"/>
  <path fill="none" d="M240 168 Q242 230 240 285"/>
  <path class="fillable" fill="#ffffff" d="M240 220 Q260 212 272 222 Q255 232 240 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 248 Q220 244 210 254 Q225 260 240 258 Z"/>
  <circle class="fillable" fill="#ffffff" cx="335" cy="170" r="20"/>
  <circle class="fillable" fill="#ffffff" cx="335" cy="170" r="13"/>
  <circle class="fillable" fill="#ffffff" cx="335" cy="170" r="6"/>
  <path fill="none" d="M335 190 Q333 240 336 285"/>
  <path class="fillable" fill="#ffffff" d="M336 235 Q320 225 308 235 Q322 245 336 240 Z"/>
  <g><ellipse class="fillable" fill="#ffffff" cx="135" cy="100" rx="2" ry="8"/><path class="fillable" fill="#ffffff" d="M133 95 Q120 87 117 96 Q120 105 133 102 Z"/><path class="fillable" fill="#ffffff" d="M137 95 Q150 87 153 96 Q150 105 137 102 Z"/></g>
  <g><ellipse class="fillable" fill="#ffffff" cx="290" cy="85" rx="2" ry="8"/><path class="fillable" fill="#ffffff" d="M288 80 Q275 72 272 81 Q275 90 288 87 Z"/><path class="fillable" fill="#ffffff" d="M292 80 Q305 72 308 81 Q305 90 292 87 Z"/></g>
  <g><ellipse class="fillable" fill="#ffffff" cx="200" cy="105" rx="14" ry="8"/><path class="fillable" fill="#ffffff" d="M192 99 L196 99 L196 111 L192 111 Z"/><path class="fillable" fill="#ffffff" d="M204 99 L208 99 L208 111 L204 111 Z"/><circle fill="#1a1a1a" cx="187" cy="103" r="1.5"/></g>
</g>
''')

add('tree', '🌳 苹果树', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 60 Q295 45 315 50 Q335 40 350 55 Q365 60 360 70 L280 70 Q270 65 280 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M20 285 Q25 275 30 285"/><path d="M50 285 Q55 273 60 285"/><path d="M340 285 Q345 275 350 285"/><path d="M370 285 Q375 273 380 285"/></g>
  <path class="fillable" fill="#ffffff" d="M185 250 L180 145 L220 145 L215 250 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M195 245 Q198 220 196 200 Q193 180 197 160"/><path d="M205 240 Q203 220 207 200 Q204 180 208 160"/></g>
  <line x1="180" y1="180" x2="155" y2="160"/>
  <line x1="220" y1="180" x2="245" y2="160"/>
  <line x1="183" y1="200" x2="170" y2="190"/>
  <line x1="217" y1="200" x2="230" y2="190"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="120" r="72"/>
  <circle class="fillable" fill="#ffffff" cx="140" cy="135" r="40"/>
  <circle class="fillable" fill="#ffffff" cx="260" cy="135" r="40"/>
  <circle class="fillable" fill="#ffffff" cx="155" cy="80" r="32"/>
  <circle class="fillable" fill="#ffffff" cx="245" cy="80" r="32"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="58" r="28"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="105" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="175" cy="135" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="135" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="265" cy="105" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="100" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="155" cy="155" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="245" cy="155" r="9"/>
  <g><line x1="135" y1="96" x2="135" y2="91"/><line x1="175" y1="126" x2="175" y2="121"/><line x1="225" y1="126" x2="225" y2="121"/><line x1="265" y1="96" x2="265" y2="91"/><line x1="200" y1="91" x2="200" y2="86"/><line x1="155" y1="146" x2="155" y2="141"/><line x1="245" y1="146" x2="245" y2="141"/></g>
  <circle class="fillable" fill="#ffffff" cx="115" cy="265" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="280" cy="262" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="320" cy="270" r="10"/>
  <g><line x1="115" y1="256" x2="115" y2="251"/><line x1="280" y1="253" x2="280" y2="248"/><line x1="320" y1="261" x2="320" y2="256"/></g>
</g>
''')

add('rainbow', '🌈 彩虹', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="335" cy="60" r="22"/>
  <g stroke-width="2"><line x1="335" y1="22" x2="335" y2="32"/><line x1="335" y1="88" x2="335" y2="98"/><line x1="295" y1="60" x2="305" y2="60"/><line x1="365" y1="60" x2="375" y2="60"/></g>
  <path class="fillable" fill="#ffffff" d="M40 240 A155 155 0 0 1 360 240 L345 240 A140 140 0 0 0 55 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M55 240 A140 140 0 0 1 345 240 L330 240 A125 125 0 0 0 70 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M70 240 A125 125 0 0 1 330 240 L315 240 A110 110 0 0 0 85 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M85 240 A110 110 0 0 1 315 240 L300 240 A95 95 0 0 0 100 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M100 240 A95 95 0 0 1 300 240 L285 240 A80 80 0 0 0 115 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M115 240 A80 80 0 0 1 285 240 L270 240 A65 65 0 0 0 130 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 240 A65 65 0 0 1 270 240 L255 240 A50 50 0 0 0 145 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M28 240 Q18 222 33 216 Q40 202 60 208 Q72 198 88 212 Q105 212 100 235 L92 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M308 240 Q302 218 318 212 Q330 200 348 210 Q368 208 365 230 Q372 240 360 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 260 Q100 252 200 262 Q300 270 400 255 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 250 Q165 280 200 282 Q235 280 230 250 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="180" cy="262" r="3"/><circle class="fillable" fill="#ffffff" cx="200" cy="265" r="3"/><circle class="fillable" fill="#ffffff" cx="220" cy="262" r="3"/></g>
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M50 130 L52 137 L60 137 L54 141 L56 149 L50 145 L44 149 L46 141 L40 137 L48 137 Z"/><path class="fillable" fill="#ffffff" d="M150 90 L152 97 L160 97 L154 101 L156 109 L150 105 L144 109 L146 101 L140 97 L148 97 Z"/><path class="fillable" fill="#ffffff" d="M250 100 L252 107 L260 107 L254 111 L256 119 L250 115 L244 119 L246 111 L240 107 L248 107 Z"/></g>
</g>
''')

add('beach', '🏖️ 海滩', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="22"/>
  <path class="fillable" fill="#ffffff" d="M260 50 Q275 35 295 40 Q315 30 330 50 Q345 50 340 65 L260 65 Q250 60 260 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 200 Q40 195 80 200 Q120 205 160 200 Q200 195 240 200 Q280 205 320 200 Q360 195 400 200 L400 230 L0 230 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 215 Q40 210 80 215 Q120 220 160 215 Q200 210 240 215 Q280 220 320 215 Q360 210 400 215"/></g>
  <path class="fillable" fill="#ffffff" d="M0 230 Q100 225 200 230 Q300 240 400 225 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M105 200 L105 130 L115 130 L115 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 130 Q60 110 50 90 Q90 95 115 115 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 130 Q140 105 175 100 Q150 125 115 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 130 Q80 80 90 50 Q105 80 115 120 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 130 Q150 85 195 80 Q170 110 115 125 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="92" cy="135" r="4"/><circle class="fillable" fill="#ffffff" cx="100" cy="138" r="4"/><circle class="fillable" fill="#ffffff" cx="108" cy="142" r="4"/></g>
  <path class="fillable" fill="#ffffff" d="M210 280 Q220 240 250 240 Q280 240 290 280 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 280 L210 290 L290 290 L290 280 Z"/>
  <path class="fillable" fill="#ffffff" d="M232 240 L240 220 L260 220 L268 240 Z"/>
  <line x1="250" y1="220" x2="250" y2="210"/>
  <path class="fillable" fill="#ffffff" d="M250 210 L262 215 L250 218 Z"/>
  <rect class="fillable" fill="#ffffff" x="170" y="240" width="32" height="40" rx="3"/>
  <line x1="170" y1="252" x2="202" y2="252"/>
  <line x1="186" y1="240" x2="186" y2="280"/>
  <path class="fillable" fill="#ffffff" d="M310 250 L330 250 L335 285 L305 285 Z"/>
  <path class="fillable" fill="#ffffff" d="M308 245 L332 245 L332 252 L308 252 Z"/>
  <circle class="fillable" fill="#ffffff" cx="345" cy="270" r="18"/>
  <path class="fillable" fill="#ffffff" d="M327 270 Q345 250 363 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M327 270 Q345 290 363 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M345 252 Q330 270 345 288"/>
  <path class="fillable" fill="#ffffff" d="M345 252 Q360 270 345 288"/>
  <g><path class="fillable" fill="#ffffff" d="M30 268 L36 258 L42 268 L48 258 L54 268 L60 258 L66 268 Z"/></g>
</g>
''')

add('mountain', '🏔️ 雪山湖泊', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="335" cy="60" r="22"/>
  <g stroke-width="2"><line x1="335" y1="22" x2="335" y2="32"/><line x1="335" y1="88" x2="335" y2="98"/><line x1="295" y1="60" x2="305" y2="60"/><line x1="365" y1="60" x2="375" y2="60"/></g>
  <path class="fillable" fill="#ffffff" d="M60 60 Q75 45 95 50 Q115 40 130 60 Q145 60 140 75 L60 75 Q50 70 60 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 60 Q215 45 235 50 Q255 40 270 60 Q285 60 280 75 L200 75 Q190 70 200 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 220 L80 100 L160 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M50 145 L80 100 L110 145 L95 150 L80 140 L65 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 220 L200 80 L280 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 145 L200 80 L230 145 L220 152 L210 142 L200 152 L190 142 L180 152 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 220 L320 130 L400 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M290 165 L320 130 L350 165 L340 170 L325 158 L310 170 L300 162 Z"/>
  <g><path class="fillable" fill="#ffffff" d="M55 210 L60 200 L65 210 Z"/><path class="fillable" fill="#ffffff" d="M90 215 L95 200 L100 215 Z"/><path class="fillable" fill="#ffffff" d="M250 215 L255 200 L260 215 Z"/><path class="fillable" fill="#ffffff" d="M285 215 L290 200 L295 215 Z"/></g>
  <path class="fillable" fill="#ffffff" d="M0 220 Q100 215 200 220 Q300 225 400 218 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 280 L175 245 L210 250 L240 260 L255 280 Z"/>
  <line x1="195" y1="248" x2="195" y2="225"/>
  <path class="fillable" fill="#ffffff" d="M195 225 L222 240 L195 245 Z"/>
  <g stroke-width="2" fill="none"><path d="M40 245 Q80 240 120 245"/><path d="M260 250 Q300 245 340 250"/><path d="M40 265 Q80 260 120 265"/><path d="M260 270 Q300 265 340 270"/></g>
</g>
''')

add('snowman', '⛄ 雪人', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5">
    <g transform="translate(50 50)" fill="none"><line x1="0" y1="-8" x2="0" y2="8"/><line x1="-8" y1="0" x2="8" y2="0"/><line x1="-5" y1="-5" x2="5" y2="5"/><line x1="-5" y1="5" x2="5" y2="-5"/></g>
    <g transform="translate(150 60)" fill="none"><line x1="0" y1="-6" x2="0" y2="6"/><line x1="-6" y1="0" x2="6" y2="0"/></g>
    <g transform="translate(330 70)" fill="none"><line x1="0" y1="-8" x2="0" y2="8"/><line x1="-8" y1="0" x2="8" y2="0"/><line x1="-5" y1="-5" x2="5" y2="5"/><line x1="-5" y1="5" x2="5" y2="-5"/></g>
    <g transform="translate(370 130)" fill="none"><line x1="0" y1="-6" x2="0" y2="6"/><line x1="-6" y1="0" x2="6" y2="0"/></g>
    <g transform="translate(40 180)" fill="none"><line x1="0" y1="-6" x2="0" y2="6"/><line x1="-6" y1="0" x2="6" y2="0"/></g>
  </g>
  <path class="fillable" fill="#ffffff" d="M0 220 Q100 210 200 220 Q300 230 400 215 L400 300 L0 300 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="30" cy="270" r="3"/><circle class="fillable" fill="#ffffff" cx="350" cy="265" r="3"/><circle class="fillable" fill="#ffffff" cx="80" cy="285" r="3"/></g>
  <circle class="fillable" fill="#ffffff" cx="200" cy="240" r="60"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="170" r="45"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="115" r="32"/>
  <rect class="fillable" fill="#ffffff" x="170" y="60" width="60" height="14"/>
  <rect class="fillable" fill="#ffffff" x="160" y="74" width="80" height="10"/>
  <rect class="fillable" fill="#ffffff" x="160" y="78" width="80" height="6"/>
  <circle fill="#1a1a1a" cx="188" cy="108" r="3"/>
  <circle fill="#1a1a1a" cx="212" cy="108" r="3"/>
  <path class="fillable" fill="#ffffff" d="M195 118 L210 122 L195 130 Z"/>
  <g><circle fill="#1a1a1a" cx="190" cy="130" r="1.5"/><circle fill="#1a1a1a" cx="197" cy="132" r="1.5"/><circle fill="#1a1a1a" cx="203" cy="132" r="1.5"/><circle fill="#1a1a1a" cx="210" cy="130" r="1.5"/></g>
  <path class="fillable" fill="#ffffff" d="M150 140 L250 145 L240 168 L165 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 140 L140 148 L150 158 L165 162 Z"/>
  <g><line x1="160" y1="142" x2="165" y2="160"/><line x1="180" y1="143" x2="185" y2="162"/><line x1="200" y1="144" x2="205" y2="163"/><line x1="220" y1="144" x2="225" y2="163"/></g>
  <circle class="fillable" fill="#ffffff" cx="200" cy="155" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="180" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="205" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="235" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="260" r="5"/>
  <line x1="155" y1="170" x2="115" y2="150"/>
  <g stroke-width="2"><line x1="120" y1="155" x2="110" y2="145"/><line x1="125" y1="160" x2="118" y2="170"/><line x1="115" y1="148" x2="105" y2="135"/></g>
  <line x1="245" y1="170" x2="285" y2="150"/>
  <g stroke-width="2"><line x1="280" y1="155" x2="290" y2="145"/><line x1="275" y1="160" x2="282" y2="170"/><line x1="285" y1="148" x2="295" y2="135"/></g>
</g>
''')

add('butterfly_meadow', '🦋 蝴蝶草地', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 55 Q295 40 315 45 Q335 35 350 50 Q365 55 360 65 L280 65 Q270 60 280 55 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 230 200 240 Q300 250 400 235 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M20 280 Q25 268 30 280"/><path d="M50 280 Q55 268 60 280"/><path d="M80 285 Q85 270 90 285"/><path d="M120 280 Q125 268 130 280"/><path d="M160 285 Q165 270 170 285"/><path d="M280 285 Q285 270 290 285"/><path d="M320 280 Q325 268 330 280"/><path d="M360 285 Q365 270 370 285"/></g>
  <g>
    <ellipse class="fillable" fill="#ffffff" cx="120" cy="130" rx="2" ry="10"/>
    <path class="fillable" fill="#ffffff" d="M118 124 Q100 112 95 124 Q98 138 118 134 Z"/>
    <path class="fillable" fill="#ffffff" d="M122 124 Q140 112 145 124 Q142 138 122 134 Z"/>
    <path class="fillable" fill="#ffffff" d="M118 136 Q105 148 100 138 Q105 130 118 136 Z"/>
    <path class="fillable" fill="#ffffff" d="M122 136 Q135 148 140 138 Q135 130 122 136 Z"/>
    <circle class="fillable" fill="#ffffff" cx="103" cy="120" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="137" cy="120" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="108" cy="140" r="3"/>
    <circle class="fillable" fill="#ffffff" cx="132" cy="140" r="3"/>
  </g>
  <g>
    <ellipse class="fillable" fill="#ffffff" cx="225" cy="110" rx="2" ry="9"/>
    <path class="fillable" fill="#ffffff" d="M223 105 Q208 95 205 106 Q208 118 223 114 Z"/>
    <path class="fillable" fill="#ffffff" d="M227 105 Q242 95 245 106 Q242 118 227 114 Z"/>
    <path class="fillable" fill="#ffffff" d="M223 116 Q212 126 207 118 Q213 110 223 116 Z"/>
    <path class="fillable" fill="#ffffff" d="M227 116 Q238 126 243 118 Q237 110 227 116 Z"/>
  </g>
  <g>
    <ellipse class="fillable" fill="#ffffff" cx="305" cy="155" rx="2" ry="9"/>
    <path class="fillable" fill="#ffffff" d="M303 150 Q288 140 285 151 Q288 163 303 159 Z"/>
    <path class="fillable" fill="#ffffff" d="M307 150 Q322 140 325 151 Q322 163 307 159 Z"/>
    <path class="fillable" fill="#ffffff" d="M303 161 Q292 171 287 163 Q293 155 303 161 Z"/>
    <path class="fillable" fill="#ffffff" d="M307 161 Q318 171 323 163 Q317 155 307 161 Z"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M50 210 Q45 180 60 168 Q70 162 75 172 Q80 185 70 192 Z"/>
  <path fill="none" d="M65 200 Q65 230 60 280"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="200" r="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="184" rx="5" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="216" rx="5" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="200" rx="9" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="196" cy="200" rx="9" ry="5"/>
  <path fill="none" d="M180 215 Q180 240 178 280"/>
  <path class="fillable" fill="#ffffff" d="M250 230 Q240 200 255 188 Q265 182 270 192 Q275 205 265 215 Z"/>
  <path fill="none" d="M260 215 Q258 245 252 280"/>
  <circle class="fillable" fill="#ffffff" cx="350" cy="210" r="12"/>
  <ellipse class="fillable" fill="#ffffff" cx="350" cy="196" rx="5" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="350" cy="224" rx="5" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="335" cy="210" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="365" cy="210" rx="8" ry="5"/>
  <path fill="none" d="M350 222 Q350 245 348 280"/>
</g>
''')

# --- Food (6) ---
add('cake', '🎂 生日蛋糕', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M10 30 Q200 55 390 30"/>
  <path class="fillable" fill="#ffffff" d="M28 32 L42 32 L35 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M68 38 L82 38 L75 56 Z"/>
  <path class="fillable" fill="#ffffff" d="M108 43 L122 43 L115 61 Z"/>
  <path class="fillable" fill="#ffffff" d="M148 47 L162 47 L155 65 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 49 L202 49 L195 67 Z"/>
  <path class="fillable" fill="#ffffff" d="M228 47 L242 47 L235 65 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 43 L282 43 L275 61 Z"/>
  <path class="fillable" fill="#ffffff" d="M308 38 L322 38 L315 56 Z"/>
  <path class="fillable" fill="#ffffff" d="M348 32 L362 32 L355 50 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="262" rx="120" ry="12"/>
  <rect class="fillable" fill="#ffffff" x="105" y="210" width="190" height="50"/>
  <rect class="fillable" fill="#ffffff" x="130" y="170" width="140" height="42"/>
  <rect class="fillable" fill="#ffffff" x="160" y="125" width="80" height="47"/>
  <path class="fillable" fill="#ffffff" d="M105 220 Q117 233 130 220 Q142 233 155 220 Q167 233 180 220 Q192 233 205 220 Q217 233 230 220 Q242 233 255 220 Q267 233 280 220 Q292 233 295 220 L295 210 L105 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 180 Q142 192 155 180 Q167 192 180 180 Q192 192 205 180 Q217 192 230 180 Q242 192 255 180 Q262 192 270 180 L270 170 L130 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 135 Q172 145 185 135 Q197 145 210 135 Q222 145 235 135 L235 125 L160 125 Z"/>
  <rect class="fillable" fill="#ffffff" x="170" y="90" width="6" height="35"/>
  <rect class="fillable" fill="#ffffff" x="187" y="85" width="6" height="40"/>
  <rect class="fillable" fill="#ffffff" x="204" y="85" width="6" height="40"/>
  <rect class="fillable" fill="#ffffff" x="221" y="90" width="6" height="35"/>
  <path class="fillable" fill="#ffffff" d="M173 80 Q168 90 173 95 Q178 90 173 80 Z"/>
  <path class="fillable" fill="#ffffff" d="M190 75 Q185 85 190 90 Q195 85 190 75 Z"/>
  <path class="fillable" fill="#ffffff" d="M207 75 Q202 85 207 90 Q212 85 207 75 Z"/>
  <path class="fillable" fill="#ffffff" d="M224 80 Q219 90 224 95 Q229 90 224 80 Z"/>
  <g>
    <circle class="fillable" fill="#ffffff" cx="130" cy="240" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="160" cy="240" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="190" cy="240" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="220" cy="240" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="250" cy="240" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="280" cy="240" r="5"/>
  </g>
  <g>
    <circle class="fillable" fill="#ffffff" cx="150" cy="195" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="200" cy="200" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="250" cy="195" r="4"/>
  </g>
</g>
''')

add('icecream', '🍨 冰淇淋圣代', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M70 60 L72 67 L79 67 L73 71 L75 78 L70 74 L65 78 L67 71 L61 67 L68 67 Z"/><path class="fillable" fill="#ffffff" d="M330 50 L332 57 L339 57 L333 61 L335 68 L330 64 L325 68 L327 61 L321 57 L328 57 Z"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="280" rx="130" ry="15"/>
  <path class="fillable" fill="#ffffff" d="M140 215 L260 215 L240 275 L160 275 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="155" y1="225" x2="245" y2="225"/><line x1="158" y1="245" x2="242" y2="245"/><line x1="162" y1="265" x2="238" y2="265"/><line x1="170" y1="215" x2="165" y2="275"/><line x1="200" y1="215" x2="200" y2="275"/><line x1="230" y1="215" x2="235" y2="275"/></g>
  <path class="fillable" fill="#ffffff" d="M125 195 Q120 175 145 165 Q170 155 200 160 Q230 155 255 165 Q280 175 275 195 Q275 215 200 215 Q125 215 125 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 145 Q132 115 158 100 Q185 92 200 105 Q215 92 242 100 Q268 115 260 145 Q258 165 200 165 Q142 165 140 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 100 Q150 78 175 70 Q200 65 215 80 Q225 95 215 105 Q200 110 175 105 Q160 105 155 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M185 50 Q185 38 200 38 Q215 38 215 50 Q215 62 200 78 Q185 62 185 50 Z"/>
  <line x1="200" y1="38" x2="200" y2="25"/>
  <path fill="none" d="M200 25 Q195 18 200 12"/>
  <g stroke-width="1.5">
    <ellipse class="fillable" fill="#ffffff" cx="155" cy="125" rx="3" ry="2" transform="rotate(20 155 125)"/>
    <ellipse class="fillable" fill="#ffffff" cx="175" cy="135" rx="3" ry="2" transform="rotate(-30 175 135)"/>
    <ellipse class="fillable" fill="#ffffff" cx="215" cy="130" rx="3" ry="2" transform="rotate(40 215 130)"/>
    <ellipse class="fillable" fill="#ffffff" cx="240" cy="125" rx="3" ry="2" transform="rotate(-20 240 125)"/>
    <ellipse class="fillable" fill="#ffffff" cx="190" cy="145" rx="3" ry="2" transform="rotate(-10 190 145)"/>
    <ellipse class="fillable" fill="#ffffff" cx="225" cy="155" rx="3" ry="2" transform="rotate(30 225 155)"/>
    <ellipse class="fillable" fill="#ffffff" cx="160" cy="180" rx="3" ry="2" transform="rotate(-25 160 180)"/>
    <ellipse class="fillable" fill="#ffffff" cx="235" cy="180" rx="3" ry="2" transform="rotate(20 235 180)"/>
    <ellipse class="fillable" fill="#ffffff" cx="200" cy="190" rx="3" ry="2"/>
    <ellipse class="fillable" fill="#ffffff" cx="175" cy="195" rx="3" ry="2" transform="rotate(45 175 195)"/>
    <ellipse class="fillable" fill="#ffffff" cx="220" cy="200" rx="3" ry="2" transform="rotate(-15 220 200)"/>
  </g>
</g>
''')

add('pizza', '🍕 披萨', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="200" cy="155" r="135"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="155" r="120"/>
  <g stroke-width="2" fill="none">
    <line x1="200" y1="35" x2="200" y2="275"/>
    <line x1="80" y1="155" x2="320" y2="155"/>
    <line x1="115" y1="70" x2="285" y2="240"/>
    <line x1="115" y1="240" x2="285" y2="70"/>
  </g>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="100" rx="14" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="250" cy="100" rx="14" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="120" cy="155" rx="14" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="280" cy="155" rx="14" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="210" rx="14" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="250" cy="210" rx="14" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="80" rx="14" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="230" rx="14" ry="10"/>
  <g>
    <circle class="fillable" fill="#ffffff" cx="175" cy="135" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="225" cy="135" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="200" cy="155" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="175" cy="175" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="225" cy="175" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="150" cy="140" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="250" cy="140" r="6"/>
  </g>
  <g>
    <path class="fillable" fill="#ffffff" d="M120 120 Q118 125 124 128 Q128 122 120 120 Z"/>
    <path class="fillable" fill="#ffffff" d="M275 120 Q273 125 279 128 Q283 122 275 120 Z"/>
    <path class="fillable" fill="#ffffff" d="M180 195 Q178 200 184 203 Q188 197 180 195 Z"/>
    <path class="fillable" fill="#ffffff" d="M215 195 Q213 200 219 203 Q223 197 215 195 Z"/>
    <path class="fillable" fill="#ffffff" d="M155 175 Q153 180 159 183 Q163 177 155 175 Z"/>
    <path class="fillable" fill="#ffffff" d="M240 175 Q238 180 244 183 Q248 177 240 175 Z"/>
  </g>
</g>
''')

add('fruit', '🍎 水果盘', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="270" rx="160" ry="20"/>
  <path class="fillable" fill="#ffffff" d="M50 200 Q200 215 350 200 L335 270 Q200 285 65 270 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="80" y1="245" x2="320" y2="245"/></g>
  <circle class="fillable" fill="#ffffff" cx="130" cy="180" r="32"/>
  <line x1="130" y1="148" x2="130" y2="135"/>
  <path class="fillable" fill="#ffffff" d="M130 135 Q140 130 148 138 L142 145 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="170" r="36"/>
  <g stroke-width="1.5" fill="none"><line x1="200" y1="135" x2="200" y2="150"/><line x1="184" y1="142" x2="190" y2="155"/><line x1="216" y1="142" x2="210" y2="155"/></g>
  <line x1="200" y1="134" x2="200" y2="124"/>
  <path class="fillable" fill="#ffffff" d="M195 125 L208 122 L205 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M270 195 Q265 155 285 145 Q300 142 305 155 Q310 175 290 195 Z"/>
  <line x1="285" y1="155" x2="278" y2="140"/>
  <path class="fillable" fill="#ffffff" d="M275 140 L290 138 L288 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M80 195 L78 158 Q80 152 92 152 Q102 152 100 158 L96 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M80 195 L92 198 L96 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M83 158 L80 152 L85 148 L92 152 L88 158 Z"/>
  <g>
    <circle class="fillable" fill="#ffffff" cx="328" cy="172" r="8"/>
    <circle class="fillable" fill="#ffffff" cx="320" cy="184" r="8"/>
    <circle class="fillable" fill="#ffffff" cx="336" cy="184" r="8"/>
    <circle class="fillable" fill="#ffffff" cx="312" cy="195" r="8"/>
    <circle class="fillable" fill="#ffffff" cx="328" cy="195" r="8"/>
    <circle class="fillable" fill="#ffffff" cx="344" cy="195" r="8"/>
    <circle class="fillable" fill="#ffffff" cx="320" cy="207" r="7"/>
    <circle class="fillable" fill="#ffffff" cx="334" cy="207" r="7"/>
  </g>
  <line x1="328" y1="165" x2="324" y2="155"/>
  <path class="fillable" fill="#ffffff" d="M324 155 L334 158 L330 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 200 Q175 180 195 188 Q200 200 192 215 Q170 210 165 200 Z"/>
  <g><circle fill="#1a1a1a" cx="172" cy="200" r="1.5"/><circle fill="#1a1a1a" cx="178" cy="195" r="1.5"/><circle fill="#1a1a1a" cx="186" cy="200" r="1.5"/><circle fill="#1a1a1a" cx="183" cy="207" r="1.5"/><circle fill="#1a1a1a" cx="175" cy="208" r="1.5"/></g>
  <path class="fillable" fill="#ffffff" d="M178 180 L185 173 L192 180 Z"/>
  <g>
    <circle class="fillable" fill="#ffffff" cx="225" cy="200" r="8"/>
    <circle class="fillable" fill="#ffffff" cx="235" cy="195" r="8"/>
    <line x1="225" y1="192" x2="218" y2="180"/>
    <line x1="235" y1="187" x2="228" y2="178"/>
    <line x1="218" y1="180" x2="228" y2="178"/>
  </g>
</g>
''')

add('donut', '🍩 甜甜圈', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="262" rx="160" ry="14"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="160" r="110"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="160" r="35"/>
  <path class="fillable" fill="#ffffff" d="M100 130 Q90 165 110 195 Q140 215 175 215 Q170 200 158 195 Q145 180 145 160 Q145 140 158 130 Q170 115 195 110 Q210 105 200 100 Q190 95 165 102 Q130 110 110 125 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M125 110 Q145 120 165 102"/><path d="M125 230 Q150 215 175 220"/><path d="M280 110 Q260 120 245 105"/><path d="M275 230 Q255 215 235 220"/></g>
  <g>
    <ellipse class="fillable" fill="#ffffff" cx="140" cy="80" rx="6" ry="3" transform="rotate(25 140 80)"/>
    <ellipse class="fillable" fill="#ffffff" cx="170" cy="65" rx="6" ry="3" transform="rotate(-15 170 65)"/>
    <ellipse class="fillable" fill="#ffffff" cx="200" cy="60" rx="6" ry="3"/>
    <ellipse class="fillable" fill="#ffffff" cx="230" cy="65" rx="6" ry="3" transform="rotate(15 230 65)"/>
    <ellipse class="fillable" fill="#ffffff" cx="260" cy="80" rx="6" ry="3" transform="rotate(-25 260 80)"/>
    <ellipse class="fillable" fill="#ffffff" cx="100" cy="120" rx="6" ry="3" transform="rotate(45 100 120)"/>
    <ellipse class="fillable" fill="#ffffff" cx="80" cy="160" rx="6" ry="3" transform="rotate(90 80 160)"/>
    <ellipse class="fillable" fill="#ffffff" cx="100" cy="200" rx="6" ry="3" transform="rotate(-45 100 200)"/>
    <ellipse class="fillable" fill="#ffffff" cx="135" cy="235" rx="6" ry="3" transform="rotate(-25 135 235)"/>
    <ellipse class="fillable" fill="#ffffff" cx="170" cy="248" rx="6" ry="3" transform="rotate(15 170 248)"/>
    <ellipse class="fillable" fill="#ffffff" cx="200" cy="250" rx="6" ry="3"/>
    <ellipse class="fillable" fill="#ffffff" cx="230" cy="248" rx="6" ry="3" transform="rotate(-15 230 248)"/>
    <ellipse class="fillable" fill="#ffffff" cx="265" cy="235" rx="6" ry="3" transform="rotate(25 265 235)"/>
    <ellipse class="fillable" fill="#ffffff" cx="300" cy="200" rx="6" ry="3" transform="rotate(45 300 200)"/>
    <ellipse class="fillable" fill="#ffffff" cx="320" cy="160" rx="6" ry="3" transform="rotate(90 320 160)"/>
    <ellipse class="fillable" fill="#ffffff" cx="300" cy="120" rx="6" ry="3" transform="rotate(-45 300 120)"/>
    <ellipse class="fillable" fill="#ffffff" cx="155" cy="155" rx="6" ry="3" transform="rotate(-30 155 155)"/>
    <ellipse class="fillable" fill="#ffffff" cx="180" cy="195" rx="6" ry="3" transform="rotate(40 180 195)"/>
    <ellipse class="fillable" fill="#ffffff" cx="225" cy="125" rx="6" ry="3" transform="rotate(20 225 125)"/>
    <ellipse class="fillable" fill="#ffffff" cx="245" cy="180" rx="6" ry="3" transform="rotate(60 245 180)"/>
  </g>
</g>
''')

add('hamburger', '🍔 汉堡', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="280" rx="155" ry="12"/>
  <path class="fillable" fill="#ffffff" d="M60 130 Q60 60 200 60 Q340 60 340 130 Z"/>
  <g>
    <circle class="fillable" fill="#ffffff" cx="100" cy="100" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="140" cy="80" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="180" cy="70" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="220" cy="70" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="260" cy="80" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="300" cy="100" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="120" cy="118" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="200" cy="100" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="280" cy="118" r="4"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M50 130 Q60 145 90 138 Q120 150 150 138 Q180 150 210 138 Q240 150 270 138 Q300 150 350 130 L348 158 Q300 165 270 158 Q240 165 210 158 Q180 165 150 158 Q120 165 90 158 Q60 165 52 158 Z"/>
  <rect class="fillable" fill="#ffffff" x="55" y="160" width="290" height="20" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M50 185 Q60 195 90 188 Q120 200 150 188 Q180 200 210 188 Q240 200 270 188 Q300 200 350 185 L350 215 Q60 220 50 215 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="100" cy="200" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="135" cy="200" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="200" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="205" cy="200" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="240" cy="200" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="275" cy="200" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="310" cy="200" r="9"/>
  <path class="fillable" fill="#ffffff" d="M55 215 Q60 240 100 245 Q150 252 200 250 Q250 252 300 245 Q340 240 345 215 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M80 230 Q90 232 100 230"/><path d="M150 235 Q160 237 170 235"/><path d="M230 235 Q240 237 250 235"/><path d="M300 230 Q310 232 320 230"/></g>
</g>
''')

# --- Other / Holidays (7) ---
add('christmas', '🎄 圣诞树', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="40" cy="80" r="3"/><circle class="fillable" fill="#ffffff" cx="360" cy="60" r="3"/><circle class="fillable" fill="#ffffff" cx="80" cy="220" r="3"/><circle class="fillable" fill="#ffffff" cx="330" cy="200" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M200 30 L214 60 L246 60 L222 78 L232 110 L200 90 L168 110 L178 78 L154 60 L186 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 85 L165 130 L235 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 125 L150 175 L250 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 170 L135 225 L265 225 Z"/>
  <rect class="fillable" fill="#ffffff" x="186" y="220" width="28" height="35"/>
  <g>
    <circle class="fillable" fill="#ffffff" cx="180" cy="155" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="220" cy="155" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="200" cy="145" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="160" cy="205" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="200" cy="200" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="240" cy="205" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="180" cy="195" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="220" cy="195" r="6"/>
    <circle class="fillable" fill="#ffffff" cx="175" cy="115" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="225" cy="115" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="200" cy="105" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="155" cy="160" r="5"/>
    <circle class="fillable" fill="#ffffff" cx="245" cy="160" r="5"/>
  </g>
  <path fill="none" d="M155 200 Q200 215 245 200"/>
  <path fill="none" d="M165 155 Q200 168 235 155"/>
  <path fill="none" d="M175 115 Q200 125 225 115"/>
  <rect class="fillable" fill="#ffffff" x="55" y="240" width="80" height="50" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="55" y="240" width="80" height="10"/>
  <rect class="fillable" fill="#ffffff" x="91" y="240" width="8" height="50"/>
  <path class="fillable" fill="#ffffff" d="M95 240 Q82 226 75 232 Q82 244 95 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M95 240 Q108 226 115 232 Q108 244 95 245 Z"/>
  <rect class="fillable" fill="#ffffff" x="265" y="245" width="80" height="45" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="265" y="245" width="80" height="9"/>
  <rect class="fillable" fill="#ffffff" x="301" y="245" width="8" height="45"/>
  <path class="fillable" fill="#ffffff" d="M305 245 Q292 232 285 238 Q292 248 305 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M305 245 Q318 232 325 238 Q318 248 305 250 Z"/>
</g>
''')

add('halloween', '🎃 万圣节南瓜', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="55" r="22"/>
  <g><g><path class="fillable" fill="#ffffff" d="M70 70 L72 78 L67 73 Z"/><path class="fillable" fill="#ffffff" d="M68 73 L73 78 L65 76 Z"/></g><g transform="translate(280 90)"><path class="fillable" fill="#ffffff" d="M0 0 L2 8 L-3 3 Z"/><path class="fillable" fill="#ffffff" d="M-2 3 L3 8 L-5 6 Z"/></g><g transform="translate(120 50)"><path class="fillable" fill="#ffffff" d="M0 0 L2 8 L-3 3 Z"/><path class="fillable" fill="#ffffff" d="M-2 3 L3 8 L-5 6 Z"/></g></g>
  <path class="fillable" fill="#ffffff" d="M50 175 Q40 110 110 100 L120 95 L130 100 Q160 90 200 90 Q240 90 270 100 L280 95 L290 100 Q360 110 350 175 Q360 245 290 260 Q200 280 110 260 Q40 245 50 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M85 175 Q80 105 120 100 Q150 175 120 255 Q90 245 85 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 175 Q165 95 200 95 Q200 175 200 265 Q180 265 165 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M235 175 Q235 95 200 95 Q200 175 200 265 Q220 265 235 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M315 175 Q320 105 280 100 Q250 175 280 255 Q310 245 315 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 95 Q185 75 195 65 Q205 60 210 70 Q215 80 210 95 Z"/>
  <path class="fillable" fill="#ffffff" d="M118 140 L138 130 L138 170 L118 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M282 140 L262 130 L262 170 L282 180 Z"/>
  <circle fill="#1a1a1a" cx="128" cy="155" r="4"/>
  <circle fill="#1a1a1a" cx="272" cy="155" r="4"/>
  <path class="fillable" fill="#ffffff" d="M175 145 L195 145 L185 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M225 145 L205 145 L215 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 210 L135 200 L150 215 L170 200 L185 215 L200 200 L215 215 L230 200 L250 215 L265 200 L290 210 L270 240 L120 240 Z"/>
  <g>
    <path class="fillable" fill="#ffffff" d="M40 60 Q30 65 28 55 Q35 50 45 55 Q50 50 55 55 Q52 65 45 65 Z"/>
    <line x1="40" y1="65" x2="40" y2="75"/>
    <line x1="38" y1="73" x2="32" y2="78"/>
    <line x1="42" y1="73" x2="48" y2="78"/>
  </g>
  <g transform="translate(330 130)">
    <path class="fillable" fill="#ffffff" d="M0 0 Q-10 5 -12 -5 Q-5 -10 5 -5 Q10 -10 15 -5 Q12 5 5 5 Z"/>
    <line x1="0" y1="5" x2="0" y2="15"/>
  </g>
</g>
''')

add('easter', '🐰 复活节彩蛋', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 55 Q295 40 315 45 Q335 35 350 50 Q365 55 360 65 L280 65 Q270 60 280 55 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 290 Q60 220 200 215 Q340 220 340 290 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M70 240 L80 290"/><path d="M90 230 L95 290"/><path d="M110 222 L112 290"/><path d="M130 220 L130 290"/><path d="M150 218 L150 290"/><path d="M170 217 L170 290"/><path d="M190 215 L190 290"/><path d="M210 215 L210 290"/><path d="M230 217 L230 290"/><path d="M250 218 L250 290"/><path d="M270 220 L270 290"/><path d="M290 222 L290 290"/><path d="M310 230 L305 290"/><path d="M330 240 L320 290"/></g>
  <g stroke-width="1.5" fill="none"><line x1="60" y1="250" x2="340" y2="250"/><line x1="60" y1="270" x2="340" y2="270"/></g>
  <path class="fillable" fill="#ffffff" d="M55 220 Q200 195 345 220 L345 230 L55 230 Z"/>
  <g>
    <path class="fillable" fill="#ffffff" d="M110 200 Q90 200 90 175 Q90 150 110 145 Q130 150 130 175 Q130 200 110 200 Z"/>
    <path fill="none" d="M95 170 Q110 165 125 170"/>
    <circle class="fillable" fill="#ffffff" cx="100" cy="160" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="120" cy="160" r="4"/>
    <circle class="fillable" fill="#ffffff" cx="110" cy="183" r="4"/>
    <path fill="none" d="M100 188 Q110 193 120 188"/>
  </g>
  <g>
    <path class="fillable" fill="#ffffff" d="M170 200 Q150 200 150 175 Q150 150 170 145 Q190 150 190 175 Q190 200 170 200 Z"/>
    <g stroke-width="1.5" fill="none"><path d="M155 158 Q170 154 185 158"/><path d="M153 168 Q170 165 187 168"/><path d="M152 180 Q170 178 188 180"/><path d="M155 192 Q170 195 185 192"/></g>
  </g>
  <g>
    <path class="fillable" fill="#ffffff" d="M230 200 Q210 200 210 175 Q210 150 230 145 Q250 150 250 175 Q250 200 230 200 Z"/>
    <path class="fillable" fill="#ffffff" d="M218 162 Q228 152 238 162 Q228 172 218 162 Z"/>
    <path class="fillable" fill="#ffffff" d="M222 188 Q232 178 242 188 Q232 198 222 188 Z"/>
    <circle class="fillable" fill="#ffffff" cx="230" cy="175" r="4"/>
  </g>
  <g>
    <path class="fillable" fill="#ffffff" d="M290 200 Q270 200 270 175 Q270 150 290 145 Q310 150 310 175 Q310 200 290 200 Z"/>
    <g stroke-width="1.5" fill="none"><line x1="275" y1="160" x2="305" y2="155"/><line x1="278" y1="172" x2="305" y2="168"/><line x1="278" y1="185" x2="305" y2="180"/><line x1="280" y1="195" x2="302" y2="192"/></g>
  </g>
  <g><path class="fillable" fill="#ffffff" d="M70 215 Q60 200 75 195 Q80 205 85 215 Z"/><path class="fillable" fill="#ffffff" d="M330 215 Q340 200 325 195 Q320 205 315 215 Z"/></g>
</g>
''')

add('party', '🎉 派对场景', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="262" rx="100" ry="10"/>
  <path fill="none" d="M10 30 Q200 55 390 30"/>
  <path class="fillable" fill="#ffffff" d="M28 32 L42 32 L35 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M68 38 L82 38 L75 56 Z"/>
  <path class="fillable" fill="#ffffff" d="M108 43 L122 43 L115 61 Z"/>
  <path class="fillable" fill="#ffffff" d="M148 47 L162 47 L155 65 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 49 L202 49 L195 67 Z"/>
  <path class="fillable" fill="#ffffff" d="M228 47 L242 47 L235 65 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 43 L282 43 L275 61 Z"/>
  <path class="fillable" fill="#ffffff" d="M308 38 L322 38 L315 56 Z"/>
  <path class="fillable" fill="#ffffff" d="M348 32 L362 32 L355 50 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="55" cy="105" rx="22" ry="28"/>
  <path class="fillable" fill="#ffffff" d="M50 131 L55 138 L60 131 Z"/>
  <path fill="none" d="M55 138 Q50 180 60 230"/>
  <ellipse class="fillable" fill="#ffffff" cx="100" cy="80" rx="24" ry="30"/>
  <path class="fillable" fill="#ffffff" d="M95 108 L100 115 L105 108 Z"/>
  <path fill="none" d="M100 115 Q104 170 95 232"/>
  <ellipse class="fillable" fill="#ffffff" cx="345" cy="90" rx="24" ry="30"/>
  <path class="fillable" fill="#ffffff" d="M340 118 L345 125 L350 118 Z"/>
  <path fill="none" d="M345 125 Q350 170 343 232"/>
  <ellipse class="fillable" fill="#ffffff" cx="305" cy="120" rx="22" ry="28"/>
  <path class="fillable" fill="#ffffff" d="M300 146 L305 153 L310 146 Z"/>
  <path fill="none" d="M305 153 Q302 190 308 232"/>
  <rect class="fillable" fill="#ffffff" x="125" y="210" width="150" height="50"/>
  <rect class="fillable" fill="#ffffff" x="145" y="170" width="110" height="42"/>
  <rect class="fillable" fill="#ffffff" x="170" y="135" width="60" height="37"/>
  <path class="fillable" fill="#ffffff" d="M125 220 Q137 233 150 220 Q162 233 175 220 Q187 233 200 220 Q212 233 225 220 Q237 233 250 220 Q262 233 275 220 L275 210 L125 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M145 180 Q157 192 170 180 Q182 192 195 180 Q207 192 220 180 Q232 192 245 180 Q252 192 255 180 L255 170 L145 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 145 Q182 155 195 145 Q207 155 220 145 Q227 155 230 145 L230 135 L170 135 Z"/>
  <rect class="fillable" fill="#ffffff" x="180" y="105" width="6" height="30"/>
  <rect class="fillable" fill="#ffffff" x="197" y="100" width="6" height="35"/>
  <rect class="fillable" fill="#ffffff" x="214" y="105" width="6" height="30"/>
  <path class="fillable" fill="#ffffff" d="M183 95 Q178 105 183 110 Q188 105 183 95 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 90 Q195 100 200 106 Q205 100 200 90 Z"/>
  <path class="fillable" fill="#ffffff" d="M217 95 Q212 105 217 110 Q222 105 217 95 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="150" cy="240" r="5"/><circle class="fillable" fill="#ffffff" cx="180" cy="240" r="5"/><circle class="fillable" fill="#ffffff" cx="210" cy="240" r="5"/><circle class="fillable" fill="#ffffff" cx="240" cy="240" r="5"/></g>
  <rect class="fillable" fill="#ffffff" x="20" y="240" width="55" height="42"/>
  <rect class="fillable" fill="#ffffff" x="43" y="240" width="9" height="42"/>
  <path class="fillable" fill="#ffffff" d="M47 240 Q35 228 28 235 Q35 247 47 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M48 240 Q60 228 67 235 Q60 247 48 245 Z"/>
  <rect class="fillable" fill="#ffffff" x="325" y="240" width="55" height="42"/>
  <rect class="fillable" fill="#ffffff" x="348" y="240" width="9" height="42"/>
  <path class="fillable" fill="#ffffff" d="M352 240 Q340 228 333 235 Q340 247 352 245 Z"/>
  <path class="fillable" fill="#ffffff" d="M353 240 Q365 228 372 235 Q365 247 353 245 Z"/>
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="150" cy="40" r="2.5"/><circle class="fillable" fill="#ffffff" cx="250" cy="48" r="2.5"/><circle class="fillable" fill="#ffffff" cx="80" cy="180" r="2.5"/><circle class="fillable" fill="#ffffff" cx="320" cy="190" r="2.5"/></g>
</g>
''')

add('house', '🏡 房子和花园', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 60 Q295 45 315 50 Q335 40 350 55 Q365 60 360 70 L280 70 Q270 65 280 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 230 200 240 Q300 250 400 235 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="115" y="170" width="170" height="100"/>
  <g><rect class="fillable" fill="#ffffff" x="115" y="170" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="137" y="184" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="159" y="170" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="181" y="184" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="203" y="170" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="225" y="184" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="247" y="170" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="115" y="198" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="137" y="212" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="159" y="198" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="203" y="198" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="225" y="212" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="247" y="198" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="115" y="226" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="159" y="226" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="203" y="226" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="247" y="226" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="115" y="254" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="137" y="240" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="159" y="254" width="22" height="14"/><rect class="fillable" fill="#ffffff" x="247" y="254" width="22" height="14"/></g>
  <path class="fillable" fill="#ffffff" d="M100 170 L200 110 L300 170 Z"/>
  <rect class="fillable" fill="#ffffff" x="240" y="100" width="22" height="50"/>
  <g><circle class="fillable" fill="#ffffff" cx="250" cy="92" r="6"/><circle class="fillable" fill="#ffffff" cx="245" cy="78" r="5"/><circle class="fillable" fill="#ffffff" cx="255" cy="65" r="4"/><circle class="fillable" fill="#ffffff" cx="262" cy="52" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M183 270 L183 235 Q183 220 200 220 Q217 220 217 235 L217 270 Z"/>
  <circle class="fillable" fill="#ffffff" cx="210" cy="248" r="2"/>
  <rect class="fillable" fill="#ffffff" x="140" y="225" width="22" height="22"/>
  <line x1="151" y1="225" x2="151" y2="247"/>
  <line x1="140" y1="236" x2="162" y2="236"/>
  <rect class="fillable" fill="#ffffff" x="240" y="225" width="22" height="22"/>
  <line x1="251" y1="225" x2="251" y2="247"/>
  <line x1="240" y1="236" x2="262" y2="236"/>
  <rect class="fillable" fill="#ffffff" x="40" y="220" width="6" height="40"/>
  <path class="fillable" fill="#ffffff" d="M43 215 L48 230 L58 220 L60 235 L70 220 L75 235 L85 220 L88 240 L78 245 L65 240 L55 245 L43 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M62 200 L66 215 L52 220 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="320" cy="240" r="8"/><circle class="fillable" fill="#ffffff" cx="320" cy="225" r="8"/><line x1="320" y1="248" x2="320" y2="280"/></g>
  <g><circle class="fillable" fill="#ffffff" cx="60" cy="265" r="6"/><circle class="fillable" fill="#ffffff" cx="60" cy="252" r="6"/><line x1="60" y1="271" x2="60" y2="285"/></g>
  <g><rect class="fillable" fill="#ffffff" x="305" y="285" width="14" height="6"/><rect class="fillable" fill="#ffffff" x="325" y="285" width="14" height="6"/><rect class="fillable" fill="#ffffff" x="345" y="285" width="14" height="6"/></g>
</g>
''')

add('space', '🪐 太空场景', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5">
    <path class="fillable" fill="#ffffff" d="M40 50 L42 57 L50 57 L44 61 L46 69 L40 65 L34 69 L36 61 L30 57 L38 57 Z"/>
    <path class="fillable" fill="#ffffff" d="M120 90 L122 97 L130 97 L124 101 L126 109 L120 105 L114 109 L116 101 L110 97 L118 97 Z"/>
    <path class="fillable" fill="#ffffff" d="M200 40 L202 47 L210 47 L204 51 L206 59 L200 55 L194 59 L196 51 L190 47 L198 47 Z"/>
    <path class="fillable" fill="#ffffff" d="M280 80 L282 87 L290 87 L284 91 L286 99 L280 95 L274 99 L276 91 L270 87 L278 87 Z"/>
    <path class="fillable" fill="#ffffff" d="M360 50 L362 57 L370 57 L364 61 L366 69 L360 65 L354 69 L356 61 L350 57 L358 57 Z"/>
    <circle class="fillable" fill="#ffffff" cx="60" cy="180" r="3"/>
    <circle class="fillable" fill="#ffffff" cx="150" cy="220" r="3"/>
    <circle class="fillable" fill="#ffffff" cx="240" cy="170" r="3"/>
    <circle class="fillable" fill="#ffffff" cx="330" cy="220" r="3"/>
    <circle class="fillable" fill="#ffffff" cx="370" cy="160" r="3"/>
  </g>
  <circle class="fillable" fill="#ffffff" cx="80" cy="100" r="30"/>
  <circle class="fillable" fill="#ffffff" cx="75" cy="92" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="88" cy="105" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="78" cy="115" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="320" cy="130" r="32"/>
  <ellipse fill="none" cx="320" cy="130" rx="48" ry="11"/>
  <path class="fillable" fill="#ffffff" d="M280 130 Q280 110 320 110 L320 150 Q280 150 280 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M360 130 Q360 110 320 110 L320 150 Q360 150 360 130 Z"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="250" r="22"/>
  <g stroke-width="1.5" fill="none"><path d="M165 240 Q180 248 195 240"/><path d="M170 252 Q180 258 190 252"/></g>
  <circle class="fillable" fill="#ffffff" cx="175" cy="246" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="185" cy="248" r="3"/>
  <path class="fillable" fill="#ffffff" d="M210 200 L240 170 L260 195 L235 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M220 195 L235 180 L245 195 Z"/>
  <line x1="210" y1="218" x2="190" y2="240"/>
  <line x1="200" y1="208" x2="180" y2="230"/>
  <path class="fillable" fill="#ffffff" d="M260 195 L290 180 L295 195 Q280 200 268 200 Z"/>
</g>
''')

add('blank', '⬜ 空白画板', 'other', '<g><rect class="fillable" fill="#ffffff" x="0" y="0" width="400" height="300"/></g>')

# Sanity: make sure we have 50
assert len(TEMPLATES) == 50, f'expected 50 templates, got {len(TEMPLATES)}'







# =============================================================================
# Populate stamps
# =============================================================================

S = '<g stroke="#1a1a1a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round">'

# --- People (6) ---
stamp('kid_boy', '小男孩', 50, S + '<circle fill="__C__" cx="25" cy="14" r="8"/><path fill="__C__" d="M16 26 L34 26 L36 42 L14 42 Z"/><line x1="20" y1="42" x2="20" y2="48"/><line x1="30" y1="42" x2="30" y2="48"/><line x1="14" y1="32" x2="8" y2="38"/><line x1="36" y1="32" x2="42" y2="38"/><circle fill="#1a1a1a" cx="22" cy="14" r="1"/><circle fill="#1a1a1a" cx="28" cy="14" r="1"/></g>', 'people')
stamp('kid_girl', '小女孩', 50, S + '<circle fill="__C__" cx="25" cy="14" r="8"/><path fill="__C__" d="M14 22 L36 22 L40 18 L30 14 L25 6 L20 14 L10 18 Z"/><path fill="__C__" d="M14 26 L36 26 L40 44 L10 44 Z"/><line x1="18" y1="44" x2="18" y2="48"/><line x1="32" y1="44" x2="32" y2="48"/><circle fill="#1a1a1a" cx="22" cy="15" r="1"/><circle fill="#1a1a1a" cx="28" cy="15" r="1"/></g>', 'people')
stamp('princess_h', '公主', 50, S + '<circle fill="__C__" cx="25" cy="22" r="14"/><path fill="__C__" d="M11 18 L15 8 L19 16 L23 6 L27 16 L31 8 L35 18 Z"/><circle fill="#1a1a1a" cx="20" cy="22" r="1.5"/><circle fill="#1a1a1a" cx="30" cy="22" r="1.5"/><path fill="none" d="M21 28 Q25 31 29 28"/><path fill="__C__" d="M11 38 L39 38 L42 48 L8 48 Z"/></g>', 'people')
stamp('knight_h', '骑士', 50, S + '<rect fill="__C__" x="15" y="6" width="20" height="22" rx="3"/><path fill="__C__" d="M22 6 L25 2 L28 6 Z"/><rect fill="__C__" x="18" y="14" width="14" height="6"/><line x1="22" y1="14" x2="22" y2="20"/><line x1="28" y1="14" x2="28" y2="20"/><path fill="__C__" d="M12 28 L38 28 L42 48 L8 48 Z"/></g>', 'people')
stamp('pirate_h', '海盗', 50, S + '<path fill="__C__" d="M8 18 L42 18 L40 12 Q25 4 10 12 Z"/><circle fill="__C__" cx="25" cy="28" r="12"/><circle fill="#1a1a1a" cx="20" cy="28" r="1.5"/><path fill="__C__" d="M28 24 L34 22 L34 30 L28 32 Z"/><path fill="none" d="M21 36 Q25 38 29 36"/><path fill="__C__" d="M14 40 L36 40 L40 48 L10 48 Z"/></g>', 'people')
stamp('family', '一家人', 50, S + '<circle fill="__C__" cx="14" cy="16" r="6"/><path fill="__C__" d="M8 24 L20 24 L22 38 L6 38 Z"/><circle fill="__C__" cx="36" cy="16" r="6"/><path fill="__C__" d="M30 24 L42 24 L44 38 L28 38 Z"/><circle fill="__C__" cx="25" cy="26" r="4"/><path fill="__C__" d="M21 32 L29 32 L30 42 L20 42 Z"/></g>', 'people')

# --- Nature (6) ---
stamp('grass', '草丛', 50, S + '<path fill="none" d="M6 44 Q10 32 14 44"/><path fill="none" d="M14 44 Q18 28 22 44"/><path fill="none" d="M22 44 Q26 30 30 44"/><path fill="none" d="M30 44 Q34 26 38 44"/><path fill="none" d="M38 44 Q42 32 46 44"/><line x1="2" y1="46" x2="48" y2="46"/></g>', 'nature')
stamp('small_tree', '小树', 50, S + '<rect fill="__C__" x="22" y="30" width="6" height="16"/><circle fill="__C__" cx="25" cy="20" r="14"/><circle fill="__C__" cx="16" cy="22" r="8"/><circle fill="__C__" cx="34" cy="22" r="8"/></g>', 'nature')
stamp('small_flower', '小花', 50, S + '<line x1="25" y1="28" x2="25" y2="46" stroke="#1a1a1a"/><path fill="__C__" d="M22 40 Q16 36 14 42 Q20 44 24 42 Z"/><circle fill="__C__" cx="25" cy="18" r="6"/><circle fill="__C__" cx="17" cy="22" r="6"/><circle fill="__C__" cx="33" cy="22" r="6"/><circle fill="__C__" cx="21" cy="28" r="5"/><circle fill="__C__" cx="29" cy="28" r="5"/><circle fill="#1a1a1a" cx="25" cy="22" r="2"/></g>', 'nature')
stamp('bush', '灌木丛', 50, S + '<path fill="__C__" d="M6 44 Q4 30 14 28 Q18 18 26 22 Q34 16 40 26 Q48 28 44 44 Z"/></g>', 'nature')
stamp('mushroom', '蘑菇', 50, S + '<path fill="__C__" d="M8 28 Q8 12 25 12 Q42 12 42 28 Z"/><circle fill="#ffffff" cx="18" cy="22" r="3"/><circle fill="#ffffff" cx="28" cy="18" r="3"/><circle fill="#ffffff" cx="34" cy="24" r="2"/><path fill="__C__" d="M18 28 L18 42 Q18 46 25 46 Q32 46 32 42 L32 28 Z"/></g>', 'nature')
stamp('leaf', '叶子', 50, S + '<path fill="__C__" d="M25 6 Q40 12 38 28 Q34 42 25 44 Q16 42 12 28 Q10 12 25 6 Z"/><path fill="none" d="M25 6 L25 44"/><g stroke-width="1.5" fill="none"><line x1="25" y1="14" x2="18" y2="18"/><line x1="25" y1="14" x2="32" y2="18"/><line x1="25" y1="22" x2="16" y2="26"/><line x1="25" y1="22" x2="34" y2="26"/><line x1="25" y1="30" x2="17" y2="34"/><line x1="25" y1="30" x2="33" y2="34"/></g></g>', 'nature')

# --- Animals (6) ---
stamp('dog_small', '小狗', 50, S + '<ellipse fill="__C__" cx="28" cy="32" rx="14" ry="10"/><circle fill="__C__" cx="14" cy="26" r="9"/><path fill="__C__" d="M8 18 L8 28 L12 28 Z"/><path fill="__C__" d="M22 22 L22 30 L16 28 Z"/><circle fill="#1a1a1a" cx="11" cy="25" r="1.2"/><circle fill="#1a1a1a" cx="7" cy="28" r="1"/><line x1="20" y1="42" x2="20" y2="46"/><line x1="36" y1="42" x2="36" y2="46"/><path fill="__C__" d="M40 28 Q44 22 42 32 Z"/></g>', 'animal')
stamp('cat_small', '小猫', 50, S + '<ellipse fill="__C__" cx="28" cy="32" rx="14" ry="10"/><circle fill="__C__" cx="14" cy="24" r="8"/><path fill="__C__" d="M8 16 L11 22 L14 18 Z"/><path fill="__C__" d="M20 16 L17 22 L14 18 Z"/><circle fill="#1a1a1a" cx="11" cy="24" r="1"/><circle fill="#1a1a1a" cx="17" cy="24" r="1"/><line x1="20" y1="42" x2="20" y2="46"/><line x1="36" y1="42" x2="36" y2="46"/><path fill="none" d="M40 32 Q46 18 42 14"/></g>', 'animal')
stamp('bird', '小鸟', 50, S + '<ellipse fill="__C__" cx="22" cy="26" rx="14" ry="10"/><circle fill="__C__" cx="34" cy="22" r="7"/><path fill="__C__" d="M40 22 L46 22 L42 26 Z"/><circle fill="#1a1a1a" cx="35" cy="22" r="1.2"/><path fill="__C__" d="M14 22 Q8 14 18 16 Z"/><path fill="__C__" d="M16 28 Q10 22 20 24 Z"/><line x1="22" y1="36" x2="22" y2="42"/><line x1="28" y1="36" x2="28" y2="42"/></g>', 'animal')
stamp('fish_small', '小鱼', 50, S + '<path fill="__C__" d="M8 25 Q14 14 30 14 Q40 14 42 25 Q40 36 30 36 Q14 36 8 25 Z"/><path fill="__C__" d="M42 25 L48 18 L46 25 L48 32 Z"/><path fill="__C__" d="M20 14 Q22 8 26 12 Z"/><circle fill="#ffffff" cx="32" cy="22" r="3"/><circle fill="#1a1a1a" cx="33" cy="22" r="1.5"/><path fill="none" d="M18 25 Q24 28 18 30"/></g>', 'animal')
stamp('butterfly', '蝴蝶', 50, S + '<ellipse fill="__C__" cx="25" cy="25" rx="2" ry="12"/><path fill="__C__" d="M23 18 Q12 10 6 18 Q10 26 23 24 Z"/><path fill="__C__" d="M27 18 Q38 10 44 18 Q40 26 27 24 Z"/><path fill="__C__" d="M23 26 Q14 34 8 28 Q14 22 23 26 Z"/><path fill="__C__" d="M27 26 Q36 34 42 28 Q36 22 27 26 Z"/><line x1="24" y1="14" x2="20" y2="8"/><line x1="26" y1="14" x2="30" y2="8"/></g>', 'animal')
stamp('ladybug', '瓢虫', 50, S + '<ellipse fill="__C__" cx="25" cy="28" rx="18" ry="14"/><line x1="25" y1="14" x2="25" y2="42"/><circle fill="#1a1a1a" cx="16" cy="22" r="2"/><circle fill="#1a1a1a" cx="14" cy="32" r="2"/><circle fill="#1a1a1a" cx="34" cy="22" r="2"/><circle fill="#1a1a1a" cx="36" cy="32" r="2"/><path fill="#1a1a1a" d="M16 16 Q25 8 34 16 L34 18 Q25 14 16 18 Z"/><circle fill="#1a1a1a" cx="20" cy="12" r="1.5"/><circle fill="#1a1a1a" cx="30" cy="12" r="1.5"/></g>', 'animal')

# --- Things / Decoration (6) ---
stamp('star', '星星', 50, S + '<path fill="__C__" d="M25 4 L30 18 L46 18 L33 27 L38 42 L25 33 L12 42 L17 27 L4 18 L20 18 Z"/></g>', 'thing')
stamp('heart', '爱心', 50, S + '<path fill="__C__" d="M25 44 Q4 28 8 14 Q12 4 18 6 Q22 6 25 12 Q28 6 32 6 Q38 4 42 14 Q46 28 25 44 Z"/></g>', 'thing')
stamp('balloon_s', '气球', 50, S + '<ellipse fill="__C__" cx="25" cy="20" rx="14" ry="18"/><path fill="__C__" d="M22 36 L25 42 L28 36 Z"/><path fill="none" d="M25 42 Q22 46 28 46"/></g>', 'thing')
stamp('gift', '礼物', 50, S + '<rect fill="__C__" x="8" y="24" width="34" height="20"/><rect fill="__C__" x="22" y="24" width="6" height="20"/><path fill="__C__" d="M25 24 Q14 14 8 18 Q14 24 25 24 Z"/><path fill="__C__" d="M25 24 Q36 14 42 18 Q36 24 25 24 Z"/><rect fill="__C__" x="8" y="20" width="34" height="6"/></g>', 'thing')
stamp('crown', '皇冠', 50, S + '<path fill="__C__" d="M6 38 L8 16 L15 26 L20 12 L25 24 L30 12 L35 26 L42 16 L44 38 Z"/><circle fill="__C__" cx="10" cy="16" r="2"/><circle fill="__C__" cx="20" cy="12" r="2"/><circle fill="__C__" cx="30" cy="12" r="2"/><circle fill="__C__" cx="40" cy="16" r="2"/><line x1="6" y1="42" x2="44" y2="42"/></g>', 'thing')
stamp('sparkle', '闪光', 50, S + '<path fill="__C__" d="M25 4 L28 22 L46 25 L28 28 L25 46 L22 28 L4 25 L22 22 Z"/></g>', 'thing')

# --- Weather (6) ---
stamp('sun', '太阳', 50, S + '<circle fill="__C__" cx="25" cy="25" r="11"/><g stroke-width="2"><line x1="25" y1="4" x2="25" y2="12"/><line x1="25" y1="38" x2="25" y2="46"/><line x1="4" y1="25" x2="12" y2="25"/><line x1="38" y1="25" x2="46" y2="25"/><line x1="10" y1="10" x2="16" y2="16"/><line x1="34" y1="34" x2="40" y2="40"/><line x1="40" y1="10" x2="34" y2="16"/><line x1="16" y1="34" x2="10" y2="40"/></g></g>', 'weather')
stamp('moon', '月亮', 50, S + '<path fill="__C__" d="M30 6 Q12 10 12 25 Q12 40 30 44 Q18 38 18 25 Q18 12 30 6 Z"/><g stroke-width="1.5"><circle fill="__C__" cx="40" cy="14" r="1.5"/><circle fill="__C__" cx="42" cy="22" r="1.5"/><circle fill="__C__" cx="40" cy="32" r="1.5"/></g></g>', 'weather')
stamp('cloud', '云朵', 50, S + '<path fill="__C__" d="M8 32 Q4 22 14 20 Q16 10 26 14 Q34 6 40 16 Q48 18 44 30 L8 32 Z"/></g>', 'weather')
stamp('rainbow_s', '彩虹', 50, S + '<path fill="__C__" d="M4 40 Q4 14 25 14 Q46 14 46 40 L40 40 Q40 20 25 20 Q10 20 10 40 Z"/><path fill="__C__" d="M10 40 Q10 20 25 20 Q40 20 40 40 L34 40 Q34 26 25 26 Q16 26 16 40 Z"/><path fill="__C__" d="M16 40 Q16 26 25 26 Q34 26 34 40 L28 40 Q28 32 25 32 Q22 32 22 40 Z"/></g>', 'weather')
stamp('snowflake', '雪花', 50, S + '<g stroke="__C__" stroke-width="2.5" fill="none"><line x1="25" y1="4" x2="25" y2="46"/><line x1="4" y1="25" x2="46" y2="25"/><line x1="10" y1="10" x2="40" y2="40"/><line x1="40" y1="10" x2="10" y2="40"/><path d="M25 8 L21 4 M25 8 L29 4"/><path d="M25 42 L21 46 M25 42 L29 46"/><path d="M8 25 L4 21 M8 25 L4 29"/><path d="M42 25 L46 21 M42 25 L46 29"/></g></g>', 'weather')
stamp('raindrop', '雨滴', 50, S + '<path fill="__C__" d="M25 6 Q14 22 14 32 Q14 42 25 42 Q36 42 36 32 Q36 22 25 6 Z"/><path fill="#ffffff" d="M22 18 Q19 24 19 30 Q23 30 23 22 Z"/></g>', 'weather')

assert len(STAMPS) == 30, f'expected 30 stamps, got {len(STAMPS)}'


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
    --accent: #4ab3ff;
    --accent-dark: #2a6db0;
    --bg: #fff8e7;
    --panel: #ffffff;
    --shadow: 0 4px 14px rgba(0,0,0,.08);
    --radius: 18px;
    --hit: 56px;   /* min touch target */
  }
  * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  html, body {
    margin: 0; padding: 0; height: 100%;
    font-family: -apple-system, "PingFang SC", "Helvetica Neue", Arial, sans-serif;
    background: var(--bg);
    overscroll-behavior: none;
    touch-action: manipulation;
    user-select: none; -webkit-user-select: none;
  }
  body { display: flex; flex-direction: column; height: 100dvh; }

  /* Top bar */
  header {
    display: flex; align-items: center; gap: 8px;
    padding: 8px 12px;
    background: var(--accent); color: white;
    box-shadow: var(--shadow);
    flex-shrink: 0;
  }
  header h1 { font-size: 18px; margin: 0; letter-spacing: 1px; flex-shrink: 0; }
  .timer-chip {
    background: rgba(255,255,255,.18); padding: 6px 12px; border-radius: 999px;
    font-size: 16px; font-weight: 600; cursor: pointer; min-height: var(--hit);
    display: inline-flex; align-items: center; gap: 6px;
  }
  .timer-chip.warn { background: rgba(255,180,0,.35); }
  .timer-chip.danger { background: rgba(255,80,80,.5); animation: blink 1s infinite; }
  @keyframes blink { 50% { opacity: .5; } }
  .header-spacer { flex: 1; }
  .header-btns { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
  .big-btn {
    background: rgba(255,255,255,.22); border: none; color: white;
    padding: 10px 14px; border-radius: 12px;
    font-size: 15px; font-weight: 700;
    min-height: var(--hit); min-width: 64px;
    cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  }
  .big-btn:active { background: rgba(255,255,255,.42); }
  .big-btn.danger:active { background: rgba(255,80,80,.6); }

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
    box-shadow: 0 1px 4px rgba(0,0,0,.18);
    cursor: pointer;
  }
  .swatch.active {
    outline: 4px solid var(--accent); outline-offset: 2px;
  }
  .custom-color {
    display: flex; align-items: center; gap: 8px; margin-top: 6px;
  }
  .custom-color input[type=color] {
    width: 48px; height: 48px; border: none; background: none; padding: 0; cursor: pointer;
  }
  .pattern-grid {
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;
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

  /* Bottom toolbar with tools + zoom */
  .bottom-bar {
    position: absolute; left: 12px; right: 12px; bottom: 12px;
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
    background: rgba(0,0,0,.5);
    display: none; align-items: center; justify-content: center;
    z-index: 50; padding: 12px;
  }
  .modal.show { display: flex; }
  .modal-box {
    background: #fff; border-radius: 20px;
    width: 100%; max-width: 920px;
    max-height: 92vh; overflow: hidden;
    display: flex; flex-direction: column;
    box-shadow: 0 12px 40px rgba(0,0,0,.25);
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
    background: var(--accent); color: #fff; border: none;
    padding: 12px 24px; border-radius: 12px; font-size: 16px; font-weight: 700;
    min-height: var(--hit); cursor: pointer;
  }
  .secondary-btn {
    background: #f1f4f8; color: #333; border: none;
    padding: 12px 24px; border-radius: 12px; font-size: 16px; font-weight: 600;
    min-height: var(--hit); cursor: pointer;
  }

  /* Picture / Stamp picker */
  .cat-tabs {
    display: flex; gap: 6px; padding-bottom: 10px; flex-wrap: wrap;
    position: sticky; top: 0; background: #fff; z-index: 2;
    border-bottom: 1px solid #eef1f5; margin-bottom: 10px;
  }
  .cat-tab {
    background: #f1f4f8; border: 2px solid transparent;
    padding: 10px 14px; border-radius: 999px;
    font-size: 14px; font-weight: 600; cursor: pointer;
    min-height: 44px;
  }
  .cat-tab.active { background: var(--accent); color: #fff; border-color: var(--accent); }
  .picker-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 10px;
  }
  .picker-card {
    background: #f9fafc; border: 3px solid transparent;
    border-radius: 14px; padding: 6px; cursor: pointer;
    aspect-ratio: 4 / 3; position: relative;
    display: flex; flex-direction: column;
  }
  .picker-card.active { border-color: var(--accent); background: #e6f3ff; }
  .picker-card svg { width: 100%; flex: 1; }
  .picker-card .pc-label {
    font-size: 11px; color: #555; text-align: center; padding-top: 4px;
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
    background: #f9fafc; border: 3px solid transparent;
    border-radius: 14px; padding: 6px; cursor: pointer;
    aspect-ratio: 1; display: flex; align-items: center; justify-content: center;
  }
  .stamp-card.active { border-color: var(--accent); background: #e6f3ff; }
  .stamp-card svg { width: 80%; height: 80%; }

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
    position: fixed; left: 50%; bottom: 24px; transform: translateX(-50%);
    background: rgba(0,0,0,.78); color: #fff;
    padding: 10px 18px; border-radius: 999px;
    font-size: 14px; z-index: 60;
    opacity: 0; pointer-events: none;
    transition: opacity .25s;
  }
  .toast.show { opacity: 1; }

  /* iPad and phone responsive */
  @media (max-width: 900px) {
    .palette { width: 160px; }
    header h1 { font-size: 16px; }
    .big-btn { padding: 8px 10px; font-size: 13px; min-width: 56px; }
  }
  @media (max-width: 640px) {
    main { flex-direction: column; }
    .palette {
      width: 100%; flex-shrink: 0; max-height: 38vh;
      padding: 8px 10px 70px;
    }
    .stage-wrap { padding: 6px; }
    header { gap: 4px; padding: 6px; }
    header h1 { display: none; }
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
    <button class="big-btn" id="pickPictureBtn">🖼️ 选图</button>
    <button class="big-btn" id="pickStampBtn">⭐ 贴纸</button>
    <button class="big-btn" id="undoBtn">↶ 撤销</button>
    <button class="big-btn danger" id="clearBtn">🗑 清空</button>
    <button class="big-btn" id="saveBtn">💾 保存</button>
    <button class="big-btn" id="fullscreenBtn">⛶ 全屏</button>
    <button class="big-btn" id="helpBtn">?</button>
  </div>
</header>

<main>
  <aside class="palette">
    <div>
      <h3>颜色</h3>
      <div class="swatches" id="swatches"></div>
      <div class="custom-color">
        <input type="color" id="customColor" value="#4ab3ff" />
        <span style="font-size:12px;color:#666">自选</span>
      </div>
    </div>
    <div>
      <h3>纹路 (填色用)</h3>
      <div class="pattern-grid" id="patternGrid"></div>
    </div>
    <div>
      <h3>画笔粗细</h3>
      <div class="brush-row">
        <input type="range" id="brushSize" min="3" max="40" value="10" />
        <div class="brush-preview" id="brushPreview"><div class="brush-dot"></div></div>
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
        <button class="tool" id="zoomReset" title="复位"><span>⌂</span></button>
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
      <div class="upload-row">
        <label class="ghost-btn">📁 上传图片
          <input id="fileInput" type="file" accept="image/*" style="display:none" />
        </label>
        <button class="ghost-btn" id="googleBtn">🔍 谷歌找图</button>
        <input id="urlInput" type="url" placeholder="或粘贴图片网址…" />
        <button class="ghost-btn" id="urlLoadBtn">载入</button>
        <div class="hint" style="flex-basis:100%">谷歌图片很多禁止跨站点加载,推荐先长按/右键存到本地,再用"上传图片"。</div>
      </div>
      <div class="cat-tabs" id="pictureCatTabs"></div>
      <div class="picker-grid" id="pictureGrid"></div>
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

<!-- Timer modal -->
<div class="modal" id="timerModal" role="dialog" aria-modal="true">
  <div class="modal-box" style="max-width:420px">
    <div class="modal-header">
      <h2>⏱ 倒计时</h2>
      <button class="modal-close-x" data-close="timerModal">×</button>
    </div>
    <div class="modal-body">
      <p style="margin:0 0 6px;color:#555">画多久?到时间会弹提示。</p>
      <div class="timer-options" id="timerOptions">
        <button data-min="5">5分钟</button>
        <button data-min="10">10分钟</button>
        <button data-min="15">15分钟</button>
        <button data-min="20">20分钟</button>
        <button data-min="30">30分钟</button>
        <button data-min="45">45分钟</button>
        <button data-min="60">60分钟</button>
        <button data-min="0">关掉</button>
      </div>
    </div>
    <div class="modal-footer">
      <button class="secondary-btn" id="timerReset">↺ 重新开始</button>
      <button class="primary-btn" id="timerPauseResume">⏸ 暂停</button>
    </div>
  </div>
</div>

<!-- Timer-expired alert -->
<div class="modal" id="timerExpiredModal" role="dialog" aria-modal="true">
  <div class="modal-box" style="max-width:380px; text-align:center;">
    <div class="modal-body" style="padding:32px 24px">
      <div style="font-size:56px">⏰</div>
      <h2 style="font-size:24px; margin:8px 0; color:var(--accent-dark)">时间到啦!</h2>
      <p style="font-size:16px;color:#555;">画得真棒 🎉</p>
    </div>
    <div class="modal-footer" style="justify-content:center;gap:10px">
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
  pageKey: 'panda',
  pictureCat: CATEGORIES[0][0],
  stampCat: STAMP_CATEGORIES[0][0],
  stampKey: null,
  view: { tx: 0, ty: 0, scale: 1 },
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
      pageKey: data.pageKey || state.pageKey,
      pictureCat: data.pictureCat || state.pictureCat,
      stampCat: data.stampCat || state.stampCat,
      view: data.view || state.view,
      customPages: data.customPages || {},
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
      brushSize: state.brushSize, pageKey: state.pageKey,
      pictureCat: state.pictureCat, stampCat: state.stampCat,
      view: state.view, customPages: state.customPages,
      timer: state.timer, pageStates,
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
    if (f && f !== '#ffffff') fills.push([i, f]);
  });
  // Capture stamps placed in SVG
  const stamps = [];
  svgEl.querySelectorAll('.stamp-instance').forEach(g => {
    stamps.push({
      key: g.dataset.stampKey,
      x: +g.dataset.x, y: +g.dataset.y,
      color: g.dataset.color,
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
      if (fillables[i]) fillables[i].setAttribute('fill', f);
    });
  }
  if (Array.isArray(s.stamps)) {
    s.stamps.forEach(st => placeStamp(st.key, st.x, st.y, st.color, false));
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
    sw.addEventListener('click', () => selectColor(c));
    swatchesBox.appendChild(sw);
  });
}
function selectColor(c) {
  state.color = c;
  customColor.value = (c.length === 7 && c.startsWith('#')) ? c : '#000000';
  document.querySelectorAll('.swatch').forEach(s => s.classList.toggle('active', s.dataset.color === c));
  updateBrushPreview();
  updatePatternDefs();
  savePersisted();
}
customColor.addEventListener('input', e => {
  state.color = e.target.value;
  document.querySelectorAll('.swatch').forEach(s => s.classList.remove('active'));
  updateBrushPreview();
  updatePatternDefs();
  savePersisted();
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
      // Inline a preview using the pattern def with current color
      const previewDef = def.replace(/__FG__/g, state.color).replace(/__BG__/g, '#ffffff');
      tile.innerHTML = `<svg viewBox="0 0 30 30"><defs>${previewDef}</defs><rect width="30" height="30" fill="url(#pat-${id})"/></svg><div>${name}</div>`;
    }
    tile.addEventListener('click', () => {
      state.pattern = id;
      buildPatternTiles();
      savePersisted();
    });
    patternGrid.appendChild(tile);
  });
}
function updatePatternDefs() {
  // Re-render the global pattern defs with current color so .stage SVG can use them.
  const parts = [];
  PATTERNS.forEach(([id, name, def]) => {
    if (!def) return;
    parts.push(def.replace(/__FG__/g, state.color).replace(/__BG__/g, '#ffffff'));
  });
  patternDefsContent.innerHTML = parts.join('');
  buildPatternTiles();
}

function currentFillValue() {
  if (state.pattern === 'solid') return state.color;
  return `url(#pat-${state.pattern})`;
}

/* =========================================================================
   Brush size
   ========================================================================= */
function updateBrushPreview() {
  const s = Math.max(4, Math.min(32, state.brushSize));
  brushDot.style.width = s + 'px';
  brushDot.style.height = s + 'px';
  brushPreview.style.color = state.color;
}
brushSizeInput.addEventListener('input', e => {
  state.brushSize = +e.target.value;
  updateBrushPreview();
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
function setTool(t) {
  state.tool = t;
  document.querySelectorAll('#tools .tool').forEach(b => b.classList.toggle('active', b.dataset.tool === t));
  if (t === 'brush' || t === 'eraser') {
    canvas.classList.add('draw-mode');
  } else {
    canvas.classList.remove('draw-mode');
  }
  if (t !== 'stamp') state.stampKey = null;
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
  svgEl.querySelectorAll('.fillable').forEach(el => {
    const handler = (e) => {
      if (state.tool === 'fill') {
        e.preventDefault();
        const prev = el.getAttribute('fill') || '#ffffff';
        const next = currentFillValue();
        state.history.push({ kind: 'fill', el, prevColor: prev });
        el.setAttribute('fill', next);
        savePersisted();
      }
    };
    el.addEventListener('click', handler);
    el.addEventListener('touchstart', handler, { passive: false });
  });
}
// Stamp placement is a single delegated listener on the SVG (bound once)
svgEl.addEventListener('click', svgStampClick);
function svgStampClick(e) {
  if (state.tool !== 'stamp' || !state.stampKey) return;
  // Compute click position in SVG user units (400x300)
  const pt = svgEventToPoint(e);
  if (!pt) return;
  placeStamp(state.stampKey, pt.x, pt.y, state.color, true);
}
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
function placeStamp(key, x, y, color, addHistory) {
  const stamp = STAMPS.find(s => s[0] === key);
  if (!stamp) return;
  const [, , vb, body] = stamp;
  // Build a <g> wrapping the stamp SVG content, translated to (x, y), sized ~40 SVG units
  const SIZE = 50;
  const halfSize = SIZE / 2;
  const ns = 'http://www.w3.org/2000/svg';
  const g = document.createElementNS(ns, 'g');
  g.setAttribute('class', 'stamp-instance');
  g.setAttribute('transform', `translate(${x - halfSize} ${y - halfSize}) scale(${SIZE / vb})`);
  g.setAttribute('data-stamp-key', key);
  g.setAttribute('data-x', x);
  g.setAttribute('data-y', y);
  g.setAttribute('data-color', color);
  g.innerHTML = body.replace(/__C__/g, color);
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

// pointerdown on canvas — used for brush/eraser AND pinch zoom
canvas.addEventListener('pointerdown', (e) => {
  canvas.setPointerCapture?.(e.pointerId);
  pointers.set(e.pointerId, { x: e.clientX, y: e.clientY });
  if (pointers.size === 2) {
    // start pinch
    drawing = false; strokeSnapshot = null;
    const pts = [...pointers.values()];
    pinchStart = {
      dist: Math.hypot(pts[0].x - pts[1].x, pts[0].y - pts[1].y),
      mid: { x: (pts[0].x + pts[1].x) / 2, y: (pts[0].y + pts[1].y) / 2 },
      view: { ...state.view },
    };
    stageInner.classList.add('dragging');
  } else if (pointers.size === 1 && (state.tool === 'brush' || state.tool === 'eraser')) {
    e.preventDefault();
    const p = canvasEventToLocal(e);
    startStroke(p.x, p.y);
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
    // Pan delta
    const dx = mid.x - pinchStart.mid.x;
    const dy = mid.y - pinchStart.mid.y;
    setView(pinchStart.view.tx + dx, pinchStart.view.ty + dy, newScale);
  } else if (pointers.size === 1 && drawing) {
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
// Overwrite earlier pinch helper:
function pointerEnd(e) {
  pointers.delete(e.pointerId);
  if (pointers.size < 2) { pinchStart = null; stageInner.classList.remove('dragging'); }
  if (pointers.size === 0) endStroke();
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
    });
    pictureGrid.appendChild(card);
  });
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
  const q = encodeURIComponent('cute animal coloring page for kids');
  window.open('https://www.google.com/search?tbm=isch&q=' + q, '_blank', 'noopener');
});
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
   Stamp picker modal
   ========================================================================= */
document.getElementById('pickStampBtn').addEventListener('click', () => {
  buildStampCatTabs(); buildStampGrid(); openModal('stampModal');
});
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
   Timer
   ========================================================================= */
function fmtMs(ms) {
  const s = Math.max(0, Math.floor(ms / 1000));
  return `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;
}
function tickTimer() {
  const t = state.timer;
  if (t.durationSec <= 0) { timerText.textContent = '⏱ 关'; timerChip.className = 'timer-chip'; return; }
  const elapsed = t.paused ? t.elapsedBefore : t.elapsedBefore + (Date.now() - t.startTs);
  const remaining = t.durationSec * 1000 - elapsed;
  timerText.textContent = fmtMs(remaining);
  timerChip.classList.remove('warn', 'danger');
  if (remaining <= 60_000 && remaining > 0) timerChip.classList.add('warn');
  if (remaining <= 10_000 && remaining > 0) timerChip.classList.add('danger');
  if (remaining <= 0 && !t.fired) {
    t.fired = true;
    openModal('timerExpiredModal');
    savePersisted();
  }
}
setInterval(tickTimer, 500);
timerChip.addEventListener('click', () => {
  // Highlight current option
  document.querySelectorAll('#timerOptions button').forEach(b => {
    b.classList.toggle('active', +b.dataset.min === state.timer.durationSec / 60);
  });
  document.getElementById('timerPauseResume').textContent = state.timer.paused ? '▶ 继续' : '⏸ 暂停';
  openModal('timerModal');
});
document.getElementById('timerOptions').addEventListener('click', (e) => {
  const b = e.target.closest('button'); if (!b) return;
  const m = +b.dataset.min;
  setTimerDuration(m * 60);
  document.querySelectorAll('#timerOptions button').forEach(x => x.classList.toggle('active', x === b));
});
function setTimerDuration(sec) {
  state.timer.durationSec = sec;
  state.timer.elapsedBefore = 0;
  state.timer.startTs = Date.now();
  state.timer.paused = false;
  state.timer.fired = false;
  tickTimer();
  savePersisted();
}
document.getElementById('timerReset').addEventListener('click', () => {
  setTimerDuration(state.timer.durationSec);
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
  document.getElementById('timerPauseResume').textContent = t.paused ? '▶ 继续' : '⏸ 暂停';
  savePersisted();
});
document.getElementById('timerExpired10More').addEventListener('click', () => {
  // Add 10 minutes by resetting with extended duration
  state.timer.durationSec += 600;
  state.timer.fired = false;
  state.timer.elapsedBefore = state.timer.elapsedBefore; // keep elapsed
  closeModal('timerExpiredModal');
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
setTool(state.tool);
loadPage(state.pageKey);
applyView();
tickTimer();
// First-run help popup
try {
  if (!localStorage.getItem('cga_help_seen')) {
    openModal('helpModal');
    localStorage.setItem('cga_help_seen', '1');
  }
} catch (_) {}

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
