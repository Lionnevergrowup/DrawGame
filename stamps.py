"""All 30 small "stamp" icons that the user can stick on the canvas.

Each call to stamp() registers one stamp:
    stamp(key, display_name, viewBox_size, svg_body, category)
The svg_body uses __C__ as the placeholder for the foreground color
(replaced with state.color at placement time).
"""

STAMPS = []
def stamp(key, name, vb, svg, cat='thing'):
    STAMPS.append((key, name, vb, svg.strip(), cat))

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
