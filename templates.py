"""All 100 coloring page templates.

Each call to add() registers one template:
    add(key, display_name, category, svg_body)
Categories must match those in CATEGORIES (see build.py).
The svg_body is inline SVG inside a <g> wrapper; mark color-fillable
regions with class="fillable" fill="#ffffff".
"""

TEMPLATES = []
def add(key, name, cat, svg):
    TEMPLATES.append((key, name, cat, svg.strip()))

# --- Animals (10) ---
add('panda', '🐼 熊猫吃竹子', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="340" cy="52" r="24"/>
  <path class="fillable" fill="#ffffff" d="M38 74 Q38 54 60 56 Q68 38 90 44 Q108 36 116 56 Q134 58 130 74 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M54 252 L54 120 Q54 112 62 112 L70 112 Q78 112 78 120 L78 250 Z"/>
  <path fill="none" d="M54 160 L78 160 M54 205 L78 205"/>
  <path class="fillable" fill="#ffffff" d="M78 140 Q104 118 126 128 Q104 150 78 148 Z"/>
  <path class="fillable" fill="#ffffff" d="M54 182 Q28 164 14 176 Q32 194 54 190 Z"/>
  <circle class="fillable" fill="#ffffff" cx="146" cy="66" r="24"/>
  <circle class="fillable" fill="#ffffff" cx="254" cy="66" r="24"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="206" rx="72" ry="60"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="218" rx="42" ry="36"/>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="252" rx="30" ry="20"/>
  <ellipse class="fillable" fill="#ffffff" cx="250" cy="252" rx="30" ry="20"/>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="254" rx="13" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="250" cy="254" rx="13" ry="9"/>
  <path class="fillable" fill="#ffffff" d="M134 170 Q108 196 120 222 Q136 230 148 214 Q154 192 150 176 Z"/>
  <path class="fillable" fill="#ffffff" d="M266 170 Q292 196 280 222 Q264 230 252 214 Q246 192 250 176 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="116" r="64"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="112" rx="17" ry="22" transform="rotate(-25 172 112)"/>
  <ellipse class="fillable" fill="#ffffff" cx="228" cy="112" rx="17" ry="22" transform="rotate(25 228 112)"/>
  <circle class="fillable" fill="#ffffff" cx="174" cy="110" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="226" cy="110" r="8"/>
  <circle fill="#1a1a1a" stroke="none" cx="175" cy="111" r="5"/>
  <circle fill="#1a1a1a" stroke="none" cx="225" cy="111" r="5"/>
  <circle fill="#ffffff" stroke="none" cx="177" cy="108" r="2"/>
  <circle fill="#ffffff" stroke="none" cx="227" cy="108" r="2"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="140" rx="24" ry="17"/>
  <path class="fillable" fill="#ffffff" d="M190 132 Q200 126 210 132 Q206 140 200 140 Q194 140 190 132 Z"/>
  <path fill="none" d="M200 140 L200 146 M188 148 Q194 154 200 146 Q206 154 212 148"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="142" rx="10" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="242" cy="142" rx="10" ry="7"/>
</g>
''')

add('lion', '🦁 小狮子', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="50" r="22"/>
  <path class="fillable" fill="#ffffff" d="M28 74 Q28 55 48.9 56.9 Q56.5 39.8 77.4 45.5 Q94.5 37.9 102.1 56.9 Q119.2 58.8 115.4 74 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 252 Q100 238 200 250 Q300 262 400 246 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M249.4 242 L250.6 242.1 L252.3 242.4 L254.4 242.7 L256.8 243.2 L259.5 243.7 L262.4 244.2 L265.4 244.8 L268.6 245.3 L271.8 245.8 L275.1 246.2 L278.3 246.5 L281.6 246.6 L284.7 246.6 L287.8 246.4 L290.8 246 L293.7 245.2 L296.3 244.2 L298.7 242.9 L300.9 241.5 L303.1 239.8 L305 238.1 L306.9 236.2 L308.7 234.3 L310.3 232.3 L311.9 230.3 L313.3 228.2 L314.7 226.1 L316 224.1 L317.2 222.1 L318.4 220.1 L319.4 218.2 L320.4 216.4 L321.4 214.3 L322.3 212.2 L323 210 L323.6 207.7 L324.1 205.5 L324.6 203.3 L324.9 201.2 L325.2 199 L325.4 197 L325.6 195.1 L325.8 193.2 L325.9 191.5 L326.1 190 L326.2 188.7 L326.3 187.7 L326.4 186.9 C327.7 181.1 318.9 179.2 317.6 185.1 L317.3 186.3 L317.1 187.6 L316.9 189.1 L316.7 190.6 L316.5 192.3 L316.3 194 L316.1 195.8 L315.8 197.7 L315.5 199.6 L315.1 201.5 L314.7 203.4 L314.2 205.2 L313.6 207 L313 208.6 L312.4 210.2 L311.6 211.6 L310.6 213.3 L309.6 215 L308.5 216.8 L307.4 218.6 L306.1 220.4 L304.9 222.2 L303.5 224 L302.2 225.7 L300.8 227.3 L299.3 228.8 L297.8 230.2 L296.3 231.5 L294.8 232.6 L293.3 233.5 L291.8 234.2 L290.3 234.8 L288.8 235.1 L286.8 235.4 L284.5 235.5 L282 235.4 L279.3 235.2 L276.4 234.9 L273.4 234.5 L270.4 234 L267.5 233.4 L264.6 232.8 L261.8 232.2 L259.1 231.7 L256.7 231.1 L254.4 230.7 L252.4 230.3 L250.6 230 C242.6 229.3 241.5 241.2 249.4 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M322 194 Q300 186 306 166 Q310 154 318 160 Q318 144 330 146 Q338 150 336 160 Q346 156 348 170 Q348 190 322 194 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="130" cy="258" rx="26" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="270" cy="258" rx="26" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="214" rx="72" ry="50"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="222" rx="28" ry="32"/>
  <path class="fillable" fill="#ffffff" d="M156 214 Q156 200 170 200 Q184 200 184 214 L184 255.4 Q184 268 170 268 Q156 268 156 255.4 Z"/>
  <path fill="none" stroke-width="3" d="M164.4 260 L164.4 268 M175.6 260 L175.6 268"/>
  <path class="fillable" fill="#ffffff" d="M216 214 Q216 200 230 200 Q244 200 244 214 L244 255.4 Q244 268 230 268 Q216 268 216 255.4 Z"/>
  <path fill="none" stroke-width="3" d="M224.4 260 L224.4 268 M235.6 260 L235.6 268"/>
  <path class="fillable" fill="#ffffff" d="M200 34 Q221.8 18.5 234.7 41.9 Q261.1 37.4 262.5 64.1 Q288.3 71.5 278 96.2 Q298 114 278 131.8 Q288.3 156.5 262.5 163.9 Q261.1 190.6 234.7 186.1 Q221.8 209.5 200 194 Q178.2 209.5 165.3 186.1 Q138.9 190.6 137.5 163.9 Q111.7 156.5 122 131.8 Q102 114 122 96.2 Q111.7 71.5 137.5 64.1 Q138.9 37.4 165.3 41.9 Q178.2 18.5 200 34 Z"/>
  <path class="fillable" fill="#ffffff" d="M217.1 50.2 Q240 44.7 246.7 67.3 Q269.3 74 263.8 96.9 Q280 114 263.8 131.1 Q269.3 154 246.7 160.7 Q240 183.3 217.1 177.8 Q200 194 182.9 177.8 Q160 183.3 153.3 160.7 Q130.7 154 136.2 131.1 Q120 114 136.2 96.9 Q130.7 74 153.3 67.3 Q160 44.7 182.9 50.2 Q200 34 217.1 50.2 Z"/>
  <circle class="fillable" fill="#ffffff" cx="150" cy="62" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="250" cy="62" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="150" cy="62" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="250" cy="62" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="118" r="54"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="106" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="107" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="183.2" cy="104.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="106" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="107" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="223.2" cy="104.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="189" cy="140" rx="14" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="211" cy="140" rx="14" ry="11"/>
  <path class="fillable" fill="#ffffff" d="M189 127 Q200 121 211 127 Q207 136 200 138 Q193 136 189 127 Z"/>
  <path fill="none" stroke-width="3" d="M200 138 L200 144 M193 156 Q200 160 207 156"/>
  <ellipse class="fillable" fill="#ffffff" cx="160" cy="132" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="240" cy="132" rx="9" ry="6"/>
</g>
''')

add('tiger', '🐯 老虎', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="52" cy="50" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 252 Q100 238 200 250 Q300 262 400 246 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M254.5 248.9 L255.6 249.1 L257.3 249.4 L259.4 249.8 L261.9 250.4 L264.8 251 L267.8 251.7 L271 252.3 L274.4 253 L277.9 253.6 L281.4 254.2 L284.9 254.7 L288.4 255 L291.9 255.2 L295.4 255.3 L298.9 255 L302.4 254.4 L305.2 253.6 L307.8 252.7 L310.4 251.6 L312.9 250.4 L315.3 249 L317.6 247.4 L319.7 245.8 L321.8 243.9 L323.7 242 L325.5 240 L327.2 237.8 L328.7 235.6 L330.1 233.2 L331.4 230.8 L332.6 228.3 L333.7 225.7 L334.7 222.3 L335.4 219 L336 215.5 L336.3 212 L336.5 208.4 L336.7 204.8 L336.7 201.1 L336.7 197.5 L336.6 194 L336.5 190.6 L336.4 187.4 L336.2 184.5 L336.1 181.8 L336 179.5 L336 177.7 L336 176.4 C336.6 163.1 316.6 162.3 316 175.6 L315.9 177.7 L316 179.9 L316 182.4 L316.1 185.2 L316.2 188.1 L316.2 191.2 L316.3 194.4 L316.3 197.7 L316.3 201 L316.2 204.2 L316.1 207.3 L315.9 210.2 L315.6 212.9 L315.2 215.2 L314.8 217.1 L314.3 218.3 L313.7 219.9 L312.9 221.4 L312.2 222.8 L311.3 224.1 L310.4 225.4 L309.5 226.5 L308.5 227.6 L307.5 228.6 L306.4 229.5 L305.3 230.3 L304.1 231 L302.9 231.7 L301.7 232.3 L300.4 232.8 L299 233.3 L297.6 233.6 L296.5 233.8 L294.9 233.8 L292.8 233.8 L290.3 233.6 L287.6 233.3 L284.7 232.9 L281.7 232.3 L278.6 231.7 L275.5 231.1 L272.5 230.4 L269.6 229.7 L266.8 229.1 L264.2 228.5 L261.8 227.9 L259.6 227.5 L257.5 227.1 C243 225.1 240 246.9 254.5 248.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M316 186 L336 186 L336 174 Q336 164 326 164 Q316 164 316 174 Z"/>
  <path class="fillable" fill="#ffffff" d="M304 233 L318 244 L329 232 L316 222 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="128" cy="258" rx="26" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="272" cy="258" rx="26" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="212" rx="72" ry="50"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="224" rx="30" ry="32"/>
  <path class="fillable" fill="#ffffff" d="M131 198 Q148 200 156 208 Q146 214 130 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M269 198 Q252 200 244 208 Q254 214 270 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M156 214 Q156 200 170 200 Q184 200 184 214 L184 255.4 Q184 268 170 268 Q156 268 156 255.4 Z"/>
  <path fill="none" stroke-width="3" d="M164.4 260 L164.4 268 M175.6 260 L175.6 268"/>
  <path class="fillable" fill="#ffffff" d="M216 214 Q216 200 230 200 Q244 200 244 214 L244 255.4 Q244 268 230 268 Q216 268 216 255.4 Z"/>
  <path fill="none" stroke-width="3" d="M224.4 260 L224.4 268 M235.6 260 L235.6 268"/>
  <circle class="fillable" fill="#ffffff" cx="148" cy="72" r="19"/>
  <circle class="fillable" fill="#ffffff" cx="252" cy="72" r="19"/>
  <circle class="fillable" fill="#ffffff" cx="148" cy="72" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="252" cy="72" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="116" rx="64" ry="56"/>
  <path class="fillable" fill="#ffffff" d="M184 62 Q200 92 216 62 Q200 58 184 62 Z"/>
  <path class="fillable" fill="#ffffff" d="M137 104 Q154 106 162 114 Q152 120 137 120 Z"/>
  <path class="fillable" fill="#ffffff" d="M263 104 Q246 106 238 114 Q248 120 263 120 Z"/>
  <path class="fillable" fill="#ffffff" d="M139 132 Q152 132 158 138 Q150 144 142 142 Z"/>
  <path class="fillable" fill="#ffffff" d="M261 132 Q248 132 242 138 Q250 144 258 142 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="184" cy="144" rx="19" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="216" cy="144" rx="19" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="178" cy="108" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="179" cy="109" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="181.2" cy="106.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="222" cy="108" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="223" cy="109" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="225.2" cy="106.5" r="2.1"/>
  <path class="fillable" fill="#ffffff" d="M188 128 Q200 122 212 128 Q208 138 200 140 Q192 138 188 128 Z"/>
  <path fill="none" stroke-width="3" d="M200 140 L200 148 M190 156 Q200 162 210 156"/>
  <path fill="none" stroke-width="2.5" d="M168 144 L146 140 M168 150 L148 154 M232 144 L254 140 M232 150 L252 154"/>
</g>
''')

add('penguin', '🐧 小企鹅', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="344" cy="46" r="22"/>
  <path class="fillable" fill="#ffffff" d="M30 72 Q30 54 49.8 55.8 Q57 39.6 76.8 45 Q93 37.8 100.2 55.8 Q116.4 57.6 112.8 72 Z"/>
  <path class="fillable" fill="#ffffff" d="M14 256 Q14 184 66 184 Q118 184 118 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M48 256 L48 238 Q48 222 66 222 Q84 222 84 238 L84 256 Z"/>
  <path fill="none" stroke-width="3" d="M24 216 L108 216 M17 236 L48 236 M84 236 L115 236 M40 196 L92 196 M60 184 L60 196 M50 196 L50 216 M82 196 L82 216 M34 216 L34 236 M98 216 L98 236"/>
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 244 200 252 Q300 262 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M136 140 Q102 172 110 216 Q126 210 140 184 Z"/>
  <path class="fillable" fill="#ffffff" d="M262 150 Q288 122 306 110 Q320 104 316 120 Q302 152 270 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 50 C262 50 282 150 274 210 C268 250 240 262 200 262 C160 262 132 250 126 210 C118 150 138 50 200 50 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="206" rx="50" ry="52"/>
  <path class="fillable" fill="#ffffff" d="M200 98 C182 78 150 84 152 116 C154 140 172 152 200 152 C228 152 246 140 248 116 C250 84 218 78 200 98 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="266" rx="24" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="228" cy="266" rx="24" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="181" cy="114" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="182" cy="115" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="184.2" cy="112.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="219" cy="114" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="220" cy="115" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="222.2" cy="112.5" r="2.1"/>
  <path class="fillable" fill="#ffffff" d="M187 128 Q200 122 213 128 Q207 144 200 146 Q193 144 187 128 Z"/>
  <path fill="none" stroke-width="2.5" d="M190 132 Q200 137 210 132"/>
  <ellipse class="fillable" fill="#ffffff" cx="166" cy="136" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="234" cy="136" rx="9" ry="6"/>
  <path class="fillable" fill="#ffffff" d="M146 150 Q200 172 254 150 L256 166 Q200 190 144 166 Z"/>
  <path class="fillable" fill="#ffffff" d="M226 172 L236 210 L254 206 L246 166 Z"/>
  <path class="fillable" fill="#ffffff" d="M146 84 Q150 36 200 34 Q250 36 254 84 Q200 72 146 84 Z"/>
  <path class="fillable" fill="#ffffff" d="M142 92 Q200 74 258 92 L256 78 Q200 62 144 78 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="30" r="13"/>
</g>
''')

add('cat', '🐱 小猫和毛线球', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="52" cy="48" r="20"/>
  <path class="fillable" fill="#ffffff" d="M250 70 Q250 53 268.7 54.7 Q275.5 39.4 294.2 44.5 Q309.5 37.7 316.3 54.7 Q331.6 56.4 328.2 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 252 Q100 238 200 250 Q300 262 400 246 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M200.7 247 L201.6 246.9 L203 246.8 L204.9 246.9 L207.2 246.9 L209.7 247 L212.4 247 L215.3 247 L218.3 247 L221.4 246.9 L224.5 246.7 L227.6 246.4 L230.6 245.9 L233.6 245.2 L236.6 244.2 L239.4 242.9 L242.1 241.1 L244.2 239.1 L246 236.9 L247.6 234.6 L249 232.1 L250.2 229.5 L251.3 226.8 L252.2 224.1 L253 221.3 L253.7 218.5 L254.3 215.7 L254.8 212.9 L255.2 210.2 L255.5 207.5 L255.8 205 L255.9 202.5 L256 200.2 L256 197.7 L255.8 195.2 L255.4 192.8 L255 190.4 L254.5 188 L253.8 185.6 L253.1 183.3 L252.3 181 L251.4 178.9 L250.5 176.8 L249.5 174.8 L248.5 172.9 L247.5 171.1 L246.5 169.4 L245.4 167.9 L244.2 166.5 L242.7 164.9 L241 163.7 L239.2 162.7 L237.4 162 L235.7 161.5 L233.9 161.2 L232.3 161 L230.7 160.9 L229.2 160.9 L227.8 160.9 L226.5 160.9 L225.3 161 L224.3 161 L223.5 161.1 L223.1 161.1 L223.1 161.1 C216.6 159.7 214.4 169.4 220.9 170.9 L222.2 171.1 L223.3 171.2 L224.4 171.2 L225.5 171.2 L226.7 171.2 L227.8 171.3 L228.9 171.3 L230.1 171.4 L231.1 171.5 L232.1 171.7 L233.1 171.9 L233.9 172.1 L234.5 172.5 L235 172.8 L235.4 173.1 L235.8 173.5 L236.4 174.4 L237.1 175.5 L237.9 176.8 L238.6 178.2 L239.4 179.7 L240.1 181.4 L240.8 183.1 L241.5 185 L242.1 186.8 L242.6 188.7 L243.1 190.7 L243.5 192.6 L243.8 194.5 L243.9 196.3 L244 198.1 L244 199.8 L243.9 201.8 L243.7 203.9 L243.4 206.1 L243.1 208.4 L242.7 210.8 L242.2 213.2 L241.6 215.6 L241 217.9 L240.3 220.2 L239.5 222.3 L238.6 224.3 L237.7 226.1 L236.8 227.7 L235.8 229.1 L234.8 230.1 L233.9 230.9 L233.2 231.4 L231.9 231.9 L230.2 232.4 L228.2 232.8 L226 233.1 L223.5 233.4 L220.9 233.5 L218.2 233.5 L215.5 233.5 L212.8 233.4 L210.2 233.3 L207.7 233.2 L205.3 233.1 L203.2 233 L201.2 233 L199.3 233 C190 234 191.5 247.9 200.7 247 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="118" cy="248" rx="24" ry="18"/>
  <ellipse class="fillable" fill="#ffffff" cx="198" cy="248" rx="24" ry="18"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="210" rx="56" ry="48"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="220" rx="26" ry="30"/>
  <path class="fillable" fill="#ffffff" d="M128 213 Q128 200 141 200 Q154 200 154 213 L154 256.3 Q154 268 141 268 Q128 268 128 256.3 Z"/>
  <path fill="none" stroke-width="3" d="M135.8 260 L135.8 268 M146.2 260 L146.2 268"/>
  <path class="fillable" fill="#ffffff" d="M162 213 Q162 200 175 200 Q188 200 188 213 L188 256.3 Q188 268 175 268 Q162 268 162 256.3 Z"/>
  <path fill="none" stroke-width="3" d="M169.8 260 L169.8 268 M180.2 260 L180.2 268"/>
  <path class="fillable" fill="#ffffff" d="M108 98 L106 44 Q108 34 118 40 L150 66 Z"/>
  <path class="fillable" fill="#ffffff" d="M208 98 L210 44 Q208 34 198 40 L166 66 Z"/>
  <path class="fillable" fill="#ffffff" d="M116 80 L115 54 L136 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 80 L201 54 L180 70 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="108" rx="58" ry="48"/>
  <path class="fillable" fill="#ffffff" d="M150 61 Q158 76 166 61 Q158 59 150 61 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="140" cy="104" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="141" cy="105" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="143.2" cy="102.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="178" cy="104" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="178" cy="105" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="180.2" cy="102.5" r="2.1"/>
  <path class="fillable" fill="#ffffff" d="M151 120 Q158 116 165 120 Q162 127 158 128 Q154 127 151 120 Z"/>
  <path fill="none" stroke-width="3" d="M158 128 L158 133 M148 136 Q153 141 158 133 Q163 141 168 136"/>
  <path fill="none" stroke-width="2.5" d="M128 124 L102 120 M128 130 L104 134 M188 124 L214 120 M188 130 L212 134"/>
  <ellipse class="fillable" fill="#ffffff" cx="126" cy="128" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="190" cy="128" rx="8" ry="5"/>
  <path class="fillable" fill="#ffffff" d="M120 146 Q158 166 196 146 L196 156 Q158 176 120 156 Z"/>
  <circle class="fillable" fill="#ffffff" cx="158" cy="170" r="8"/>
  <path fill="none" stroke-width="3" d="M286 256 Q262 272 236 266 Q222 262 228 254"/>
  <circle class="fillable" fill="#ffffff" cx="312" cy="232" r="38"/>
  <path fill="none" stroke-width="3" d="M282 212 Q312 222 330 262 M276 240 Q304 238 322 268 M290 200 Q326 210 346 236 M300 196 Q340 210 349 222"/>
</g>
''')

add('dog', '🐶 小狗和骨头', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="52" cy="46" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 240 200 252 Q300 264 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 252 L268 150 L372 150 L372 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M254 158 L320 96 L386 158 Q390 166 380 166 L260 166 Q250 166 254 158 Z"/>
  <path class="fillable" fill="#ffffff" d="M298 252 L298 214 Q298 192 320 192 Q342 192 342 214 L342 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M214.9 232.4 L215.5 232.1 L216.5 231.6 L217.8 231.1 L219.3 230.6 L220.9 229.9 L222.7 229.3 L224.7 228.5 L226.7 227.7 L228.7 226.9 L230.8 225.9 L232.8 224.9 L234.9 223.9 L236.9 222.7 L238.8 221.5 L240.6 220.1 L242.4 218.6 L243.8 217.1 L245.1 215.5 L246.3 213.8 L247.5 212.1 L248.6 210.4 L249.6 208.6 L250.5 206.7 L251.3 204.9 L252.1 203.1 L252.8 201.3 L253.4 199.5 L254 197.7 L254.5 195.9 L254.9 194.3 L255.3 192.6 L255.6 191.1 L255.8 189.2 L255.8 187.3 L255.7 185.6 L255.5 183.9 L255.1 182.2 L254.7 180.7 L254.3 179.2 L253.8 177.8 L253.3 176.5 L252.8 175.3 L252.3 174.2 L251.9 173.2 L251.5 172.3 L251.2 171.6 L251 171.1 L250.9 170.9 C249.4 164.4 239.7 166.6 241.1 173.1 L241.4 174.1 L241.6 175.1 L242 176 L242.3 177 L242.6 178 L243 179 L243.4 180.1 L243.7 181.2 L244 182.3 L244.2 183.4 L244.4 184.4 L244.6 185.5 L244.7 186.4 L244.7 187.3 L244.6 188.2 L244.4 188.9 L244.1 190.1 L243.8 191.3 L243.4 192.7 L242.9 194 L242.4 195.5 L241.8 196.9 L241.1 198.4 L240.4 199.8 L239.7 201.3 L238.9 202.7 L238.1 204 L237.2 205.3 L236.3 206.5 L235.4 207.6 L234.5 208.6 L233.6 209.4 L232.8 210.1 L231.7 210.8 L230.4 211.6 L228.9 212.4 L227.2 213.1 L225.5 213.9 L223.7 214.6 L221.8 215.3 L220 215.9 L218.2 216.6 L216.4 217.1 L214.7 217.7 L213.2 218.2 L211.7 218.7 L210.4 219.1 L209.1 219.6 C200.6 223.5 206.5 236.3 214.9 232.4 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="124" cy="258" rx="24" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="258" rx="24" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="214" rx="58" ry="48"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="224" rx="26" ry="30"/>
  <path class="fillable" fill="#ffffff" d="M140 215 Q140 202 153 202 Q166 202 166 215 L166 256.3 Q166 268 153 268 Q140 268 140 256.3 Z"/>
  <path fill="none" stroke-width="3" d="M147.8 260 L147.8 268 M158.2 260 L158.2 268"/>
  <path class="fillable" fill="#ffffff" d="M178 215 Q178 202 191 202 Q204 202 204 215 L204 256.3 Q204 268 191 268 Q178 268 178 256.3 Z"/>
  <path fill="none" stroke-width="3" d="M185.8 260 L185.8 268 M196.2 260 L196.2 268"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="112" rx="56" ry="48"/>
  <ellipse class="fillable" fill="#ffffff" cx="192" cy="104" rx="17" ry="19"/>
  <path class="fillable" fill="#ffffff" d="M130 76 Q104 86 104 136 Q108 158 124 150 Q138 120 142 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M214 76 Q240 86 240 136 Q236 158 220 150 Q206 120 202 86 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="154" cy="104" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="155" cy="105" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="157.2" cy="102.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="192" cy="104" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="193" cy="105" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="195.2" cy="102.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="138" rx="26" ry="18"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="128" rx="11" ry="8"/>
  <path class="fillable" fill="#ffffff" d="M164 145 Q164 160 172 160 Q180 160 180 145 Z"/>
  <path fill="none" stroke-width="3" d="M172 136 L172 143 M158 143 Q165 150 172 143 Q179 150 186 143"/>
  <path class="fillable" fill="#ffffff" d="M130 156 Q172 176 214 156 L214 166 Q172 186 130 166 Z"/>
  <circle class="fillable" fill="#ffffff" cx="172" cy="182" r="8"/>
  <path class="fillable" fill="#ffffff" d="M292 262 Q286 248 276 254 Q268 260 276 268 Q268 276 276 282 Q286 288 292 274 L338 274 Q344 288 354 282 Q362 276 354 268 Q362 260 354 254 Q344 248 338 262 Z"/>
</g>
''')

add('rabbit', '🐰 小兔子和胡萝卜', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M26 76 Q26 58 45.8 59.8 Q53 43.6 72.8 49 Q89 41.8 96.2 59.8 Q112.4 61.6 108.8 76 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 240 200 252 Q300 264 400 248 L400 300 L0 300 Z"/>
  <path fill="none" stroke-width="3" d="M64 252 Q60 220 66 196"/>
  <path class="fillable" fill="#ffffff" d="M66 196 Q50 178 62 168 Q66 152 78 160 Q92 156 88 172 Q100 184 82 190 Q76 204 66 196 Z"/>
  <circle class="fillable" fill="#ffffff" cx="74" cy="178" r="8"/>
  <path class="fillable" fill="#ffffff" d="M63 230 Q46 220 40 230 Q50 240 63 236 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="58" rx="17" ry="46" transform="rotate(-10 170 58)"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="58" rx="17" ry="46" transform="rotate(10 220 58)"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="62" rx="8" ry="32" transform="rotate(-10 170 62)"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="62" rx="8" ry="32" transform="rotate(10 220 62)"/>
  <circle class="fillable" fill="#ffffff" cx="252" cy="236" r="15"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="214" rx="58" ry="48"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="224" rx="34" ry="32"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="260" rx="28" ry="12"/>
  <ellipse class="fillable" fill="#ffffff" cx="232" cy="260" rx="28" ry="12"/>
  <circle class="fillable" fill="#ffffff" cx="195" cy="126" r="50"/>
  <ellipse class="fillable" fill="#ffffff" cx="176" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="177" cy="121" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="179.2" cy="118.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="214" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="215" cy="121" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="217.2" cy="118.5" r="2.1"/>
  <path class="fillable" fill="#ffffff" d="M189 136 Q195 132 201 136 Q199 142 195 143 Q191 142 189 136 Z"/>
  <path class="fillable" fill="#ffffff" d="M189 150 L189 158 Q189 161 192 161 L198 161 Q201 161 201 158 L201 150 Z"/>
  <path fill="none" stroke-width="2.5" d="M195 143 L195 148 M185 146 Q190 152 195 148 Q200 152 205 146 M195 150 L195 160"/>
  <ellipse class="fillable" fill="#ffffff" cx="160" cy="140" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="230" cy="140" rx="9" ry="6"/>
  <path class="fillable" fill="#ffffff" d="M256 166 Q244 136 254 116 Q268 134 266 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M264 168 Q276 138 298 132 Q296 158 272 174 Z"/>
  <path class="fillable" fill="#ffffff" d="M270 178 Q294 166 310 178 Q292 194 272 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M236 170 Q254 152 274 170 Q288 188 270 204 L186 254 Q172 260 172 246 Z"/>
  <path fill="none" stroke-width="2.5" d="M246 186 L256 196 M222 204 L230 214 M200 222 L206 230"/>
  <ellipse class="fillable" fill="#ffffff" cx="204" cy="220" rx="14" ry="11" transform="rotate(-30 204 220)"/>
  <ellipse class="fillable" fill="#ffffff" cx="248" cy="192" rx="14" ry="11" transform="rotate(-30 248 192)"/>
</g>
''')

add('fox', '🦊 小狐狸', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M28 74 Q28 56 47.8 57.8 Q55 41.6 74.8 47 Q91 39.8 98.2 57.8 Q114.4 59.6 110.8 74 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 240 200 252 Q300 264 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 252 L62 222 Q70 218 78 222 L80 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M38 224 Q40 188 70 186 Q100 188 102 224 Q70 234 38 224 Z"/>
  <circle class="fillable" fill="#ffffff" cx="70" cy="202" r="8"/>
  <path class="fillable" fill="#ffffff" d="M236.4 249 L237.9 250.4 L239.8 251.5 L242.2 252.5 L244.9 253.4 L248 254.4 L251.3 255.3 L254.9 256.1 L258.6 256.8 L262.5 257.5 L266.5 258 L270.6 258.3 L274.7 258.4 L279 258.3 L283.3 257.8 L287.8 256.9 L292.5 255.3 L296.2 253.6 L299.7 251.6 L303 249.4 L306.2 247 L309.1 244.3 L311.9 241.6 L314.5 238.7 L316.9 235.6 L319.1 232.5 L321.1 229.2 L323 225.9 L324.7 222.5 L326.2 219.1 L327.5 215.5 L328.6 212 L329.5 208.3 L330.3 203.8 L330.6 199.5 L330.6 195.3 L330.3 191.3 L329.8 187.4 L329.1 183.6 L328.3 179.9 L327.4 176.3 L326.3 172.9 L325.2 169.6 L324 166.4 L322.8 163.4 L321.5 160.6 L320.3 158 L319.1 155.6 L317.9 153.5 L316.2 150.5 L314.4 147.8 L282.1 164.3 L282.2 165.4 L282.1 166.5 L282.5 168.7 L282.9 171 L283.4 173.4 L283.8 175.8 L284.3 178.4 L284.8 180.9 L285.2 183.4 L285.6 185.9 L286 188.4 L286.3 190.7 L286.5 192.8 L286.6 194.8 L286.6 196.5 L286.6 198 L286.5 199 L286.5 199.7 L286.2 201.1 L285.9 202.7 L285.4 204.3 L284.9 206.1 L284.3 207.9 L283.7 209.7 L282.9 211.6 L282.1 213.4 L281.3 215.1 L280.5 216.8 L279.6 218.4 L278.7 219.9 L277.8 221.3 L277 222.6 L276.2 223.7 L275.5 224.7 L275.3 225.4 L274.3 226.3 L272.6 227.3 L270.4 228.3 L267.8 229.2 L264.8 230.1 L261.7 230.9 L258.4 231.7 L255.1 232.4 L251.8 233.1 L248.5 233.9 L245.5 234.6 L242.6 235.4 L239.9 236.4 L237.6 237.5 L235.6 239 C229 239.6 229.8 249.5 236.4 249 Z"/>
  <path class="fillable" fill="#ffffff" d="M314.4 147.8 L312.5 145.3 L310.6 143.1 L308.6 141.2 L306.6 139.4 L304.7 137.9 L302.7 136.5 L300.9 135.4 L299.1 134.4 L297.4 133.7 L295.8 133.1 L294.4 132.7 L293.1 132.5 L292 132.5 L291.2 132.8 C284.2 123.3 269.9 133.7 276.8 143.2 L277.1 145 L277.5 146.6 L277.9 148.2 L278.3 149.8 L278.8 151.4 L279.3 152.9 L279.8 154.4 L280.3 156 L280.7 157.5 L281.1 158.9 L281.5 160.4 L281.8 161.7 L282 163.1 L282.1 164.3 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="146" cy="258" rx="24" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="254" cy="258" rx="24" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="214" rx="60" ry="48"/>
  <path class="fillable" fill="#ffffff" d="M182 160 Q160 204 200 236 Q240 204 218 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 217 Q164 204 177 204 Q190 204 190 217 L190 256.3 Q190 268 177 268 Q164 268 164 256.3 Z"/>
  <path fill="none" stroke-width="3" d="M171.8 260 L171.8 268 M182.2 260 L182.2 268"/>
  <path class="fillable" fill="#ffffff" d="M210 217 Q210 204 223 204 Q236 204 236 217 L236 256.3 Q236 268 223 268 Q210 268 210 256.3 Z"/>
  <path fill="none" stroke-width="3" d="M217.8 260 L217.8 268 M228.2 260 L228.2 268"/>
  <path class="fillable" fill="#ffffff" d="M142 84 L134 30 Q136 20 146 24 L188 62 Z"/>
  <path class="fillable" fill="#ffffff" d="M258 84 L266 30 Q264 20 254 24 L212 62 Z"/>
  <path class="fillable" fill="#ffffff" d="M148 70 L144 40 L170 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M252 70 L256 40 L230 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M134 102 Q136 56 200 54 Q264 56 266 102 Q268 120 248 134 L214 160 Q200 170 186 160 L152 134 Q132 120 134 102 Z"/>
  <path class="fillable" fill="#ffffff" d="M138 116 Q170 108 190 128 Q200 138 210 128 Q230 108 262 116 Q258 128 246 136 L213 159 Q200 168 187 159 L154 136 Q142 128 138 116 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="174" cy="100" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="175" cy="101" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="177.2" cy="98.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="226" cy="100" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="227" cy="101" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="229.2" cy="98.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="156" rx="10" ry="7"/>
  <path fill="none" stroke-width="3" d="M188 140 Q194 146 200 140 Q206 146 212 140"/>
  <ellipse class="fillable" fill="#ffffff" cx="160" cy="124" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="240" cy="124" rx="9" ry="6"/>
</g>
''')

add('elephant', '🐘 大象洗澡', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="52" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 254 Q300 266 400 250 L400 300 L0 300 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="136" cy="112" rx="42" ry="48" transform="rotate(-10 136 112)"/>
  <ellipse class="fillable" fill="#ffffff" cx="264" cy="112" rx="42" ry="48" transform="rotate(10 264 112)"/>
  <ellipse class="fillable" fill="#ffffff" cx="140" cy="116" rx="26" ry="32" transform="rotate(-10 140 116)"/>
  <ellipse class="fillable" fill="#ffffff" cx="260" cy="116" rx="26" ry="32" transform="rotate(10 260 116)"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="186" rx="76" ry="34"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="116" rx="58" ry="52"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="104" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="105" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="183.2" cy="102.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="104" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="105" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="223.2" cy="102.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="134" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="134" rx="9" ry="6"/>
  <path class="fillable" fill="#ffffff" d="M86 188 L314 188 Q312 262 262 262 L138 262 Q88 262 86 188 Z"/>
  <path fill="none" stroke-width="5" d="M150 262 L142 276 M250 262 L258 276"/>
  <path class="fillable" fill="#ffffff" d="M78 176 L322 176 Q332 176 332 186 Q332 196 322 196 L78 196 Q68 196 68 186 Q68 176 78 176 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="192" rx="19" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="250" cy="192" rx="19" ry="14"/>
  <path fill="none" stroke-width="3" d="M144 200 L144 206 M156 200 L156 206 M244 200 L244 206 M256 200 L256 206"/>
  <path class="fillable" fill="#ffffff" d="M186 132 Q186 168 214 166 Q246 162 262 122 Q268 106 276 98 L292 108 Q282 120 278 132 Q260 182 214 182 Q172 182 172 134 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="284" cy="103" rx="10" ry="6" transform="rotate(34 284 103)"/>
  <path fill="none" stroke-width="2.5" d="M188 148 Q196 152 204 150 M232 156 Q240 160 248 152"/>
  <path class="fillable" fill="#ffffff" d="M300 70 Q308 82 300 88 Q292 82 300 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M304 28 Q316 42 304 50 Q292 42 304 28 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 64 Q344 76 332 86 Q320 76 330 64 Z"/>
  <path fill="none" stroke-width="3" d="M290 90 Q296 70 304 60 M296 96 Q314 82 326 76"/>
  <circle class="fillable" fill="#ffffff" cx="98" cy="162" r="14"/>
  <circle class="fillable" fill="#ffffff" cx="120" cy="150" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="318" cy="162" r="12"/>
</g>
''')

add('owl', '🦉 猫头鹰', 'animal', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M70 22 A34 34 0 1 0 104 74 A27 27 0 1 1 70 22 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 28 L334.7 37.5 L345.2 39.1 L337.6 46.5 L339.4 56.9 L330 52 L320.6 56.9 L322.4 46.5 L314.8 39.1 L325.3 37.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M370 81 L373.2 87.6 L380.5 88.6 L375.2 93.7 L376.5 100.9 L370 97.5 L363.5 100.9 L364.8 93.7 L359.5 88.6 L366.8 87.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 232 Q120 222 250 232 Q330 238 392 226 Q398 234 392 242 Q330 254 250 248 Q120 240 0 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 240 Q318 262 336 270 Q340 262 334 258 Q322 250 316 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M334 236 Q355.5 233.6 361.6 212.9 Q340.1 215.2 334 236 Z"/>
  <path class="fillable" fill="#ffffff" d="M350 240 Q362.2 256.2 381.9 251.6 Q369.7 235.5 350 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 238 Q39.9 243.3 38.1 264 Q58.3 258.7 60 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M142 112 L134 60 Q136 54 142 58 L182 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M258 112 L266 60 Q264 54 258 58 L218 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 76 C264 76 276 140 274 180 C272 228 242 250 200 250 C158 250 128 228 126 180 C124 140 136 76 200 76 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="206" rx="44" ry="40"/>
  <path fill="none" stroke-width="3" d="M176 196 Q182 204 188 196 M194 196 Q200 204 206 196 M212 196 Q218 204 224 196 M184 216 Q190 224 196 216 M204 216 Q210 224 216 216"/>
  <path class="fillable" fill="#ffffff" d="M134 150 Q104 192 124 236 Q150 228 158 196 Q156 164 134 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M266 150 Q296 192 276 236 Q250 228 242 196 Q244 164 266 150 Z"/>
  <circle class="fillable" fill="#ffffff" cx="174" cy="128" r="27"/>
  <circle class="fillable" fill="#ffffff" cx="226" cy="128" r="27"/>
  <ellipse class="fillable" fill="#ffffff" cx="176" cy="128" rx="15" ry="15"/>
  <circle fill="#1a1a1a" stroke="none" cx="178" cy="129" r="8"/>
  <circle fill="#ffffff" stroke="none" cx="181.2" cy="125.4" r="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="224" cy="128" rx="15" ry="15"/>
  <circle fill="#1a1a1a" stroke="none" cx="222" cy="129" r="8"/>
  <circle fill="#ffffff" stroke="none" cx="225.2" cy="125.4" r="3"/>
  <path class="fillable" fill="#ffffff" d="M190 150 Q200 144 210 150 L200 168 Z"/>
  <path class="fillable" fill="#ffffff" d="M174 244 Q170 256 178 256 Q184 262 190 256 Q198 256 194 244 Z"/>
  <path class="fillable" fill="#ffffff" d="M206 244 Q202 256 210 256 Q216 262 222 256 Q230 256 226 244 Z"/>
</g>
''')

# --- Ocean (6) ---
add('ocean', '🐠 海底世界', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 250 Q60 236 130 246 Q220 258 300 242 Q360 234 400 244 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M48.7 257.8 L47.9 255.3 L46.8 252.7 L45.7 249.8 L44.4 246.7 L43.1 243.4 L41.8 239.9 L40.6 236.4 L39.5 232.9 L38.6 229.4 L38 226.2 L37.6 223.3 L37.6 220.8 L37.9 218.6 L38.6 216.1 L39.8 213.3 L41.3 210.3 L43.1 207.1 L45.1 203.7 L47.2 200.3 L49.2 196.7 L51.1 192.9 L52.6 188.9 L53.8 184.7 L54.3 180.3 L54 175.9 L53.1 171.8 L51.8 167.9 L50.2 164.2 L48.4 160.6 L46.5 157.2 L44.7 153.9 L42.9 150.7 L41.4 147.7 L40.2 144.8 L39.4 142.2 L38.9 139.7 L38.9 137 L39.1 134.1 L39.6 130.9 L40.3 127.6 L41.1 124.2 L42.2 120.9 L43.2 117.7 L44.3 114.7 L45.3 111.8 L46.2 109.3 L46.9 107 L47.5 105 C48.8 100.4 41.8 98.4 40.5 103 L39.9 104.5 L39.1 106.5 L38 108.9 L36.8 111.7 L35.4 114.8 L34.1 118.1 L32.8 121.5 L31.6 125.2 L30.5 128.9 L29.7 132.6 L29.2 136.4 L29.1 140.3 L29.5 144.2 L30.4 148.1 L31.7 151.8 L33.2 155.4 L34.9 158.9 L36.5 162.3 L38.1 165.7 L39.5 168.9 L40.6 171.9 L41.4 174.8 L41.7 177.4 L41.7 179.7 L41.3 181.9 L40.4 184.4 L39.1 187.1 L37.5 190 L35.5 193.1 L33.4 196.3 L31.1 199.6 L28.9 203 L26.8 206.7 L24.9 210.6 L23.3 214.7 L22.4 219.2 L22.1 223.7 L22.3 228.1 L22.9 232.5 L23.8 236.8 L24.8 241 L26 245.1 L27.2 249 L28.3 252.6 L29.4 255.8 L30.3 258.6 L31 260.8 L31.3 262.2 C34.2 273.8 51.6 269.4 48.7 257.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M73.5 260.8 L73.8 259.7 L74.5 257.9 L75.5 255.7 L76.7 253 L78.1 250.1 L79.4 246.9 L80.7 243.6 L82 240.1 L83 236.6 L83.9 233.1 L84.4 229.5 L84.4 225.8 L83.8 222 L82.6 218.7 L81 215.6 L79.3 212.8 L77.5 210.2 L75.6 207.7 L73.8 205.3 L72.2 203.1 L70.9 201 L69.8 199.1 L69.1 197.4 L68.8 195.8 L68.8 194 L69 191.7 L69.6 189.2 L70.5 186.5 L71.5 183.7 L72.7 180.9 L74 178.2 L75.2 175.6 L76.4 173.1 L77.4 170.9 L78.3 168.9 L79 167.2 C80.6 163.2 74.6 160.9 73 164.8 L72.4 166 L71.3 167.6 L70.1 169.7 L68.6 172 L67.1 174.6 L65.5 177.3 L64 180.3 L62.6 183.3 L61.3 186.4 L60.2 189.6 L59.5 192.8 L59.2 196.2 L59.5 199.6 L60.4 202.8 L61.7 205.9 L63.2 208.7 L64.8 211.4 L66.4 214.1 L67.9 216.5 L69.3 218.9 L70.4 221.1 L71.2 223.1 L71.5 224.8 L71.6 226.2 L71.4 227.9 L70.9 230.1 L70.1 232.6 L69 235.3 L67.7 238.1 L66.3 240.9 L64.9 243.6 L63.4 246.3 L62 248.8 L60.7 251 L59.5 253.1 L58.5 255.2 C54.8 265.2 69.8 270.8 73.5 260.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M326 252 L330 214 Q314 196 318 170 Q324 160 330 168 Q330 188 338 200 L342 160 Q346 146 354 152 L354 196 Q364 186 366 168 Q372 158 378 166 Q380 196 358 214 L362 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M246 270 Q246 240 268 238 Q290 240 290 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M258 270 L278 270 L274 280 L262 280 Z"/>
  <path fill="none" stroke-width="2.5" d="M258 270 L262 246 M268 270 L268 242 M278 270 L274 246"/>
  <path class="fillable" fill="#ffffff" d="M103.1 254.3 L106.5 265.7 L117.8 269.5 L107.9 276.2 L107.9 288.2 L98.4 280.9 L87.1 284.5 L91.1 273.3 L84.1 263.5 L96.1 263.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M246 130 Q273.5 100 293.5 92.5 Q283.5 130 293.5 167.5 Q273.5 160 246 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M178.5 95 Q201 65 233.5 80 Q228.5 92.5 223.5 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M133.5 130 Q138.5 87.5 196 87.5 Q251 90 258.5 130 Q251 170 196 172.5 Q138.5 172.5 133.5 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M201 87.5 Q216 130 201 172.5 Q216 171.9 226 168.1 Q236 130 226 91.9 Q216 88.1 201 87.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M193.5 140 Q208.5 160 228.5 157.5 Q218.5 137.5 193.5 140 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="163.5" cy="122.5" rx="10" ry="10"/>
  <circle fill="#1a1a1a" stroke="none" cx="161.6" cy="122.5" r="6.2"/>
  <circle fill="#ffffff" stroke="none" cx="164.1" cy="119.7" r="2.4"/>
  <path fill="none" stroke-width="3" d="M141 142.5 Q148.5 150 156 145"/>
  <path class="fillable" fill="#ffffff" d="M294 64 Q280.8 49.6 271.2 46 Q276 64 271.2 82 Q280.8 78.4 294 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M326.4 47.2 Q315.6 32.8 300 40 Q302.4 46 304.8 49.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M348 64 Q345.6 43.6 318 43.6 Q291.6 44.8 288 64 Q291.6 83.2 318 84.4 Q345.6 84.4 348 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M319.2 68.8 Q312 78.4 302.4 77.2 Q307.2 67.6 319.2 68.8 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="333.6" cy="60.4" rx="4.8" ry="4.8"/>
  <circle fill="#1a1a1a" stroke="none" cx="334.5" cy="60.4" r="3"/>
  <circle fill="#ffffff" stroke="none" cx="335.7" cy="59" r="1.6"/>
  <path fill="none" stroke-width="3" d="M344.4 70 Q340.8 73.6 337.2 71.2"/>
  <circle class="fillable" fill="#ffffff" cx="112" cy="112" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="98" cy="86" r="12"/>
  <circle class="fillable" fill="#ffffff" cx="112" cy="54" r="14"/>
</g>
''')

add('whale', '🐋 鲸鱼', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="50" r="22"/>
  <path class="fillable" fill="#ffffff" d="M212 70 Q212 52 231.8 53.8 Q239 37.6 258.8 43 Q275 35.8 282.2 53.8 Q298.4 55.6 294.8 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M290 164 Q316 152 320 126 Q302 116 296 98 Q320 98 332 116 Q346 100 370 102 Q358 124 334 132 Q330 158 304 174 Z"/>
  <path class="fillable" fill="#ffffff" d="M40 170 C38 110 110 82 180 92 C244 100 272 140 302 154 C298 204 240 228 160 228 C88 228 42 212 40 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M40 170 Q120 196 200 194 Q262 192 302 154 C298 204 240 228 160 228 C88 228 42 212 40 170 Z"/>
  <path fill="none" stroke-width="3" d="M90 204 Q140 214 190 212 M126 222 Q170 226 220 220"/>
  <path class="fillable" fill="#ffffff" d="M144 188 Q118 206 128 226 Q152 222 172 196 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="176" cy="112" rx="14" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="214" cy="120" rx="11" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="146" cy="106" rx="9" ry="6"/>
  <path class="fillable" fill="#ffffff" d="M110 90 Q106 62 86 48 Q102 48 112 62 Q112 40 104 22 Q120 30 122 58 Q130 42 148 36 Q136 56 124 90 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="96" cy="146" rx="10" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="97" cy="147" r="6.2"/>
  <circle fill="#ffffff" stroke="none" cx="99.5" cy="144.2" r="2.4"/>
  <ellipse class="fillable" fill="#ffffff" cx="104" cy="172" rx="10" ry="6"/>
  <path fill="none" stroke-width="3" d="M50 176 Q74 188 98 180"/>
  <path class="fillable" fill="#ffffff" d="M0 238 Q25 222 50 238 Q75 254 100 238 Q125 222 150 238 Q175 254 200 238 Q225 222 250 238 Q275 254 300 238 Q325 222 350 238 Q375 254 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 270 Q33 258 66 270 Q100 282 133 270 Q166 258 200 270 Q233 282 266 270 Q300 258 333 270 Q366 282 400 270 L400 300 L0 300 Z"/>
</g>
''')

add('octopus', '🐙 章鱼', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 252 Q80 240 160 250 Q260 262 400 244 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M376.8 260 L376 257.8 L375.2 255.4 L374.2 252.7 L373.1 249.8 L372 246.8 L370.8 243.6 L369.8 240.4 L368.9 237.2 L368.2 234.1 L367.6 231.3 L367.3 228.8 L367.3 226.9 L367.5 225.4 L368 223.6 L368.9 221.6 L370.1 219.5 L371.6 217.2 L373.3 214.7 L375.1 212.2 L376.8 209.5 L378.5 206.6 L380 203.5 L381.1 200.2 L381.7 196.5 L381.6 193 L381.1 189.5 L380.2 186.1 L379.1 182.8 L377.9 179.5 L376.5 176.3 L375.1 173.3 L373.8 170.5 L372.5 168 L371.4 165.8 L370.5 164 L369.9 162.8 C368.3 157.7 360.5 160.1 362.1 165.2 L362.7 167.1 L363.4 169.2 L364.3 171.6 L365.4 174.2 L366.4 177 L367.5 179.9 L368.5 182.9 L369.3 185.8 L370 188.7 L370.4 191.3 L370.5 193.6 L370.3 195.5 L369.9 196.9 L369.1 198.6 L368 200.4 L366.6 202.4 L364.8 204.5 L362.9 206.8 L360.9 209.2 L358.9 211.8 L356.9 214.6 L355.2 217.7 L353.7 221.2 L352.7 225.1 L352.4 229 L352.5 232.8 L352.8 236.7 L353.5 240.6 L354.3 244.4 L355.2 248.2 L356.1 251.7 L357 255.1 L357.8 258.1 L358.5 260.7 L359 262.7 L359.2 264 C361.8 275.6 379.4 271.7 376.8 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M24 262 Q24 240 44 238 Q64 240 64 262 Z"/>
  <circle class="fillable" fill="#ffffff" cx="56" cy="66" r="13"/>
  <circle class="fillable" fill="#ffffff" cx="84" cy="40" r="9"/>
  <path class="fillable" fill="#ffffff" d="M161.1 123.3 L158.9 124 L156.6 124.7 L154.2 125.6 L151.6 126.5 L148.9 127.4 L146 128.4 L143 129.3 L139.9 130.3 L136.9 131.1 L134 131.9 L131.2 132.5 L128.5 133 L126.2 133.4 L124.3 133.6 L122.1 133.7 L119.7 133.7 L117.3 133.6 L114.9 133.4 L112.4 133.1 L110 132.8 L107.6 132.3 L105.2 131.8 L102.9 131.3 L100.7 130.6 L98.6 130 L96.7 129.3 L94.8 128.5 L93.2 127.7 L91.7 127 L90.2 126 L88.6 124.8 L87 123.6 L85.4 122.2 L83.9 120.7 L82.5 119.2 L81.2 117.7 L80.1 116.3 L79.1 114.9 L78.3 113.7 L77.7 112.7 L77.4 111.9 L77.1 111.6 L76.9 112.3 L76.6 112.5 L76.6 112.1 L77.1 111.4 L77.8 110.5 L78.8 109.4 L80 108.4 L81.4 107.3 L82.8 106.3 L84.2 105.3 L85.5 104.3 L86.7 103.4 L87.9 102.4 L89 101.4 C93.5 97.4 87.5 90.7 83 94.6 L82.7 94.6 L81.8 95 L80.5 95.5 L79 96.1 L77.4 96.8 L75.6 97.7 L73.7 98.6 L71.8 99.7 L69.9 100.9 L68.1 102.3 L66.3 104.1 L64.7 106.2 L63.4 109 L62.9 112.4 L63 114.9 L63.5 117.4 L64.2 119.8 L65.1 122.2 L66.3 124.5 L67.5 126.9 L69 129.3 L70.6 131.6 L72.3 133.9 L74.1 136.2 L76.1 138.4 L78.2 140.4 L80.4 142.4 L82.8 144.3 L85.2 145.9 L87.7 147.4 L90.3 148.8 L93 150.2 L95.8 151.4 L98.7 152.6 L101.7 153.7 L104.7 154.6 L107.8 155.5 L110.9 156.3 L114.1 157 L117.3 157.6 L120.5 158 L123.7 158.4 L127.4 158.5 L131.2 158.4 L134.9 158.1 L138.6 157.7 L142.3 157.2 L146 156.6 L149.5 155.9 L152.9 155.2 L156.1 154.6 L159.1 154 L161.8 153.4 L164.1 153 L165.9 152.8 L166.9 152.7 C186.5 148.8 180.6 119.4 161.1 123.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M233.1 152.7 L234.1 152.8 L235.9 153 L238.2 153.4 L240.9 154 L243.9 154.6 L247.1 155.2 L250.5 155.9 L254 156.6 L257.7 157.2 L261.4 157.7 L265.1 158.1 L268.8 158.4 L272.6 158.5 L276.3 158.4 L279.5 158 L282.7 157.6 L285.9 157 L289.1 156.3 L292.2 155.5 L295.3 154.6 L298.3 153.7 L301.3 152.6 L304.2 151.4 L307 150.2 L309.7 148.8 L312.3 147.4 L314.8 145.9 L317.2 144.3 L319.6 142.4 L321.8 140.4 L323.9 138.4 L325.9 136.2 L327.7 133.9 L329.4 131.6 L331 129.3 L332.5 126.9 L333.7 124.5 L334.9 122.2 L335.8 119.8 L336.5 117.4 L337 114.9 L337.1 112.4 L336.6 109 L335.3 106.2 L333.7 104.1 L331.9 102.3 L330.1 100.9 L328.2 99.7 L326.3 98.6 L324.4 97.7 L322.6 96.8 L321 96.1 L319.5 95.5 L318.2 95 L317.3 94.6 L317 94.6 C312.5 90.7 306.5 97.4 311 101.4 L312.1 102.4 L313.3 103.4 L314.5 104.3 L315.8 105.3 L317.2 106.3 L318.6 107.3 L320 108.4 L321.2 109.4 L322.2 110.5 L322.9 111.4 L323.4 112.1 L323.4 112.5 L323.1 112.3 L322.9 111.6 L322.6 111.9 L322.3 112.7 L321.7 113.7 L320.9 114.9 L319.9 116.3 L318.8 117.7 L317.5 119.2 L316.1 120.7 L314.6 122.2 L313 123.6 L311.4 124.8 L309.8 126 L308.3 127 L306.8 127.7 L305.2 128.5 L303.3 129.3 L301.4 130 L299.3 130.6 L297.1 131.3 L294.8 131.8 L292.4 132.3 L290 132.8 L287.6 133.1 L285.1 133.4 L282.7 133.6 L280.3 133.7 L277.9 133.7 L275.7 133.6 L273.8 133.4 L271.5 133 L268.8 132.5 L266 131.9 L263.1 131.1 L260.1 130.3 L257 129.3 L254 128.4 L251.1 127.4 L248.4 126.5 L245.8 125.6 L243.4 124.7 L241.1 124 L238.9 123.3 C219.4 119.4 213.5 148.8 233.1 152.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M159.8 139.4 L158.1 140.8 L156.1 142.4 L153.8 144.2 L151.2 146.2 L148.4 148.3 L145.4 150.6 L142.4 152.9 L139.2 155.2 L136 157.5 L132.9 159.8 L129.9 161.9 L127.1 163.9 L124.5 165.6 L122.2 167.1 L119.8 168.5 L117.5 170 L115.2 171.3 L113 172.6 L110.8 173.8 L108.7 175 L106.7 176 L104.8 176.9 L103 177.8 L101.3 178.5 L99.7 179.1 L98.2 179.6 L96.9 180 L95.6 180.3 L94.6 180.4 L93.3 180.5 L92 180.5 L90.6 180.3 L89.1 180.1 L87.7 179.7 L86.3 179.3 L85 178.8 L83.7 178.3 L82.6 177.7 L81.7 177.2 L81 176.8 L80.5 176.5 L80.2 176.5 L80.3 177.3 L80.2 177.6 L80 177.3 L80 176.6 L80.1 175.5 L80.4 174.3 L80.9 172.9 L81.4 171.5 L81.9 170 L82.5 168.6 L83 167.3 L83.5 166 L83.9 164.7 L84.3 163.4 C86.2 157.7 77.6 154.9 75.7 160.6 L75.4 160.8 L74.9 161.4 L74.2 162.4 L73.3 163.5 L72.4 164.8 L71.4 166.3 L70.4 167.8 L69.4 169.5 L68.5 171.3 L67.7 173.3 L67.1 175.4 L66.7 177.8 L66.8 180.5 L67.8 183.5 L68.9 185.5 L70.2 187.3 L71.7 188.9 L73.3 190.4 L75 191.8 L76.9 193.2 L78.9 194.5 L81.1 195.6 L83.4 196.7 L85.7 197.6 L88.2 198.4 L90.8 199.1 L93.5 199.5 L96.4 199.7 L99.1 199.7 L101.7 199.5 L104.4 199.2 L107.1 198.7 L109.7 198.1 L112.4 197.3 L115 196.5 L117.7 195.6 L120.3 194.6 L123 193.6 L125.7 192.5 L128.4 191.3 L131.1 190.2 L133.8 188.9 L136.9 187.4 L140.2 185.7 L143.6 183.9 L147.1 181.9 L150.6 179.8 L154.2 177.7 L157.6 175.6 L161 173.5 L164.3 171.5 L167.3 169.7 L170.1 168 L172.6 166.6 L174.6 165.4 L176.2 164.6 C192.9 153.7 176.6 128.6 159.8 139.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M223.8 164.6 L225.4 165.4 L227.4 166.6 L229.9 168 L232.7 169.7 L235.7 171.5 L239 173.5 L242.4 175.6 L245.8 177.7 L249.4 179.8 L252.9 181.9 L256.4 183.9 L259.8 185.7 L263.1 187.4 L266.2 188.9 L268.9 190.2 L271.6 191.3 L274.3 192.5 L277 193.6 L279.7 194.6 L282.3 195.6 L285 196.5 L287.6 197.3 L290.3 198.1 L292.9 198.7 L295.6 199.2 L298.3 199.5 L300.9 199.7 L303.6 199.7 L306.5 199.5 L309.2 199.1 L311.8 198.4 L314.3 197.6 L316.6 196.7 L318.9 195.6 L321.1 194.5 L323.1 193.2 L325 191.8 L326.7 190.4 L328.3 188.9 L329.8 187.3 L331.1 185.5 L332.2 183.5 L333.2 180.5 L333.3 177.8 L332.9 175.4 L332.3 173.3 L331.5 171.3 L330.6 169.5 L329.6 167.8 L328.6 166.3 L327.6 164.8 L326.7 163.5 L325.8 162.4 L325.1 161.4 L324.6 160.8 L324.3 160.6 C322.4 154.9 313.8 157.7 315.7 163.4 L316.1 164.7 L316.5 166 L317 167.3 L317.5 168.6 L318.1 170 L318.6 171.5 L319.1 172.9 L319.6 174.3 L319.9 175.5 L320 176.6 L320 177.3 L319.8 177.6 L319.7 177.3 L319.8 176.5 L319.5 176.5 L319 176.8 L318.3 177.2 L317.4 177.7 L316.3 178.3 L315 178.8 L313.7 179.3 L312.3 179.7 L310.9 180.1 L309.4 180.3 L308 180.5 L306.7 180.5 L305.4 180.4 L304.4 180.3 L303.1 180 L301.8 179.6 L300.3 179.1 L298.7 178.5 L297 177.8 L295.2 176.9 L293.3 176 L291.3 175 L289.2 173.8 L287 172.6 L284.8 171.3 L282.5 170 L280.2 168.5 L277.8 167.1 L275.5 165.6 L272.9 163.9 L270.1 161.9 L267.1 159.8 L264 157.5 L260.8 155.2 L257.6 152.9 L254.6 150.6 L251.6 148.3 L248.8 146.2 L246.2 144.2 L243.9 142.4 L241.9 140.8 L240.2 139.4 C223.4 128.6 207.1 153.7 223.8 164.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M164.7 153.1 L163.7 155.6 L162.6 158.3 L161.4 161.4 L160.1 164.7 L158.7 168.3 L157.2 172.1 L155.6 175.9 L154 179.8 L152.3 183.5 L150.6 187.1 L148.9 190.5 L147.3 193.5 L145.8 196.1 L144.6 198 L143.1 199.9 L141.6 201.7 L139.9 203.4 L138.1 205.1 L136.3 206.6 L134.3 208.1 L132.3 209.5 L130.4 210.9 L128.4 212.1 L126.4 213.2 L124.5 214.2 L122.6 215.1 L120.9 215.9 L119.2 216.7 L118.1 217.1 L116.9 217.5 L115.7 217.8 L114.5 218 L113.2 218.1 L111.9 218.2 L110.7 218.1 L109.5 218 L108.5 217.9 L107.5 217.7 L106.7 217.5 L106 217.3 L105.5 217.2 L105.3 217.2 L105.7 218.1 L105.6 218.6 L105.4 218.4 L105.2 217.7 L105.2 216.7 L105.2 215.5 L105.3 214.1 L105.5 212.7 L105.7 211.2 L105.9 209.7 L106.1 208.4 L106.3 207.1 L106.4 205.8 L106.5 204.5 C107.1 198.5 98.2 197.6 97.5 203.5 L97.3 203.7 L96.9 204.4 L96.4 205.5 L95.8 206.7 L95.2 208.2 L94.6 209.7 L94 211.4 L93.4 213.2 L92.9 215 L92.5 217 L92.3 219.1 L92.5 221.5 L93.1 224.1 L94.7 226.8 L96.1 228.4 L97.6 229.7 L99.2 231 L101 232 L102.9 233 L104.9 233.9 L107.1 234.6 L109.3 235.2 L111.7 235.7 L114.1 236 L116.7 236.2 L119.3 236.1 L122 235.8 L124.8 235.3 L127.1 234.8 L129.6 234.1 L132.2 233.3 L134.9 232.4 L137.7 231.3 L140.5 230.1 L143.4 228.7 L146.3 227.2 L149.3 225.5 L152.2 223.6 L155.1 221.5 L157.9 219.2 L160.7 216.7 L163.4 214 L166.2 210.8 L168.8 207.3 L171.3 203.6 L173.7 199.7 L176 195.7 L178.2 191.6 L180.4 187.6 L182.4 183.7 L184.3 179.9 L186.1 176.4 L187.8 173.2 L189.2 170.5 L190.4 168.3 L191.3 166.9 C200.5 149.3 173.9 135.4 164.7 153.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M208.7 166.9 L209.6 168.3 L210.8 170.5 L212.2 173.2 L213.9 176.4 L215.7 179.9 L217.6 183.7 L219.6 187.6 L221.8 191.6 L224 195.7 L226.3 199.7 L228.7 203.6 L231.2 207.3 L233.8 210.8 L236.6 214 L239.3 216.7 L242.1 219.2 L244.9 221.5 L247.8 223.6 L250.7 225.5 L253.7 227.2 L256.6 228.7 L259.5 230.1 L262.3 231.3 L265.1 232.4 L267.8 233.3 L270.4 234.1 L272.9 234.8 L275.2 235.3 L278 235.8 L280.7 236.1 L283.3 236.2 L285.9 236 L288.3 235.7 L290.7 235.2 L292.9 234.6 L295.1 233.9 L297.1 233 L299 232 L300.8 231 L302.4 229.7 L303.9 228.4 L305.3 226.8 L306.9 224.1 L307.5 221.5 L307.7 219.1 L307.5 217 L307.1 215 L306.6 213.2 L306 211.4 L305.4 209.7 L304.8 208.2 L304.2 206.7 L303.6 205.5 L303.1 204.4 L302.7 203.7 L302.5 203.5 C301.8 197.6 292.9 198.5 293.5 204.5 L293.6 205.8 L293.7 207.1 L293.9 208.4 L294.1 209.7 L294.3 211.2 L294.5 212.7 L294.7 214.1 L294.8 215.5 L294.8 216.7 L294.8 217.7 L294.6 218.4 L294.4 218.6 L294.3 218.1 L294.7 217.2 L294.5 217.2 L294 217.3 L293.3 217.5 L292.5 217.7 L291.5 217.9 L290.5 218 L289.3 218.1 L288.1 218.2 L286.8 218.1 L285.5 218 L284.3 217.8 L283.1 217.5 L281.9 217.1 L280.8 216.7 L279.1 215.9 L277.4 215.1 L275.5 214.2 L273.6 213.2 L271.6 212.1 L269.6 210.9 L267.7 209.5 L265.7 208.1 L263.7 206.6 L261.9 205.1 L260.1 203.4 L258.4 201.7 L256.9 199.9 L255.4 198 L254.2 196.1 L252.7 193.5 L251.1 190.5 L249.4 187.1 L247.7 183.5 L246 179.8 L244.4 175.9 L242.8 172.1 L241.3 168.3 L239.9 164.7 L238.6 161.4 L237.4 158.3 L236.3 155.6 L235.3 153.1 C226.1 135.4 199.5 149.3 208.7 166.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M177.3 161.3 L177 163.8 L176.7 166.8 L176.4 170.2 L176 174 L175.5 178.1 L175 182.4 L174.5 186.9 L173.9 191.4 L173.3 195.9 L172.7 200.2 L172.1 204.4 L171.4 208.2 L170.8 211.6 L170.2 214.3 L169.5 217 L168.8 219.6 L168.1 222 L167.3 224.4 L166.5 226.5 L165.7 228.6 L164.9 230.6 L164.1 232.4 L163.2 234.1 L162.4 235.8 L161.5 237.3 L160.7 238.7 L159.8 240.1 L158.9 241.3 L158.3 242.2 L157.5 243.1 L156.6 244 L155.6 244.8 L154.6 245.6 L153.5 246.3 L152.4 247 L151.4 247.5 L150.4 248 L149.6 248.3 L148.8 248.6 L148.3 248.8 L148 249 L148.1 249.2 L149.2 249.9 L149.5 250.5 L149.3 250.5 L148.9 250.1 L148.4 249.4 L147.9 248.3 L147.4 247.2 L146.9 245.9 L146.5 244.5 L146 243.2 L145.6 241.9 L145.2 240.7 L144.8 239.6 L144.2 238.4 C142.1 232.8 133.7 236 135.8 241.6 L135.7 241.8 L135.6 242.6 L135.7 243.7 L135.7 245 L135.8 246.5 L135.9 248.1 L136.1 249.8 L136.4 251.6 L136.7 253.4 L137.3 255.3 L138 257.2 L139.2 259.2 L141.1 261.2 L143.9 262.8 L146 263.5 L148 263.8 L150 263.9 L152.1 263.9 L154.1 263.7 L156.2 263.3 L158.3 262.8 L160.4 262.1 L162.6 261.3 L164.7 260.3 L166.9 259.2 L169 257.9 L171.1 256.4 L173.1 254.7 L174.8 253.1 L176.4 251.4 L178.1 249.6 L179.7 247.7 L181.3 245.6 L182.8 243.5 L184.3 241.2 L185.8 238.8 L187.3 236.2 L188.7 233.6 L190 230.8 L191.3 227.9 L192.6 224.8 L193.8 221.7 L195.1 218 L196.2 214 L197.4 209.7 L198.5 205.2 L199.5 200.6 L200.5 196 L201.5 191.3 L202.4 186.8 L203.3 182.5 L204.1 178.4 L204.9 174.6 L205.6 171.4 L206.2 168.7 L206.7 166.7 C210.4 147.1 180.9 141.7 177.3 161.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M193.3 166.7 L193.8 168.7 L194.4 171.4 L195.1 174.6 L195.9 178.4 L196.7 182.5 L197.6 186.8 L198.5 191.3 L199.5 196 L200.5 200.6 L201.5 205.2 L202.6 209.7 L203.8 214 L204.9 218 L206.2 221.7 L207.4 224.8 L208.7 227.9 L210 230.8 L211.3 233.6 L212.7 236.2 L214.2 238.8 L215.7 241.2 L217.2 243.5 L218.7 245.6 L220.3 247.7 L221.9 249.6 L223.6 251.4 L225.2 253.1 L226.9 254.7 L228.9 256.4 L231 257.9 L233.1 259.2 L235.3 260.3 L237.4 261.3 L239.6 262.1 L241.7 262.8 L243.8 263.3 L245.9 263.7 L247.9 263.9 L250 263.9 L252 263.8 L254 263.5 L256.1 262.8 L258.9 261.2 L260.8 259.2 L262 257.2 L262.7 255.3 L263.3 253.4 L263.6 251.6 L263.9 249.8 L264.1 248.1 L264.2 246.5 L264.3 245 L264.3 243.7 L264.4 242.6 L264.3 241.8 L264.2 241.6 C266.3 236 257.9 232.8 255.8 238.4 L255.2 239.6 L254.8 240.7 L254.4 241.9 L254 243.2 L253.5 244.5 L253.1 245.9 L252.6 247.2 L252.1 248.3 L251.6 249.4 L251.1 250.1 L250.7 250.5 L250.5 250.5 L250.8 249.9 L251.9 249.2 L252 249 L251.7 248.8 L251.2 248.6 L250.4 248.3 L249.6 248 L248.6 247.5 L247.6 247 L246.5 246.3 L245.4 245.6 L244.4 244.8 L243.4 244 L242.5 243.1 L241.7 242.2 L241.1 241.3 L240.2 240.1 L239.3 238.7 L238.5 237.3 L237.6 235.8 L236.8 234.1 L235.9 232.4 L235.1 230.6 L234.3 228.6 L233.5 226.5 L232.7 224.4 L231.9 222 L231.2 219.6 L230.5 217 L229.8 214.3 L229.2 211.6 L228.6 208.2 L227.9 204.4 L227.3 200.2 L226.7 195.9 L226.1 191.4 L225.5 186.9 L225 182.4 L224.5 178.1 L224 174 L223.6 170.2 L223.3 166.8 L223 163.8 L222.7 161.3 C219.1 141.7 189.6 147.1 193.3 166.7 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="96" rx="72" ry="68"/>
  <ellipse class="fillable" fill="#ffffff" cx="156" cy="64" rx="12" ry="9" transform="rotate(-30 156 64)"/>
  <ellipse class="fillable" fill="#ffffff" cx="244" cy="64" rx="12" ry="9" transform="rotate(30 244 64)"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="46" rx="10" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="176" cy="104" rx="12" ry="14"/>
  <circle fill="#1a1a1a" stroke="none" cx="177" cy="105" r="7.4"/>
  <circle fill="#ffffff" stroke="none" cx="180" cy="101.7" r="2.8"/>
  <ellipse class="fillable" fill="#ffffff" cx="224" cy="104" rx="12" ry="14"/>
  <circle fill="#1a1a1a" stroke="none" cx="225" cy="105" r="7.4"/>
  <circle fill="#ffffff" stroke="none" cx="228" cy="101.7" r="2.8"/>
  <ellipse class="fillable" fill="#ffffff" cx="154" cy="128" rx="11" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="246" cy="128" rx="11" ry="7"/>
  <path fill="none" stroke-width="3" d="M186 128 Q200 140 214 128"/>
</g>
''')

add('dolphin', '🐬 海豚跳跃', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="50" r="22"/>
  <path class="fillable" fill="#ffffff" d="M24 64 Q24 46 43.8 47.8 Q51 31.6 70.8 37 Q87 29.8 94.2 47.8 Q110.4 49.6 106.8 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M88.3 191 Q101.2 214.9 108.6 227.4 Q106.6 213.1 83.5 228.6 Q77.9 212.6 61.9 218.2 Q59.7 190.5 47.3 197.9 Q61.6 195.9 88.3 191 Z"/>
  <path class="fillable" fill="#ffffff" d="M136.7 78.6 Q134.8 51.7 124.8 47.7 Q174.5 45.4 176.5 59.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M89.4 202.6 L93.7 202.4 L96.4 201.1 L98.7 199.5 L100.8 197.6 L102.9 195.6 L104.9 193.4 L106.9 191.1 L108.8 188.7 L110.7 186.3 L112.6 183.9 L114.6 181.4 L116.5 179 L118.4 176.6 L120.4 174.3 L122.3 172.2 L124.2 170.2 L126 168.4 L127.8 166.8 L129.6 165.4 L131.2 164.3 L133.5 162.5 L135.9 160.6 L138.5 158.6 L141.1 156.6 L143.8 154.6 L146.6 152.6 L149.4 150.5 L152.3 148.5 L155.2 146.5 L158.2 144.5 L161.1 142.6 L164 140.7 L167 139 L169.9 137.3 L172.7 135.7 L175.5 134.3 L178.1 133 L180.7 131.8 L183.1 130.8 L185.4 129.9 L188 129 L190.7 128.1 L193.4 127.3 L196.3 126.4 L199.2 125.7 L202.1 124.9 L205.1 124.2 L208.1 123.6 L211.1 123 L214.1 122.5 L217.2 122.1 L220.2 121.7 L223.2 121.3 L226.2 121.1 L229.1 120.8 L232.1 120.7 L234.9 120.6 L237.7 120.5 L240.4 120.6 L243.1 120.6 L244.7 120.6 L246.9 120.9 L249.6 121.3 L252.5 122 L255.8 122.8 L259.2 123.8 L262.9 125 L266.6 126.3 L270.4 127.6 L274.8 127.9 L280.1 126.6 L285.4 125.4 L290.5 124.4 L295.5 123.5 L300.2 122.7 L304.6 121.9 L307.5 123.5 L310.1 125 L312.5 126.2 L314.7 127.3 C324.4 131.7 331 117.1 321.3 112.7 L319.7 111.9 L317.6 110.9 L315.2 109.5 L312.5 108 L310.9 103.8 L309.2 99.4 L307.3 94.6 L305.3 89.6 L303.1 84.3 L300.7 78.8 L297.3 75 L293 72.4 L288.6 69.7 L284 67.2 L279.3 64.8 L274.5 62.5 L269.4 60.4 L264.2 58.4 L258.7 56.7 L252.9 55.4 L248.2 54.5 L243.4 53.7 L238.7 53.1 L233.9 52.7 L229 52.5 L224.2 52.4 L219.4 52.4 L214.5 52.6 L209.7 53 L204.9 53.5 L200.1 54.1 L195.3 54.9 L190.6 55.8 L185.8 56.8 L181.2 58 L176.5 59.4 L171.9 60.8 L167.4 62.4 L163 64.2 L158.6 66.1 L153.9 68.3 L149.4 70.7 L145.1 73.2 L140.8 75.8 L136.7 78.6 L132.6 81.5 L128.7 84.5 L124.9 87.6 L121.2 90.8 L117.6 94 L114.1 97.3 L110.8 100.6 L107.5 104 L104.4 107.4 L101.5 110.8 L98.6 114.2 L96 117.6 L93.4 121 L91 124.4 L88.8 127.7 L86.1 131.9 L83.8 136 L81.8 140.2 L80 144.4 L78.4 148.5 L77.1 152.6 L76 156.6 L75 160.5 L74.2 164.4 L73.6 168.1 L73.1 171.8 L72.8 175.3 L72.6 178.6 L72.6 181.8 L72.8 184.7 L73.1 187.5 L73.6 190.1 L74.4 192.4 L75.6 194.7 L78.6 197.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M120.4 174.3 L122.3 172.2 L124.2 170.2 L126 168.4 L127.8 166.8 L129.6 165.4 L131.2 164.3 L133.5 162.5 L135.9 160.6 L138.5 158.6 L141.1 156.6 L143.8 154.6 L146.6 152.6 L149.4 150.5 L152.3 148.5 L155.2 146.5 L158.2 144.5 L161.1 142.6 L164 140.7 L167 139 L169.9 137.3 L172.7 135.7 L175.5 134.3 L178.1 133 L180.7 131.8 L183.1 130.8 L185.4 129.9 L188 129 L190.7 128.1 L193.4 127.3 L196.3 126.4 L199.2 125.7 L202.1 124.9 L205.1 124.2 L208.1 123.6 L211.1 123 L214.1 122.5 L217.2 122.1 L220.2 121.7 L223.2 121.3 L226.2 121.1 L229.1 120.8 L232.1 120.7 L234.9 120.6 L237.7 120.5 L240.4 120.6 L243.1 120.6 L244.7 120.6 L246.9 120.9 L249.6 121.3 L252.5 122 L255.8 122.8 L259.2 123.8 L262.9 125 L266.6 126.3 L270.4 127.6 L274.8 127.9 L280.1 126.6 L285.4 125.4 L290.5 124.4 L295.5 123.5 L300.2 122.7 L304.6 121.9 L307.5 123.5 L309.4 120 L306.6 118.5 L302.9 118 L298.9 117.5 L294.7 116.9 L290.4 116.5 L289.9 108.6 L285.8 107.1 L281.8 105.3 L277.8 103.4 L273.8 101.5 L269.8 99.8 L265.8 98.1 L261.9 96.7 L258 95.4 L254.3 94.3 L250.7 93.5 L247.3 92.9 L243.7 92.5 L240.2 92.1 L236.5 91.9 L232.8 91.8 L229.1 91.8 L225.3 91.9 L221.6 92 L217.8 92.3 L214 92.7 L210.2 93.2 L206.4 93.7 L202.6 94.4 L198.9 95.2 L195.2 96 L191.5 96.9 L187.9 97.9 L184.3 99 L180.8 100.2 L177.4 101.5 L174 102.8 L170.7 104.2 L167.4 105.8 L164.1 107.6 L160.7 109.5 L157.4 111.5 L154 113.6 L150.7 115.8 L147.4 118.2 L144.1 120.6 L140.9 123 L137.8 125.6 L134.7 128.1 L131.6 130.7 L128.7 133.4 L125.8 136 L123.1 138.6 L120.4 141.2 L117.9 143.8 L115.5 146.3 L113.2 148.7 L111.1 151.1 L109.1 153.7 L107.2 156.4 L105.4 159.2 L103.6 162.1 L102 165.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M206.2 111.7 Q202.2 147.7 186.2 155.7 Q224.2 151.7 230.2 117.7 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="267" cy="82.8" rx="9" ry="10"/>
  <circle fill="#1a1a1a" stroke="none" cx="268" cy="83.8" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="270.2" cy="81.3" r="2.1"/>
  <path fill="none" stroke-width="3" d="M285.3 111.5 Q299.3 121.5 313.3 117.5"/>
  <path class="fillable" fill="#ffffff" d="M0 238 Q25 228 50 238 Q75 248 100 238 Q125 228 150 238 Q175 248 200 238 Q225 228 250 238 Q275 248 300 238 Q325 228 350 238 Q375 248 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 268 Q20 260 40 268 Q60 276 80 268 Q100 260 120 268 Q140 276 160 268 Q180 260 200 268 Q220 276 240 268 Q260 260 280 268 Q300 276 320 268 Q340 260 360 268 Q380 276 400 268 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 196 Q342 210 330 218 Q318 210 330 196 Z"/>
  <path class="fillable" fill="#ffffff" d="M358 206 Q370 220 358 228 Q346 220 358 206 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 248 Q296 226 306 220 Q312 232 318 234 Q322 216 334 214 Q336 230 340 236 Q348 226 356 228 Q350 240 352 250 Q326 258 300 248 Z"/>
</g>
''')

add('crab', '🦀 螃蟹', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="350" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M30 60 Q30 43 48.7 44.7 Q55.5 29.4 74.2 34.5 Q89.5 27.7 96.3 44.7 Q111.6 46.4 108.2 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 150 Q50 140 100 150 Q150 160 200 150 Q250 140 300 150 Q350 160 400 150 L400 240 L0 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 232 Q100 218 200 230 Q300 242 400 226 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M137.9 188.3 L136.9 188.6 L135.5 188.9 L133.8 189.3 L131.7 189.8 L129.4 190.2 L126.9 190.8 L124.3 191.3 L121.5 192 L118.7 192.6 L115.9 193.4 L113.1 194.2 L110.3 195.1 L107.6 196.1 L104.9 197.3 L102.4 198.6 L100 200 L97.9 201.6 L96 203.3 L94.2 205.1 L92.6 207 L91.1 209 L89.6 211 L88.3 213 L87.1 215 L86 217 L84.9 219 L84 220.9 L83.1 222.8 L82.3 224.6 L81.5 226.3 L80.8 227.9 L80.2 229.4 L79.5 231.2 L79 233 L78.6 234.7 L78.3 236.4 L78.1 238.1 L78 239.6 L77.9 241.1 L78 242.5 L78 243.9 L78.1 245.1 L78.2 246.2 L78.3 247.2 L78.4 248.1 L78.4 248.7 L78.5 249.2 L78.5 249.4 C77.7 256.7 88.7 257.9 89.5 250.6 L89.6 249.6 L89.6 248.6 L89.7 247.6 L89.7 246.7 L89.7 245.7 L89.7 244.7 L89.7 243.7 L89.8 242.7 L89.9 241.7 L90 240.6 L90.2 239.6 L90.4 238.6 L90.6 237.5 L90.9 236.5 L91.3 235.6 L91.8 234.6 L92.5 233.2 L93.2 231.7 L94 230.2 L94.8 228.6 L95.7 226.9 L96.6 225.3 L97.6 223.7 L98.6 222 L99.7 220.4 L100.8 218.9 L102 217.5 L103.1 216.1 L104.3 214.9 L105.5 213.8 L106.8 212.8 L108 212 L109.2 211.3 L110.8 210.6 L112.7 209.8 L114.9 209.2 L117.2 208.5 L119.6 207.9 L122.2 207.3 L124.7 206.8 L127.3 206.3 L129.8 205.9 L132.2 205.5 L134.5 205.1 L136.7 204.7 L138.7 204.4 L140.5 204.1 L142.1 203.7 C152.4 200.9 148.1 185.4 137.9 188.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M257.9 203.7 L259.5 204.1 L261.3 204.4 L263.3 204.7 L265.5 205.1 L267.8 205.5 L270.2 205.9 L272.7 206.3 L275.3 206.8 L277.8 207.3 L280.4 207.9 L282.8 208.5 L285.1 209.2 L287.3 209.8 L289.2 210.6 L290.8 211.3 L292 212 L293.2 212.8 L294.5 213.8 L295.7 214.9 L296.9 216.1 L298 217.5 L299.2 218.9 L300.3 220.4 L301.4 222 L302.4 223.7 L303.4 225.3 L304.3 226.9 L305.2 228.6 L306 230.2 L306.8 231.7 L307.5 233.2 L308.2 234.6 L308.7 235.6 L309.1 236.5 L309.4 237.5 L309.6 238.6 L309.8 239.6 L310 240.6 L310.1 241.7 L310.2 242.7 L310.3 243.7 L310.3 244.7 L310.3 245.7 L310.3 246.7 L310.3 247.6 L310.4 248.6 L310.4 249.6 L310.5 250.6 C311.3 257.9 322.3 256.7 321.5 249.4 L321.5 249.2 L321.6 248.7 L321.6 248.1 L321.7 247.2 L321.8 246.2 L321.9 245.1 L322 243.9 L322 242.5 L322.1 241.1 L322 239.6 L321.9 238.1 L321.7 236.4 L321.4 234.7 L321 233 L320.5 231.2 L319.8 229.4 L319.2 227.9 L318.5 226.3 L317.7 224.6 L316.9 222.8 L316 220.9 L315.1 219 L314 217 L312.9 215 L311.7 213 L310.4 211 L308.9 209 L307.4 207 L305.8 205.1 L304 203.3 L302.1 201.6 L300 200 L297.6 198.6 L295.1 197.3 L292.4 196.1 L289.7 195.1 L286.9 194.2 L284.1 193.4 L281.3 192.6 L278.5 192 L275.7 191.3 L273.1 190.8 L270.6 190.2 L268.3 189.8 L266.2 189.3 L264.5 188.9 L263.1 188.6 L262.1 188.3 C251.9 185.4 247.6 200.9 257.9 203.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M141.7 205.3 L141 205.8 L139.8 206.5 L138.4 207.3 L136.8 208.3 L135 209.3 L133 210.4 L131 211.7 L128.8 212.9 L126.7 214.3 L124.5 215.7 L122.3 217.1 L120.2 218.6 L118.1 220.1 L116.2 221.7 L114.4 223.4 L112.7 225.2 L111.3 226.9 L110 228.7 L108.9 230.6 L107.9 232.4 L106.9 234.3 L106.1 236.1 L105.4 238 L104.8 239.8 L104.2 241.7 L103.7 243.4 L103.3 245.2 L102.9 246.8 L102.6 248.4 L102.3 250 L102 251.4 L101.8 252.8 L101.6 254.5 L101.5 256.2 L101.5 257.8 L101.6 259.3 L101.8 260.8 L102 262.2 L102.3 263.5 L102.6 264.8 L102.9 265.9 L103.2 267 L103.6 268 L103.9 268.8 L104.1 269.6 L104.3 270.2 L104.5 270.6 L104.5 270.7 C105.4 277.9 116.4 276.6 115.5 269.3 L115.3 268.4 L115.2 267.5 L115 266.6 L114.9 265.8 L114.7 264.9 L114.5 264 L114.3 263.1 L114.2 262.2 L114 261.3 L113.9 260.4 L113.8 259.5 L113.8 258.6 L113.8 257.7 L113.9 256.8 L114 256 L114.2 255.2 L114.5 254 L114.8 252.7 L115.2 251.4 L115.6 250 L116 248.6 L116.5 247.2 L116.9 245.8 L117.5 244.4 L118.1 243 L118.7 241.7 L119.3 240.4 L120.1 239.1 L120.8 237.9 L121.6 236.8 L122.4 235.8 L123.3 234.8 L124.2 233.9 L125.5 232.9 L126.9 231.8 L128.6 230.7 L130.4 229.5 L132.4 228.4 L134.4 227.2 L136.4 226.1 L138.5 225 L140.5 223.9 L142.4 222.9 L144.3 221.9 L146 221 L147.6 220.2 L149 219.5 L150.3 218.7 C159.3 213 150.6 199.5 141.7 205.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M249.7 218.7 L251 219.5 L252.4 220.2 L254 221 L255.7 221.9 L257.6 222.9 L259.5 223.9 L261.5 225 L263.6 226.1 L265.6 227.2 L267.6 228.4 L269.6 229.5 L271.4 230.7 L273.1 231.8 L274.5 232.9 L275.8 233.9 L276.7 234.8 L277.6 235.8 L278.4 236.8 L279.2 237.9 L279.9 239.1 L280.7 240.4 L281.3 241.7 L281.9 243 L282.5 244.4 L283.1 245.8 L283.5 247.2 L284 248.6 L284.4 250 L284.8 251.4 L285.2 252.7 L285.5 254 L285.8 255.2 L286 256 L286.1 256.8 L286.2 257.7 L286.2 258.6 L286.2 259.5 L286.1 260.4 L286 261.3 L285.8 262.2 L285.7 263.1 L285.5 264 L285.3 264.9 L285.1 265.8 L285 266.6 L284.8 267.5 L284.7 268.4 L284.5 269.3 C283.6 276.6 294.6 277.9 295.5 270.7 L295.5 270.6 L295.7 270.2 L295.9 269.6 L296.1 268.8 L296.4 268 L296.8 267 L297.1 265.9 L297.4 264.8 L297.7 263.5 L298 262.2 L298.2 260.8 L298.4 259.3 L298.5 257.8 L298.5 256.2 L298.4 254.5 L298.2 252.8 L298 251.4 L297.7 250 L297.4 248.4 L297.1 246.8 L296.7 245.2 L296.3 243.4 L295.8 241.7 L295.2 239.8 L294.6 238 L293.9 236.1 L293.1 234.3 L292.1 232.4 L291.1 230.6 L290 228.7 L288.7 226.9 L287.3 225.2 L285.6 223.4 L283.8 221.7 L281.9 220.1 L279.8 218.6 L277.7 217.1 L275.5 215.7 L273.3 214.3 L271.2 212.9 L269 211.7 L267 210.4 L265 209.3 L263.2 208.3 L261.6 207.3 L260.2 206.5 L259 205.8 L258.3 205.3 C249.4 199.5 240.7 213 249.7 218.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M154.1 216.6 L153.6 217.2 L152.8 218.1 L151.8 219.1 L150.6 220.4 L149.3 221.7 L147.9 223.1 L146.4 224.7 L144.9 226.3 L143.3 228 L141.7 229.7 L140.2 231.4 L138.7 233.2 L137.3 235 L136 236.8 L134.8 238.7 L133.7 240.6 L132.9 242.4 L132.1 244.2 L131.5 246 L131 247.7 L130.6 249.5 L130.3 251.3 L130 253 L129.8 254.6 L129.7 256.3 L129.6 257.8 L129.5 259.4 L129.5 260.8 L129.5 262.2 L129.6 263.6 L129.6 264.8 L129.7 266 L129.8 267.5 L130 269 L130.2 270.4 L130.6 271.8 L130.9 273 L131.3 274.2 L131.8 275.4 L132.2 276.4 L132.6 277.4 L133.1 278.3 L133.5 279.2 L133.8 279.9 L134.2 280.5 L134.4 281 L134.6 281.4 L134.7 281.5 C136.7 288.5 147.3 285.5 145.3 278.5 L145.1 277.7 L144.8 276.9 L144.6 276.2 L144.3 275.4 L144.1 274.7 L143.8 273.9 L143.5 273.1 L143.3 272.3 L143.1 271.5 L142.8 270.7 L142.7 269.8 L142.5 269 L142.4 268.2 L142.3 267.4 L142.3 266.7 L142.3 266 L142.4 264.9 L142.4 263.7 L142.5 262.5 L142.6 261.3 L142.7 260.1 L142.8 258.8 L143 257.6 L143.2 256.4 L143.4 255.2 L143.7 254 L144 252.8 L144.4 251.6 L144.8 250.5 L145.2 249.4 L145.7 248.4 L146.3 247.4 L146.9 246.5 L147.7 245.4 L148.8 244.1 L150 242.8 L151.3 241.3 L152.7 239.9 L154.1 238.4 L155.6 237 L157.1 235.5 L158.6 234.1 L160.1 232.8 L161.4 231.6 L162.7 230.4 L163.9 229.3 L165 228.3 L165.9 227.4 C173.1 219.5 161.2 208.7 154.1 216.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M234.1 227.4 L235 228.3 L236.1 229.3 L237.3 230.4 L238.6 231.6 L239.9 232.8 L241.4 234.1 L242.9 235.5 L244.4 237 L245.9 238.4 L247.3 239.9 L248.7 241.3 L250 242.8 L251.2 244.1 L252.3 245.4 L253.1 246.5 L253.7 247.4 L254.3 248.4 L254.8 249.4 L255.2 250.5 L255.6 251.6 L256 252.8 L256.3 254 L256.6 255.2 L256.8 256.4 L257 257.6 L257.2 258.8 L257.3 260.1 L257.4 261.3 L257.5 262.5 L257.6 263.7 L257.6 264.9 L257.7 266 L257.7 266.7 L257.7 267.4 L257.6 268.2 L257.5 269 L257.3 269.8 L257.2 270.7 L256.9 271.5 L256.7 272.3 L256.5 273.1 L256.2 273.9 L255.9 274.7 L255.7 275.4 L255.4 276.2 L255.2 276.9 L254.9 277.7 L254.7 278.5 C252.7 285.5 263.3 288.5 265.3 281.5 L265.4 281.4 L265.6 281 L265.8 280.5 L266.2 279.9 L266.5 279.2 L266.9 278.3 L267.4 277.4 L267.8 276.4 L268.2 275.4 L268.7 274.2 L269.1 273 L269.4 271.8 L269.8 270.4 L270 269 L270.2 267.5 L270.3 266 L270.4 264.8 L270.4 263.6 L270.5 262.2 L270.5 260.8 L270.5 259.4 L270.4 257.8 L270.3 256.3 L270.2 254.6 L270 253 L269.7 251.3 L269.4 249.5 L269 247.7 L268.5 246 L267.9 244.2 L267.1 242.4 L266.3 240.6 L265.2 238.7 L264 236.8 L262.7 235 L261.3 233.2 L259.8 231.4 L258.3 229.7 L256.7 228 L255.1 226.3 L253.6 224.7 L252.1 223.1 L250.7 221.7 L249.4 220.4 L248.2 219.1 L247.2 218.1 L246.4 217.2 L245.9 216.6 C238.8 208.7 226.9 219.5 234.1 227.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M139.1 178.9 L137.8 177.8 L136.4 176.6 L134.8 175.4 L133.2 174.1 L131.5 172.7 L129.6 171.2 L127.7 169.7 L125.8 168.1 L123.9 166.4 L122.1 164.7 L120.3 163.1 L118.6 161.4 L117.1 159.8 L115.8 158.2 L114.7 156.8 L113.8 155.6 L113.1 154.3 L112.4 152.7 L111.6 150.9 L111 148.9 L110.3 146.7 L109.8 144.5 L109.2 142.2 L108.8 139.9 L108.3 137.6 L107.9 135.4 L107.5 133.2 L107.2 131.2 L106.9 129.2 L106.5 127.4 L106.2 125.8 L105.8 124.2 C103.4 113.8 87.8 117.5 90.2 127.8 L90.3 128.7 L90.5 129.9 L90.6 131.5 L90.8 133.4 L91.1 135.5 L91.3 137.8 L91.6 140.3 L92 142.8 L92.4 145.5 L92.9 148.2 L93.5 150.9 L94.1 153.7 L94.9 156.4 L95.8 159.1 L96.9 161.8 L98.2 164.4 L99.7 167 L101.3 169.4 L103.1 171.7 L105 173.9 L107 176.1 L109.1 178.2 L111.1 180.2 L113.2 182.2 L115.2 184.1 L117.1 185.8 L118.9 187.5 L120.6 189 L122.1 190.3 L123.4 191.5 L124.4 192.4 L124.9 193.1 C134.3 202.5 148.5 188.3 139.1 178.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M275.1 193.1 L275.6 192.4 L276.6 191.5 L277.9 190.3 L279.4 189 L281.1 187.5 L282.9 185.8 L284.8 184.1 L286.8 182.2 L288.9 180.2 L290.9 178.2 L293 176.1 L295 173.9 L296.9 171.7 L298.7 169.4 L300.3 167 L301.8 164.4 L303.1 161.8 L304.2 159.1 L305.1 156.4 L305.9 153.7 L306.5 150.9 L307.1 148.2 L307.6 145.5 L308 142.8 L308.4 140.3 L308.7 137.8 L308.9 135.5 L309.2 133.4 L309.4 131.5 L309.5 129.9 L309.7 128.7 L309.8 127.8 C312.2 117.5 296.6 113.8 294.2 124.2 L293.8 125.8 L293.5 127.4 L293.1 129.2 L292.8 131.2 L292.5 133.2 L292.1 135.4 L291.7 137.6 L291.2 139.9 L290.8 142.2 L290.2 144.5 L289.7 146.7 L289 148.9 L288.4 150.9 L287.6 152.7 L286.9 154.3 L286.2 155.6 L285.3 156.8 L284.2 158.2 L282.9 159.8 L281.4 161.4 L279.7 163.1 L277.9 164.7 L276.1 166.4 L274.2 168.1 L272.3 169.7 L270.4 171.2 L268.5 172.7 L266.8 174.1 L265.2 175.4 L263.6 176.6 L262.2 177.8 L260.9 178.9 C251.5 188.3 265.7 202.5 275.1 193.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M96 108 L108 76 A34 34 0 1 0 128 96 Z"/>
  <path class="fillable" fill="#ffffff" d="M304 108 L292 76 A34 34 0 1 1 272 96 Z"/>
  <path class="fillable" fill="#ffffff" d="M171 160 L171 120 L185 120 L185 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M215 160 L215 120 L229 120 L229 160 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="198" rx="86" ry="54"/>
  <ellipse class="fillable" fill="#ffffff" cx="162" cy="176" rx="13" ry="9" transform="rotate(-20 162 176)"/>
  <ellipse class="fillable" fill="#ffffff" cx="238" cy="176" rx="13" ry="9" transform="rotate(20 238 176)"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="164" rx="12" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="178" cy="112" rx="16" ry="16"/>
  <circle fill="#1a1a1a" stroke="none" cx="179" cy="113" r="8"/>
  <circle fill="#ffffff" stroke="none" cx="182.2" cy="109.4" r="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="222" cy="112" rx="16" ry="16"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="113" r="8"/>
  <circle fill="#ffffff" stroke="none" cx="224.2" cy="109.4" r="3"/>
  <path fill="none" stroke-width="3.5" d="M178 206 Q200 224 222 206"/>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="206" rx="11" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="250" cy="206" rx="11" ry="7"/>
</g>
''')

add('jellyfish', '🪼 水母', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 244 200 254 Q300 264 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M48.7 263.8 L47.9 261.4 L46.9 258.7 L45.8 255.8 L44.5 252.6 L43.2 249.3 L41.9 245.7 L40.7 242.1 L39.6 238.6 L38.7 235.1 L38.1 231.9 L37.7 229 L37.6 226.6 L37.8 224.7 L38.4 222.5 L39.4 220.1 L40.7 217.5 L42.2 214.7 L44 211.8 L45.8 208.7 L47.6 205.5 L49.3 202.1 L50.8 198.4 L51.8 194.5 L52.3 190.3 L52.1 186.2 L51.3 182.2 L50.1 178.3 L48.7 174.6 L47.2 171 L45.5 167.5 L43.9 164.1 L42.4 160.8 L41.1 157.7 L40 154.8 L39.3 152.2 L38.9 149.9 L38.9 147.4 L39.2 144.7 L39.7 141.8 L40.4 138.9 L41.2 136 L42.2 133.1 L43.3 130.3 L44.3 127.6 L45.3 125.2 L46.2 122.9 L46.9 120.9 L47.4 119.1 C48.9 114.5 42 112.4 40.6 116.9 L40 118.1 L39.2 119.9 L38.1 121.9 L36.9 124.4 L35.6 127 L34.3 129.9 L33 133 L31.8 136.2 L30.7 139.6 L29.9 143 L29.3 146.5 L29.1 150.1 L29.3 153.9 L30.1 157.7 L31.1 161.3 L32.4 164.9 L33.8 168.5 L35.2 172 L36.6 175.4 L37.8 178.7 L38.8 181.9 L39.4 184.8 L39.8 187.4 L39.7 189.7 L39.3 191.7 L38.5 193.9 L37.4 196.3 L35.9 198.8 L34.2 201.4 L32.3 204.2 L30.3 207.1 L28.2 210.2 L26.3 213.5 L24.6 217.1 L23.2 221.1 L22.4 225.4 L22.2 229.7 L22.5 233.9 L23.1 238.2 L23.9 242.5 L24.9 246.7 L26.1 250.8 L27.2 254.7 L28.4 258.3 L29.4 261.6 L30.3 264.5 L31 266.8 L31.3 268.2 C34.2 279.8 51.6 275.4 48.7 263.8 Z"/>
  <circle class="fillable" fill="#ffffff" cx="84" cy="60" r="12"/>
  <circle class="fillable" fill="#ffffff" cx="66" cy="30" r="8"/>
  <path class="fillable" fill="#ffffff" d="M297.8 103.7 L297.6 104.3 L297.2 105.3 L296.7 106.6 L296.1 108.1 L295.4 109.8 L294.8 111.5 L294.3 113.4 L293.9 115.3 L293.7 117.2 L293.8 119.2 L294.3 121.2 L295.1 123.1 L296.2 124.7 L297.3 126.2 L298.4 127.7 L299.5 129.1 L300.4 130.3 L301.1 131.5 L301.5 132.5 L301.6 133.2 L301.6 134 L301.3 135 L300.7 136.2 L300 137.5 L299.1 138.9 L298.1 140.3 L297.2 141.7 L296.3 143.1 L295.6 144.7 L295.2 146.3 L295.3 147.9 L295.6 149.3 L296.1 150.6 L296.7 151.8 L297.4 152.8 L298.1 153.7 L298.8 154.5 L299.4 155.2 L299.8 155.6 L299.9 155.8 C301.1 158.1 304.5 156.4 303.3 154.2 L302.9 153.4 L302.4 152.7 L301.9 152 L301.3 151.3 L300.8 150.5 L300.3 149.7 L300 148.9 L299.7 148.1 L299.6 147.5 L299.6 146.9 L299.8 146.3 L300.3 145.4 L301 144.2 L301.9 143 L302.9 141.6 L304 140.2 L305 138.6 L305.8 136.9 L306.4 135.1 L306.7 133.1 L306.4 131.1 L305.7 129.2 L304.8 127.5 L303.7 126 L302.7 124.5 L301.6 123 L300.7 121.7 L300 120.4 L299.6 119.4 L299.4 118.5 L299.4 117.5 L299.6 116.3 L300 114.9 L300.4 113.4 L301 111.9 L301.6 110.5 L302.3 109.1 L302.9 107.8 L303.4 106.6 L303.8 105.5 C305 101.5 299 99.7 297.8 103.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M323 105.5 L323.4 106.6 L323.9 107.8 L324.5 109.1 L325.2 110.5 L325.8 111.9 L326.4 113.4 L326.8 114.9 L327.2 116.3 L327.4 117.5 L327.4 118.5 L327.2 119.4 L326.8 120.4 L326.1 121.7 L325.2 123 L324.1 124.5 L323.1 126 L322 127.5 L321.1 129.2 L320.4 131.1 L320.1 133.1 L320.4 135.1 L321 136.9 L321.8 138.6 L322.8 140.2 L323.9 141.6 L324.9 143 L325.8 144.2 L326.5 145.4 L327 146.3 L327.2 146.9 L327.2 147.5 L327.1 148.1 L326.8 148.9 L326.5 149.7 L326 150.5 L325.5 151.3 L324.9 152 L324.4 152.7 L323.9 153.4 L323.5 154.2 C322.3 156.4 325.7 158.1 326.9 155.8 L327 155.6 L327.4 155.2 L328 154.5 L328.7 153.7 L329.4 152.8 L330.1 151.8 L330.7 150.6 L331.2 149.3 L331.5 147.9 L331.6 146.3 L331.2 144.7 L330.5 143.1 L329.6 141.7 L328.7 140.3 L327.7 138.9 L326.8 137.5 L326.1 136.2 L325.5 135 L325.2 134 L325.2 133.2 L325.3 132.5 L325.7 131.5 L326.4 130.3 L327.3 129.1 L328.4 127.7 L329.5 126.2 L330.6 124.7 L331.7 123.1 L332.5 121.2 L333 119.2 L333.1 117.2 L332.9 115.3 L332.5 113.4 L332 111.5 L331.4 109.8 L330.7 108.1 L330.1 106.6 L329.6 105.3 L329.2 104.3 L329 103.7 C327.8 99.7 321.8 101.5 323 105.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M348.2 103.7 L348 104.3 L347.6 105.3 L347.1 106.6 L346.5 108.1 L345.8 109.8 L345.2 111.5 L344.7 113.4 L344.3 115.3 L344.1 117.2 L344.2 119.2 L344.7 121.2 L345.5 123.1 L346.6 124.7 L347.7 126.2 L348.8 127.7 L349.9 129.1 L350.8 130.3 L351.5 131.5 L351.9 132.5 L352 133.2 L352 134 L351.7 135 L351.1 136.2 L350.4 137.5 L349.5 138.9 L348.5 140.3 L347.6 141.7 L346.7 143.1 L346 144.7 L345.6 146.3 L345.7 147.9 L346 149.3 L346.5 150.6 L347.1 151.8 L347.8 152.8 L348.5 153.7 L349.2 154.5 L349.8 155.2 L350.2 155.6 L350.3 155.8 C351.5 158.1 354.9 156.4 353.7 154.2 L353.3 153.4 L352.8 152.7 L352.3 152 L351.7 151.3 L351.2 150.5 L350.7 149.7 L350.4 148.9 L350.1 148.1 L350 147.5 L350 146.9 L350.2 146.3 L350.7 145.4 L351.4 144.2 L352.3 143 L353.3 141.6 L354.4 140.2 L355.4 138.6 L356.2 136.9 L356.8 135.1 L357.1 133.1 L356.8 131.1 L356.1 129.2 L355.2 127.5 L354.1 126 L353.1 124.5 L352 123 L351.1 121.7 L350.4 120.4 L350 119.4 L349.8 118.5 L349.8 117.5 L350 116.3 L350.4 114.9 L350.8 113.4 L351.4 111.9 L352 110.5 L352.7 109.1 L353.3 107.8 L353.8 106.6 L354.2 105.5 C355.4 101.5 349.4 99.7 348.2 103.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M292.4 104.6 Q292.4 62.6 326 62.6 Q359.6 62.6 359.6 104.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M290.7 102.9 Q326 108 361.3 102.9 L362.1 107.1 Q356.2 117.2 350.4 108 Q344.3 117.2 338.2 108 Q332.1 117.2 326 108 Q319.9 117.2 313.8 108 Q307.7 117.2 301.6 108 Q295.8 117.2 289.9 108 Z"/>
  <circle fill="#1a1a1a" stroke="none" cx="314" cy="84" r="4"/>
  <circle fill="#1a1a1a" stroke="none" cx="338" cy="84" r="4"/>
  <path class="fillable" fill="#ffffff" d="M128.8 139.9 L128.4 141.3 L127.4 143.7 L126.2 146.8 L124.7 150.4 L123.2 154.3 L121.8 158.5 L120.5 162.9 L119.6 167.4 L119.1 172.1 L119.3 176.8 L120.5 181.6 L122.5 185.9 L125 189.9 L127.6 193.5 L130.3 197 L132.8 200.2 L135 203.3 L136.6 206 L137.6 208.4 L138 210.2 L137.9 212 L137.2 214.5 L135.8 217.3 L134 220.4 L131.9 223.6 L129.6 226.9 L127.4 230.3 L125.4 233.8 L123.7 237.4 L122.8 241.4 L122.8 245.1 L123.6 248.5 L124.8 251.6 L126.3 254.3 L128 256.8 L129.7 258.9 L131.2 260.8 L132.6 262.4 L133.6 263.5 L134 264 C136.7 269.4 144.7 265.3 142 260 L141 258.2 L139.9 256.6 L138.6 254.9 L137.3 253.1 L136 251.2 L134.9 249.3 L134 247.4 L133.4 245.7 L133.1 244 L133.2 242.6 L133.7 241.2 L134.8 239 L136.5 236.4 L138.7 233.4 L141.1 230.1 L143.6 226.6 L145.9 223 L148 219 L149.4 214.6 L150 209.8 L149.3 205 L147.7 200.6 L145.5 196.6 L143 192.9 L140.5 189.3 L138 185.9 L135.9 182.7 L134.2 179.7 L133.1 177.2 L132.7 175.2 L132.7 172.8 L133.2 169.9 L134 166.5 L135.1 163 L136.5 159.4 L138 155.9 L139.5 152.6 L140.9 149.5 L142.2 146.8 L143.2 144.1 C146 134.5 131.6 130.3 128.8 139.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M158.8 144.1 L159.8 146.8 L161.1 149.5 L162.5 152.6 L164 155.9 L165.5 159.4 L166.9 163 L168 166.5 L168.8 169.9 L169.3 172.8 L169.3 175.2 L168.9 177.2 L167.8 179.7 L166.1 182.7 L164 185.9 L161.5 189.3 L159 192.9 L156.5 196.6 L154.3 200.6 L152.7 205 L152 209.8 L152.6 214.6 L154 219 L156.1 223 L158.4 226.6 L160.9 230.1 L163.3 233.4 L165.5 236.4 L167.2 239 L168.3 241.2 L168.8 242.6 L168.9 244 L168.6 245.7 L168 247.4 L167.1 249.3 L166 251.2 L164.7 253.1 L163.4 254.9 L162.1 256.6 L161 258.2 L160 260 C157.3 265.3 165.3 269.4 168 264 L168.4 263.5 L169.4 262.4 L170.8 260.8 L172.3 258.9 L174 256.8 L175.7 254.3 L177.2 251.6 L178.4 248.5 L179.2 245.1 L179.2 241.4 L178.3 237.4 L176.6 233.8 L174.6 230.3 L172.4 226.9 L170.1 223.6 L168 220.4 L166.2 217.3 L164.8 214.5 L164.1 212 L164 210.2 L164.4 208.4 L165.4 206 L167 203.3 L169.2 200.2 L171.7 197 L174.4 193.5 L177 189.9 L179.5 185.9 L181.5 181.6 L182.7 176.8 L182.9 172.1 L182.4 167.4 L181.5 162.9 L180.2 158.5 L178.8 154.3 L177.3 150.4 L175.8 146.8 L174.6 143.7 L173.6 141.3 L173.2 139.9 C170.4 130.3 156 134.5 158.8 144.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M188.8 139.9 L188.4 141.3 L187.4 143.7 L186.2 146.8 L184.7 150.4 L183.2 154.3 L181.8 158.5 L180.5 162.9 L179.6 167.4 L179.1 172.1 L179.3 176.8 L180.5 181.6 L182.5 185.9 L185 189.9 L187.6 193.5 L190.3 197 L192.8 200.2 L195 203.3 L196.6 206 L197.6 208.4 L198 210.2 L197.9 212 L197.2 214.5 L195.8 217.3 L194 220.4 L191.9 223.6 L189.6 226.9 L187.4 230.3 L185.4 233.8 L183.7 237.4 L182.8 241.4 L182.8 245.1 L183.6 248.5 L184.8 251.6 L186.3 254.3 L188 256.8 L189.7 258.9 L191.2 260.8 L192.6 262.4 L193.6 263.5 L194 264 C196.7 269.4 204.7 265.3 202 260 L201 258.2 L199.9 256.6 L198.6 254.9 L197.3 253.1 L196 251.2 L194.9 249.3 L194 247.4 L193.4 245.7 L193.1 244 L193.2 242.6 L193.7 241.2 L194.8 239 L196.5 236.4 L198.7 233.4 L201.1 230.1 L203.6 226.6 L205.9 223 L208 219 L209.4 214.6 L210 209.8 L209.3 205 L207.7 200.6 L205.5 196.6 L203 192.9 L200.5 189.3 L198 185.9 L195.9 182.7 L194.2 179.7 L193.1 177.2 L192.7 175.2 L192.7 172.8 L193.2 169.9 L194 166.5 L195.1 163 L196.5 159.4 L198 155.9 L199.5 152.6 L200.9 149.5 L202.2 146.8 L203.2 144.1 C206 134.5 191.6 130.3 188.8 139.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M218.8 144.1 L219.8 146.8 L221.1 149.5 L222.5 152.6 L224 155.9 L225.5 159.4 L226.9 163 L228 166.5 L228.8 169.9 L229.3 172.8 L229.3 175.2 L228.9 177.2 L227.8 179.7 L226.1 182.7 L224 185.9 L221.5 189.3 L219 192.9 L216.5 196.6 L214.3 200.6 L212.7 205 L212 209.8 L212.6 214.6 L214 219 L216.1 223 L218.4 226.6 L220.9 230.1 L223.3 233.4 L225.5 236.4 L227.2 239 L228.3 241.2 L228.8 242.6 L228.9 244 L228.6 245.7 L228 247.4 L227.1 249.3 L226 251.2 L224.7 253.1 L223.4 254.9 L222.1 256.6 L221 258.2 L220 260 C217.3 265.3 225.3 269.4 228 264 L228.4 263.5 L229.4 262.4 L230.8 260.8 L232.3 258.9 L234 256.8 L235.7 254.3 L237.2 251.6 L238.4 248.5 L239.2 245.1 L239.2 241.4 L238.3 237.4 L236.6 233.8 L234.6 230.3 L232.4 226.9 L230.1 223.6 L228 220.4 L226.2 217.3 L224.8 214.5 L224.1 212 L224 210.2 L224.4 208.4 L225.4 206 L227 203.3 L229.2 200.2 L231.7 197 L234.4 193.5 L237 189.9 L239.5 185.9 L241.5 181.6 L242.7 176.8 L242.9 172.1 L242.4 167.4 L241.5 162.9 L240.2 158.5 L238.8 154.3 L237.3 150.4 L235.8 146.8 L234.6 143.7 L233.6 141.3 L233.2 139.9 C230.4 130.3 216 134.5 218.8 144.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M248.8 139.9 L248.4 141.3 L247.4 143.7 L246.2 146.8 L244.7 150.4 L243.2 154.3 L241.8 158.5 L240.5 162.9 L239.6 167.4 L239.1 172.1 L239.3 176.8 L240.5 181.6 L242.5 185.9 L245 189.9 L247.6 193.5 L250.3 197 L252.8 200.2 L255 203.3 L256.6 206 L257.6 208.4 L258 210.2 L257.9 212 L257.2 214.5 L255.8 217.3 L254 220.4 L251.9 223.6 L249.6 226.9 L247.4 230.3 L245.4 233.8 L243.7 237.4 L242.8 241.4 L242.8 245.1 L243.6 248.5 L244.8 251.6 L246.3 254.3 L248 256.8 L249.7 258.9 L251.2 260.8 L252.6 262.4 L253.6 263.5 L254 264 C256.7 269.4 264.7 265.3 262 260 L261 258.2 L259.9 256.6 L258.6 254.9 L257.3 253.1 L256 251.2 L254.9 249.3 L254 247.4 L253.4 245.7 L253.1 244 L253.2 242.6 L253.7 241.2 L254.8 239 L256.5 236.4 L258.7 233.4 L261.1 230.1 L263.6 226.6 L265.9 223 L268 219 L269.4 214.6 L270 209.8 L269.3 205 L267.7 200.6 L265.5 196.6 L263 192.9 L260.5 189.3 L258 185.9 L255.9 182.7 L254.2 179.7 L253.1 177.2 L252.7 175.2 L252.7 172.8 L253.2 169.9 L254 166.5 L255.1 163 L256.5 159.4 L258 155.9 L259.5 152.6 L260.9 149.5 L262.2 146.8 L263.2 144.1 C266 134.5 251.6 130.3 248.8 139.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M116 142 Q116 42 196 42 Q276 42 276 142 Z"/>
  <path class="fillable" fill="#ffffff" d="M112 138 Q196 150 280 138 L282 148 Q268 172 254 150 Q239.5 172 225 150 Q210.5 172 196 150 Q181.5 172 167 150 Q152.5 172 138 150 Q124 172 110 150 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="62" rx="11" ry="7" transform="rotate(-25 164 62)"/>
  <ellipse class="fillable" fill="#ffffff" cx="232" cy="58" rx="13" ry="8" transform="rotate(20 232 58)"/>
  <ellipse class="fillable" fill="#ffffff" cx="176" cy="100" rx="11" ry="13"/>
  <circle fill="#1a1a1a" stroke="none" cx="177" cy="101" r="6.8"/>
  <circle fill="#ffffff" stroke="none" cx="179.7" cy="97.9" r="2.6"/>
  <ellipse class="fillable" fill="#ffffff" cx="216" cy="100" rx="11" ry="13"/>
  <circle fill="#1a1a1a" stroke="none" cx="217" cy="101" r="6.8"/>
  <circle fill="#ffffff" stroke="none" cx="219.7" cy="97.9" r="2.6"/>
  <ellipse class="fillable" fill="#ffffff" cx="152" cy="118" rx="11" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="240" cy="118" rx="11" ry="7"/>
  <path fill="none" stroke-width="3" d="M186 116 Q196 126 206 116"/>
  <path fill="none" stroke-width="2.5" d="M311 98 Q326 106 341 98"/>
</g>
''')

# --- Fantasy (7) ---
add('dinosaur', '🦖 霸王龙', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="350" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M26 70 Q26 52 45.8 53.8 Q53 37.6 72.8 43 Q89 35.8 96.2 53.8 Q112.4 55.6 108.8 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 254 Q300 266 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M49.2 236.9 L52.4 221.3 Q58.4 218.1 64.9 220.2 L70.8 235.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M85 230.3 L87.2 210.9 Q94.2 206.3 102.3 208.2 L111 225.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M137.5 214.2 L118.5 204.7 Q116.4 195.8 121.4 188.2 L142.5 185.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M136.3 181.8 L116.3 167.1 Q115.7 156.4 123 148.7 L147.7 150.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M144.1 145.9 L132.2 124.1 Q136.2 114.2 146.1 110.2 L167.9 122.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M184.2 89.5 L168.3 72.8 Q169.5 63 177.4 57.1 L199.8 62.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M194.5 56.9 L193.1 35.7 Q199.8 29.4 208.9 30 L221.5 47.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M161.8 194.3 L159.8 195.4 L157.7 196.7 L155.4 198 L152.8 199.4 L150 200.8 L147 202.4 L143.9 204 L140.7 205.6 L137.4 207.2 L134.1 208.8 L130.7 210.3 L127.4 211.9 L124.2 213.3 L121.1 214.7 L118.2 216 L115.5 217.2 L112.5 218.4 L109.6 219.6 L106.7 220.7 L103.7 221.9 L100.8 223 L97.8 224 L94.9 225.1 L92 226.1 L89.1 227.1 L86.2 228 L83.4 228.9 L80.6 229.7 L77.8 230.4 L75.1 231.1 L72.4 231.8 L69.8 232.3 L67.2 232.8 L64.5 233.2 L61.6 233.5 L58.6 233.7 L55.5 233.8 L52.4 233.8 L49.3 233.8 L46.2 233.8 L43.2 233.7 L40.3 233.7 L37.5 233.6 L34.9 233.6 L32.5 233.6 L30.3 233.7 L28.3 233.8 L26.5 234 C21.3 233.3 20.2 241.2 25.5 242 L26.8 242.7 L28.5 243.4 L30.4 244.3 L32.6 245.2 L35.1 246.2 L37.7 247.2 L40.6 248.2 L43.5 249.2 L46.6 250.2 L49.8 251.2 L53.1 252.2 L56.5 253 L59.9 253.8 L63.3 254.6 L66.8 255.2 L70.2 255.7 L73.5 256 L76.8 256.3 L80.2 256.5 L83.6 256.7 L87 256.8 L90.4 256.8 L93.8 256.7 L97.3 256.6 L100.7 256.5 L104.1 256.4 L107.6 256.2 L111 255.9 L114.4 255.7 L117.8 255.4 L121.2 255.1 L124.5 254.8 L128.2 254.4 L132.1 253.8 L136 253.2 L139.9 252.5 L143.9 251.8 L147.8 251 L151.7 250.2 L155.5 249.4 L159.2 248.7 L162.8 248 L166.1 247.3 L169.3 246.8 L172.1 246.3 L174.6 245.9 L176.7 245.7 L178.2 245.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M218 248 Q218 266 234 266 L264 266 Q274 266 272 252 Q266 238 248 238 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="198" cy="190" rx="60" ry="66" transform="rotate(-10 198 190)"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="200" rx="32" ry="46" transform="rotate(-10 220 200)"/>
  <path fill="none" stroke-width="3" d="M196 172 Q220 176 244 166 M192 198 Q218 202 248 190 M196 224 Q218 228 244 216"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="176" rx="10" ry="7" transform="rotate(-20 158 176)"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="148" rx="8" ry="6" transform="rotate(-20 172 148)"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="218" rx="30" ry="34" transform="rotate(-10 172 218)"/>
  <path class="fillable" fill="#ffffff" d="M140 252 Q140 268 156 268 L198 268 Q210 268 208 254 Q202 238 176 238 Q140 238 140 252 Z"/>
  <path fill="none" stroke-width="3" d="M172 268 L172 260 M188 268 L188 260"/>
  <path class="fillable" fill="#ffffff" d="M243.4 173 L244.3 173.3 L245.2 173.5 L246.1 173.7 L247.1 173.9 L248.1 174.1 L249.2 174.4 L250.3 174.6 L251.4 174.9 L252.5 175.2 L253.6 175.5 L254.6 175.8 L255.6 176.2 L256.4 176.5 L257.2 176.8 L257.7 177 L258.1 177.2 L258.4 177.4 L258.8 177.7 L259.3 178.1 L259.8 178.6 L260.3 179.2 L260.8 179.9 L261.3 180.6 L261.8 181.3 L262.3 182.1 L262.7 182.8 L263.2 183.6 L263.6 184.3 L264.1 185 L264.5 185.7 L264.9 186.4 L265.4 187.1 C269.5 193.1 278.6 187 274.6 180.9 L274.5 180.8 L274.4 180.4 L274.2 179.8 L273.9 179.1 L273.5 178.3 L273.1 177.4 L272.7 176.4 L272.2 175.4 L271.7 174.4 L271.1 173.3 L270.5 172.2 L269.7 171.1 L269 170 L268.1 168.9 L267.1 167.8 L265.9 166.8 L264.7 165.9 L263.4 165.1 L262.1 164.4 L260.8 163.7 L259.5 163.1 L258.2 162.6 L256.9 162.1 L255.6 161.6 L254.4 161.1 L253.2 160.7 L252.1 160.3 L251.1 160 L250.2 159.6 L249.4 159.4 L248.9 159.1 L248.6 159 C239.3 155.5 234 169.5 243.4 173 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 92 Q180 48 236 46 Q300 46 308 90 Q312 128 278 134 L222 136 Q182 136 180 92 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="214" cy="62" rx="10" ry="6" transform="rotate(-15 214 62)"/>
  <ellipse class="fillable" fill="#ffffff" cx="196" cy="82" rx="7" ry="9"/>
  <path fill="none" stroke-width="3.5" d="M246 114 Q274 126 300 110"/>
  <path fill="none" stroke-width="3" d="M292 72 L296 78 M282 70 L286 76"/>
  <ellipse class="fillable" fill="#ffffff" cx="244" cy="84" rx="11" ry="13"/>
  <circle fill="#1a1a1a" stroke="none" cx="246" cy="85" r="6.8"/>
  <circle fill="#ffffff" stroke="none" cx="248.7" cy="81.9" r="2.6"/>
  <ellipse class="fillable" fill="#ffffff" cx="268" cy="104" rx="10" ry="6"/>
</g>
''')

add('dragon', '🐲 飞龙', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="350" cy="46" r="20"/>
  <path class="fillable" fill="#ffffff" d="M20 64 Q20 47 38.7 48.7 Q45.5 33.4 64.2 38.5 Q79.5 31.7 86.3 48.7 Q101.6 50.4 98.2 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 240 200 252 Q300 264 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 170 Q118 120 66 98 Q60 128 72 150 Q86 144 94 160 Q90 178 106 184 Q118 176 124 192 Q136 198 160 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M 240 170 Q 282 120 334 98 Q 340 128 328 150 Q 314 144 306 160 Q 310 178 294 184 Q 282 176 276 192 Q 264 198 240 200 Z"/>
  <path fill="none" stroke-width="3" d="M152 178 L72 104 M150 186 L96 162 M150 194 L122 192"/>
  <path fill="none" stroke-width="3" d="M 248 178 L 328 104 M 250 186 L 304 162 M 250 194 L 278 192"/>
  <path class="fillable" fill="#ffffff" d="M238.6 250.9 L240 251.1 L242.1 251.4 L244.6 251.9 L247.4 252.5 L250.6 253.1 L254 253.8 L257.6 254.6 L261.3 255.3 L265.1 256 L269 256.6 L272.8 257.1 L276.6 257.6 L280.4 257.9 L284 258 L287.5 257.9 L290.9 257.6 L294 257.1 L296.9 256.3 L299.7 255.4 L302.4 254.4 L305.1 253.2 L307.6 251.9 L310 250.5 L312.3 249.1 L314.5 247.6 L316.6 246 L318.6 244.4 L320.4 242.8 L322.2 241.1 L323.8 239.5 L325.3 237.9 L326.7 236.3 L328.2 234.2 L329.5 232.1 L330.6 229.9 L331.5 227.6 L332.2 225.4 L332.7 223.2 L333.2 221.1 L333.6 219 L333.8 217 L334.1 215 L334.3 213.2 L334.4 211.6 L334.5 210.2 L334.6 208.9 L334.7 208 L334.8 207.5 L325.2 204.5 L324.8 205.8 L324.5 207.2 L324.1 208.6 L323.8 210.1 L323.5 211.7 L323.2 213.4 L322.8 215.1 L322.4 216.8 L322 218.5 L321.5 220.2 L320.9 221.8 L320.3 223.3 L319.6 224.6 L318.9 225.9 L318.1 226.9 L317.3 227.7 L316.1 228.9 L314.8 230.1 L313.3 231.4 L311.8 232.6 L310.2 233.8 L308.5 235 L306.8 236.1 L304.9 237.2 L303.1 238.2 L301.2 239.1 L299.2 239.9 L297.2 240.7 L295.2 241.3 L293.2 241.8 L291.1 242.2 L289.1 242.4 L287 242.5 L284.5 242.4 L281.7 242.1 L278.6 241.7 L275.2 241.2 L271.8 240.5 L268.3 239.8 L264.7 239 L261.2 238.1 L257.8 237.3 L254.5 236.4 L251.4 235.6 L248.5 234.9 L245.9 234.2 L243.5 233.6 L241.4 233.1 C229.6 231.2 226.8 249 238.6 250.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 210 Q312 206 314 192 Q318 180 330 168 Q342 180 346 192 Q348 206 330 210 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="148" cy="256" rx="28" ry="14"/>
  <ellipse class="fillable" fill="#ffffff" cx="252" cy="256" rx="28" ry="14"/>
  <path fill="none" stroke-width="3" d="M136 262 L136 270 M148 264 L148 270 M160 262 L160 270 M240 262 L240 270 M252 264 L252 270 M264 262 L264 270"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="208" rx="62" ry="52"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="218" rx="34" ry="40"/>
  <path fill="none" stroke-width="3" d="M172 202 Q200 210 228 202 M168 226 Q200 234 232 226"/>
  <path class="fillable" fill="#ffffff" d="M146 182 Q126 204 136 226 Q152 232 162 218 Q166 198 160 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M254 182 Q274 204 264 226 Q248 232 238 218 Q234 198 240 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 74 Q150 46 156 26 Q174 40 188 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M230 74 Q250 46 244 26 Q226 40 212 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M186.8 62 L192.3 43.3 Q200 40 207.7 43.3 L213.2 62 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 100 Q120 84 116 104 Q128 120 150 120 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 100 Q280 84 284 104 Q272 120 250 120 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="114" r="54"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="142" rx="32" ry="20"/>
  <path fill="none" stroke-width="3.5" d="M192 136 L190 140 M208 136 L210 140"/>
  <path fill="none" stroke-width="3" d="M188 150 Q200 158 212 150"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="104" rx="10" ry="12"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="105" r="6.2"/>
  <circle fill="#ffffff" stroke="none" cx="183.5" cy="102.2" r="2.4"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="104" rx="10" ry="12"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="105" r="6.2"/>
  <circle fill="#ffffff" stroke="none" cx="223.5" cy="102.2" r="2.4"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="130" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="242" cy="130" rx="9" ry="6"/>
</g>
''')

add('unicorn', '🦄 彩虹独角兽', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M18 258 A182 182 0 0 1 382 258 L364 258 A164 164 0 0 0 36 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M36 258 A164 164 0 0 1 364 258 L346 258 A146 146 0 0 0 54 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M54 258 A146 146 0 0 1 346 258 L328 258 A128 128 0 0 0 72 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 250 200 256 Q300 264 400 252 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M4 262 Q4 240 28.2 242.2 Q37 222.4 61.2 229 Q81 220.2 89.8 242.2 Q109.6 244.4 105.2 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M294 262 Q294 240 318.2 242.2 Q327 222.4 351.2 229 Q371 220.2 379.8 242.2 Q399.6 244.4 395.2 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M122.3 158.1 L122.1 158.3 L121.2 158.5 L119.7 158.7 L117.9 158.9 L115.8 159.1 L113.5 159.3 L111 159.5 L108.4 159.8 L105.7 160.1 L102.9 160.5 L100.1 161 L97.2 161.7 L94.4 162.5 L91.5 163.6 L88.6 165.1 L85.7 167 L83.6 168.8 L81.8 170.8 L80.1 172.8 L78.6 174.9 L77.2 177.2 L75.9 179.4 L74.8 181.7 L73.8 184.1 L72.9 186.5 L72.2 188.9 L71.5 191.4 L71 193.8 L70.5 196.3 L70.2 198.7 L70.1 201.1 L70 203.5 L70.2 206.3 L70.6 209 L71.2 211.7 L72 214.3 L72.9 216.8 L73.9 219.3 L75 221.7 L76.1 224.1 L77.2 226.4 L78.3 228.6 L79.4 230.6 L80.4 232.4 L81.3 234.1 L82.1 235.5 L82.8 236.7 L83.2 237.5 C85.2 243.8 94.8 240.9 92.8 234.5 L92.5 233 L92 231.5 L91.5 229.7 L90.9 227.9 L90.3 225.9 L89.6 223.8 L88.9 221.6 L88.2 219.4 L87.5 217.1 L86.9 214.9 L86.5 212.8 L86.1 210.7 L85.8 208.8 L85.7 207 L85.8 205.6 L86 204.5 L86.3 203.1 L86.7 201.6 L87.2 200.1 L87.8 198.5 L88.5 196.9 L89.2 195.4 L90.1 193.9 L90.9 192.4 L91.8 191 L92.8 189.7 L93.8 188.5 L94.8 187.5 L95.8 186.6 L96.7 185.9 L97.5 185.4 L98.3 185 L98.5 185.1 L99.2 185 L100.3 184.9 L101.7 184.8 L103.4 184.7 L105.3 184.6 L107.3 184.7 L109.4 184.7 L111.5 184.9 L113.6 185 L115.7 185.2 L117.8 185.4 L119.7 185.6 L121.7 185.8 L123.6 185.9 L125.7 185.9 C144.2 183.6 140.7 155.8 122.3 158.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M118.2 178.2 L118.2 178.5 L117.7 179.1 L116.9 179.9 L115.9 180.9 L114.7 182 L113.4 183.2 L112.1 184.5 L110.6 185.9 L109.1 187.4 L107.6 189 L106.2 190.6 L104.7 192.4 L103.4 194.2 L102.1 196.2 L100.9 198.4 L100 200.7 L99.4 202.8 L98.9 204.8 L98.6 206.9 L98.4 209 L98.3 211 L98.3 213.1 L98.4 215.1 L98.5 217.1 L98.7 219.1 L99 221.1 L99.4 223 L99.8 224.9 L100.2 226.8 L100.8 228.6 L101.3 230.3 L102 231.9 L102.8 233.8 L103.8 235.6 L104.9 237.2 L106.1 238.7 L107.3 240.2 L108.6 241.6 L109.9 242.9 L111.2 244.1 L112.4 245.2 L113.7 246.3 L114.8 247.3 L115.9 248.2 L116.9 249 L117.7 249.6 L118.4 250.1 L118.8 250.5 C122.1 254.7 128.4 249.7 125.2 245.5 L124.6 244.6 L123.9 243.7 L123.2 242.8 L122.4 241.7 L121.6 240.7 L120.7 239.5 L119.7 238.4 L118.8 237.1 L117.9 235.9 L117.1 234.7 L116.3 233.4 L115.6 232.2 L115 231 L114.5 229.9 L114.2 228.9 L114 228.1 L113.8 226.9 L113.7 225.6 L113.5 224.2 L113.4 222.8 L113.4 221.3 L113.4 219.9 L113.4 218.4 L113.5 216.9 L113.6 215.4 L113.8 214 L114.1 212.6 L114.4 211.3 L114.8 210.1 L115.2 209 L115.6 208.1 L116 207.3 L116.4 206.9 L116.9 206.3 L117.7 205.5 L118.6 204.7 L119.6 203.7 L120.8 202.8 L122.1 201.8 L123.4 200.8 L124.8 199.9 L126.1 199 L127.5 198.1 L128.8 197.2 L130.1 196.4 L131.3 195.6 L132.5 194.8 L133.8 193.8 C144.1 183.4 128.6 167.9 118.2 178.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 211 Q150 200 161 200 Q172 200 172 211 L172 256.1 Q172 266 161 266 Q150 266 150 256.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M214 211 Q214 200 225 200 Q236 200 236 211 L236 256.1 Q236 266 225 266 Q214 266 214 256.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M126 216 Q126 204 138 204 Q150 204 150 216 L150 261.2 Q150 272 138 272 Q126 272 126 261.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M236 216 Q236 204 248 204 Q260 204 260 216 L260 261.2 Q260 272 248 272 Q236 272 236 261.2 Z"/>
  <path fill="none" stroke-width="3" d="M152 254 L170 254 M216 254 L234 254 M128 260 L148 260 M238 260 L258 260"/>
  <path class="fillable" fill="#ffffff" d="M212 178 Q216 128 244 98 L296 118 Q270 148 264 188 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="190" cy="190" rx="74" ry="42"/>
  <path class="fillable" fill="#ffffff" d="M252 68 L258 34 Q260 28 264 34 L276 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M282 66 L306 18 Q310 14 310 20 L298 72 Z"/>
  <path fill="none" stroke-width="2.5" d="M287 60 L301 64 M292 48 L304 52 M297 36 L307 40"/>
  <path class="fillable" fill="#ffffff" d="M236 94 Q234 58 270 56 Q302 56 314 84 Q328 108 330 124 Q334 146 308 148 Q284 150 268 134 Q238 124 236 94 Z"/>
  <path fill="none" stroke-width="4" d="M314 120 L318 125"/>
  <path fill="none" stroke-width="3" d="M292 136 Q304 142 316 138"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="72" rx="16" ry="20" transform="rotate(-30 236 72)"/>
  <ellipse class="fillable" fill="#ffffff" cx="222" cy="102" rx="17" ry="21" transform="rotate(-10 222 102)"/>
  <ellipse class="fillable" fill="#ffffff" cx="218" cy="136" rx="17" ry="21"/>
  <ellipse class="fillable" fill="#ffffff" cx="224" cy="168" rx="15" ry="18" transform="rotate(15 224 168)"/>
  <ellipse class="fillable" fill="#ffffff" cx="272" cy="88" rx="10" ry="12"/>
  <circle fill="#1a1a1a" stroke="none" cx="273" cy="89" r="6.2"/>
  <circle fill="#ffffff" stroke="none" cx="275.5" cy="86.2" r="2.4"/>
  <ellipse class="fillable" fill="#ffffff" cx="280" cy="112" rx="9" ry="5"/>
</g>
''')

add('mermaid', '🧜‍♀️ 美人鱼', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="46" r="22"/>
  <path class="fillable" fill="#ffffff" d="M22 70 Q22 52 41.8 53.8 Q49 37.6 68.8 43 Q85 35.8 92.2 53.8 Q108.4 55.6 104.8 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M172 84 Q168 34 214 32 Q262 34 258 84 Q258 116 278 136 Q300 160 290 188 Q276 202 264 186 Q272 162 252 148 Q238 136 236 124 L192 124 Q174 132 160 124 Q174 108 172 84 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 256 Q124 186 210 178 Q312 172 334 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M235.5 138 L236.2 137.7 L237.1 137.1 L238.3 136.5 L239.7 135.8 L241.2 135 L242.8 134.2 L244.5 133.3 L246.3 132.3 L248.2 131.3 L250 130.2 L251.9 129.1 L253.7 128 L255.5 126.8 L257.2 125.6 L258.9 124.3 L260.4 123 L261.8 121.6 L263.2 120.2 L264.4 118.8 L265.6 117.3 L266.7 115.9 L267.8 114.4 L268.8 112.9 L269.7 111.4 L270.6 109.9 L271.5 108.5 L272.3 107.1 L273 105.8 L273.7 104.5 L274.4 103.3 L275 102.1 L275.5 101.1 L276.2 99.9 L276.7 98.7 L277.2 97.5 L277.6 96.4 L278 95.3 L278.3 94.2 L278.6 93.2 L278.8 92.3 L279 91.4 L279.2 90.6 L279.3 89.9 L279.5 89.2 L279.6 88.7 L279.6 88.3 L279.7 88 L279.7 87.9 C282.2 80.3 270.8 76.5 268.3 84.1 L268.1 84.8 L267.9 85.5 L267.7 86.1 L267.6 86.7 L267.4 87.3 L267.3 87.9 L267.1 88.6 L266.9 89.2 L266.7 89.9 L266.5 90.5 L266.2 91.2 L266 91.9 L265.6 92.7 L265.3 93.4 L264.9 94.1 L264.5 94.9 L263.9 96 L263.2 97.1 L262.6 98.2 L261.9 99.4 L261.1 100.6 L260.4 101.9 L259.6 103.1 L258.8 104.4 L257.9 105.6 L257.1 106.8 L256.2 108 L255.3 109.1 L254.4 110.2 L253.4 111.2 L252.5 112.2 L251.6 113 L250.6 113.8 L249.4 114.7 L248 115.6 L246.6 116.5 L245 117.5 L243.3 118.4 L241.6 119.3 L239.9 120.2 L238.2 121.1 L236.6 121.9 L235 122.7 L233.4 123.4 L232 124.1 L230.7 124.8 L229.5 125.4 L228.5 126 Z"/>
  <circle class="fillable" fill="#ffffff" cx="276" cy="80" r="10"/>
  <path class="fillable" fill="#ffffff" d="M190.2 128.1 L189.7 128.8 L189.1 129.7 L188.3 130.8 L187.4 132.1 L186.4 133.5 L185.3 135 L184.2 136.6 L183 138.3 L181.8 140.1 L180.6 141.9 L179.4 143.7 L178.2 145.6 L177.1 147.5 L176 149.4 L175 151.4 L174.1 153.3 L173.3 155.2 L172.5 157.3 L171.8 159.4 L171.2 161.5 L170.6 163.6 L170 165.8 L169.4 167.9 L168.9 170 L168.5 172 L168 174 L167.6 175.8 L167.3 177.5 L167 179 L166.7 180.4 L166.4 181.5 L166.2 182.4 C164 190 175.6 193.3 177.8 185.6 L178.1 184.5 L178.5 183.2 L178.8 181.8 L179.2 180.3 L179.6 178.6 L180.1 176.8 L180.6 174.9 L181.1 173 L181.6 171.1 L182.1 169.1 L182.7 167.2 L183.3 165.3 L184 163.5 L184.6 161.7 L185.3 160.1 L185.9 158.7 L186.6 157.3 L187.5 155.9 L188.4 154.3 L189.4 152.7 L190.5 151.1 L191.6 149.4 L192.8 147.8 L194 146.2 L195.2 144.6 L196.3 143.1 L197.4 141.7 L198.4 140.3 L199.4 139.1 L200.3 137.9 L201.1 136.9 L201.8 135.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 124 Q188 156 194 188 L234 188 Q240 156 232 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M194 158 Q198 142 205 142 Q213 142 214 158 Q204 164 194 158 Z"/>
  <path class="fillable" fill="#ffffff" d="M214 158 Q215 142 223 142 Q230 142 234 158 Q224 164 214 158 Z"/>
  <path class="fillable" fill="#ffffff" d="M104 226 Q78 230 60 212 Q80 198 96 204 Q86 186 94 166 Q112 182 116 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M189 182 L189.4 185.1 L189.8 187.6 L190.4 189.9 L190.9 192.2 L191.4 194.5 L192 196.8 L192.5 199.2 L193 201.4 L193.4 203.6 L193.7 205.7 L194 207.6 L194.2 209.1 L194.3 210.4 L194.4 211.1 L194.6 211.3 L195.1 210.9 L194.9 211.8 L194.6 212.8 L194.1 213.9 L193.6 215 L192.9 216.2 L192.1 217.4 L191.2 218.6 L190.2 219.8 L189.1 221 L187.9 222.1 L186.7 223.2 L185.4 224.2 L184 225.2 L182.6 226.1 L181.1 226.9 L179.6 227.6 L178 228.2 L176 228.8 L173.6 229.4 L171 229.8 L168.2 230.2 L165.2 230.5 L162 230.8 L158.8 230.9 L155.6 230.9 L152.4 230.9 L149.2 230.8 L146.2 230.7 L143.2 230.4 L140.4 230.2 L137.9 229.8 L135.6 229.5 L133.9 229.2 L132.1 228.7 L130.1 228 L128.1 227.1 L126 226.1 L123.9 224.9 L121.8 223.7 L119.7 222.3 L117.7 221 L115.7 219.6 L113.8 218.3 L111.9 217 L110.2 215.7 L108.5 214.6 L106.8 213.5 L105.1 212.6 C95.2 205.8 85 220.6 94.9 227.4 L95.4 228.1 L96.2 229.1 L97.3 230.4 L98.6 231.9 L100.2 233.6 L101.9 235.4 L103.8 237.4 L105.8 239.4 L108 241.5 L110.4 243.6 L112.9 245.6 L115.6 247.7 L118.5 249.6 L121.6 251.4 L124.9 253.1 L128.4 254.5 L131.6 255.6 L135 256.6 L138.4 257.5 L142.1 258.4 L145.8 259.1 L149.6 259.8 L153.5 260.4 L157.4 260.9 L161.4 261.2 L165.3 261.5 L169.2 261.7 L173.1 261.8 L177 261.7 L180.8 261.5 L184.6 261 L188.4 260.4 L192 259.6 L195.5 258.6 L198.8 257.4 L202.1 256.1 L205.3 254.6 L208.4 252.9 L211.4 251.1 L214.3 249.2 L217.1 247.1 L219.7 244.9 L222.3 242.6 L224.7 240.2 L227 237.6 L229.1 234.9 L231.1 232.1 L232.9 229.1 L235 224.6 L236.5 220.2 L237.4 216 L238.1 212 L238.5 208.2 L238.7 204.5 L238.8 201 L238.8 197.6 L238.7 194.3 L238.7 191.3 L238.6 188.6 L238.5 186.1 L238.5 184 L238.6 182.5 L238.7 181.6 L239 182 Z"/>
  <path fill="none" stroke-width="3" d="M200 218 Q206 226 214 218 M176 232 Q182 240 190 234 M148 230 Q154 238 162 232"/>
  <path class="fillable" fill="#ffffff" d="M190 180 Q214 188 238 180 L238 196 Q214 204 190 196 Z"/>
  <circle class="fillable" fill="#ffffff" cx="214" cy="86" r="36"/>
  <path class="fillable" fill="#ffffff" d="M178 86 Q178 50 214 50 Q250 50 250 86 Q236 68 214 72 Q192 68 178 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M250.4 43.8 L251.4 52.4 L259 56.5 L251.1 60 L249.6 68.5 L243.8 62.1 L235.2 63.3 L239.5 55.8 L235.8 48 L244.2 49.8 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="202" cy="92" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="202.5" cy="93" r="4.6"/>
  <circle fill="#ffffff" stroke="none" cx="204.3" cy="90.9" r="1.7"/>
  <ellipse class="fillable" fill="#ffffff" cx="226" cy="92" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="226.5" cy="93" r="4.6"/>
  <circle fill="#ffffff" stroke="none" cx="228.3" cy="90.9" r="1.7"/>
  <ellipse class="fillable" fill="#ffffff" cx="192" cy="106" rx="7" ry="4.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="106" rx="7" ry="4.5"/>
  <path fill="none" stroke-width="3" d="M207 108 Q214 114 221 108"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q25 240 50 250 Q75 260 100 250 Q125 240 150 250 Q175 260 200 250 Q225 240 250 250 Q275 260 300 250 Q325 240 350 250 Q375 260 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 276 Q20 268 40 276 Q60 284 80 276 Q100 268 120 276 Q140 284 160 276 Q180 268 200 276 Q220 284 240 276 Q260 268 280 276 Q300 284 320 276 Q340 268 360 276 Q380 284 400 276 L400 300 L0 300 Z"/>
</g>
''')

add('castle', '🏰 城堡', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M57.2 46.8 L64.6 49.9 M44.8 59.2 L47.9 66.6 M27.2 59.2 L24.1 66.6 M14.8 46.8 L7.4 49.9 M14.8 29.2 L7.4 26.1 M27.2 16.8 L24.1 9.4 M44.8 16.8 L47.9 9.4 M57.2 29.2 L64.6 26.1" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="36" cy="38" r="16"/>
  <path class="fillable" fill="#ffffff" d="M325.5 69.9 Q325.5 57.5 339.1 58.8 Q344.1 47.6 357.7 51.3 Q368.9 46.4 373.8 58.8 Q385 60 382.5 69.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 230 200 246 Q300 262 400 240 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="170" y="82" width="60" height="76" rx="0"/>
  <rect class="fillable" fill="#ffffff" x="62" y="108" width="64" height="146" rx="0"/>
  <rect class="fillable" fill="#ffffff" x="274" y="108" width="64" height="146" rx="0"/>
  <path class="fillable" fill="#ffffff" d="M128 254 L128 146 L124 146 L124 132 L140.9 132 L140.9 146 L157.8 146 L157.8 132 L174.7 132 L174.7 146 L191.6 146 L191.6 132 L208.4 132 L208.4 146 L225.3 146 L225.3 132 L242.2 132 L242.2 146 L259.1 146 L259.1 132 L276 132 L276 146 L272 146 L272 254 Z"/>
  <path fill="none" d="M94 44 L94 20" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M94 20 L118 27 L94 34 Z"/>
  <path class="fillable" fill="#ffffff" d="M54 108 Q78 82 94 40 Q110 82 134 108 Q94 116 54 108 Z"/>
  <path fill="none" d="M306 44 L306 20" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M306 20 L330 27 L306 34 Z"/>
  <path class="fillable" fill="#ffffff" d="M266 108 Q290 82 306 40 Q322 82 346 108 Q306 116 266 108 Z"/>
  <path fill="none" d="M200 30 L200 12" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M200 12 L224 19 L200 26 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 86 Q186 62 200 28 Q214 62 240 86 Q200 94 160 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M189 124 L189 112 Q189 102 200 102 Q211 102 211 112 L211 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M83 172 L83 152 Q83 140 94 140 Q105 140 105 152 L105 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M83 222 L83 202 Q83 190 94 190 Q105 190 105 202 L105 222 Z"/>
  <path class="fillable" fill="#ffffff" d="M295 172 L295 152 Q295 140 306 140 Q317 140 317 152 L317 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M295 222 L295 202 Q295 190 306 190 Q317 190 317 202 L317 222 Z"/>
  <path class="fillable" fill="#ffffff" d="M142 190 L142 172 Q142 162 152 162 Q162 162 162 172 L162 190 Z"/>
  <path class="fillable" fill="#ffffff" d="M238 190 L238 172 Q238 162 248 162 Q258 162 258 172 L258 190 Z"/>
  <path class="fillable" fill="#ffffff" d="M174 254 L174 214 Q174 186 200 186 Q226 186 226 214 L226 254 Z"/>
  <path fill="none" d="M200 188 L200 254" stroke-width="3"/>
  <circle fill="#1a1a1a" stroke="none" cx="191" cy="228" r="3"/>
  <circle fill="#1a1a1a" stroke="none" cx="209" cy="228" r="3"/>
</g>
''')

add('princess', '👸 公主', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M374.9 56.3 L382.3 59.4 M360.3 70.9 L363.4 78.3 M339.7 70.9 L336.6 78.3 M325.1 56.3 L317.7 59.4 M325.1 35.7 L317.7 32.6 M339.7 21.1 L336.6 13.7 M360.3 21.1 L363.4 13.7 M374.9 35.7 L382.3 32.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="350" cy="46" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 230 200 246 Q300 262 400 240 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 100 Q140 40 200 40 Q260 40 250 100 Q262 130 270 160 Q276 180 256 182 Q240 184 236 168 L164 168 Q160 184 144 182 Q124 180 130 160 Q138 130 150 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M172 196 Q136 226 120 254 Q200 270 280 254 Q264 226 228 196 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 252 Q200 268 280 252 L292 268 Q280 284 264 274 Q250 286 234 276 Q218 288 200 278 Q182 288 166 276 Q150 286 136 274 Q120 284 108 268 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 150 Q200 160 222 150 L230 200 Q200 208 170 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M168 192 Q200 202 232 192 L234 206 Q200 216 166 206 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 202 Q184 188 178 200 Q180 214 200 204 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 202 Q216 188 222 200 Q220 214 200 204 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="203" r="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="152" cy="191" rx="8" ry="21" transform="rotate(35 152 191)"/>
  <ellipse class="fillable" fill="#ffffff" cx="248" cy="191" rx="8" ry="21" transform="rotate(-35 248 191)"/>
  <circle class="fillable" fill="#ffffff" cx="140" cy="210" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="260" cy="210" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="168" cy="162" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="232" cy="162" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="102" r="48"/>
  <path class="fillable" fill="#ffffff" d="M152 106 Q148 54 200 54 Q252 54 248 106 Q240 80 214 76 Q206 74 200 84 Q194 74 186 76 Q160 80 152 106 Z"/>
  <path class="fillable" fill="#ffffff" d="M166 64 L160 28 L182 46 L200 22 L218 46 L240 28 L234 64 Q200 72 166 64 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="50" r="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="182" cy="108" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="183" cy="109" r="6"/>
  <circle fill="#ffffff" stroke="none" cx="185.4" cy="106.3" r="2.3"/>
  <ellipse class="fillable" fill="#ffffff" cx="218" cy="108" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="219" cy="109" r="6"/>
  <circle fill="#ffffff" stroke="none" cx="221.4" cy="106.3" r="2.3"/>
  <ellipse class="fillable" fill="#ffffff" cx="166" cy="124" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="234" cy="124" rx="8" ry="5"/>
  <path fill="none" d="M191 128 Q200 136 209 128" stroke-width="3"/>
</g>
''')

add('robot', '🤖 机器人', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M82.8 61.1 L90.2 64.2 M67.1 76.8 L70.2 84.2 M44.9 76.8 L41.8 84.2 M29.2 61.1 L21.8 64.2 M29.2 38.9 L21.8 35.8 M44.9 23.2 L41.8 15.8 M67.1 23.2 L70.2 15.8 M82.8 38.9 L90.2 35.8" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="56" cy="50" r="22"/>
  <path class="fillable" fill="#ffffff" d="M295.5 72 Q295.5 57 312 58.5 Q318 45 334.5 49.5 Q348 43.5 354 58.5 Q367.5 60 364.5 72 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 230 200 246 Q300 262 400 240 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="156" y="222" width="26" height="36" rx="6"/>
  <rect class="fillable" fill="#ffffff" x="218" y="222" width="26" height="36" rx="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="166" cy="262" rx="26" ry="12"/>
  <ellipse class="fillable" fill="#ffffff" cx="234" cy="262" rx="26" ry="12"/>
  <path class="fillable" fill="#ffffff" d="M136 152 Q104 162 94 196 L112 202 Q118 178 138 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M264 152 Q296 140 306 106 L288 100 Q282 124 262 134 Z"/>
  <path class="fillable" fill="#ffffff" d="M90 194 A14 14 0 1 0 116 204 L104 202 Z"/>
  <path class="fillable" fill="#ffffff" d="M310 108 A14 14 0 1 0 286 98 L298 104 Z"/>
  <rect class="fillable" fill="#ffffff" x="132" y="134" width="136" height="98" rx="20"/>
  <rect class="fillable" fill="#ffffff" x="160" y="152" width="80" height="58" rx="10"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="168" r="7"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="168" r="7"/>
  <circle class="fillable" fill="#ffffff" cx="220" cy="168" r="7"/>
  <path class="fillable" fill="#ffffff" d="M200 204 Q180 192 186 184 Q194 178 200 186 Q206 178 214 184 Q220 192 200 204 Z"/>
  <rect class="fillable" fill="#ffffff" x="184" y="120" width="32" height="18" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="126" y="70" width="16" height="34" rx="6"/>
  <rect class="fillable" fill="#ffffff" x="258" y="70" width="16" height="34" rx="6"/>
  <path fill="none" d="M200 48 L200 28"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="22" r="9"/>
  <rect class="fillable" fill="#ffffff" x="140" y="46" width="120" height="80" rx="22"/>
  <ellipse class="fillable" fill="#ffffff" cx="174" cy="82" rx="15" ry="15"/>
  <circle fill="#1a1a1a" stroke="none" cx="175" cy="83" r="8"/>
  <circle fill="#ffffff" stroke="none" cx="178.2" cy="79.4" r="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="226" cy="82" rx="15" ry="15"/>
  <circle fill="#1a1a1a" stroke="none" cx="227" cy="83" r="8"/>
  <circle fill="#ffffff" stroke="none" cx="230.2" cy="79.4" r="3"/>
  <rect class="fillable" fill="#ffffff" x="178" y="102" width="44" height="14" rx="7"/>
  <path fill="none" d="M189 102 L189 116 M200 102 L200 116 M211 102 L211 116" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="152" cy="106" rx="7" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="248" cy="106" rx="7" ry="5"/>
</g>
''')

# --- Vehicles (7) ---
add('car', '🚗 小汽车', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M371.8 61.1 L379.2 64.2 M356.1 76.8 L359.2 84.2 M333.9 76.8 L330.8 84.2 M318.2 61.1 L310.8 64.2 M318.2 38.9 L310.8 35.8 M333.9 23.2 L330.8 15.8 M356.1 23.2 L359.2 15.8 M371.8 38.9 L379.2 35.8" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="345" cy="50" r="22"/>
  <path class="fillable" fill="#ffffff" d="M43.2 64.8 Q43.2 48.8 60.8 50.4 Q67.2 36 84.8 40.8 Q99.2 34.4 105.6 50.4 Q120 52 116.8 64.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 230 200 246 Q300 262 400 240 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 266 Q200 256 400 266 L400 300 L0 300 Z"/>
  <path fill="none" d="M30 284 L70 284 M120 283 L160 283 M210 283 L250 283 M300 284 L340 284" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M100 154 Q112 84 170 80 L236 80 Q276 84 296 154 Z"/>
  <path class="fillable" fill="#ffffff" d="M122 148 Q132 102 168 98 L192 98 L192 148 Z"/>
  <path class="fillable" fill="#ffffff" d="M208 98 L234 98 Q262 102 276 148 L208 148 Z"/>
  <path class="fillable" fill="#ffffff" d="M44 202 Q46 152 92 150 L312 150 Q354 154 358 198 L358 214 Q358 228 344 228 L58 228 Q44 228 44 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M46 184 L356 184 L357 198 L45 198 Z"/>
  <path fill="none" d="M200 152 L200 182 M200 200 L200 226" stroke-width="3"/>
  <path fill="none" d="M176 168 L188 168 M212 168 L224 168" stroke-width="4"/>
  <ellipse class="fillable" fill="#ffffff" cx="346" cy="170" rx="8" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="50" cy="168" rx="5" ry="10"/>
  <rect class="fillable" fill="#ffffff" x="328" y="210" width="40" height="16" rx="8"/>
  <rect class="fillable" fill="#ffffff" x="34" y="210" width="40" height="16" rx="8"/>
  <circle class="fillable" fill="#ffffff" cx="110" cy="228" r="32"/>
  <circle class="fillable" fill="#ffffff" cx="110" cy="228" r="13"/>
  <circle class="fillable" fill="#ffffff" cx="292" cy="228" r="32"/>
  <circle class="fillable" fill="#ffffff" cx="292" cy="228" r="13"/>
</g>
''')

add('train', '🚂 小火车', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M76.9 56.3 L84.3 59.4 M62.3 70.9 L65.4 78.3 M41.7 70.9 L38.6 78.3 M27.1 56.3 L19.7 59.4 M27.1 35.7 L19.7 32.6 M41.7 21.1 L38.6 13.7 M62.3 21.1 L65.4 13.7 M76.9 35.7 L84.3 32.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="52" cy="46" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 238 Q200 228 400 238 L400 300 L0 300 Z"/>
  <path fill="none" d="M0 252 Q200 244 400 252" stroke-width="3"/>
  <rect class="fillable" fill="#ffffff" x="18" y="132" width="80" height="78" rx="10"/>
  <rect class="fillable" fill="#ffffff" x="12" y="118" width="92" height="18" rx="8"/>
  <rect class="fillable" fill="#ffffff" x="32" y="148" width="52" height="32" rx="8"/>
  <path fill="none" d="M98 200 L108 200"/>
  <circle class="fillable" fill="#ffffff" cx="40" cy="222" r="14"/>
  <circle fill="#1a1a1a" stroke="none" cx="40" cy="222" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="78" cy="222" r="14"/>
  <circle fill="#1a1a1a" stroke="none" cx="78" cy="222" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="312" cy="60" r="14"/>
  <circle class="fillable" fill="#ffffff" cx="338" cy="40" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="368" cy="26" r="13"/>
  <path class="fillable" fill="#ffffff" d="M282 132 L286 94 L274 78 L320 78 L308 94 L312 132 Z"/>
  <path class="fillable" fill="#ffffff" d="M222 134 Q222 106 240 106 Q258 106 258 134 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 208 L110 98 L188 98 L188 208 Z"/>
  <rect class="fillable" fill="#ffffff" x="98" y="84" width="102" height="18" rx="8"/>
  <rect class="fillable" fill="#ffffff" x="124" y="114" width="48" height="40" rx="8"/>
  <rect class="fillable" fill="#ffffff" x="180" y="128" width="136" height="78" rx="12"/>
  <path fill="none" d="M216 130 L216 204 M276 130 L276 204" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="318" cy="167" rx="14" ry="39"/>
  <path class="fillable" fill="#ffffff" d="M326 202 L360 232 L326 232 Z"/>
  <rect class="fillable" fill="#ffffff" x="102" y="200" width="230" height="20" rx="8"/>
  <circle class="fillable" fill="#ffffff" cx="150" cy="220" r="28"/>
  <circle class="fillable" fill="#ffffff" cx="150" cy="220" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="238" cy="226" r="20"/>
  <circle class="fillable" fill="#ffffff" cx="238" cy="226" r="7"/>
  <circle class="fillable" fill="#ffffff" cx="294" cy="226" r="20"/>
  <circle class="fillable" fill="#ffffff" cx="294" cy="226" r="7"/>
  <path fill="none" d="M150 220 L294 226" stroke-width="4"/>
</g>
''')

add('airplane', '✈️ 飞机', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M376.8 61.1 L384.2 64.2 M361.1 76.8 L364.2 84.2 M338.9 76.8 L335.8 84.2 M323.2 61.1 L315.8 64.2 M323.2 38.9 L315.8 35.8 M338.9 23.2 L335.8 15.8 M361.1 23.2 L364.2 15.8 M376.8 38.9 L384.2 35.8" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="350" cy="50" r="22"/>
  <path class="fillable" fill="#ffffff" d="M28.6 70.4 Q28.6 52.4 48.4 54.2 Q55.6 38 75.4 43.4 Q91.6 36.2 98.8 54.2 Q115 56 111.4 70.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M295.5 250 Q295.5 235 312 236.5 Q318 223 334.5 227.5 Q348 221.5 354 236.5 Q367.5 238 364.5 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 272 Q100 258 200 270 Q300 282 400 266 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M168 124 L218 124 L196 84 Q190 76 182 80 Z"/>
  <path class="fillable" fill="#ffffff" d="M70 140 L50 74 Q48 62 62 66 L112 120 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="76" cy="146" rx="30" ry="10" transform="rotate(-6 76 146)"/>
  <path class="fillable" fill="#ffffff" d="M58 152 Q58 120 112 118 L280 118 Q338 120 352 152 Q338 184 280 186 L112 186 Q66 184 58 152 Z"/>
  <path class="fillable" fill="#ffffff" d="M66 160 L346 160 Q342 168 336 172 L74 172 Q68 168 66 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M290 124 Q326 128 342 148 L292 148 Z"/>
  <circle class="fillable" fill="#ffffff" cx="140" cy="140" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="172" cy="140" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="204" cy="140" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="236" cy="140" r="10"/>
  <rect class="fillable" fill="#ffffff" x="256" y="128" width="20" height="40" rx="8"/>
  <path class="fillable" fill="#ffffff" d="M150 164 L218 164 L178 240 Q172 248 160 246 L146 242 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="362" cy="152" rx="7" ry="36"/>
  <circle class="fillable" fill="#ffffff" cx="354" cy="152" r="9"/>
</g>
''')

add('rocket', '🚀 太空火箭', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M20 80 A50 15 0 0 1 120 80 L104 80 A34 7 0 0 0 36 80 Z" transform="rotate(-18 70 80)"/>
  <circle class="fillable" fill="#ffffff" cx="70" cy="80" r="28"/>
  <path class="fillable" fill="#ffffff" d="M20 80 A50 15 0 0 0 120 80 L104 80 A34 7 0 0 1 36 80 Z" transform="rotate(-18 70 80)"/>
  <path class="fillable" fill="#ffffff" d="M350 34 A38 38 0 1 0 350 106 A40 40 0 0 1 350 34 Z"/>
  <path class="fillable" fill="#ffffff" d="M310 180 L314.1 190.3 L325.2 191.1 L316.7 198.2 L319.4 208.9 L310 203 L300.6 208.9 L303.3 198.2 L294.8 191.1 L305.9 190.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M80 172 L83.5 181.1 L93.3 181.7 L85.7 187.9 L88.2 197.3 L80 192 L71.8 197.3 L74.3 187.9 L66.7 181.7 L76.5 181.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 19 L132.9 26 L140.5 26.6 L134.8 31.5 L136.5 38.9 L130 35 L123.5 38.9 L125.2 31.5 L119.5 26.6 L127.1 26 Z"/>
  <path class="fillable" fill="#ffffff" d="M154 156 Q112 176 108 236 L156 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M246 156 Q288 176 292 236 L244 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 20 Q252 60 252 140 L252 214 L148 214 L148 140 Q148 60 200 20 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 20 Q236 46 246 88 Q200 98 154 88 Q164 46 200 20 Z"/>
  <path class="fillable" fill="#ffffff" d="M149 154 Q200 164 251 154 L252 172 Q200 182 148 172 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="124" r="24"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="124" r="15"/>
  <circle fill="#ffffff" stroke="none" cx="194" cy="117" r="4"/>
  <rect class="fillable" fill="#ffffff" x="192" y="186" width="16" height="52" rx="8"/>
  <rect class="fillable" fill="#ffffff" x="144" y="206" width="112" height="18" rx="8"/>
  <path class="fillable" fill="#ffffff" d="M176 236 Q162 258 182 268 Q184 282 200 288 Q216 282 218 268 Q238 258 224 236 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 236 Q182 254 200 272 Q218 254 212 236 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 222 L230 222 L222 240 L178 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M106 288 Q92 288 94 274 Q90 258 108 258 Q114 244 132 250 Q150 242 158 258 Q174 262 170 278 Q172 290 158 288 Z"/>
  <path class="fillable" fill="#ffffff" d="M294 288 Q308 288 306 274 Q310 258 292 258 Q286 244 268 250 Q250 242 242 258 Q226 262 230 278 Q228 290 242 288 Z"/>
</g>
''')

add('pirate', '🏴‍☠️ 海盗船', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M374.9 54.3 L382.3 57.4 M360.3 68.9 L363.4 76.3 M339.7 68.9 L336.6 76.3 M325.1 54.3 L317.7 57.4 M325.1 33.7 L317.7 30.6 M339.7 19.1 L336.6 11.7 M360.3 19.1 L363.4 11.7 M374.9 33.7 L382.3 30.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="350" cy="44" r="20"/>
  <path class="fillable" fill="#ffffff" d="M31.8 57.2 Q31.8 43.2 47.2 44.6 Q52.8 32 68.2 36.2 Q80.8 30.6 86.4 44.6 Q99 46 96.2 57.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 236 Q50 224 100 236 Q150 248 200 236 Q250 224 300 236 Q350 248 400 236 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="105" y="74" width="10" height="100" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="194" y="26" width="12" height="148" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="285" y="74" width="10" height="100" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M206 28 Q226 22 246 32 Q232 38 236 48 Q222 40 206 46 Z"/>
  <path class="fillable" fill="#ffffff" d="M80 88 Q110 96 140 88 Q148 118 140 150 Q110 142 80 150 Q72 118 80 88 Z"/>
  <path class="fillable" fill="#ffffff" d="M320 88 Q290 96 260 88 Q252 118 260 150 Q290 142 320 150 Q328 118 320 88 Z"/>
  <path class="fillable" fill="#ffffff" d="M148 54 Q200 66 252 54 Q264 102 252 152 Q200 140 148 152 Q136 102 148 54 Z"/>
  <path fill="none" d="M178 96 L222 128 M222 96 L178 128" stroke-width="6"/>
  <path class="fillable" fill="#ffffff" d="M184 112 Q184 80 200 80 Q216 80 216 112 L210 112 L210 120 L190 120 L190 112 Z"/>
  <circle fill="#1a1a1a" stroke="none" cx="193" cy="99" r="5"/>
  <circle fill="#1a1a1a" stroke="none" cx="207" cy="99" r="5"/>
  <path class="fillable" fill="#ffffff" d="M40 164 L360 164 L352 182 L48 182 Z"/>
  <path class="fillable" fill="#ffffff" d="M48 180 L352 180 Q344 236 296 248 L104 248 Q56 236 48 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M64 216 Q200 226 336 216 L328 230 Q200 240 72 230 Z"/>
  <circle class="fillable" fill="#ffffff" cx="130" cy="198" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="198" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="270" cy="198" r="11"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q25 244 50 256 Q75 268 100 256 Q125 244 150 256 Q175 268 200 256 Q225 244 250 256 Q275 268 300 256 Q325 244 350 256 Q375 268 400 256 L400 300 L0 300 Z"/>
</g>
''')

add('fire_truck', '🚒 消防车', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M80.9 56.3 L88.3 59.4 M66.3 70.9 L69.4 78.3 M45.7 70.9 L42.6 78.3 M31.1 56.3 L23.7 59.4 M31.1 35.7 L23.7 32.6 M45.7 21.1 L42.6 13.7 M66.3 21.1 L69.4 13.7 M80.9 35.7 L88.3 32.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="56" cy="46" r="20"/>
  <path class="fillable" fill="#ffffff" d="M295.5 58 Q295.5 43 312 44.5 Q318 31 334.5 35.5 Q348 29.5 354 44.5 Q367.5 46 364.5 58 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 230 200 246 Q300 262 400 240 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="120" y="106" width="30" height="22" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="40" y="88" width="216" height="22" rx="8"/>
  <path fill="none" d="M64 90 L64 108 M88 90 L88 108 M112 90 L112 108 M136 90 L136 108 M160 90 L160 108 M184 90 L184 108 M208 90 L208 108 M232 90 L232 108" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M284 112 Q284 90 300 90 Q316 90 316 112 Z"/>
  <rect class="fillable" fill="#ffffff" x="36" y="120" width="222" height="104" rx="12"/>
  <path class="fillable" fill="#ffffff" d="M250 224 L250 120 Q250 110 260 110 L306 110 Q330 112 342 150 L358 160 Q364 164 364 172 L364 224 Z"/>
  <path class="fillable" fill="#ffffff" d="M264 124 L302 124 Q320 126 328 156 L264 156 Z"/>
  <path fill="none" d="M270 168 L290 168" stroke-width="4"/>
  <rect class="fillable" fill="#ffffff" x="52" y="136" width="84" height="58" rx="10"/>
  <rect class="fillable" fill="#ffffff" x="150" y="136" width="92" height="58" rx="10"/>
  <circle class="fillable" fill="#ffffff" cx="94" cy="165" r="18"/>
  <circle class="fillable" fill="#ffffff" cx="94" cy="165" r="6"/>
  <path class="fillable" fill="#ffffff" d="M38 198 L362 198 L362 212 L38 212 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="356" cy="180" rx="6" ry="10"/>
  <rect class="fillable" fill="#ffffff" x="340" y="212" width="40" height="16" rx="8"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="228" r="30"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="228" r="12"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="228" r="30"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="228" r="12"/>
</g>
''')

add('balloon', '🎈 热气球', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M372.8 59.1 L380.2 62.2 M357.1 74.8 L360.2 82.2 M334.9 74.8 L331.8 82.2 M319.2 59.1 L311.8 62.2 M319.2 36.9 L311.8 33.8 M334.9 21.2 L331.8 13.8 M357.1 21.2 L360.2 13.8 M372.8 36.9 L380.2 33.8" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="346" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M24.6 84.4 Q24.6 66.4 44.4 68.2 Q51.6 52 71.4 57.4 Q87.6 50.2 94.8 68.2 Q111 70 107.4 84.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M303.5 198 Q303.5 183 320 184.5 Q326 171 342.5 175.5 Q356 169.5 362 184.5 Q375.5 186 372.5 198 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q90 244 170 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M400 254 Q310 244 230 300 L400 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 22 C110 22 90 128 170 200 L182 200 C134 128 146 22 200 22 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 22 C146 22 134 128 182 200 L194 200 C178 128 182 22 200 22 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 22 C182 22 178 128 194 200 L206 200 C222 128 218 22 200 22 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 22 C218 22 222 128 206 200 L218 200 C266 128 254 22 200 22 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 22 C254 22 266 128 218 200 L230 200 C310 128 290 22 200 22 Z"/>
  <path fill="none" d="M174 214 L168 236 M226 214 L232 236 M192 214 L190 236 M208 214 L210 236" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M168 198 L232 198 L226 216 L174 216 Z"/>
  <path class="fillable" fill="#ffffff" d="M162 240 L238 240 L232 280 L168 280 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 256 L236 256 L234 266 L166 266 Z"/>
  <rect class="fillable" fill="#ffffff" x="156" y="232" width="88" height="12" rx="6"/>
  <path fill="none" d="M244 240 L250 250" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="252" cy="258" rx="8" ry="10"/>
  <path fill="none" d="M156 240 L150 250" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="148" cy="258" rx="8" ry="10"/>
</g>
''')

# --- Nature (7) ---
add('garden', '🌻 花园', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M376.9 50.3 L384.3 53.4 M362.3 64.9 L365.4 72.3 M341.7 64.9 L338.6 72.3 M327.1 50.3 L319.7 53.4 M327.1 29.7 L319.7 26.6 M341.7 15.1 L338.6 7.7 M362.3 15.1 L365.4 7.7 M376.9 29.7 L384.3 26.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="352" cy="40" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 238 Q100 226 200 236 Q300 246 400 232 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="12" y="150" width="376" height="16" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="12" y="196" width="376" height="16" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M20 242 L20 132 Q35 112 50 132 L50 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 242 L60 132 Q75 112 90 132 L90 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M100 242 L100 132 Q115 112 130 132 L130 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 242 L140 132 Q155 112 170 132 L170 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 242 L180 132 Q195 112 210 132 L210 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M220 242 L220 132 Q235 112 250 132 L250 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M260 242 L260 132 Q275 112 290 132 L290 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 242 L300 132 Q315 112 330 132 L330 242 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 242 L340 132 Q355 112 370 132 L370 242 Z"/>
  <rect class="fillable" fill="#ffffff" x="91" y="124" width="10" height="144" rx="5"/>
  <path class="fillable" fill="#ffffff" d="M91 230 Q56 196 34 210 Q56 238 91 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M96 86.3 A20.3 20.3 0 0 1 125.5 100.5 A20.3 20.3 0 0 1 132.8 132.4 A20.3 20.3 0 0 1 112.4 158 A20.3 20.3 0 0 1 79.6 158 A20.3 20.3 0 0 1 59.2 132.4 A20.3 20.3 0 0 1 66.5 100.5 A20.3 20.3 0 0 1 96 86.3 Z"/>
  <circle class="fillable" fill="#ffffff" cx="96" cy="124" r="19.3"/>
  <rect class="fillable" fill="#ffffff" x="195" y="92" width="10" height="176" rx="5"/>
  <path class="fillable" fill="#ffffff" d="M205 204 Q240 170 262 184 Q240 212 205 204 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 214 Q160 180 138 194 Q160 222 195 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 49.4 A26.4 26.4 0 0 1 236.9 70.7 A26.4 26.4 0 0 1 236.9 113.3 A26.4 26.4 0 0 1 200 134.6 A26.4 26.4 0 0 1 163.1 113.3 A26.4 26.4 0 0 1 163.1 70.7 A26.4 26.4 0 0 1 200 49.4 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="92" r="21.8"/>
  <rect class="fillable" fill="#ffffff" x="299" y="126" width="10" height="142" rx="5"/>
  <path class="fillable" fill="#ffffff" d="M309 232 Q344 198 366 212 Q344 240 309 232 Z"/>
  <path class="fillable" fill="#ffffff" d="M304 88.3 A27.5 27.5 0 0 1 339.9 114.3 A27.5 27.5 0 0 1 326.2 156.5 A27.5 27.5 0 0 1 281.8 156.5 A27.5 27.5 0 0 1 268.1 114.3 A27.5 27.5 0 0 1 304 88.3 Z"/>
  <circle class="fillable" fill="#ffffff" cx="304" cy="126" r="19.3"/>
  <ellipse class="fillable" fill="#ffffff" cx="191" cy="87" rx="5" ry="6"/>
  <circle fill="#1a1a1a" stroke="none" cx="191.5" cy="87.5" r="3.5"/>
  <circle fill="#ffffff" stroke="none" cx="192.9" cy="85.9" r="1.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="209" cy="87" rx="5" ry="6"/>
  <circle fill="#1a1a1a" stroke="none" cx="209.5" cy="87.5" r="3.5"/>
  <circle fill="#ffffff" stroke="none" cx="210.9" cy="85.9" r="1.5"/>
  <path fill="none" d="M193 100 Q200 107 207 100" stroke-width="3"/>
</g>
''')

add('tree', '🌳 苹果树', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M380.9 50.3 L388.3 53.4 M366.3 64.9 L369.4 72.3 M345.7 64.9 L342.6 72.3 M331.1 50.3 L323.7 53.4 M331.1 29.7 L323.7 26.6 M345.7 15.1 L342.6 7.7 M366.3 15.1 L369.4 7.7 M380.9 29.7 L388.3 26.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="356" cy="40" r="20"/>
  <path class="fillable" fill="#ffffff" d="M22.1 50.4 Q22.1 37.4 36.4 38.7 Q41.6 27 55.9 30.9 Q67.6 25.7 72.8 38.7 Q84.5 40 81.9 50.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 230 200 246 Q300 262 400 240 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M166 256 Q182 232 182 170 L218 170 Q218 232 234 256 Q200 264 166 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 162 Q238 140 252 120 L262 128 Q248 152 218 176 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 24 A36.9 36.9 0 0 1 259 31.7 A32.3 32.3 0 0 1 306.3 53.4 A25.3 25.3 0 0 1 332.6 84.6 A21.5 21.5 0 0 1 332.6 119.4 A25.3 25.3 0 0 1 306.3 150.6 A32.3 32.3 0 0 1 259 172.3 A36.9 36.9 0 0 1 200 180 A36.9 36.9 0 0 1 141 172.3 A32.3 32.3 0 0 1 93.7 150.6 A25.3 25.3 0 0 1 67.4 119.4 A21.5 21.5 0 0 1 67.4 84.6 A25.3 25.3 0 0 1 93.7 53.4 A32.3 32.3 0 0 1 141 31.7 A36.9 36.9 0 0 1 200 24 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="214" rx="7" ry="11"/>
  <path fill="none" d="M118 83.6 Q119 78 122 75.2" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M118 82.9 Q130.6 74.5 132 93.4 Q129.9 107.4 118 104.6 Q106.1 107.4 104 93.4 Q105.4 74.5 118 82.9 Z"/>
  <path fill="none" d="M166 47.6 Q167 42 170 39.2" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M166 46.9 Q178.6 38.5 180 57.4 Q177.9 71.4 166 68.6 Q154.1 71.4 152 57.4 Q153.4 38.5 166 46.9 Z"/>
  <path fill="none" d="M236 49.6 Q237 44 240 41.2" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M236 48.9 Q248.6 40.5 250 59.4 Q247.9 73.4 236 70.6 Q224.1 73.4 222 59.4 Q223.4 40.5 236 48.9 Z"/>
  <path fill="none" d="M288 89.6 Q289 84 292 81.2" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M288 88.9 Q300.6 80.5 302 99.4 Q299.9 113.4 288 110.6 Q276.1 113.4 274 99.4 Q275.4 80.5 288 88.9 Z"/>
  <path fill="none" d="M146 131.6 Q147 126 150 123.2" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M146 130.9 Q158.6 122.5 160 141.4 Q157.9 155.4 146 152.6 Q134.1 155.4 132 141.4 Q133.4 122.5 146 130.9 Z"/>
  <path fill="none" d="M214 109.6 Q215 104 218 101.2" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M214 108.9 Q226.6 100.5 228 119.4 Q225.9 133.4 214 130.6 Q202.1 133.4 200 119.4 Q201.4 100.5 214 108.9 Z"/>
  <path fill="none" d="M262 141.6 Q263 136 266 133.2" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M262 140.9 Q274.6 132.5 276 151.4 Q273.9 165.4 262 162.6 Q250.1 165.4 248 151.4 Q249.4 132.5 262 140.9 Z"/>
  <path fill="none" d="M186 159.6 Q187 154 190 151.2" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M186 158.9 Q198.6 150.5 200 169.4 Q197.9 183.4 186 180.6 Q174.1 183.4 172 169.4 Q173.4 150.5 186 158.9 Z"/>
  <path fill="none" d="M130 248.2 Q131 243 134 240.4" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M130 247.6 Q141.7 239.8 143 257.3 Q141.1 270.3 130 267.7 Q119 270.3 117 257.3 Q118.3 239.8 130 247.6 Z"/>
  <path fill="none" d="M300 208.2 Q301 203 304 200.4" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M300 207.6 Q311.7 199.8 313 217.3 Q311.1 230.3 300 227.7 Q288.9 230.3 287 217.3 Q288.3 199.8 300 207.6 Z"/>
  <path fill="none" d="M326 206.2 Q327 201 330 198.4" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M326 205.6 Q337.7 197.8 339 215.3 Q337.1 228.3 326 225.7 Q314.9 228.3 313 215.3 Q314.3 197.8 326 205.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M278 222 L350 222 L342 262 Q314 270 286 262 Z"/>
  <path fill="none" d="M284 238 Q314 244 346 238" stroke-width="3"/>
</g>
''')

add('rainbow', '🌈 彩虹', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M378.8 55.1 L386.2 58.2 M363.1 70.8 L366.2 78.2 M340.9 70.8 L337.8 78.2 M325.2 55.1 L317.8 58.2 M325.2 32.9 L317.8 29.8 M340.9 17.2 L337.8 9.8 M363.1 17.2 L366.2 9.8 M378.8 32.9 L386.2 29.8" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="352" cy="44" r="22"/>
  <path class="fillable" fill="#ffffff" d="M31.5 56 Q31.5 41 48 42.5 Q54 29 70.5 33.5 Q84 27.5 90 42.5 Q103.5 44 100.5 56 Z"/>
  <path class="fillable" fill="#ffffff" d="M227 38 Q227 28 238 29 Q242 20 253 23 Q262 19 266 29 Q275 30 273 38 Z"/>
  <path class="fillable" fill="#ffffff" d="M400 248 Q290 236 150 300 L400 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 252 Q110 238 250 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M22 238 A178 178 0 0 1 378 238 L360 238 A160 160 0 0 0 40 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M40 238 A160 160 0 0 1 360 238 L342 238 A142 142 0 0 0 58 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M58 238 A142 142 0 0 1 342 238 L324 238 A124 124 0 0 0 76 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M76 238 A124 124 0 0 1 324 238 L306 238 A106 106 0 0 0 94 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M94 238 A106 106 0 0 1 306 238 L288 238 A88 88 0 0 0 112 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M112 238 A88 88 0 0 1 288 238 L270 238 A70 70 0 0 0 130 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M14 236 Q8 214 30 210 Q30 186 58 190 Q72 172 96 186 Q120 184 120 208 Q134 220 124 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M22 266 Q4 262 12 244 Q12 226 36 230 Q50 214 72 226 Q92 216 106 232 Q130 230 132 250 Q140 268 120 268 Z"/>
  <path class="fillable" fill="#ffffff" d="M386 236 Q392 214 370 210 Q370 186 342 190 Q328 172 304 186 Q280 184 280 208 Q266 220 276 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M378 266 Q396 262 388 244 Q388 226 364 230 Q350 214 328 226 Q308 216 294 232 Q270 230 268 250 Q260 268 280 268 Z"/>
</g>
''')

add('beach', '🏖️ 海滩', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M376.9 52.3 L384.3 55.4 M362.3 66.9 L365.4 74.3 M341.7 66.9 L338.6 74.3 M327.1 52.3 L319.7 55.4 M327.1 31.7 L319.7 28.6 M341.7 17.1 L338.6 9.7 M362.3 17.1 L365.4 9.7 M376.9 31.7 L384.3 28.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="352" cy="42" r="20"/>
  <path class="fillable" fill="#ffffff" d="M217.8 57.2 Q217.8 43.2 233.2 44.6 Q238.8 32 254.2 36.2 Q266.8 30.6 272.4 44.6 Q285 46 282.2 57.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 160 Q50 152 100 160 Q150 168 200 160 Q250 152 300 160 Q350 168 400 160 L400 216 L0 216 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 206 Q100 194 200 206 Q300 218 400 200 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="104" y="104" width="10" height="156" rx="5" transform="rotate(-6 109 104)"/>
  <path class="fillable" fill="#ffffff" d="M110 24 Q26 28 26 112 Q47 126 68 112 Q68 28 110 24 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 24 Q68 28 68 112 Q89 126 110 112 Q110 28 110 24 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 24 Q110 28 110 112 Q131 126 152 112 Q152 28 110 24 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 24 Q152 28 152 112 Q173 126 194 112 Q194 28 110 24 Z"/>
  <circle class="fillable" fill="#ffffff" cx="110" cy="20" r="6"/>
  <path class="fillable" fill="#ffffff" d="M252 250 L252 196 L262 196 L262 186 L276 186 L276 196 L288 196 L288 186 L302 186 L302 196 L314 196 L314 186 L328 186 L328 196 L338 196 L338 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M232 252 L232 172 L236 172 L236 162 L246 162 L246 172 L254 172 L254 162 L264 162 L264 172 L268 172 L268 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 252 L330 172 L334 172 L334 162 L344 162 L344 172 L352 172 L352 162 L362 162 L362 172 L366 172 L366 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M282 250 L282 230 Q282 216 295 216 Q308 216 308 230 L308 250 Z"/>
  <path fill="none" d="M295 186 L295 150" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M295 150 L318 157 L295 164 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 220 A26 26 0 0 0 180 272 Q166 246 180 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 220 Q166 246 180 272 Q194 246 180 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 220 A26 26 0 0 1 180 272 Q194 246 180 220 Z"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="229" r="5"/>
  <path class="fillable" fill="#ffffff" d="M65.5 242.3 L69.2 255.1 L81.8 259.2 L70.8 266.7 L70.8 280 L60.3 271.8 L47.6 275.9 L52.1 263.4 L44.3 252.6 L57.6 253 Z"/>
</g>
''')

add('mountain', '🏔️ 雪山湖泊', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M80.9 56.3 L88.3 59.4 M66.3 70.9 L69.4 78.3 M45.7 70.9 L42.6 78.3 M31.1 56.3 L23.7 59.4 M31.1 35.7 L23.7 32.6 M45.7 21.1 L42.6 13.7 M66.3 21.1 L69.4 13.7 M80.9 35.7 L88.3 32.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="56" cy="46" r="20"/>
  <path class="fillable" fill="#ffffff" d="M307.8 51.2 Q307.8 37.2 323.2 38.6 Q328.8 26 344.2 30.2 Q356.8 24.6 362.4 38.6 Q375 40 372.2 51.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M8 200 L90 96 Q104 80 118 96 L210 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M67 126 L90 96 Q104 80 118 96 L144 126 Q132 136 120 126 Q106 140 94 126 Q80 136 67 126 Z"/>
  <path class="fillable" fill="#ffffff" d="M190 200 L292 86 Q306 70 320 86 L392 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M265 116 L292 86 Q306 70 320 86 L339 116 Q326 126 314 116 Q300 130 288 116 Q276 126 265 116 Z"/>
  <path class="fillable" fill="#ffffff" d="M88 204 L180 54 Q200 30 220 54 L316 204 Z"/>
  <path class="fillable" fill="#ffffff" d="M152 100 L180 54 Q200 30 220 54 L249 100 Q236 112 224 100 Q212 116 200 104 Q188 116 176 100 Q164 112 152 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 198 Q100 188 200 196 Q300 204 400 192 L400 300 L0 300 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="248" rx="142" ry="32"/>
  <path fill="none" d="M130 244 L160 244 M226 258 L262 258 M120 262 L144 262" stroke-width="3"/>
  <path fill="none" d="M206 236 L206 204" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M206 206 L230 232 L206 232 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 236 L232 236 L224 250 L188 250 Z"/>
  <rect class="fillable" fill="#ffffff" x="30" y="240" width="12" height="24" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M36 154 L54 182 L46 182 L62 210 L52 210 L68 242 L4 242 L20 210 L10 210 L26 182 L18 182 Z"/>
  <rect class="fillable" fill="#ffffff" x="360" y="240" width="12" height="24" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M366 154 L384 182 L376 182 L392 210 L382 210 L398 242 L334 242 L350 210 L340 210 L356 182 L348 182 Z"/>
</g>
''')

add('snowman', '⛄ 雪人', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M376.9 52.3 L384.3 55.4 M362.3 66.9 L365.4 74.3 M341.7 66.9 L338.6 74.3 M327.1 52.3 L319.7 55.4 M327.1 31.7 L319.7 28.6 M341.7 17.1 L338.6 9.7 M362.3 17.1 L365.4 9.7 M376.9 31.7 L384.3 28.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="352" cy="42" r="20"/>
  <path class="fillable" fill="#ffffff" d="M25.5 58 Q25.5 43 42 44.5 Q48 31 64.5 35.5 Q78 29.5 84 44.5 Q97.5 46 94.5 58 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 244 Q100 230 200 240 Q300 250 400 236 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="334" y="236" width="14" height="24" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M341 120 L362 156 L352 156 L372 192 L360 192 L380 238 L302 238 L322 192 L310 192 L330 156 L320 156 Z"/>
  <path class="fillable" fill="#ffffff" d="M146 178 L96 146 L84 132 L92 128 L102 140 L150 168 Z"/>
  <path class="fillable" fill="#ffffff" d="M254 178 L304 146 L316 132 L308 128 L298 140 L250 168 Z"/>
  <circle class="fillable" fill="#ffffff" cx="88" cy="132" r="12"/>
  <circle class="fillable" fill="#ffffff" cx="312" cy="132" r="12"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="202" r="62"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="180" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="208" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="236" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="106" r="46"/>
  <path class="fillable" fill="#ffffff" d="M218 150 L242 150 L250 202 Q238 210 226 204 Z"/>
  <path fill="none" d="M232 202 L232 210 M242 200 L244 208" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M154 136 Q200 160 246 136 L250 152 Q200 178 150 152 Z"/>
  <rect class="fillable" fill="#ffffff" x="172" y="20" width="56" height="52" rx="6"/>
  <rect class="fillable" fill="#ffffff" x="172" y="48" width="56" height="12" rx="0"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="70" rx="46" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="184" cy="100" rx="8" ry="10"/>
  <circle fill="#1a1a1a" stroke="none" cx="185" cy="101" r="5.5"/>
  <circle fill="#ffffff" stroke="none" cx="187.2" cy="98.5" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="216" cy="100" rx="8" ry="10"/>
  <circle fill="#1a1a1a" stroke="none" cx="217" cy="101" r="5.5"/>
  <circle fill="#ffffff" stroke="none" cx="219.2" cy="98.5" r="2.1"/>
  <path class="fillable" fill="#ffffff" d="M200 110 L230 119 L200 126 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="166" cy="126" rx="7" ry="4.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="234" cy="126" rx="7" ry="4.5"/>
  <path fill="none" d="M188 132 Q198 140 208 132" stroke-width="3"/>
</g>
''')

add('butterfly_meadow', '🦋 蝴蝶草地', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M380.9 50.3 L388.3 53.4 M366.3 64.9 L369.4 72.3 M345.7 64.9 L342.6 72.3 M331.1 50.3 L323.7 53.4 M331.1 29.7 L323.7 26.6 M345.7 15.1 L342.6 7.7 M366.3 15.1 L369.4 7.7 M380.9 29.7 L388.3 26.6" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="356" cy="40" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 226 200 236 Q300 246 400 230 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="42" y="226" width="8" height="40" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M50 252 Q76 220 86 226 Q80 252 50 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M28 200 L37 210 L46 196 L55 210 L64 200 Q68 232 46 234 Q24 232 28 200 Z"/>
  <rect class="fillable" fill="#ffffff" x="350" y="220" width="8" height="42" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M358 248 Q384 216 394 222 Q388 248 358 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M336 194 L345 204 L354 190 L363 204 L372 194 Q376 226 354 228 Q332 226 336 194 Z"/>
  <rect class="fillable" fill="#ffffff" x="92" y="252" width="8" height="32" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M100 270 Q126 238 136 244 Q130 270 100 278 Z"/>
  <path class="fillable" fill="#ffffff" d="M78 226 L87 236 L96 222 L105 236 L114 226 Q118 258 96 260 Q74 258 78 226 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 112 Q160 30 104 42 Q66 56 86 104 Q110 140 196 128 Z"/>
  <path class="fillable" fill="#ffffff" d="M204 112 Q240 30 296 42 Q334 56 314 104 Q290 140 204 128 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 130 Q132 132 112 172 Q108 204 142 200 Q184 190 198 146 Z"/>
  <path class="fillable" fill="#ffffff" d="M204 130 Q268 132 288 172 Q292 204 258 200 Q216 190 202 146 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="134" cy="88" rx="22" ry="18" transform="rotate(-20 134 88)"/>
  <ellipse class="fillable" fill="#ffffff" cx="266" cy="88" rx="22" ry="18" transform="rotate(20 266 88)"/>
  <circle class="fillable" fill="#ffffff" cx="150" cy="170" r="13"/>
  <circle class="fillable" fill="#ffffff" cx="250" cy="170" r="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="150" rx="13" ry="46"/>
  <path fill="none" d="M188 140 Q200 146 212 140 M188 162 Q200 168 212 162" stroke-width="3"/>
  <path fill="none" d="M193 82 Q184 54 168 46 M207 82 Q216 54 232 46" stroke-width="3"/>
  <circle fill="#1a1a1a" stroke="none" cx="167" cy="45" r="6"/>
  <circle fill="#1a1a1a" stroke="none" cx="233" cy="45" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="96" r="22"/>
  <ellipse class="fillable" fill="#ffffff" cx="192" cy="94" rx="5" ry="6"/>
  <circle fill="#1a1a1a" stroke="none" cx="192.6" cy="94.6" r="3.6"/>
  <circle fill="#ffffff" stroke="none" cx="194" cy="93" r="1.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="208" cy="94" rx="5" ry="6"/>
  <circle fill="#1a1a1a" stroke="none" cx="208.6" cy="94.6" r="3.6"/>
  <circle fill="#ffffff" stroke="none" cx="210" cy="93" r="1.5"/>
  <path fill="none" d="M195 105 Q200 110 205 105" stroke-width="2.5"/>
</g>
''')

# --- Food (6) ---
add('cake', '🎂 生日蛋糕', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path fill="none" d="M44 118 Q50 160 40 200" stroke-width="3"/>
  <path fill="none" d="M356 112 Q350 150 360 190" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M44 118 Q14 104 16 70 Q20 38 44 38 Q68 38 72 70 Q74 104 44 118 Z"/>
  <path class="fillable" fill="#ffffff" d="M356 112 Q326 98 328 64 Q332 32 356 32 Q380 32 384 64 Q386 98 356 112 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 264 L400 264 L400 300 L0 300 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="256" rx="150" ry="16"/>
  <path class="fillable" fill="#ffffff" d="M72 180 L72 244 Q200 262 328 244 L328 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M66 192 L66 180 Q66 174 72 174 L328 174 Q334 174 334 180 L334 192 Q330.6 215.4 317.2 210 Q303.9 215.4 300.5 192 Q297.1 202.4 283.8 200 Q270.4 202.4 267 192 Q263.6 215.4 250.2 210 Q236.8 215.4 233.5 192 Q230.2 202.4 216.8 200 Q203.3 202.4 200 192 Q196.7 215.4 183.2 210 Q169.8 215.4 166.5 192 Q163.2 202.4 149.8 200 Q136.3 202.4 133 192 Q129.7 215.4 116.2 210 Q102.8 215.4 99.5 192 Q96.2 202.4 82.8 200 Q69.3 202.4 66 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M110 120 L110 172 Q200 184 290 172 L290 120 Z"/>
  <path class="fillable" fill="#ffffff" d="M104 128 L104 118 Q104 112 110 112 L290 112 Q296 112 296 118 L296 128 Q292.8 151.4 280 146 Q267.2 151.4 264 128 Q260.8 138.4 248 136 Q235.2 138.4 232 128 Q228.8 151.4 216 146 Q203.2 151.4 200 128 Q196.8 138.4 184 136 Q171.2 138.4 168 128 Q164.8 151.4 152 146 Q139.2 151.4 136 128 Q132.8 138.4 120 136 Q107.2 138.4 104 128 Z"/>
  <rect class="fillable" fill="#ffffff" x="148" y="72" width="16" height="42" rx="4"/>
  <path fill="none" d="M148 86 L164 80 M148 100 L164 94" stroke-width="2.5"/>
  <path class="fillable" fill="#ffffff" d="M156 40 Q168 56 164 62 Q156 70 148 62 Q144 56 156 40 Z"/>
  <rect class="fillable" fill="#ffffff" x="192" y="72" width="16" height="42" rx="4"/>
  <path fill="none" d="M192 86 L208 80 M192 100 L208 94" stroke-width="2.5"/>
  <path class="fillable" fill="#ffffff" d="M200 40 Q212 56 208 62 Q200 70 192 62 Q188 56 200 40 Z"/>
  <rect class="fillable" fill="#ffffff" x="236" y="72" width="16" height="42" rx="4"/>
  <path fill="none" d="M236 86 L252 80 M236 100 L252 94" stroke-width="2.5"/>
  <path class="fillable" fill="#ffffff" d="M244 40 Q256 56 252 62 Q244 70 236 62 Q232 56 244 40 Z"/>
  <path class="fillable" fill="#ffffff" d="M104 235 Q87.1 223.3 92.3 215.5 Q98.8 209 104 217.4 Q109.2 209 115.7 215.5 Q120.9 223.3 104 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M296 235 Q279.1 223.3 284.3 215.5 Q290.8 209 296 217.4 Q301.2 209 307.7 215.5 Q312.9 223.3 296 235 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="216" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="217" r="5"/>
  <circle fill="#ffffff" stroke="none" cx="183" cy="214.8" r="1.9"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="216" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="217" r="5"/>
  <circle fill="#ffffff" stroke="none" cx="223" cy="214.8" r="1.9"/>
  <ellipse class="fillable" fill="#ffffff" cx="162" cy="232" rx="7" ry="4.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="238" cy="232" rx="7" ry="4.5"/>
  <path fill="none" d="M191 232 Q200 241 209 232" stroke-width="3"/>
</g>
''')

add('icecream', '🍨 冰淇淋圣代', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 266 Q200 256 400 266 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 88 Q36.6 71.8 43.8 61 Q52.8 52 60 63.7 Q67.2 52 76.2 61 Q83.4 71.8 60 88 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 106 Q319.2 91.6 325.6 82 Q333.6 74 340 84.4 Q346.4 74 354.4 82 Q360.8 91.6 340 106 Z"/>
  <rect class="fillable" fill="#ffffff" x="250" y="34" width="18" height="74" rx="4" transform="rotate(22 259 71)"/>
  <path fill="none" d="M250 50 L274 60 M244 66 L268 76 M238 82 L262 92" stroke-width="2.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="258" rx="62" ry="12"/>
  <rect class="fillable" fill="#ffffff" x="188" y="222" width="24" height="36" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M108 162 L292 162 Q288 222 222 230 L178 230 Q112 222 108 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M113 186 L287 186 Q284 196 280 202 L120 202 Q116 196 113 186 Z"/>
  <rect class="fillable" fill="#ffffff" x="98" y="150" width="204" height="18" rx="9"/>
  <path class="fillable" fill="#ffffff" d="M112 139.4 A44 50.6 0 1 1 200 139.4 Q189 153.4 178 143.4 Q167 153.4 156 143.4 Q145 153.4 134 143.4 Q123 153.4 112 139.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 139.4 A44 50.6 0 1 1 288 139.4 Q277 153.4 266 143.4 Q255 153.4 244 143.4 Q233 153.4 222 143.4 Q211 153.4 200 139.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M156 109.4 A44 50.6 0 1 1 244 109.4 Q233 123.4 222 113.4 Q211 123.4 200 113.4 Q189 123.4 178 113.4 Q167 123.4 156 109.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M168 66 Q158 48 180 44 Q184 28 200 30 Q216 28 220 44 Q242 48 232 66 Q200 74 168 66 Z"/>
  <path fill="none" d="M208 26 Q212 16 222 12" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="208" cy="32" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="183" cy="92" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="184" cy="93" r="5"/>
  <circle fill="#ffffff" stroke="none" cx="186" cy="90.8" r="1.9"/>
  <ellipse class="fillable" fill="#ffffff" cx="217" cy="92" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="218" cy="93" r="5"/>
  <circle fill="#ffffff" stroke="none" cx="220" cy="90.8" r="1.9"/>
  <ellipse class="fillable" fill="#ffffff" cx="167" cy="106" rx="7" ry="4.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="233" cy="106" rx="7" ry="4.5"/>
  <path fill="none" d="M193 104 Q200 111 207 104" stroke-width="3"/>
</g>
''')

add('pizza', '🍕 披萨', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M323.5 87.8 A124 124 0 0 1 323.5 204.2 L305.8 194.8 A104 104 0 0 0 305.8 97.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M214 146 L305.8 97.2 A104 104 0 0 1 305.8 194.8 Z"/>
  <circle class="fillable" fill="#ffffff" cx="284" cy="146" r="14"/>
  <path class="fillable" fill="#ffffff" d="M240.9 155.2 Q240.9 144.2 250.9 144.2 Q260.9 144.2 260.9 155.2 L254.9 155.2 L254.9 163.2 L246.9 163.2 L246.9 155.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M301.2 211.7 A124 124 0 0 1 200.3 269.9 L199.6 249.9 A104 104 0 0 0 284.2 201.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 146 L284.2 201.1 A104 104 0 0 1 199.6 249.9 Z"/>
  <circle class="fillable" fill="#ffffff" cx="231" cy="206.6" r="14"/>
  <path class="fillable" fill="#ffffff" d="M196.5 182.5 Q196.5 171.5 206.5 171.5 Q216.5 171.5 216.5 182.5 L210.5 182.5 L210.5 190.5 L202.5 190.5 L202.5 182.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M191.7 269.9 A124 124 0 0 1 90.8 211.7 L107.8 201.1 A104 104 0 0 0 192.4 249.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 146 L192.4 249.9 A104 104 0 0 1 107.8 201.1 Z"/>
  <circle class="fillable" fill="#ffffff" cx="161" cy="206.6" r="14"/>
  <path class="fillable" fill="#ffffff" d="M159.6 173.3 Q159.6 162.3 169.6 162.3 Q179.6 162.3 179.6 173.3 L173.6 173.3 L173.6 181.3 L165.6 181.3 L165.6 173.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M86.5 204.2 A124 124 0 0 1 86.5 87.8 L104.2 97.2 A104 104 0 0 0 104.2 194.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 146 L104.2 194.8 A104 104 0 0 1 104.2 97.2 Z"/>
  <circle class="fillable" fill="#ffffff" cx="126" cy="146" r="14"/>
  <path class="fillable" fill="#ffffff" d="M149.1 136.8 Q149.1 125.8 159.1 125.8 Q169.1 125.8 169.1 136.8 L163.1 136.8 L163.1 144.8 L155.1 144.8 L155.1 136.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M90.8 80.3 A124 124 0 0 1 191.7 22.1 L192.4 42.1 A104 104 0 0 0 107.8 90.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 146 L107.8 90.9 A104 104 0 0 1 192.4 42.1 Z"/>
  <circle class="fillable" fill="#ffffff" cx="161" cy="85.4" r="14"/>
  <path class="fillable" fill="#ffffff" d="M175.5 109.5 Q175.5 98.5 185.5 98.5 Q195.5 98.5 195.5 109.5 L189.5 109.5 L189.5 117.5 L181.5 117.5 L181.5 109.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M200.3 22.1 A124 124 0 0 1 301.2 80.3 L284.2 90.9 A104 104 0 0 0 199.6 42.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 146 L199.6 42.1 A104 104 0 0 1 284.2 90.9 Z"/>
  <circle class="fillable" fill="#ffffff" cx="231" cy="85.4" r="14"/>
  <path class="fillable" fill="#ffffff" d="M212.4 118.7 Q212.4 107.7 222.4 107.7 Q232.4 107.7 232.4 118.7 L226.4 118.7 L226.4 126.7 L218.4 126.7 L218.4 118.7 Z"/>
</g>
''')

add('fruit', '🍎 水果盘', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 262 Q100 252 200 258 Q300 264 400 254 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M282 70 Q296 60 308 72 Q296 84 282 70 Z"/>
  <path fill="none" d="M282 96 Q280 78 294 66"/>
  <circle class="fillable" fill="#ffffff" cx="266" cy="112" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="112" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="250" cy="140" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="284" cy="140" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="318" cy="140" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="266" cy="166" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="166" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="124" cy="150" r="36"/>
  <path class="fillable" fill="#ffffff" d="M124 116 Q134 98 154 102 Q146 120 124 116 Z"/>
  <path fill="none" d="M108 134 Q112 126 120 126"/>
  <path class="fillable" fill="#ffffff" d="M196 112 Q174 96 156 110 Q140 128 148 156 Q158 186 196 184 Q234 186 244 156 Q252 128 236 110 Q218 96 196 112 Z"/>
  <path fill="none" d="M196 112 Q194 96 202 84"/>
  <path class="fillable" fill="#ffffff" d="M200 94 Q214 78 236 84 Q222 102 200 94 Z"/>
  <path fill="none" d="M170 126 Q164 138 166 150"/>
  <path class="fillable" fill="#ffffff" d="M168 244 L232 244 L242 262 L158 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M80 178 L320 178 Q316 202 304 216 Q200 232 96 216 Q84 202 80 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M96 216 Q200 232 304 216 Q276 250 200 250 Q124 250 96 216 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="178" rx="122" ry="10"/>
  <path class="fillable" fill="#ffffff" d="M150 176 Q230 194 312 140 Q326 132 328 146 Q312 194 238 204 Q178 210 146 192 Q138 180 150 176 Z"/>
  <path fill="none" d="M150 182 L140 176 M318 138 L324 126"/>
  <path fill="none" d="M176 190 Q240 190 300 160" stroke-width="3"/>
</g>
''')

add('donut', '🍩 甜甜圈', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 262 Q100 250 200 256 Q300 262 400 250 L400 300 L0 300 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="240" rx="180" ry="30"/>
  <ellipse fill="none" cx="200" cy="238" rx="130" ry="18" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" fill-rule="evenodd" d="M350.0 158.0 L349.4 166.4 L347.7 174.7 L344.9 182.8 L341.0 190.8 L335.9 198.6 L329.9 206.0 L322.9 213.1 L314.9 219.7 L306.1 225.9 L296.4 231.5 L286.0 236.6 L275.0 241.1 L263.4 245.0 L251.3 248.2 L238.8 250.7 L226.0 252.5 L213.1 253.6 L200.0 254.0 L186.9 253.6 L174.0 252.5 L161.2 250.7 L148.7 248.2 L136.6 245.0 L125.0 241.1 L114.0 236.6 L103.6 231.5 L93.9 225.9 L85.1 219.7 L77.1 213.1 L70.1 206.0 L64.1 198.6 L59.0 190.8 L55.1 182.8 L52.3 174.7 L50.6 166.4 L50.0 158.0 L50.6 149.6 L52.3 141.3 L55.1 133.2 L59.0 125.2 L64.1 117.4 L70.1 110.0 L77.1 102.9 L85.1 96.3 L93.9 90.1 L103.6 84.5 L114.0 79.4 L125.0 74.9 L136.6 71.0 L148.7 67.8 L161.2 65.3 L174.0 63.5 L186.9 62.4 L200.0 62.0 L213.1 62.4 L226.0 63.5 L238.8 65.3 L251.3 67.8 L263.4 71.0 L275.0 74.9 L286.0 79.4 L296.4 84.5 L306.1 90.1 L314.9 96.3 L322.9 102.9 L329.9 110.0 L335.9 117.4 L341.0 125.2 L344.9 133.2 L347.7 141.3 L349.4 149.6 Z M239.8 147.9 L239.4 145.8 L238.6 143.8 L237.6 141.8 L236.3 139.9 L234.6 138.0 L232.8 136.2 L230.6 134.6 L228.3 133.0 L225.7 131.6 L222.9 130.3 L220.0 129.2 L216.9 128.2 L213.7 127.4 L210.4 126.8 L206.9 126.4 L203.5 126.1 L200.0 126.0 L196.5 126.1 L193.1 126.4 L189.6 126.8 L186.3 127.4 L183.1 128.2 L180.0 129.2 L177.1 130.3 L174.3 131.6 L171.7 133.0 L169.4 134.6 L167.2 136.2 L165.4 138.0 L163.7 139.9 L162.4 141.8 L161.4 143.8 L160.6 145.8 L160.2 147.9 L160.0 150.0 L160.2 152.1 L160.6 154.2 L161.4 156.2 L162.4 158.2 L163.7 160.1 L165.4 162.0 L167.2 163.8 L169.4 165.4 L171.7 167.0 L174.3 168.4 L177.1 169.7 L180.0 170.8 L183.1 171.8 L186.3 172.6 L189.6 173.2 L193.1 173.6 L196.5 173.9 L200.0 174.0 L203.5 173.9 L206.9 173.6 L210.4 173.2 L213.7 172.6 L216.9 171.8 L220.0 170.8 L222.9 169.7 L225.7 168.4 L228.3 167.0 L230.6 165.4 L232.8 163.8 L234.6 162.0 L236.3 160.1 L237.6 158.2 L238.6 156.2 L239.4 154.2 L239.8 152.1 L240.0 150.0 Z"/>
  <path class="fillable" fill="#ffffff" fill-rule="evenodd" d="M350.0 140.0 L349.4 148.4 L347.7 156.7 L344.9 164.8 L341.0 172.8 L335.9 180.6 L329.9 188.0 L322.9 195.1 L314.9 201.7 L306.1 207.9 L296.4 213.5 L286.0 218.6 L275.0 223.1 L263.4 227.0 L251.3 230.2 L238.8 232.7 L226.0 234.5 L213.1 235.6 L200.0 236.0 L186.9 235.6 L174.0 234.5 L161.2 232.7 L148.7 230.2 L136.6 227.0 L125.0 223.1 L114.0 218.6 L103.6 213.5 L93.9 207.9 L85.1 201.7 L77.1 195.1 L70.1 188.0 L64.1 180.6 L59.0 172.8 L55.1 164.8 L52.3 156.7 L50.6 148.4 L50.0 140.0 L50.6 131.6 L52.3 123.3 L55.1 115.2 L59.0 107.2 L64.1 99.4 L70.1 92.0 L77.1 84.9 L85.1 78.3 L93.9 72.1 L103.6 66.5 L114.0 61.4 L125.0 56.9 L136.6 53.0 L148.7 49.8 L161.2 47.3 L174.0 45.5 L186.9 44.4 L200.0 44.0 L213.1 44.4 L226.0 45.5 L238.8 47.3 L251.3 49.8 L263.4 53.0 L275.0 56.9 L286.0 61.4 L296.4 66.5 L306.1 72.1 L314.9 78.3 L322.9 84.9 L329.9 92.0 L335.9 99.4 L341.0 107.2 L344.9 115.2 L347.7 123.3 L349.4 131.6 Z M239.8 137.9 L239.4 135.8 L238.6 133.8 L237.6 131.8 L236.3 129.9 L234.6 128.0 L232.8 126.2 L230.6 124.6 L228.3 123.0 L225.7 121.6 L222.9 120.3 L220.0 119.2 L216.9 118.2 L213.7 117.4 L210.4 116.8 L206.9 116.4 L203.5 116.1 L200.0 116.0 L196.5 116.1 L193.1 116.4 L189.6 116.8 L186.3 117.4 L183.1 118.2 L180.0 119.2 L177.1 120.3 L174.3 121.6 L171.7 123.0 L169.4 124.6 L167.2 126.2 L165.4 128.0 L163.7 129.9 L162.4 131.8 L161.4 133.8 L160.6 135.8 L160.2 137.9 L160.0 140.0 L160.2 142.1 L160.6 144.2 L161.4 146.2 L162.4 148.2 L163.7 150.1 L165.4 152.0 L167.2 153.8 L169.4 155.4 L171.7 157.0 L174.3 158.4 L177.1 159.7 L180.0 160.8 L183.1 161.8 L186.3 162.6 L189.6 163.2 L193.1 163.6 L196.5 163.9 L200.0 164.0 L203.5 163.9 L206.9 163.6 L210.4 163.2 L213.7 162.6 L216.9 161.8 L220.0 160.8 L222.9 159.7 L225.7 158.4 L228.3 157.0 L230.6 155.4 L232.8 153.8 L234.6 152.0 L236.3 150.1 L237.6 148.2 L238.6 146.2 L239.4 144.2 L239.8 142.1 L240.0 140.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M321.3 163.5 L317.8 165.6 L314.9 167.8 L312.7 170.2 L311.3 172.7 L310.5 175.5 L310.0 178.4 L309.5 181.4 L308.6 184.4 L307.1 187.2 L304.7 189.7 L301.5 191.7 L297.5 193.3 L293.0 194.6 L288.3 195.5 L283.7 196.4 L279.4 197.4 L275.6 198.7 L272.4 200.4 L269.6 202.6 L267.2 205.2 L264.9 208.0 L262.4 211.0 L259.6 213.7 L256.3 216.1 L252.4 217.9 L248.0 219.0 L243.3 219.4 L238.3 219.2 L233.3 218.7 L228.4 218.0 L212.1 174.2 L213.7 173.4 L215.3 172.6 L217.0 172.1 L218.7 171.6 L220.5 171.4 L222.5 171.3 L224.5 171.2 L226.7 171.2 L228.9 171.2 L231.1 171.0 L233.3 170.8 L235.3 170.3 L237.2 169.7 L238.8 168.9 L240.1 167.8 L241.2 166.7 L242.0 165.3 L242.6 164.0 L243.1 162.6 L243.5 161.2 L243.9 159.9 L244.4 158.7 L245.1 157.5 L246.0 156.5 L247.1 155.6 L248.5 154.7 L250.0 153.8 L251.6 152.9 L253.3 151.9 L254.9 150.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M228.4 218.0 L223.7 217.4 L219.1 217.2 L214.8 217.4 L210.5 218.0 L206.2 219.1 L201.8 220.3 L197.3 221.6 L192.6 222.6 L187.9 223.0 L183.3 222.8 L178.8 221.9 L174.6 220.4 L170.6 218.3 L167.0 216.0 L163.5 213.7 L160.1 211.6 L156.6 209.9 L152.8 208.8 L148.7 208.2 L144.1 208.0 L139.2 208.0 L134.1 208.1 L129.0 207.8 L124.2 207.2 L119.9 206.0 L116.2 204.3 L113.2 202.0 L110.8 199.4 L108.9 196.5 L107.2 193.7 L157.9 165.1 L158.6 166.4 L159.7 167.6 L160.9 168.7 L162.5 169.6 L164.3 170.2 L166.3 170.7 L168.5 171.0 L170.7 171.1 L172.9 171.2 L175.1 171.2 L177.1 171.2 L179.1 171.4 L181.0 171.6 L182.7 172.0 L184.3 172.5 L186.0 173.2 L187.6 174.0 L189.3 174.9 L191.0 175.8 L192.8 176.6 L194.7 177.3 L196.7 177.8 L198.8 178.1 L200.8 178.1 L202.9 177.9 L204.9 177.4 L206.8 176.8 L208.7 176.0 L210.4 175.1 L212.1 174.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M107.2 193.7 L105.4 191.0 L103.2 188.7 L100.4 186.6 L97.0 184.7 L93.0 183.1 L88.7 181.5 L84.4 179.8 L80.4 177.8 L77.1 175.5 L74.7 172.9 L73.6 170.0 L73.5 166.9 L74.3 163.7 L75.8 160.5 L77.4 157.4 L78.8 154.5 L79.6 151.7 L79.6 149.0 L78.7 146.4 L77.1 143.8 L75.0 141.1 L72.9 138.4 L71.1 135.5 L70.0 132.6 L69.8 129.7 L70.8 126.9 L72.7 124.3 L75.4 121.7 L78.5 119.4 L81.6 117.1 L147.9 129.6 L148.2 131.0 L148.3 132.2 L148.3 133.4 L148.0 134.6 L147.5 135.7 L146.7 136.9 L145.7 138.1 L144.6 139.3 L143.6 140.5 L142.6 141.8 L141.9 143.1 L141.5 144.5 L141.4 145.8 L141.7 147.2 L142.4 148.4 L143.5 149.6 L144.8 150.7 L146.4 151.7 L148.1 152.7 L149.7 153.6 L151.3 154.5 L152.7 155.4 L153.8 156.3 L154.8 157.3 L155.5 158.4 L156.0 159.7 L156.5 160.9 L156.9 162.3 L157.3 163.7 L157.9 165.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M81.6 117.1 L84.4 114.9 L86.5 112.5 L87.9 110.0 L88.4 107.2 L88.5 104.2 L88.2 101.0 L88.1 97.7 L88.4 94.4 L89.5 91.3 L91.6 88.6 L94.7 86.3 L98.7 84.6 L103.3 83.2 L108.2 82.2 L113.1 81.4 L117.8 80.5 L122.1 79.5 L125.8 78.0 L129.1 76.2 L132.0 74.1 L134.8 71.7 L137.7 69.2 L140.9 66.9 L144.6 65.1 L148.7 63.8 L153.2 63.1 L158.1 63.0 L163.0 63.5 L168.0 64.3 L172.7 65.1 L187.3 104.0 L185.1 103.8 L183.0 103.7 L180.9 103.9 L178.9 104.3 L177.1 105.0 L175.5 105.9 L174.0 106.9 L172.7 108.1 L171.5 109.3 L170.4 110.5 L169.3 111.7 L168.2 112.7 L167.0 113.6 L165.6 114.4 L164.0 115.0 L162.3 115.6 L160.3 116.1 L158.3 116.6 L156.3 117.1 L154.2 117.7 L152.4 118.4 L150.7 119.3 L149.3 120.3 L148.2 121.4 L147.5 122.7 L147.1 124.0 L147.0 125.4 L147.2 126.8 L147.5 128.3 L147.9 129.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M172.7 65.1 L177.3 65.7 L181.6 65.9 L185.8 65.6 L189.9 64.6 L194.0 63.3 L198.2 61.6 L202.7 59.9 L207.3 58.4 L212.0 57.3 L216.8 57.0 L221.4 57.3 L225.8 58.4 L230.0 60.0 L233.9 61.9 L237.7 63.9 L241.4 65.7 L245.1 67.2 L249.2 68.3 L253.5 68.9 L258.2 69.2 L263.1 69.4 L268.1 69.7 L273.0 70.2 L277.6 71.2 L281.5 72.8 L284.8 75.0 L287.2 77.7 L289.0 80.8 L290.2 84.0 L291.3 87.1 L240.0 116.2 L238.1 115.7 L236.3 115.1 L234.7 114.5 L233.3 113.8 L232.0 112.9 L230.9 111.9 L229.8 110.7 L228.7 109.5 L227.5 108.3 L226.2 107.2 L224.8 106.1 L223.2 105.2 L221.4 104.5 L219.5 104.0 L217.4 103.7 L215.3 103.7 L213.1 103.9 L211.0 104.3 L208.9 104.7 L206.8 105.2 L204.9 105.6 L203.0 105.9 L201.1 106.1 L199.3 106.1 L197.4 106.0 L195.5 105.7 L193.5 105.3 L191.5 104.8 L189.4 104.4 L187.3 104.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M291.3 87.1 L292.5 90.1 L294.1 92.7 L296.3 95.0 L299.2 96.9 L302.8 98.6 L306.9 100.1 L311.2 101.8 L315.2 103.6 L318.7 105.7 L321.3 108.1 L323.0 110.8 L323.6 113.7 L323.5 116.7 L322.8 119.7 L322.0 122.7 L321.5 125.5 L321.6 128.2 L322.4 130.9 L324.1 133.5 L326.4 136.1 L329.1 138.9 L331.7 141.7 L333.8 144.7 L335.1 147.7 L335.2 150.7 L334.2 153.6 L331.9 156.3 L328.8 158.9 L325.1 161.2 L321.3 163.5 L254.9 150.9 L256.3 149.8 L257.4 148.6 L258.2 147.4 L258.6 146.1 L258.6 144.7 L258.2 143.4 L257.5 142.1 L256.6 140.8 L255.6 139.5 L254.5 138.3 L253.5 137.1 L252.7 136.0 L252.1 134.8 L251.7 133.6 L251.6 132.5 L251.8 131.2 L252.1 129.9 L252.4 128.5 L252.7 127.1 L252.9 125.7 L252.9 124.3 L252.6 122.9 L252.0 121.6 L251.0 120.5 L249.6 119.4 L248.0 118.6 L246.1 117.8 L244.1 117.2 L242.1 116.7 L240.0 116.2 Z"/>
  <rect class="fillable" fill="#ffffff" x="259.1" y="180.8" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(-90 269.1 184.8)"/>
  <rect class="fillable" fill="#ffffff" x="192.2" y="203.7" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(-43 202.2 207.7)"/>
  <rect class="fillable" fill="#ffffff" x="131.6" y="186.5" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(4 141.6 190.5)"/>
  <rect class="fillable" fill="#ffffff" x="86.7" y="152.0" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(51 96.7 156.0)"/>
  <rect class="fillable" fill="#ffffff" x="104.6" y="102.5" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(-82 114.6 106.5)"/>
  <rect class="fillable" fill="#ffffff" x="156.9" y="71.6" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(-35 166.9 75.6)"/>
  <rect class="fillable" fill="#ffffff" x="218.5" y="75.3" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(12 228.5 79.3)"/>
  <rect class="fillable" fill="#ffffff" x="278.8" y="99.2" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(59 288.8 103.2)"/>
  <rect class="fillable" fill="#ffffff" x="288.5" y="143.3" width="20" height="8" rx="4" stroke-width="2.5" transform="rotate(-74 298.5 147.3)"/>
</g>
''')

add('hamburger', '🍔 汉堡', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="350" cy="50" r="24"/>
  <path class="fillable" fill="#ffffff" d="M30 78 Q30 58 52 60 Q60 42 82 48 Q100 40 108 60 Q126 62 122 78 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 270 Q100 258 200 266 Q300 274 400 260 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M90 236 L310 236 Q316 236 314 246 Q308 268 280 268 L120 268 Q92 268 86 246 Q84 236 90 236 Z"/>
  <path class="fillable" fill="#ffffff" d="M84 212 Q84 200 100 200 L300 200 Q316 200 316 212 L316 228 Q316 242 300 242 L100 242 Q84 242 84 228 Z"/>
  <path class="fillable" fill="#ffffff" d="M82 192 L318 192 L318 204 L298 204 L286 224 L274 204 L198 204 L184 228 L170 204 L110 204 L100 220 L90 204 L82 204 Z"/>
  <path class="fillable" fill="#ffffff" d="M96 174 L200 174 L200 196 L96 196 Q86 185 96 174 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 174 L304 174 Q314 185 304 196 L200 196 Z"/>
  <path class="fillable" fill="#ffffff" d="M78 160 Q76 152 88 154 L312 154 Q324 152 322 160 Q330 168 318 172 Q310 184 296 174 Q284 186 270 174 Q256 186 242 174 Q228 186 214 174 Q200 186 186 174 Q172 186 158 174 Q144 186 130 174 Q116 186 104 174 Q90 184 82 172 Q70 168 78 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M80 156 Q80 62 200 58 Q320 62 320 156 Q320 164 310 164 L90 164 Q80 164 80 156 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="140" cy="92" rx="8" ry="5" stroke-width="2.5" transform="rotate(-25 140 92)"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="76" rx="8" ry="5" stroke-width="2.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="262" cy="92" rx="8" ry="5" stroke-width="2.5" transform="rotate(25 262 92)"/>
  <ellipse class="fillable" fill="#ffffff" cx="112" cy="126" rx="8" ry="5" stroke-width="2.5" transform="rotate(-40 112 126)"/>
  <ellipse class="fillable" fill="#ffffff" cx="288" cy="126" rx="8" ry="5" stroke-width="2.5" transform="rotate(40 288 126)"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="112" rx="11" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="228" cy="112" rx="11" ry="13"/>
  <circle fill="#1a1a1a" stroke="none" cx="174" cy="114" r="6"/>
  <circle fill="#1a1a1a" stroke="none" cx="226" cy="114" r="6"/>
  <circle fill="#ffffff" stroke="none" cx="176" cy="111" r="2.2"/>
  <circle fill="#ffffff" stroke="none" cx="228" cy="111" r="2.2"/>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="134" rx="11" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="250" cy="134" rx="11" ry="7"/>
  <path fill="none" d="M186 132 Q200 146 214 132"/>
</g>
''')

# --- Other / Holidays (7) ---
add('christmas', '🎄 圣诞树', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 240 200 248 Q300 256 400 242 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="184" y="222" width="32" height="34" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M200 146 Q160 186 100 222 Q114 236 132 230 Q150 242 166 232 Q183 242 200 232 Q217 242 234 232 Q250 242 268 230 Q286 236 300 222 Q240 186 200 146 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 96 Q170 134 124 166 Q136 178 152 172 Q168 184 184 174 Q200 184 216 174 Q232 184 248 172 Q264 178 276 166 Q230 134 200 96 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 52 Q182 82 150 110 Q162 120 176 114 Q188 122 200 116 Q212 122 224 114 Q238 120 250 110 Q218 82 200 52 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 18 L208 34 L226 36 L213 48 L217 66 L200 57 L183 66 L187 48 L174 36 L192 34 Z"/>
  <circle class="fillable" fill="#ffffff" cx="186" cy="96" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="222" cy="104" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="166" cy="152" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="212" cy="146" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="248" cy="160" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="140" cy="214" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="190" cy="204" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="244" cy="208" r="10"/>
  <rect class="fillable" fill="#ffffff" x="52" y="206" width="70" height="52" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="46" y="194" width="82" height="16" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="78" y="194" width="18" height="64" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M87 194 Q66 170 60 184 Q62 196 87 194 Z"/>
  <path class="fillable" fill="#ffffff" d="M87 194 Q108 170 114 184 Q112 196 87 194 Z"/>
  <rect class="fillable" fill="#ffffff" x="286" y="222" width="62" height="38" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="280" y="212" width="74" height="14" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="309" y="212" width="16" height="48" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M317 212 Q298 192 292 204 Q294 214 317 212 Z"/>
  <path class="fillable" fill="#ffffff" d="M317 212 Q336 192 342 204 Q340 214 317 212 Z"/>
</g>
''')

add('halloween', '🎃 万圣节南瓜', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M340 22 Q316 40 322 66 Q330 90 358 92 Q340 80 338 58 Q338 36 352 24 Q346 20 340 22 Z"/>
  <path class="fillable" fill="#ffffff" d="M30 70 Q30 54 48 56 Q54 42 72 46 Q88 40 94 56 Q110 58 106 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 244 200 252 Q300 260 400 246 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 96 Q190 70 184 52 Q196 44 210 50 Q206 70 212 96 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 70 Q236 46 262 60 Q238 86 210 76 Z"/>
  <path fill="none" d="M236 66 L222 72" stroke-width="3"/>
  <path fill="none" d="M188 72 Q164 58 154 72 Q148 88 166 86"/>
  <ellipse class="fillable" fill="#ffffff" cx="104" cy="174" rx="56" ry="68"/>
  <ellipse class="fillable" fill="#ffffff" cx="296" cy="174" rx="56" ry="68"/>
  <ellipse class="fillable" fill="#ffffff" cx="144" cy="174" rx="66" ry="80"/>
  <ellipse class="fillable" fill="#ffffff" cx="256" cy="174" rx="66" ry="80"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="174" rx="78" ry="88"/>
  <path class="fillable" fill="#ffffff" d="M142 156 Q144 150 148 144 L160 124 Q164 118 168 124 L180 144 Q184 150 186 156 Q164 162 142 156 Z"/>
  <path class="fillable" fill="#ffffff" d="M214 156 Q216 150 220 144 L232 124 Q236 118 240 124 L252 144 Q256 150 258 156 Q236 162 214 156 Z"/>
  <circle fill="#ffffff" stroke="none" cx="160" cy="142" r="4"/>
  <circle fill="#ffffff" stroke="none" cx="232" cy="142" r="4"/>
  <path class="fillable" fill="#ffffff" d="M192 176 L200 164 L208 176 Q200 180 192 176 Z"/>
  <path class="fillable" fill="#ffffff" d="M144 186 Q200 200 256 186 Q250 234 200 236 Q150 234 144 186 Z"/>
  <rect class="fillable" fill="#ffffff" x="168" y="194" width="18" height="16" rx="3" stroke-width="3"/>
  <rect class="fillable" fill="#ffffff" x="214" y="194" width="18" height="16" rx="3" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M56 220 Q54 206 62 202 L68 204 Q62 210 64 220 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="44" cy="240" rx="18" ry="22"/>
  <ellipse class="fillable" fill="#ffffff" cx="76" cy="240" rx="18" ry="22"/>
  <ellipse class="fillable" fill="#ffffff" cx="60" cy="240" rx="18" ry="24"/>
</g>
''')

add('easter', '🐰 复活节彩蛋', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="52" r="24"/>
  <path class="fillable" fill="#ffffff" d="M0 252 Q100 238 200 246 Q300 254 400 240 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M98 176 Q98 46 200 46 Q302 46 302 176 L286 176 Q286 62 200 62 Q114 62 114 176 Z"/>
  <path class="fillable" fill="#ffffff" d="M104.5 130.7 L104.4 128.5 L104.5 126.3 L104.6 124.1 L104.8 122.0 L105.0 119.9 L105.3 117.8 L105.7 115.8 L106.1 113.8 L106.6 111.9 L107.1 110.0 L107.7 108.2 L108.4 106.5 L109.1 104.9 L109.9 103.3 L110.7 101.9 L111.5 100.5 L112.5 99.2 L113.4 98.0 L114.5 96.9 L115.5 96.0 L116.6 95.1 L117.8 94.3 L119.0 93.6 L120.3 93.1 L121.6 92.6 L122.9 92.2 L124.3 92.0 L125.7 91.9 L127.1 91.8 L128.6 91.9 L130.2 92.1 L131.7 92.4 L133.3 92.7 L134.9 93.2 L136.5 93.8 L138.2 94.5 L139.8 95.2 L141.5 96.1 L143.2 97.1 L144.9 98.1 L146.5 99.2 L148.2 100.4 L149.9 101.7 L151.5 103.1 L153.1 104.5 L154.7 106.0 L156.3 107.6 L157.8 109.2 L158.9 110.9 L158.3 112.1 L157.0 111.8 L155.7 111.4 L154.4 111.0 L153.1 110.5 L151.8 110.1 L150.5 109.7 L149.2 109.2 L147.9 108.8 L146.6 108.3 L145.3 107.9 L144.0 107.5 L142.7 107.0 L141.4 106.6 L140.4 106.9 L139.8 108.1 L139.2 109.4 L138.6 110.6 L137.9 111.8 L137.3 113.0 L136.7 114.2 L136.0 115.4 L135.4 116.6 L134.8 117.9 L134.1 119.1 L133.5 120.3 L132.9 121.5 L132.3 122.7 L131.0 122.3 L129.7 121.9 L128.4 121.4 L127.1 121.0 L125.8 120.5 L124.5 120.1 L123.2 119.7 L121.9 119.2 L120.6 118.8 L119.3 118.4 L118.0 117.9 L116.7 117.5 L115.4 117.0 L114.4 117.5 L113.8 118.7 L113.2 119.9 L112.5 121.1 L111.9 122.4 L111.3 123.6 L110.7 124.8 L110.0 126.0 L109.4 127.2 L108.8 128.4 L108.1 129.7 L107.5 130.9 L106.9 132.1 L106.2 133.2 L104.9 132.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M104.9 132.7 L106.2 133.2 L106.9 132.1 L107.5 130.9 L108.1 129.7 L108.8 128.4 L109.4 127.2 L110.0 126.0 L110.7 124.8 L111.3 123.6 L111.9 122.4 L112.5 121.1 L113.2 119.9 L113.8 118.7 L114.4 117.5 L115.4 117.0 L116.7 117.5 L118.0 117.9 L119.3 118.4 L120.6 118.8 L121.9 119.2 L123.2 119.7 L124.5 120.1 L125.8 120.5 L127.1 121.0 L128.4 121.4 L129.7 121.9 L131.0 122.3 L132.3 122.7 L132.9 121.5 L133.5 120.3 L134.1 119.1 L134.8 117.9 L135.4 116.6 L136.0 115.4 L136.7 114.2 L137.3 113.0 L137.9 111.8 L138.6 110.6 L139.2 109.4 L139.8 108.1 L140.4 106.9 L141.4 106.6 L142.7 107.0 L144.0 107.5 L145.3 107.9 L146.6 108.3 L147.9 108.8 L149.2 109.2 L150.5 109.7 L151.8 110.1 L153.1 110.5 L154.4 111.0 L155.7 111.4 L157.0 111.8 L158.3 112.1 L158.9 110.9 L159.3 110.9 L160.7 112.6 L162.0 114.4 L163.3 116.2 L164.5 118.1 L165.7 120.0 L166.7 122.0 L167.7 123.9 L168.3 125.8 L167.6 127.0 L167.0 128.3 L166.4 129.5 L165.8 130.7 L164.5 130.4 L163.2 129.9 L161.9 129.5 L160.6 129.1 L159.3 128.6 L158.0 128.2 L156.7 127.8 L155.4 127.3 L154.1 126.9 L152.8 126.4 L151.5 126.0 L150.2 125.6 L148.9 125.1 L147.9 125.5 L147.3 126.7 L146.7 127.9 L146.0 129.1 L145.4 130.3 L144.8 131.5 L144.2 132.8 L143.5 134.0 L142.9 135.2 L142.3 136.4 L141.6 137.6 L141.0 138.8 L140.4 140.1 L139.7 141.3 L138.4 140.8 L137.1 140.4 L135.9 140.0 L134.6 139.5 L133.3 139.1 L132.0 138.7 L130.7 138.2 L129.4 137.8 L128.1 137.3 L126.8 136.9 L125.5 136.5 L124.2 136.0 L122.9 135.6 L121.9 136.0 L121.3 137.3 L120.7 138.5 L120.0 139.7 L119.4 140.9 L118.8 142.1 L118.1 143.3 L117.5 144.6 L116.9 145.8 L116.3 147.0 L115.6 148.2 L115.0 149.4 L114.4 150.6 L113.7 151.7 L112.4 151.3 L111.1 150.9 L109.8 150.4 L108.5 150.0 L107.6 148.2 L106.9 146.1 L106.3 144.0 L105.8 141.8 L105.4 139.6 L105.1 137.4 L104.8 135.2 L104.6 133.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M108.5 150.0 L109.8 150.4 L111.1 150.9 L112.4 151.3 L113.7 151.7 L114.4 150.6 L115.0 149.4 L115.6 148.2 L116.3 147.0 L116.9 145.8 L117.5 144.6 L118.1 143.3 L118.8 142.1 L119.4 140.9 L120.0 139.7 L120.7 138.5 L121.3 137.3 L121.9 136.0 L122.9 135.6 L124.2 136.0 L125.5 136.5 L126.8 136.9 L128.1 137.3 L129.4 137.8 L130.7 138.2 L132.0 138.7 L133.3 139.1 L134.6 139.5 L135.9 140.0 L137.1 140.4 L138.4 140.8 L139.7 141.3 L140.4 140.1 L141.0 138.8 L141.6 137.6 L142.3 136.4 L142.9 135.2 L143.5 134.0 L144.2 132.8 L144.8 131.5 L145.4 130.3 L146.0 129.1 L146.7 127.9 L147.3 126.7 L147.9 125.5 L148.9 125.1 L150.2 125.6 L151.5 126.0 L152.8 126.4 L154.1 126.9 L155.4 127.3 L156.7 127.8 L158.0 128.2 L159.3 128.6 L160.6 129.1 L161.9 129.5 L163.2 129.9 L164.5 130.4 L165.8 130.7 L166.4 129.5 L167.0 128.3 L167.6 127.0 L168.3 125.8 L168.6 125.9 L169.4 127.9 L170.1 130.0 L170.6 132.0 L171.1 134.0 L171.5 136.1 L171.7 138.1 L171.9 140.2 L171.9 142.2 L171.8 144.2 L171.6 146.1 L171.2 148.1 L170.8 150.0 L170.2 151.8 L169.5 153.7 L168.7 155.4 L167.8 157.1 L166.8 158.8 L165.6 160.4 L164.4 161.9 L163.1 163.3 L161.7 164.7 L160.2 166.0 L158.6 167.2 L157.0 168.3 L155.3 169.3 L153.5 170.1 L151.7 170.9 L149.9 171.6 L148.0 172.2 L146.1 172.7 L144.1 173.0 L142.2 173.3 L140.2 173.4 L138.3 173.4 L136.3 173.3 L134.4 173.0 L132.5 172.7 L130.6 172.2 L128.7 171.6 L126.9 170.9 L125.2 170.0 L123.5 169.1 L121.8 168.0 L120.2 166.9 L118.7 165.6 L117.2 164.2 L115.9 162.8 L114.5 161.2 L113.3 159.6 L112.2 157.9 L111.1 156.1 L110.1 154.2 L109.2 152.3 L108.3 150.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M240.7 110.9 L242.2 109.2 L243.7 107.6 L245.3 106.0 L246.9 104.5 L248.5 103.1 L250.1 101.7 L251.8 100.4 L253.5 99.2 L255.1 98.1 L256.8 97.1 L258.5 96.1 L260.2 95.2 L261.8 94.5 L263.5 93.8 L265.1 93.2 L266.7 92.7 L268.3 92.4 L269.8 92.1 L271.4 91.9 L272.9 91.8 L274.3 91.9 L275.7 92.0 L277.1 92.2 L278.4 92.6 L279.7 93.1 L281.0 93.6 L282.2 94.3 L283.4 95.1 L284.5 96.0 L285.5 96.9 L286.6 98.0 L287.5 99.2 L288.5 100.5 L289.3 101.9 L290.1 103.3 L290.9 104.9 L291.6 106.5 L292.3 108.2 L292.9 110.0 L293.4 111.9 L293.9 113.8 L294.3 115.8 L294.7 117.8 L295.0 119.9 L295.2 122.0 L295.4 124.1 L294.9 124.9 L293.4 125.9 L291.7 127.3 L290.0 128.8 L288.3 130.1 L286.9 131.0 L285.7 131.1 L284.9 130.4 L284.3 128.9 L284.0 126.9 L283.8 124.7 L283.6 122.4 L283.2 120.5 L282.6 119.2 L281.7 118.7 L280.5 119.0 L279.0 119.9 L277.3 121.3 L275.6 122.8 L273.9 124.1 L272.4 125.0 L271.2 125.2 L270.4 124.6 L269.8 123.2 L269.5 121.3 L269.2 119.0 L269.0 116.8 L268.7 114.8 L268.1 113.5 L267.3 112.8 L266.1 113.0 L264.6 113.9 L262.9 115.2 L261.2 116.8 L259.5 118.1 L258.0 119.1 L256.8 119.3 L255.9 118.8 L255.3 117.5 L254.9 115.6 L254.7 113.4 L254.5 111.1 L254.2 109.1 L253.6 107.7 L252.8 107.0 L251.6 107.1 L250.2 107.9 L248.5 109.2 L246.8 110.7 L245.1 112.1 L243.6 113.1 L242.3 113.5 L241.4 113.0 L240.8 111.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M240.8 111.8 L241.4 113.0 L242.3 113.5 L243.6 113.1 L245.1 112.1 L246.8 110.7 L248.5 109.2 L250.2 107.9 L251.6 107.1 L252.8 107.0 L253.6 107.7 L254.2 109.1 L254.5 111.1 L254.7 113.4 L254.9 115.6 L255.3 117.5 L255.9 118.8 L256.8 119.3 L258.0 119.1 L259.5 118.1 L261.2 116.8 L262.9 115.2 L264.6 113.9 L266.1 113.0 L267.3 112.8 L268.1 113.5 L268.7 114.8 L269.0 116.8 L269.2 119.0 L269.5 121.3 L269.8 123.2 L270.4 124.6 L271.2 125.2 L272.4 125.0 L273.9 124.1 L275.6 122.8 L277.3 121.3 L279.0 119.9 L280.5 119.0 L281.7 118.7 L282.6 119.2 L283.2 120.5 L283.6 122.4 L283.8 124.7 L284.0 126.9 L284.3 128.9 L284.9 130.4 L285.7 131.1 L286.9 131.0 L288.3 130.1 L290.0 128.8 L291.7 127.3 L293.4 125.9 L294.9 124.9 L295.5 126.3 L295.6 128.5 L295.5 130.7 L295.4 133.0 L295.2 135.2 L294.9 137.4 L294.6 139.6 L294.2 141.8 L293.7 144.0 L293.1 146.1 L292.4 148.2 L291.7 150.3 L291.0 151.1 L290.8 148.9 L290.6 146.6 L290.2 144.8 L289.6 143.6 L288.7 143.1 L287.4 143.5 L285.9 144.5 L284.2 145.9 L282.5 147.4 L280.8 148.7 L279.4 149.5 L278.2 149.6 L277.4 148.9 L276.8 147.5 L276.5 145.5 L276.3 143.2 L276.1 141.0 L275.7 139.1 L275.1 137.8 L274.2 137.3 L273.0 137.5 L271.5 138.4 L269.8 139.8 L268.1 141.3 L266.4 142.7 L264.9 143.6 L263.7 143.7 L262.9 143.1 L262.3 141.8 L262.0 139.8 L261.8 137.6 L261.5 135.3 L261.2 133.4 L260.6 132.0 L259.8 131.4 L258.6 131.6 L257.1 132.4 L255.4 133.8 L253.7 135.3 L252.0 136.7 L250.5 137.6 L249.3 137.9 L248.4 137.3 L247.8 136.1 L247.4 134.2 L247.2 131.9 L247.0 129.6 L246.7 127.7 L246.1 126.2 L245.3 125.5 L244.1 125.6 L242.7 126.4 L241.0 127.7 L239.3 129.3 L237.6 130.7 L236.1 131.7 L234.8 132.0 L233.9 131.6 L233.3 130.3 L232.9 128.5 L232.7 126.3 L232.5 124.0 L233.3 122.0 L234.3 120.0 L235.5 118.1 L236.7 116.2 L238.0 114.4 L239.3 112.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M232.5 124.0 L232.7 126.3 L232.9 128.5 L233.3 130.3 L233.9 131.6 L234.8 132.0 L236.1 131.7 L237.6 130.7 L239.3 129.3 L241.0 127.7 L242.7 126.4 L244.1 125.6 L245.3 125.5 L246.1 126.2 L246.7 127.7 L247.0 129.6 L247.2 131.9 L247.4 134.2 L247.8 136.1 L248.4 137.3 L249.3 137.9 L250.5 137.6 L252.0 136.7 L253.7 135.3 L255.4 133.8 L257.1 132.4 L258.6 131.6 L259.8 131.4 L260.6 132.0 L261.2 133.4 L261.5 135.3 L261.8 137.6 L262.0 139.8 L262.3 141.8 L262.9 143.1 L263.7 143.7 L264.9 143.6 L266.4 142.7 L268.1 141.3 L269.8 139.8 L271.5 138.4 L273.0 137.5 L274.2 137.3 L275.1 137.8 L275.7 139.1 L276.1 141.0 L276.3 143.2 L276.5 145.5 L276.8 147.5 L277.4 148.9 L278.2 149.6 L279.4 149.5 L280.8 148.7 L282.5 147.4 L284.2 145.9 L285.9 144.5 L287.4 143.5 L288.7 143.1 L289.6 143.6 L290.2 144.8 L290.6 146.6 L290.8 148.9 L291.0 151.1 L290.8 152.3 L289.9 154.2 L288.9 156.1 L287.8 157.9 L286.7 159.6 L285.5 161.2 L284.1 162.8 L282.8 164.2 L281.3 165.6 L279.8 166.9 L278.2 168.0 L276.5 169.1 L274.8 170.0 L273.1 170.9 L271.3 171.6 L269.4 172.2 L267.5 172.7 L265.6 173.0 L263.7 173.3 L261.7 173.4 L259.8 173.4 L257.8 173.3 L255.9 173.0 L253.9 172.7 L252.0 172.2 L250.1 171.6 L248.3 170.9 L246.5 170.1 L244.7 169.3 L243.0 168.3 L241.4 167.2 L239.8 166.0 L238.3 164.7 L236.9 163.3 L235.6 161.9 L234.4 160.4 L233.2 158.8 L232.2 157.1 L231.3 155.4 L230.5 153.7 L229.8 151.8 L229.2 150.0 L228.8 148.1 L228.4 146.1 L228.2 144.2 L228.1 142.2 L228.1 140.2 L228.3 138.1 L228.5 136.1 L228.9 134.0 L229.4 132.0 L229.9 130.0 L230.6 127.9 L231.4 125.9 L232.3 123.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M172.8 85.9 L174.0 83.8 L175.2 81.8 L176.5 79.9 L177.8 78.1 L179.1 76.3 L180.5 74.7 L181.9 73.2 L183.4 71.7 L184.8 70.4 L186.3 69.2 L187.8 68.1 L189.3 67.2 L190.8 66.3 L192.3 65.6 L193.8 65.0 L195.4 64.6 L196.9 64.3 L198.5 64.1 L200.0 64.0 L201.5 64.1 L203.1 64.3 L204.6 64.6 L206.2 65.0 L207.7 65.6 L209.2 66.3 L210.7 67.2 L212.2 68.1 L213.7 69.2 L215.2 70.4 L216.6 71.7 L218.1 73.2 L219.5 74.7 L220.9 76.3 L222.2 78.1 L223.5 79.9 L224.8 81.8 L226.0 83.8 L227.2 85.9 L228.4 88.0 L229.5 90.2 L230.5 92.5 L230.4 93.8 L229.2 95.6 L228.1 97.1 L226.9 97.9 L225.7 97.9 L224.6 97.3 L223.4 96.0 L222.2 94.3 L221.1 92.2 L219.9 90.1 L218.7 88.3 L217.6 86.9 L216.4 86.1 L215.2 86.1 L214.0 86.7 L212.9 88.0 L211.7 89.8 L210.5 91.9 L209.4 94.0 L208.2 95.8 L207.0 97.2 L205.8 97.9 L204.7 97.9 L203.5 97.2 L202.3 95.9 L201.2 94.1 L200.0 92.0 L198.8 89.9 L197.7 88.1 L196.5 86.8 L195.3 86.1 L194.2 86.1 L193.0 86.8 L191.8 88.2 L190.6 90.0 L189.5 92.1 L188.3 94.2 L187.1 96.0 L186.0 97.3 L184.8 97.9 L183.6 97.9 L182.4 97.1 L181.3 95.7 L180.1 93.9 L178.9 91.8 L177.8 89.7 L176.6 88.0 L175.4 86.7 L174.3 86.1 L173.1 86.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M173.1 86.1 L174.3 86.1 L175.4 86.7 L176.6 88.0 L177.8 89.7 L178.9 91.8 L180.1 93.9 L181.3 95.7 L182.4 97.1 L183.6 97.9 L184.8 97.9 L186.0 97.3 L187.1 96.0 L188.3 94.2 L189.5 92.1 L190.6 90.0 L191.8 88.2 L193.0 86.8 L194.2 86.1 L195.3 86.1 L196.5 86.8 L197.7 88.1 L198.8 89.9 L200.0 92.0 L201.2 94.1 L202.3 95.9 L203.5 97.2 L204.7 97.9 L205.8 97.9 L207.0 97.2 L208.2 95.8 L209.4 94.0 L210.5 91.9 L211.7 89.8 L212.9 88.0 L214.0 86.7 L215.2 86.1 L216.4 86.1 L217.6 86.9 L218.7 88.3 L219.9 90.1 L221.1 92.2 L222.2 94.3 L223.4 96.0 L224.6 97.3 L225.7 97.9 L226.9 97.9 L228.1 97.1 L229.2 95.6 L230.4 93.8 L231.4 94.8 L232.3 97.2 L233.2 99.6 L233.9 102.0 L234.6 104.5 L235.1 107.0 L235.1 108.0 L233.9 109.4 L232.8 110.8 L231.6 112.1 L230.4 113.5 L229.2 114.9 L228.1 116.2 L226.9 117.6 L225.7 119.0 L224.6 120.3 L223.4 120.3 L222.2 118.9 L221.1 117.6 L219.9 116.2 L218.7 114.8 L217.6 113.5 L216.4 112.1 L215.2 110.7 L214.0 109.4 L212.9 108.0 L211.7 107.4 L210.5 108.7 L209.4 110.1 L208.2 111.4 L207.0 112.8 L205.8 114.2 L204.7 115.5 L203.5 116.9 L202.3 118.3 L201.2 119.6 L200.0 121.0 L198.8 119.6 L197.7 118.3 L196.5 116.9 L195.3 115.5 L194.2 114.2 L193.0 112.8 L191.8 111.4 L190.6 110.1 L189.5 108.7 L188.3 107.4 L187.1 108.0 L186.0 109.4 L184.8 110.7 L183.6 112.1 L182.4 113.5 L181.3 114.8 L180.1 116.2 L178.9 117.6 L177.8 118.9 L176.6 120.3 L175.4 120.3 L174.3 119.0 L173.1 117.6 L171.9 116.2 L170.8 114.9 L169.6 113.5 L168.4 112.1 L167.2 110.8 L166.1 109.4 L164.9 108.0 L164.9 107.0 L165.4 104.5 L166.1 102.0 L166.8 99.6 L167.7 97.2 L168.6 94.8 L169.5 92.5 L170.5 90.2 L171.6 88.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M164.9 108.0 L166.1 109.4 L167.2 110.8 L168.4 112.1 L169.6 113.5 L170.8 114.9 L171.9 116.2 L173.1 117.6 L174.3 119.0 L175.4 120.3 L176.6 120.3 L177.8 118.9 L178.9 117.6 L180.1 116.2 L181.3 114.8 L182.4 113.5 L183.6 112.1 L184.8 110.7 L186.0 109.4 L187.1 108.0 L188.3 107.4 L189.5 108.7 L190.6 110.1 L191.8 111.4 L193.0 112.8 L194.2 114.2 L195.3 115.5 L196.5 116.9 L197.7 118.3 L198.8 119.6 L200.0 121.0 L201.2 119.6 L202.3 118.3 L203.5 116.9 L204.7 115.5 L205.8 114.2 L207.0 112.8 L208.2 111.4 L209.4 110.1 L210.5 108.7 L211.7 107.4 L212.9 108.0 L214.0 109.4 L215.2 110.7 L216.4 112.1 L217.6 113.5 L218.7 114.8 L219.9 116.2 L221.1 117.6 L222.2 118.9 L223.4 120.3 L224.6 120.3 L225.7 119.0 L226.9 117.6 L228.1 116.2 L229.2 114.9 L230.4 113.5 L231.6 112.1 L232.8 110.8 L233.9 109.4 L235.1 108.0 L235.6 109.5 L236.0 112.0 L236.3 114.5 L236.5 117.0 L236.6 119.5 L236.5 122.0 L236.4 124.4 L236.1 126.8 L235.8 129.2 L235.3 131.5 L234.7 133.8 L234.0 136.0 L233.2 138.1 L232.2 140.2 L231.1 142.2 L230.0 144.1 L228.7 145.9 L227.3 147.7 L225.8 149.3 L224.2 150.8 L222.6 152.3 L220.8 153.6 L219.0 154.8 L217.1 155.9 L215.1 156.8 L213.0 157.7 L210.9 158.4 L208.8 159.0 L206.6 159.4 L204.4 159.7 L202.2 159.9 L200.0 160.0 L197.8 159.9 L195.6 159.7 L193.4 159.4 L191.2 159.0 L189.1 158.4 L187.0 157.7 L184.9 156.8 L182.9 155.9 L181.0 154.8 L179.2 153.6 L177.4 152.3 L175.8 150.8 L174.2 149.3 L172.7 147.7 L171.3 145.9 L170.0 144.1 L168.9 142.2 L167.8 140.2 L166.8 138.1 L166.0 136.0 L165.3 133.8 L164.7 131.5 L164.2 129.2 L163.9 126.8 L163.6 124.4 L163.5 122.0 L163.4 119.5 L163.5 117.0 L163.7 114.5 L164.0 112.0 L164.4 109.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M90 178 L104 146 L112 168 L120 154 L128 168 L136 146 L144 168 L152 154 L160 168 L168 146 L176 168 L184 154 L192 168 L200 146 L208 168 L216 154 L224 168 L232 146 L240 168 L248 154 L256 168 L264 146 L272 168 L280 154 L288 168 L296 146 L304 168 L304 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M304.0 176.0 L303.6 178.3 L303.2 180.7 L302.8 183.0 L302.4 185.3 L302.0 187.7 L301.6 190.0 L301.2 192.3 L300.7 194.7 L300.3 197.0 L299.8 199.3 L299.4 201.7 L298.9 204.0 L101.1 204.0 L100.6 201.7 L100.2 199.3 L99.7 197.0 L99.3 194.7 L98.8 192.3 L98.4 190.0 L98.0 187.7 L97.6 185.3 L97.2 183.0 L96.8 180.7 L96.4 178.3 L96.0 176.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M298.9 204.0 L298.3 206.3 L297.8 208.7 L297.2 211.0 L296.5 213.3 L295.8 215.7 L295.0 218.0 L294.2 220.3 L293.3 222.7 L292.3 225.0 L291.2 227.3 L290.1 229.7 L288.8 232.0 L111.2 232.0 L109.9 229.7 L108.8 227.3 L107.7 225.0 L106.7 222.7 L105.8 220.3 L105.0 218.0 L104.2 215.7 L103.5 213.3 L102.8 211.0 L102.2 208.7 L101.7 206.3 L101.1 204.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M288.8 232.0 L287.5 234.2 L286.1 236.3 L284.6 238.5 L282.9 240.7 L281.1 242.8 L279.2 245.0 L277.1 247.2 L274.8 249.3 L272.4 251.5 L269.8 253.7 L267.0 255.8 L264.0 258.0 L254.0 260.0 L200.0 262.0 L146.0 260.0 L136.0 258.0 L133.0 255.8 L130.2 253.7 L127.6 251.5 L125.2 249.3 L122.9 247.2 L120.8 245.0 L118.9 242.8 L117.1 240.7 L115.4 238.5 L113.9 236.3 L112.5 234.2 L111.2 232.0 Z"/>
  <path fill="none" stroke-width="3" d="M150 180 L148 256 M200 180 L200 260 M250 180 L252 256"/>
  <rect class="fillable" fill="#ffffff" x="88" y="166" width="224" height="20" rx="10"/>
  <path class="fillable" fill="#ffffff" d="M323.7 206.4 L325.0 205.2 L326.4 204.1 L327.9 203.0 L329.3 202.0 L330.8 201.0 L332.2 200.1 L333.7 199.3 L335.2 198.5 L336.7 197.8 L338.1 197.2 L339.6 196.6 L341.0 196.1 L342.4 195.7 L343.8 195.3 L345.2 195.0 L346.6 194.8 L347.9 194.7 L349.2 194.6 L350.4 194.7 L351.6 194.8 L352.8 195.0 L353.9 195.2 L355.0 195.6 L356.0 196.0 L357.0 196.6 L357.9 197.2 L358.8 197.8 L359.7 198.6 L360.5 199.4 L361.2 200.3 L361.9 201.3 L362.6 202.4 L363.2 203.5 L363.7 204.7 L364.2 206.0 L364.7 207.3 L365.1 208.7 L365.4 210.2 L365.7 211.7 L365.9 213.2 L366.1 214.8 L366.2 216.4 L366.3 218.1 L366.3 219.8 L366.2 221.5 L366.1 223.3 L365.1 224.8 L363.9 225.2 L362.4 226.1 L360.8 227.1 L359.3 228.0 L358.0 228.7 L356.9 228.8 L356.2 228.3 L355.9 227.2 L355.8 225.7 L355.9 223.9 L356.0 222.0 L355.9 220.4 L355.7 219.2 L355.0 218.5 L354.1 218.5 L352.8 219.0 L351.3 219.9 L349.8 220.9 L348.3 221.8 L346.9 222.4 L345.9 222.5 L345.3 221.9 L345.0 220.8 L344.9 219.2 L345.0 217.3 L345.1 215.5 L345.0 213.9 L344.7 212.8 L344.1 212.2 L343.1 212.3 L341.7 212.8 L340.2 213.7 L338.7 214.8 L337.2 215.7 L335.9 216.2 L335.0 216.1 L334.3 215.5 L334.1 214.3 L334.0 212.7 L334.1 210.8 L334.2 209.0 L334.1 207.4 L333.8 206.4 L333.1 205.9 L332.0 206.0 L330.7 206.6 L329.2 207.6 L327.6 208.6 L326.1 209.5 L324.9 209.9 L324.0 209.8 L323.4 209.1 L323.2 207.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M323.2 207.8 L323.4 209.1 L324.0 209.8 L324.9 209.9 L326.1 209.5 L327.6 208.6 L329.2 207.6 L330.7 206.6 L332.0 206.0 L333.1 205.9 L333.8 206.4 L334.1 207.4 L334.2 209.0 L334.1 210.8 L334.0 212.7 L334.1 214.3 L334.3 215.5 L335.0 216.1 L335.9 216.2 L337.2 215.7 L338.7 214.8 L340.2 213.7 L341.7 212.8 L343.1 212.3 L344.1 212.2 L344.7 212.8 L345.0 213.9 L345.1 215.5 L345.0 217.3 L344.9 219.2 L345.0 220.8 L345.3 221.9 L345.9 222.5 L346.9 222.4 L348.3 221.8 L349.8 220.9 L351.3 219.9 L352.8 219.0 L354.1 218.5 L355.0 218.5 L355.7 219.2 L355.9 220.4 L356.0 222.0 L355.9 223.9 L355.8 225.7 L355.9 227.2 L356.2 228.3 L356.9 228.8 L358.0 228.7 L359.3 228.0 L360.8 227.1 L362.4 226.1 L363.9 225.2 L365.1 224.8 L366.0 225.0 L365.8 226.8 L365.5 228.6 L365.1 230.4 L364.7 232.1 L364.3 233.9 L363.7 235.6 L363.2 237.3 L362.5 239.0 L361.8 240.6 L361.0 242.2 L360.2 243.8 L359.3 245.3 L358.4 246.8 L357.4 248.2 L356.7 247.7 L356.8 245.8 L356.8 244.2 L356.6 242.9 L356.0 242.2 L355.1 242.1 L353.9 242.5 L352.4 243.4 L350.8 244.4 L349.3 245.4 L348.0 246.0 L346.9 246.1 L346.2 245.6 L345.9 244.6 L345.8 243.0 L345.9 241.2 L346.0 239.3 L345.9 237.7 L345.7 236.5 L345.0 235.9 L344.1 235.8 L342.8 236.3 L341.3 237.2 L339.8 238.3 L338.3 239.2 L336.9 239.7 L335.9 239.8 L335.3 239.2 L335.0 238.1 L334.9 236.5 L335.0 234.7 L335.1 232.8 L335.0 231.2 L334.7 230.1 L334.1 229.5 L333.1 229.6 L331.7 230.2 L330.2 231.1 L328.7 232.1 L327.2 233.0 L325.9 233.5 L325.0 233.5 L324.3 232.8 L324.1 231.6 L324.0 230.0 L324.1 228.1 L324.2 226.3 L324.1 224.8 L323.8 223.7 L323.1 223.2 L322.0 223.3 L320.7 224.0 L319.2 224.9 L317.6 225.9 L316.1 226.8 L314.9 227.2 L314.0 227.1 L313.4 226.4 L313.2 225.2 L313.2 223.5 L313.3 221.6 L313.3 219.8 L313.6 218.9 L314.5 217.4 L315.4 215.9 L316.4 214.4 L317.5 213.0 L318.6 211.6 L319.8 210.2 L321.0 208.9 L322.3 207.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M313.3 219.8 L313.3 221.6 L313.2 223.5 L313.2 225.2 L313.4 226.4 L314.0 227.1 L314.9 227.2 L316.1 226.8 L317.6 225.9 L319.2 224.9 L320.7 224.0 L322.0 223.3 L323.1 223.2 L323.8 223.7 L324.1 224.8 L324.2 226.3 L324.1 228.1 L324.0 230.0 L324.1 231.6 L324.3 232.8 L325.0 233.5 L325.9 233.5 L327.2 233.0 L328.7 232.1 L330.2 231.1 L331.7 230.2 L333.1 229.6 L334.1 229.5 L334.7 230.1 L335.0 231.2 L335.1 232.8 L335.0 234.7 L334.9 236.5 L335.0 238.1 L335.3 239.2 L335.9 239.8 L336.9 239.7 L338.3 239.2 L339.8 238.3 L341.3 237.2 L342.8 236.3 L344.1 235.8 L345.0 235.9 L345.7 236.5 L345.9 237.7 L346.0 239.3 L345.9 241.2 L345.8 243.0 L345.9 244.6 L346.2 245.6 L346.9 246.1 L348.0 246.0 L349.3 245.4 L350.8 244.4 L352.4 243.4 L353.9 242.5 L355.1 242.1 L356.0 242.2 L356.6 242.9 L356.8 244.2 L356.8 245.8 L356.7 247.7 L356.3 249.5 L355.2 250.7 L354.0 251.9 L352.8 253.0 L351.5 254.0 L350.2 254.9 L348.8 255.8 L347.4 256.5 L345.9 257.2 L344.4 257.7 L342.9 258.2 L341.4 258.6 L339.9 258.8 L338.3 259.0 L336.7 259.1 L335.1 259.1 L333.6 258.9 L332.0 258.7 L330.4 258.4 L328.9 258.0 L327.4 257.5 L325.9 256.9 L324.4 256.2 L323.0 255.4 L321.6 254.6 L320.3 253.7 L319.1 252.7 L317.9 251.6 L316.7 250.5 L315.7 249.3 L314.7 248.0 L313.8 246.7 L313.0 245.4 L312.3 244.0 L311.6 242.5 L311.1 241.1 L310.6 239.6 L310.3 238.0 L310.0 236.5 L309.9 234.9 L309.8 233.3 L309.9 231.7 L310.0 230.1 L310.2 228.5 L310.6 226.8 L311.0 225.2 L311.5 223.6 L312.1 222.0 L312.8 220.5 Z"/>
  <path fill="none" d="M52 250 Q50 226 56 208"/>
  <path class="fillable" fill="#ffffff" d="M54 232 Q36 220 30 230 Q40 240 54 232 Z"/>
  <circle class="fillable" fill="#ffffff" cx="56.0" cy="186.0" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="67.4" cy="194.3" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="63.1" cy="207.7" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="48.9" cy="207.7" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="44.6" cy="194.3" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="56" cy="198" r="9"/>
</g>
''')

add('party', '🎉 派对场景', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 260 Q100 250 200 256 Q300 262 400 252 L400 300 L0 300 Z"/>
  <path fill="none" d="M6 14 Q200 46 394 14" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M29.3 17.6 L68.1 22.6 L48.7 46.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M79.7 23.8 L118.5 27.2 L99.1 51.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M130.2 27.9 L169.0 29.6 L149.6 54.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M180.6 29.8 L219.4 29.8 L200.0 55.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M231.0 29.6 L269.8 27.9 L250.4 54.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M281.5 27.2 L320.3 23.8 L300.9 51.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M331.9 22.6 L370.7 17.6 L351.3 46.1 Z"/>
  <path fill="none" stroke-width="2.5" d="M60 182 Q50 218 60 238 Q70 258 80 254"/>
  <path class="fillable" fill="#ffffff" d="M60 176 L53 186 L67 186 Z" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="60" cy="138" rx="30" ry="38"/>
  <path fill="none" stroke-width="3" d="M44 122 Q48 112 56 110"/>
  <path fill="none" stroke-width="2.5" d="M112 148 Q102 184 112 204 Q122 224 128 254"/>
  <path class="fillable" fill="#ffffff" d="M112 142 L105 152 L119 152 Z" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="112" cy="104" rx="30" ry="38"/>
  <path fill="none" stroke-width="3" d="M96 88 Q100 78 108 76"/>
  <path fill="none" stroke-width="2.5" d="M288 148 Q278 184 288 204 Q298 224 272 254"/>
  <path class="fillable" fill="#ffffff" d="M288 142 L281 152 L295 152 Z" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="288" cy="104" rx="30" ry="38"/>
  <path fill="none" stroke-width="3" d="M272 88 Q276 78 284 76"/>
  <path fill="none" stroke-width="2.5" d="M340 182 Q330 218 340 238 Q350 258 320 254"/>
  <path class="fillable" fill="#ffffff" d="M340 176 L333 186 L347 186 Z" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="340" cy="138" rx="30" ry="38"/>
  <path fill="none" stroke-width="3" d="M324 122 Q328 112 336 110"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="254" rx="104" ry="12"/>
  <rect class="fillable" fill="#ffffff" x="116" y="186" width="168" height="66" rx="10"/>
  <path class="fillable" fill="#ffffff" d="M112 190 Q112 182 120 182 L280 182 Q288 182 288 190 L288 196 Q273.3 214.0 258.7 196 Q244.0 206.8 229.3 196 Q214.7 214.0 200.0 196 Q185.3 206.8 170.7 196 Q156.0 214.0 141.3 196 Q126.7 206.8 112.0 196 Z"/>
  <rect class="fillable" fill="#ffffff" x="142" y="130" width="116" height="58" rx="10"/>
  <path class="fillable" fill="#ffffff" d="M138 134 Q138 126 146 126 L254 126 Q262 126 262 134 L262 140 Q246.5 156.0 231.0 140 Q215.5 149.6 200.0 140 Q184.5 156.0 169.0 140 Q153.5 149.6 138.0 140 Z"/>
  <rect class="fillable" fill="#ffffff" x="164" y="96" width="12" height="32" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M170 66 Q182 80 178 88 Q170 96 162 88 Q158 80 170 66 Z" stroke-width="3"/>
  <path fill="none" stroke-width="2.5" d="M170 89 L170 96"/>
  <rect class="fillable" fill="#ffffff" x="194" y="96" width="12" height="32" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M200 66 Q212 80 208 88 Q200 96 192 88 Q188 80 200 66 Z" stroke-width="3"/>
  <path fill="none" stroke-width="2.5" d="M200 89 L200 96"/>
  <rect class="fillable" fill="#ffffff" x="224" y="96" width="12" height="32" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M230 66 Q242 80 238 88 Q230 96 222 88 Q218 80 230 66 Z" stroke-width="3"/>
  <path fill="none" stroke-width="2.5" d="M230 89 L230 96"/>
  <path class="fillable" fill="#ffffff" d="M200 236 Q178 222 180 212 Q184 202 200 212 Q216 202 220 212 Q222 222 200 236 Z" stroke-width="3"/>
</g>
''')

add('house', '🏡 房子和花园', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="46" r="24"/>
  <path class="fillable" fill="#ffffff" d="M24 58 Q24 40 44 42 Q52 26 72 32 Q90 24 96 42 Q114 44 110 58 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 248 Q100 236 200 244 Q300 252 400 240 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="244" y="56" width="28" height="56" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="238" y="48" width="40" height="14" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="112" y="124" width="176" height="126" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M88 132 Q84 126 90 120 L192 46 Q200 40 208 46 L310 120 Q316 126 312 132 Q308 138 300 136 L100 136 Q92 138 88 132 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="96" r="18"/>
  <path fill="none" d="M182 96 L218 96 M200 78 L200 114" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M178 250 L178 194 Q178 172 200 172 Q222 172 222 194 L222 250 Z"/>
  <circle fill="#1a1a1a" stroke="none" cx="212" cy="214" r="4"/>
  <rect class="fillable" fill="#ffffff" x="128" y="156" width="20" height="20"/>
  <rect class="fillable" fill="#ffffff" x="148" y="156" width="20" height="20"/>
  <rect class="fillable" fill="#ffffff" x="128" y="176" width="20" height="20"/>
  <rect class="fillable" fill="#ffffff" x="148" y="176" width="20" height="20"/>
  <rect class="fillable" fill="#ffffff" x="122" y="196" width="52" height="12" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="232" y="156" width="20" height="20"/>
  <rect class="fillable" fill="#ffffff" x="252" y="156" width="20" height="20"/>
  <rect class="fillable" fill="#ffffff" x="232" y="176" width="20" height="20"/>
  <rect class="fillable" fill="#ffffff" x="252" y="176" width="20" height="20"/>
  <rect class="fillable" fill="#ffffff" x="226" y="196" width="52" height="12" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M178 250 L222 250 L250 296 L150 296 Z"/>
  <path class="fillable" fill="#ffffff" d="M44 252 L46 186 L64 186 L66 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M54 92 Q86 88 92 118 Q110 132 98 158 Q100 190 70 192 Q56 202 40 192 Q10 192 12 162 Q0 136 20 120 Q24 90 54 92 Z"/>
  <path fill="none" d="M318 252 L318 212 M346 250 L346 204 M372 250 L372 216"/>
  <path class="fillable" fill="#ffffff" d="M318 238 Q304 228 298 236 Q306 246 318 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M346 232 Q360 222 366 230 Q358 240 346 234 Z"/>
  <path class="fillable" fill="#ffffff" d="M318 196 Q306 190 308 200 Q298 206 308 212 Q308 222 318 216 Q328 222 328 212 Q338 206 328 200 Q330 190 318 196 Z"/>
  <path class="fillable" fill="#ffffff" d="M346 188 Q334 182 336 192 Q326 198 336 204 Q336 214 346 208 Q356 214 356 204 Q366 198 356 192 Q358 182 346 188 Z"/>
  <path class="fillable" fill="#ffffff" d="M372 200 Q360 194 362 204 Q352 210 362 216 Q362 226 372 220 Q382 226 382 216 Q392 210 382 204 Q384 194 372 200 Z"/>
</g>
''')

add('space', '🪐 太空场景', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M236.0 27.0 L239.7 35.0 L248.4 36.0 L241.9 41.9 L243.6 50.5 L236.0 46.2 L228.4 50.5 L230.1 41.9 L223.6 36.0 L232.3 35.0 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M28.1 200.2 L30.1 208.0 L37.9 210.3 L31.1 214.7 L31.3 222.8 L25.0 217.7 L17.4 220.3 L20.3 212.8 L15.4 206.4 L23.5 206.8 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M370.3 202.1 L374.7 208.9 L382.8 208.7 L377.7 215.0 L380.3 222.6 L372.8 219.7 L366.4 224.6 L366.8 216.5 L360.2 211.9 L368.0 209.9 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M176.9 214.0 L179.1 220.4 L185.7 221.8 L180.4 225.9 L181.2 232.6 L175.6 228.8 L169.4 231.5 L171.3 225.1 L166.8 220.1 L173.5 219.9 Z" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="44" cy="44" r="24"/>
  <circle class="fillable" fill="#ffffff" cx="37" cy="38" r="7" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="53" cy="54" r="5" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 246 200 254 Q300 262 400 248 L400 300 L0 300 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="80" cy="274" rx="26" ry="8" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="300" cy="280" rx="20" ry="7" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M24.5 151.7 L24.3 149.0 L24.8 146.2 L25.9 143.3 L27.8 140.3 L30.3 137.2 L33.4 134.0 L37.2 130.8 L41.6 127.6 L46.6 124.4 L52.2 121.2 L58.2 118.1 L64.7 115.0 L71.7 112.0 L79.1 109.1 L86.8 106.3 L94.8 103.7 L103.1 101.2 L111.6 98.9 L120.2 96.7 L128.9 94.7 L137.7 93.0 L146.5 91.4 L155.2 90.1 L163.7 89.0 L172.1 88.2 L180.3 87.6 L188.2 87.3 L195.8 87.2 L203.0 87.3 L209.9 87.7 L216.2 88.4 L222.1 89.3 L227.4 90.4 L232.1 91.8 L236.3 93.4 L239.9 95.2 L242.8 97.2 L245.0 99.4 L246.6 101.8 L247.5 104.3 L220.1 110.1 L219.5 108.5 L218.4 107.0 L216.7 105.6 L214.6 104.3 L212.0 103.2 L208.9 102.3 L205.3 101.5 L201.4 100.9 L197.0 100.4 L192.2 100.1 L187.2 100.0 L181.7 100.1 L176.1 100.3 L170.1 100.7 L164.0 101.3 L157.6 102.0 L151.2 102.9 L144.6 103.9 L138.0 105.1 L131.4 106.5 L124.8 107.9 L118.3 109.5 L111.9 111.2 L105.7 113.1 L99.6 115.0 L93.7 116.9 L88.1 119.0 L82.9 121.1 L77.9 123.2 L73.3 125.4 L69.1 127.6 L65.3 129.8 L61.9 132.0 L59.0 134.2 L56.5 136.3 L54.6 138.4 L53.1 140.4 L52.2 142.3 L51.8 144.1 L51.9 145.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M72.2 110.9 L73.2 107.6 L74.4 104.3 L75.7 101.2 L77.2 98.0 L78.8 95.0 L80.6 92.1 L82.6 89.2 L84.7 86.5 L87.0 83.8 L89.3 81.3 L91.8 79.0 L94.5 76.7 L97.2 74.6 L100.1 72.6 L103.0 70.8 L106.0 69.2 L109.2 67.7 L112.3 66.4 L115.6 65.2 L118.9 64.2 L122.3 63.4 L125.7 62.8 L129.1 62.4 L132.5 62.1 L136.0 62.0 L139.5 62.1 L142.9 62.4 L146.3 62.8 L149.7 63.4 L153.1 64.2 L156.4 65.2 L159.7 66.4 L162.8 67.7 L166.0 69.2 L169.0 70.8 L171.9 72.6 L174.8 74.6 L177.5 76.7 L180.2 79.0 L180.6 79.9 L178.6 81.0 L176.7 82.3 L174.8 83.6 L172.9 84.9 L171.0 86.3 L169.1 87.6 L167.2 88.9 L165.2 90.2 L163.3 91.3 L161.3 92.4 L159.4 93.4 L157.3 94.3 L155.3 95.1 L153.2 95.7 L151.2 96.1 L149.0 96.5 L146.9 96.7 L144.7 96.8 L142.5 96.7 L140.3 96.6 L138.0 96.3 L135.8 96.0 L133.5 95.6 L131.2 95.2 L128.9 94.7 L126.6 94.3 L124.4 93.9 L122.1 93.5 L119.8 93.2 L117.6 92.9 L115.4 92.8 L113.1 92.7 L111.0 92.8 L108.8 93.0 L106.7 93.3 L104.6 93.8 L102.6 94.4 L100.5 95.2 L98.5 96.1 L96.5 97.0 L94.6 98.1 L92.6 99.3 L90.7 100.6 L88.8 101.9 L86.9 103.2 L85.0 104.6 L83.1 105.9 L81.1 107.2 L79.2 108.4 L77.3 109.6 L75.3 110.7 L73.3 111.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M73.3 111.7 L75.3 110.7 L77.3 109.6 L79.2 108.4 L81.1 107.2 L83.1 105.9 L85.0 104.6 L86.9 103.2 L88.8 101.9 L90.7 100.6 L92.6 99.3 L94.6 98.1 L96.5 97.0 L98.5 96.1 L100.5 95.2 L102.6 94.4 L104.6 93.8 L106.7 93.3 L108.8 93.0 L111.0 92.8 L113.1 92.7 L115.4 92.8 L117.6 92.9 L119.8 93.2 L122.1 93.5 L124.4 93.9 L126.6 94.3 L128.9 94.7 L131.2 95.2 L133.5 95.6 L135.8 96.0 L138.0 96.3 L140.3 96.6 L142.5 96.7 L144.7 96.8 L146.9 96.7 L149.0 96.5 L151.2 96.1 L153.2 95.7 L155.3 95.1 L157.3 94.3 L159.4 93.4 L161.3 92.4 L163.3 91.3 L165.2 90.2 L167.2 88.9 L169.1 87.6 L171.0 86.3 L172.9 84.9 L174.8 83.6 L176.7 82.3 L178.6 81.0 L180.6 79.9 L182.7 81.3 L185.0 83.8 L187.3 86.5 L189.4 89.2 L191.4 92.1 L193.2 95.0 L194.8 98.0 L196.3 101.2 L197.6 104.3 L198.8 107.6 L199.8 110.9 L198.6 112.9 L196.3 112.7 L194.1 112.6 L191.9 112.6 L189.8 112.7 L187.6 113.0 L185.5 113.4 L183.4 113.9 L181.4 114.6 L179.4 115.4 L177.4 116.4 L175.4 117.4 L173.5 118.5 L171.5 119.8 L169.6 121.0 L167.7 122.4 L165.8 123.7 L163.9 125.0 L162.0 126.4 L160.0 127.6 L158.1 128.9 L156.2 130.0 L154.2 131.0 L152.2 132.0 L150.2 132.8 L148.1 133.5 L146.1 134.0 L143.9 134.5 L141.8 134.7 L139.7 134.9 L137.5 134.9 L135.3 134.8 L133.0 134.6 L130.8 134.3 L128.5 134.0 L126.2 133.5 L123.9 133.1 L121.6 132.7 L119.4 132.2 L117.1 131.8 L114.8 131.4 L112.5 131.1 L110.3 130.9 L108.1 130.8 L105.9 130.9 L103.7 131.0 L101.6 131.3 L99.5 131.7 L97.4 132.2 L95.4 132.9 L93.4 133.7 L91.4 134.6 L89.4 135.7 L87.4 136.8 L85.5 138.0 L83.6 139.3 L81.7 140.6 L79.8 142.0 L77.9 143.3 L75.9 144.6 L74.0 145.9 L72.2 145.1 L71.4 141.7 L70.8 138.3 L70.4 134.9 L70.1 131.5 L70.0 128.0 L70.1 124.5 L70.4 121.1 L70.8 117.7 L71.4 114.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M74.0 145.9 L75.9 144.6 L77.9 143.3 L79.8 142.0 L81.7 140.6 L83.6 139.3 L85.5 138.0 L87.4 136.8 L89.4 135.7 L91.4 134.6 L93.4 133.7 L95.4 132.9 L97.4 132.2 L99.5 131.7 L101.6 131.3 L103.7 131.0 L105.9 130.9 L108.1 130.8 L110.3 130.9 L112.5 131.1 L114.8 131.4 L117.1 131.8 L119.4 132.2 L121.6 132.7 L123.9 133.1 L126.2 133.5 L128.5 134.0 L130.8 134.3 L133.0 134.6 L135.3 134.8 L137.5 134.9 L139.7 134.9 L141.8 134.7 L143.9 134.5 L146.1 134.0 L148.1 133.5 L150.2 132.8 L152.2 132.0 L154.2 131.0 L156.2 130.0 L158.1 128.9 L160.0 127.6 L162.0 126.4 L163.9 125.0 L165.8 123.7 L167.7 122.4 L169.6 121.0 L171.5 119.8 L173.5 118.5 L175.4 117.4 L177.4 116.4 L179.4 115.4 L181.4 114.6 L183.4 113.9 L185.5 113.4 L187.6 113.0 L189.8 112.7 L191.9 112.6 L194.1 112.6 L196.3 112.7 L198.6 112.9 L200.6 114.3 L201.2 117.7 L201.6 121.1 L201.9 124.5 L202.0 128.0 L201.9 131.5 L201.6 134.9 L201.2 138.3 L200.6 141.7 L199.8 145.1 L198.8 148.4 L197.6 151.7 L196.3 154.8 L194.8 158.0 L193.2 161.0 L191.4 163.9 L189.4 166.8 L187.3 169.5 L185.0 172.2 L182.7 174.7 L180.2 177.0 L177.5 179.3 L174.8 181.4 L171.9 183.4 L169.0 185.2 L166.0 186.8 L162.8 188.3 L159.7 189.6 L156.4 190.8 L153.1 191.8 L149.7 192.6 L146.3 193.2 L142.9 193.6 L139.5 193.9 L136.0 194.0 L132.5 193.9 L129.1 193.6 L125.7 193.2 L122.3 192.6 L118.9 191.8 L115.6 190.8 L112.3 189.6 L109.2 188.3 L106.0 186.8 L103.0 185.2 L100.1 183.4 L97.2 181.4 L94.5 179.3 L91.8 177.0 L89.3 174.7 L87.0 172.2 L84.7 169.5 L82.6 166.8 L80.6 163.9 L78.8 161.0 L77.2 158.0 L75.7 154.8 L74.4 151.7 L73.2 148.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M247.5 104.3 L247.7 107.0 L247.2 109.8 L246.1 112.7 L244.2 115.7 L241.7 118.8 L238.6 122.0 L234.8 125.2 L230.4 128.4 L225.4 131.6 L219.8 134.8 L213.8 137.9 L207.3 141.0 L200.3 144.0 L192.9 146.9 L185.2 149.7 L177.2 152.3 L168.9 154.8 L160.4 157.1 L151.8 159.3 L143.1 161.3 L134.3 163.0 L125.5 164.6 L116.8 165.9 L108.3 167.0 L99.9 167.8 L91.7 168.4 L83.8 168.7 L76.2 168.8 L69.0 168.7 L62.1 168.3 L55.8 167.6 L49.9 166.7 L44.6 165.6 L39.9 164.2 L35.7 162.6 L32.1 160.8 L29.2 158.8 L27.0 156.6 L25.4 154.2 L24.5 151.7 L51.9 145.9 L52.5 147.5 L53.6 149.0 L55.3 150.4 L57.4 151.7 L60.0 152.8 L63.1 153.7 L66.7 154.5 L70.6 155.1 L75.0 155.6 L79.8 155.9 L84.8 156.0 L90.3 155.9 L95.9 155.7 L101.9 155.3 L108.0 154.7 L114.4 154.0 L120.8 153.1 L127.4 152.1 L134.0 150.9 L140.6 149.5 L147.2 148.1 L153.7 146.5 L160.1 144.8 L166.3 142.9 L172.4 141.0 L178.3 139.1 L183.9 137.0 L189.1 134.9 L194.1 132.8 L198.7 130.6 L202.9 128.4 L206.7 126.2 L210.1 124.0 L213.0 121.8 L215.5 119.7 L217.4 117.6 L218.9 115.6 L219.8 113.7 L220.2 111.9 L220.1 110.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M280.0 180.6 Q289.5 216.2 267.9 233.7 Q255.7 242.8 242.0 246.5 Q238.3 232.8 240.1 217.7 Q244.5 190.2 280.0 180.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M274.0 191.0 Q275.4 212.6 263.9 224.5 Q255.5 231.1 249.0 234.3 Q248.5 227.1 250.1 216.5 Q254.6 200.6 274.0 191.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M266.7 163.7 L301.3 183.7 L297.8 197.8 Q275.0 189.3 256.2 173.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M278.0 124.1 Q242.3 121.9 221.3 158.3 Q238.4 156.6 258.0 158.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M330.0 154.1 Q349.7 183.9 328.7 220.3 Q321.6 204.6 310.0 188.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M296.0 92.9 Q270.6 129.0 257.0 160.4 L309.0 190.4 Q329.4 163.0 348.0 122.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M296.0 92.9 Q319.2 64.7 350.0 59.4 Q360.8 88.7 348.0 122.9 Q318.0 114.8 296.0 92.9 Z"/>
  <circle class="fillable" fill="#ffffff" cx="303.0" cy="140.8" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="303.0" cy="140.8" r="10"/>
  <circle fill="#ffffff" stroke="none" cx="301.5" cy="135.3" r="3"/>
</g>
''')

add('blank', '⬜ 空白画板', 'other', '<g><rect class="fillable" fill="#ffffff" x="0" y="0" width="400" height="300"/></g>')

# =============================================================================
# 50 more templates to bring totals to ≥10 per category (100 total)
# =============================================================================

# --- Ocean: +4 ---
add('shark', '🦈 鲨鱼', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 242 200 250 Q300 258 400 246 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M30 256 Q16 220 30 190 Q44 160 32 126 Q56 156 48 190 Q40 222 46 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M52 256 Q46 230 56 210 Q66 190 60 166 Q80 190 72 214 Q64 234 66 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 252 Q338 226 360 220 Q384 218 390 240 L390 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M362 222 Q352 190 366 166 Q376 146 368 120 Q390 146 382 172 Q374 196 378 224 Z"/>
  <path class="fillable" fill="#ffffff" d="M152.5 250.2 L156.3 261.5 L167.7 264.9 L158.1 271.9 L158.5 283.9 L148.7 276.9 L137.5 280.9 L141.1 269.6 L133.8 260.1 L145.8 260.1 Z" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="352" cy="96" r="9" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="366" cy="66" r="12" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M128 126 Q84 100 50 64 Q38 58 40 72 Q46 116 72 146 Q46 172 44 212 Q46 222 56 216 Q90 186 128 164 Z"/>
  <path class="fillable" fill="#ffffff" d="M190 92 Q204 52 230 38 Q244 34 244 48 Q242 72 256 90 Z"/>
  <path class="fillable" fill="#ffffff" d="M208 180 Q208 214 186 228 Q176 206 180 176 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 176 Q266 216 238 234 Q226 212 238 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M352 148 Q352 90 282 82 Q200 76 140 112 Q116 126 96 140 Q116 156 142 174 Q210 210 292 198 Q352 190 352 148 Z"/>
  <path class="fillable" fill="#ffffff" d="M351 154 Q342 188 292 198 Q226 208 168 182 Q240 172 292 170 Q336 166 351 154 Z"/>
  <path fill="none" stroke-width="3" d="M266 112 Q260 126 266 140 M254 114 Q248 128 254 142 M242 116 Q236 130 242 144"/>
  <ellipse class="fillable" fill="#ffffff" cx="306" cy="122" rx="13" ry="15"/>
  <circle fill="#1a1a1a" stroke="none" cx="308" cy="124" r="7"/>
  <circle fill="#ffffff" stroke="none" cx="311" cy="120" r="2.6"/>
  <ellipse class="fillable" fill="#ffffff" cx="292" cy="150" rx="10" ry="6"/>
  <path fill="none" d="M312 156 Q330 168 346 154"/>
</g>
''')

add('seahorse', '🌊 海马', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 244 200 252 Q300 260 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 256 Q44 220 60 186 Q74 156 60 118 Q88 150 78 186 Q68 220 76 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M84 256 Q78 230 90 206 Q100 186 94 160 Q116 186 106 210 Q96 232 98 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 256 Q318 226 334 196 Q348 170 340 140 Q364 170 352 200 Q340 228 346 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M296 262 Q290 236 312 232 Q334 236 328 262 Z"/>
  <path fill="none" stroke-width="3" d="M312 236 L304 260 M312 236 L312 262 M312 236 L320 260"/>
  <circle class="fillable" fill="#ffffff" cx="120" cy="70" r="9" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="104" cy="42" r="12" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M162.0 130.0 Q126.0 128.0 120.0 156.0 Q126.0 182.0 160.0 182.0 Z"/>
  <path fill="none" stroke-width="2.5" d="M158.0 140.0 L130.0 148.0 M158.0 156.0 L124.0 158.0 M158.0 170.0 L130.0 170.0"/>
  <path class="fillable" fill="#ffffff" d="M170.0 186.0 Q156.0 226.0 176.0 252.0 Q200.0 276.0 230.0 262.0 Q252.0 248.0 240.0 228.0 Q228.0 214.0 212.0 224.0 Q204.0 232.0 212.0 240.0 Q220.0 246.0 226.0 240.0 Q228.0 252.0 214.0 254.0 Q194.0 252.0 190.0 234.0 Q186.0 214.0 200.0 196.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M184.0 66.0 Q166.0 54.0 178.0 44.0 Q174.0 30.0 190.0 32.0 Q194.0 18.0 210.0 26.0 Q216.0 34.0 214.0 46.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M226.0 96.0 C262.0 136.0 262.0 188.0 214.0 212.0 Q196.0 214.0 186.0 204.0 Q160.0 184.0 156.0 140.0 Q150.0 96.0 186.0 66.0 Z"/>
  <path class="fillable" fill="#ffffff" stroke-width="3" d="M237.4 110.8 L239.0 113.4 L240.5 116.0 L241.9 118.5 L243.2 121.1 L244.4 123.7 L245.5 126.3 L246.6 128.9 L247.5 131.5 L248.4 134.2 L249.1 136.8 L230.4 140.6 L229.9 138.5 L229.4 136.4 L228.8 134.4 L228.1 132.3 L227.4 130.2 L226.7 128.1 L225.8 126.0 L225.0 124.0 L224.0 121.9 L223.0 119.9 Z"/>
  <path class="fillable" fill="#ffffff" stroke-width="3" d="M249.1 136.8 L249.8 139.4 L250.3 142.0 L250.8 144.6 L251.2 147.2 L251.4 149.8 L251.6 152.4 L251.7 154.9 L251.6 157.5 L251.5 160.0 L251.3 162.5 L231.6 161.0 L231.8 159.0 L231.9 157.0 L231.9 155.0 L231.9 153.0 L231.8 150.9 L231.6 148.9 L231.4 146.8 L231.1 144.8 L230.8 142.7 L230.4 140.6 Z"/>
  <path class="fillable" fill="#ffffff" stroke-width="3" d="M251.3 162.5 L250.9 165.0 L250.5 167.5 L250.0 169.9 L249.3 172.3 L248.6 174.7 L247.7 177.1 L246.8 179.4 L245.7 181.7 L244.6 183.9 L243.3 186.1 L225.7 179.2 L226.6 177.6 L227.5 175.8 L228.2 174.1 L228.9 172.3 L229.6 170.5 L230.1 168.6 L230.6 166.7 L231.0 164.8 L231.3 162.9 L231.6 161.0 Z"/>
  <path class="fillable" fill="#ffffff" stroke-width="3" d="M243.3 186.1 L241.9 188.3 L240.4 190.4 L238.8 192.5 L237.1 194.6 L235.3 196.6 L233.4 198.5 L231.4 200.4 L229.2 202.2 L227.0 204.0 L224.6 205.7 L211.9 193.7 L213.7 192.5 L215.3 191.2 L216.9 189.8 L218.4 188.5 L219.9 187.0 L221.2 185.6 L222.4 184.0 L223.6 182.5 L224.7 180.9 L225.7 179.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M236.0 70.0 Q260.0 74.0 280.0 70.0 Q292.0 70.0 292.0 81.0 Q292.0 92.0 280.0 92.0 Q260.0 90.0 236.0 98.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M180.0 70.0 Q180.0 38.0 214.0 40.0 Q246.0 44.0 246.0 78.0 Q246.0 104.0 222.0 108.0 Q190.0 110.0 180.0 70.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M186.0 82.0 Q174.0 96.0 182.0 108.0 Q194.0 102.0 196.0 90.0 Z" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="218.0" cy="70.0" rx="11.0" ry="13.0"/>
  <circle fill="#1a1a1a" stroke="none" cx="220.0" cy="72.0" r="6.0"/>
  <circle fill="#ffffff" stroke="none" cx="222.0" cy="69.0" r="2.2"/>
  <ellipse class="fillable" fill="#ffffff" cx="230.0" cy="94.0" rx="8.0" ry="5.0"/>
  <path fill="none" stroke-width="3" d="M276.0 86.0 Q283.0 90.0 289.0 86.0"/>
</g>
''')

add('lobster', '🦞 龙虾', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 244 200 252 Q300 260 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M26 256 Q14 226 28 200 Q40 176 32 150 Q54 176 46 202 Q38 228 42 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M360 256 Q350 228 364 204 Q376 182 368 156 Q390 182 382 206 Q374 230 378 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 266 Q294 242 314 238 Q334 242 330 266 Z"/>
  <path fill="none" stroke-width="3" d="M314 242 L306 264 M314 242 L314 266 M314 242 L322 264"/>
  <path fill="none" d="M188 76 Q160 30 112 18"/>
  <path fill="none" d="M212 76 Q240 30 288 18"/>
  <path fill="none" stroke-width="5" d="M158 140 L130 150 L122 168 M156 156 L132 170 L128 188 M160 170 L142 186 L140 204"/>
  <path fill="none" stroke-width="5" d="M242 140 L270 150 L278 168 M244 156 L268 170 L272 188 M240 170 L258 186 L260 204"/>
  <path class="fillable" fill="#ffffff" d="M168 102 Q132 112 112 86 L98 100 Q128 136 168 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M232 102 Q268 112 288 86 L302 100 Q272 136 232 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M104 106 Q60 108 52 70 Q48 36 76 26 L92 56 L108 32 Q130 46 128 72 Q124 100 104 106 Z"/>
  <path class="fillable" fill="#ffffff" d="M296 106 Q340 108 348 70 Q352 36 324 26 L308 56 L292 32 Q270 46 272 72 Q276 100 296 106 Z"/>
  <path class="fillable" fill="#ffffff" d="M194 216 Q164 218 156 246 Q176 260 196 246 Z"/>
  <path class="fillable" fill="#ffffff" d="M206 216 Q236 218 244 246 Q224 260 204 246 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 214 Q186 216 182 248 Q200 258 218 248 Q214 216 200 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 202 Q170 222 200 224 Q230 222 230 202 Z"/>
  <path class="fillable" fill="#ffffff" d="M162 184 Q160 206 200 208 Q240 206 238 184 Z"/>
  <path class="fillable" fill="#ffffff" d="M154 162 Q150 188 200 190 Q250 188 246 162 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="122" rx="52" ry="52"/>
  <path class="fillable" fill="#ffffff" d="M156 96 Q200 80 244 96 Q236 76 200 72 Q164 76 156 96 Z" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="178" cy="72" rx="14" ry="16"/>
  <ellipse class="fillable" fill="#ffffff" cx="222" cy="72" rx="14" ry="16"/>
  <circle fill="#1a1a1a" stroke="none" cx="180" cy="74" r="7"/>
  <circle fill="#1a1a1a" stroke="none" cx="220" cy="74" r="7"/>
  <circle fill="#ffffff" stroke="none" cx="182" cy="70" r="2.6"/>
  <circle fill="#ffffff" stroke="none" cx="218" cy="70" r="2.6"/>
  <ellipse class="fillable" fill="#ffffff" cx="172" cy="130" rx="10" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="228" cy="130" rx="10" ry="7"/>
  <path fill="none" d="M186 136 Q200 148 214 136"/>
</g>
''')

add('scuba', '🤿 潜水员', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 242 200 250 Q300 258 400 246 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 254 Q140 232 152 214 Q162 232 162 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M162 254 Q162 226 178 208 Q182 232 176 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 252 Q338 234 352 230 Q352 214 366 214 Q380 214 380 230 Q392 236 388 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 50 L312 36 L312 66 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="350" cy="51" rx="24" ry="17"/>
  <circle fill="#1a1a1a" stroke="none" cx="360" cy="47" r="4"/>
  <path fill="none" stroke-width="3" d="M362 58 Q367 61 372 57"/>
  <circle class="fillable" fill="#ffffff" cx="284" cy="30" r="8" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="14" r="6" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M150 126 Q110 114 76 116 Q66 120 68 132 Q72 140 82 140 Q116 140 152 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M86 110 Q60 98 34 84 Q24 80 22 92 Q20 116 30 142 Q34 150 44 146 Q66 142 86 142 Z"/>
  <rect class="fillable" fill="#ffffff" x="136" y="100" width="100" height="32" rx="16"/>
  <rect class="fillable" fill="#ffffff" x="234" y="106" width="12" height="18" rx="3"/>
  <path fill="none" stroke-width="3" d="M166 100 L166 132 M206 100 L206 132"/>
  <path class="fillable" fill="#ffffff" d="M150 156 Q112 164 80 170 Q68 174 70 184 Q74 192 86 190 Q120 188 156 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M88 160 Q62 160 32 164 Q22 166 22 176 Q24 196 36 214 Q42 222 50 216 Q68 200 90 194 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="194" cy="156" rx="64" ry="32"/>
  <path class="fillable" fill="#ffffff" d="M168 125 Q160 156 168 187 L184 188 Q176 156 184 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M222 164 Q258 172 290 186 Q300 192 296 202 Q290 208 280 204 Q248 192 216 188 Z"/>
  <circle class="fillable" fill="#ffffff" cx="298" cy="196" r="12"/>
  <path class="fillable" fill="#ffffff" d="M256 120 L256 56 Q256 46 266 46 Q276 46 276 56 L276 120 Z"/>
  <rect class="fillable" fill="#ffffff" x="252" y="64" width="28" height="10" rx="4" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M250 112 Q256 82 290 80 Q326 82 332 112 Q306 98 290 100 Q270 100 250 112 Z"/>
  <circle class="fillable" fill="#ffffff" cx="290" cy="130" r="44"/>
  <path class="fillable" fill="#ffffff" d="M248 116 Q248 96 290 92 Q332 96 332 116 Q326 108 290 106 Q256 108 248 116 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M258 114 Q258 104 270 104 L310 104 Q322 104 322 114 L322 132 Q322 144 310 144 L296 144 Q290 136 284 144 L270 144 Q258 144 258 132 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="276" cy="124" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="304" cy="124" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="278" cy="126" r="5"/>
  <circle fill="#1a1a1a" stroke="none" cx="306" cy="126" r="5"/>
  <circle fill="#ffffff" stroke="none" cx="280" cy="123" r="2"/>
  <circle fill="#ffffff" stroke="none" cx="308" cy="123" r="2"/>
  <ellipse class="fillable" fill="#ffffff" cx="266" cy="154" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="316" cy="154" rx="8" ry="5"/>
  <path fill="none" d="M282 156 Q292 164 302 156"/>
</g>
''')

# --- Fantasy: +3 ---
add('witch', '🧙‍♀️ 女巫和扫帚', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="318" cy="78" r="50"/>
  <path class="fillable" fill="#ffffff" d="M48.0 27.0 L51.8 34.7 L60.4 36.0 L54.2 42.0 L55.6 50.5 L48.0 46.5 L40.4 50.5 L41.8 42.0 L35.6 36.0 L44.2 34.7 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M120.1 60.2 L121.7 66.7 L127.9 69.0 L122.3 72.5 L122.1 79.1 L117.0 74.9 L110.6 76.7 L113.0 70.5 L109.3 65.0 L116.0 65.4 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M0 252 Q60 226 130 238 Q200 250 260 236 Q330 222 400 240 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M84.7 206.0 L348.7 176.0 Q354.0 169.3 347.3 164.0 L83.3 194.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M92 190 Q60 184 22 178 Q14 196 20 216 Q24 228 32 232 Q64 220 96 210 Z"/>
  <path fill="none" stroke-width="3" d="M80 196 L34 192 M80 204 L36 214"/>
  <path class="fillable" fill="#ffffff" d="M86 186 L100 184 L104 210 L90 212 Z" stroke-width="3"/>
  <path fill="none" stroke-width="5" d="M106.0 192.0 Q90.0 172.0 98.0 152.0 Q102.0 144.0 108.0 150.0"/>
  <ellipse class="fillable" fill="#ffffff" cx="126.0" cy="182.0" rx="22.0" ry="16.0"/>
  <path class="fillable" fill="#ffffff" d="M122.0 154.0 L122.0 132.0 L138.0 148.0 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M136.0 148.0 L152.0 134.0 L150.0 156.0 Z" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="136.0" cy="160.0" r="16.0"/>
  <circle fill="#1a1a1a" stroke="none" cx="131.0" cy="158.0" r="3.0"/>
  <circle fill="#1a1a1a" stroke="none" cx="142.0" cy="158.0" r="3.0"/>
  <path fill="none" stroke-width="2.5" d="M133.0 166.0 Q136.0 169.0 139.0 166.0"/>
  <path class="fillable" fill="#ffffff" d="M196 138 Q160 140 166 196 Q182 190 200 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M212 186 L234 220 L246 214 L226 184 Z"/>
  <path class="fillable" fill="#ffffff" d="M228 214 Q240 236 266 228 Q276 222 262 220 Q252 220 246 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 194 Q172 146 206 132 Q238 146 244 188 Q206 200 170 194 Z"/>
  <path class="fillable" fill="#ffffff" d="M174 92 Q154 140 176 152 Q192 136 196 112 Z"/>
  <path class="fillable" fill="#ffffff" d="M234 92 Q254 140 232 152 Q216 136 212 112 Z"/>
  <circle class="fillable" fill="#ffffff" cx="204" cy="108" r="32"/>
  <path class="fillable" fill="#ffffff" d="M174 98 Q180 78 204 78 Q228 78 234 98 Q220 90 210 98 Q200 88 190 98 Q182 92 174 98 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="191" cy="110" rx="7" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="217" cy="110" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="192" cy="112" r="4.5"/>
  <circle fill="#1a1a1a" stroke="none" cx="218" cy="112" r="4.5"/>
  <circle fill="#ffffff" stroke="none" cx="193.5" cy="109.5" r="1.6"/>
  <circle fill="#ffffff" stroke="none" cx="219.5" cy="109.5" r="1.6"/>
  <ellipse class="fillable" fill="#ffffff" cx="183" cy="124" rx="7" ry="4.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="225" cy="124" rx="7" ry="4.5"/>
  <path fill="none" d="M197 126 Q204 132 211 126"/>
  <path class="fillable" fill="#ffffff" d="M178 78 Q190 52 200 26 Q206 12 222 14 Q212 22 214 34 Q222 56 232 78 Z"/>
  <path class="fillable" fill="#ffffff" d="M182 70 L228 70 L232 80 L178 80 Z" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="205" cy="82" rx="50" ry="9"/>
  <path class="fillable" fill="#ffffff" d="M218 146 Q238 160 248 174 L238 182 Q224 168 210 158 Z"/>
  <circle class="fillable" fill="#ffffff" cx="246" cy="180" r="9"/>
</g>
''')

add('fairy', '🧚 小仙女', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 252 Q100 238 200 246 Q300 254 400 242 L400 300 L0 300 Z"/>
  <path fill="none" d="M56 256 L56 176"/>
  <path class="fillable" fill="#ffffff" d="M56.0 162.0 C63.0 142.7 85.5 159.0 69.3 171.7 C89.8 172.4 81.2 198.8 64.2 187.3 C69.9 207.0 42.1 207.0 47.8 187.3 C30.8 198.8 22.2 172.4 42.7 171.7 C26.5 159.0 49.0 142.7 56.0 162.0 Z"/>
  <circle class="fillable" fill="#ffffff" cx="56" cy="176" r="10"/>
  <path fill="none" d="M346 252 L346 186"/>
  <path class="fillable" fill="#ffffff" d="M346.0 172.0 C353.0 152.7 375.5 169.0 359.3 181.7 C379.8 182.4 371.2 208.8 354.2 197.3 C359.9 217.0 332.1 217.0 337.8 197.3 C320.8 208.8 312.2 182.4 332.7 181.7 C316.5 169.0 339.0 152.7 346.0 172.0 Z"/>
  <circle class="fillable" fill="#ffffff" cx="346" cy="186" r="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="148" cy="110" rx="46" ry="30" transform="rotate(-30 148 110)"/>
  <ellipse class="fillable" fill="#ffffff" cx="252" cy="110" rx="46" ry="30" transform="rotate(30 252 110)"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="168" rx="34" ry="20" transform="rotate(30 158 168)"/>
  <ellipse class="fillable" fill="#ffffff" cx="242" cy="168" rx="34" ry="20" transform="rotate(-30 242 168)"/>
  <path class="fillable" fill="#ffffff" d="M164 90 Q160 140 176 150 L224 150 Q240 140 236 90 Z"/>
  <rect class="fillable" fill="#ffffff" x="184" y="214" width="12" height="28"/>
  <rect class="fillable" fill="#ffffff" x="204" y="214" width="12" height="28"/>
  <path class="fillable" fill="#ffffff" d="M196 238 L196 252 L176 252 Q172 244 182 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M204 238 L204 252 L224 252 Q228 244 218 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 140 Q170 156 164 172 Q160 184 170 186 Q178 186 176 176 Q182 162 196 150 Z"/>
  <path fill="none" stroke-width="5" d="M244 116 L272 60"/>
  <path class="fillable" fill="#ffffff" d="M278.8 32.2 L282.9 44.8 L295.7 48.5 L285.0 56.4 L285.4 69.7 L274.6 61.9 L262.1 66.4 L266.2 53.7 L258.0 43.2 L271.3 43.2 Z" stroke-width="4"/>
  <path class="fillable" fill="#ffffff" d="M212 150 Q228 134 236 120 Q240 110 248 114 Q254 120 248 126 Q236 146 218 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M190 156 Q160 190 148 222 Q170 230 186 222 Q196 190 200 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 156 Q240 190 252 222 Q230 230 214 222 Q204 190 200 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 156 Q186 190 182 226 Q200 234 218 226 Q214 190 200 156 Z"/>
  <path class="fillable" fill="#ffffff" d="M186 128 Q200 122 214 128 L214 158 Q200 164 186 158 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="92" r="34"/>
  <path class="fillable" fill="#ffffff" d="M166 90 Q166 56 200 56 Q234 56 234 90 Q224 76 212 80 Q204 68 194 78 Q180 72 166 90 Z"/>
  <path class="fillable" fill="#ffffff" d="M200.0 37.0 L203.8 44.7 L212.4 46.0 L206.2 52.0 L207.6 60.5 L200.0 56.5 L192.4 60.5 L193.8 52.0 L187.6 46.0 L196.2 44.7 Z" stroke-width="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="187" cy="96" rx="7" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="213" cy="96" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="188" cy="98" r="4.5"/>
  <circle fill="#1a1a1a" stroke="none" cx="214" cy="98" r="4.5"/>
  <circle fill="#ffffff" stroke="none" cx="189.5" cy="95.5" r="1.6"/>
  <circle fill="#ffffff" stroke="none" cx="215.5" cy="95.5" r="1.6"/>
  <ellipse class="fillable" fill="#ffffff" cx="178" cy="110" rx="7" ry="4.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="222" cy="110" rx="7" ry="4.5"/>
  <path fill="none" d="M193 112 Q200 118 207 112"/>
</g>
''')

add('genie_lamp', '🪔 神灯', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 248 200 254 Q300 260 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M361.2 112.3 L365.1 108.5 L368.4 104.7 L371.0 100.6 L372.8 96.0 L373.3 90.9 L372.3 85.8 L370.0 81.7 L367.2 78.7 L364.2 76.4 L361.1 74.7 L357.9 73.2 L354.6 72.0 L351.2 70.8 L347.8 69.8 L344.4 68.7 L341.0 67.7 L337.6 66.7 L334.4 65.6 L331.4 64.5 L328.6 63.4 L326.1 62.2 L324.0 61.0 L322.3 59.9 L321.1 58.8 L320.2 57.8 L319.6 56.8 L319.2 55.6 L319.0 54.1 L319.3 51.9 L320.4 48.9 L307.6 43.1 L305.8 47.4 L304.7 51.9 L304.4 56.4 L305.0 60.7 L306.5 64.7 L308.7 68.3 L311.4 71.4 L314.4 74.0 L317.7 76.3 L321.0 78.2 L324.5 80.0 L328.1 81.6 L331.7 83.1 L335.2 84.5 L338.6 85.8 L341.9 87.0 L344.9 88.3 L347.7 89.4 L350.1 90.6 L352.0 91.7 L353.2 92.7 L353.8 93.3 L353.7 93.5 L353.1 92.8 L352.7 91.6 L352.5 90.7 L352.3 90.7 L351.4 91.6 L349.6 93.4 L346.8 95.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M282 50 Q268 50 270 38 Q262 24 278 20 Q282 6 300 10 Q312 0 326 10 Q344 6 346 22 Q360 28 352 40 Q354 52 338 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M70 236 Q60 214 90 208 L310 208 Q340 214 330 236 Q336 256 310 258 L90 258 Q64 256 70 236 Z"/>
  <path class="fillable" fill="#ffffff" d="M70 236 Q50 236 46 252 Q62 254 72 244 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M330 236 Q350 236 354 252 Q338 254 328 244 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M80.4 137.6 Q25.2 125.6 20.4 161.6 Q18.0 197.6 80.4 192.8 L85.2 176.0 Q39.6 180.8 42.0 159.2 Q44.4 142.4 80.4 154.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M253.2 171.2 Q306.0 159.2 325.2 120.8 Q334.8 99.2 356.4 96.8 Q366.0 101.6 356.4 111.2 Q344.4 118.4 342.0 137.6 Q327.6 185.6 260.4 204.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M138.0 192.8 L234.0 192.8 L248.4 212.0 Q186.0 221.6 123.6 212.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M70.8 159.2 Q78.0 120.8 186.0 113.6 Q294.0 120.8 301.2 159.2 Q186.0 149.6 70.8 159.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M70.8 159.2 Q186.0 149.6 301.2 159.2 Q294.0 202.4 186.0 204.8 Q78.0 202.4 70.8 159.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M126.0 116.0 Q133.2 92.0 186.0 89.6 Q238.8 92.0 246.0 116.0 Q186.0 111.2 126.0 116.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M147.6 92.0 Q152.4 68.0 186.0 65.6 Q219.6 68.0 224.4 92.0 Q186.0 87.2 147.6 92.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M176.4 68.0 Q169.2 51.2 186.0 36.8 Q202.8 51.2 195.6 68.0 Z"/>
  <circle class="fillable" fill="#ffffff" cx="186.0" cy="32.0" r="9.6"/>
  <path class="fillable" fill="#ffffff" d="M186.0 125.6 L198.0 137.6 L186.0 147.2 L174.0 137.6 Z" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="133.2" cy="135.2" r="8.4" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="238.8" cy="135.2" r="8.4" stroke-width="3"/>
</g>
''')

# --- Vehicle: +3 ---
add('bicycle', '🚲 自行车', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="52" cy="48" r="24"/>
  <path class="fillable" fill="#ffffff" d="M170 62 Q170 44 190 46 Q198 30 218 36 Q236 28 242 46 Q260 48 256 62 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 246 200 252 Q300 258 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" fill-rule="evenodd" d="M156.0 204.0 L155.7 209.2 L154.9 214.4 L153.6 219.5 L151.7 224.3 L149.3 229.0 L146.5 233.4 L143.2 237.5 L139.5 241.2 L135.4 244.5 L131.0 247.3 L126.3 249.7 L121.5 251.6 L116.4 252.9 L111.2 253.7 L106.0 254.0 L100.8 253.7 L95.6 252.9 L90.5 251.6 L85.7 249.7 L81.0 247.3 L76.6 244.5 L72.5 241.2 L68.8 237.5 L65.5 233.4 L62.7 229.0 L60.3 224.3 L58.4 219.5 L57.1 214.4 L56.3 209.2 L56.0 204.0 L56.3 198.8 L57.1 193.6 L58.4 188.5 L60.3 183.7 L62.7 179.0 L65.5 174.6 L68.8 170.5 L72.5 166.8 L76.6 163.5 L81.0 160.7 L85.7 158.3 L90.5 156.4 L95.6 155.1 L100.8 154.3 L106.0 154.0 L111.2 154.3 L116.4 155.1 L121.5 156.4 L126.3 158.3 L131.0 160.7 L135.4 163.5 L139.5 166.8 L143.2 170.5 L146.5 174.6 L149.3 179.0 L151.7 183.7 L153.6 188.5 L154.9 193.6 L155.7 198.8 Z M143.8 200.0 L143.2 196.1 L142.1 192.3 L140.7 188.5 L138.9 185.0 L136.7 181.7 L134.2 178.6 L131.4 175.8 L128.3 173.3 L125.0 171.1 L121.5 169.3 L117.7 167.9 L113.9 166.8 L110.0 166.2 L106.0 166.0 L102.0 166.2 L98.1 166.8 L94.3 167.9 L90.5 169.3 L87.0 171.1 L83.7 173.3 L80.6 175.8 L77.8 178.6 L75.3 181.7 L73.1 185.0 L71.3 188.5 L69.9 192.3 L68.8 196.1 L68.2 200.0 L68.0 204.0 L68.2 208.0 L68.8 211.9 L69.9 215.7 L71.3 219.5 L73.1 223.0 L75.3 226.3 L77.8 229.4 L80.6 232.2 L83.7 234.7 L87.0 236.9 L90.5 238.7 L94.3 240.1 L98.1 241.2 L102.0 241.8 L106.0 242.0 L110.0 241.8 L113.9 241.2 L117.7 240.1 L121.5 238.7 L125.0 236.9 L128.3 234.7 L131.4 232.2 L134.2 229.4 L136.7 226.3 L138.9 223.0 L140.7 219.5 L142.1 215.7 L143.2 211.9 L143.8 208.0 L144.0 204.0 Z"/>
  <circle class="fillable" fill="#ffffff" cx="106" cy="204" r="38" stroke-width="3"/>
  <path fill="none" stroke-width="2.5" d="M106 204 L144.0 204.0 M106 204 L132.9 230.9 M106 204 L106.0 242.0 M106 204 L79.1 230.9 M106 204 L68.0 204.0 M106 204 L79.1 177.1 M106 204 L106.0 166.0 M106 204 L132.9 177.1"/>
  <circle class="fillable" fill="#ffffff" cx="106" cy="204" r="8" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" fill-rule="evenodd" d="M344.0 204.0 L343.7 209.2 L342.9 214.4 L341.6 219.5 L339.7 224.3 L337.3 229.0 L334.5 233.4 L331.2 237.5 L327.5 241.2 L323.4 244.5 L319.0 247.3 L314.3 249.7 L309.5 251.6 L304.4 252.9 L299.2 253.7 L294.0 254.0 L288.8 253.7 L283.6 252.9 L278.5 251.6 L273.7 249.7 L269.0 247.3 L264.6 244.5 L260.5 241.2 L256.8 237.5 L253.5 233.4 L250.7 229.0 L248.3 224.3 L246.4 219.5 L245.1 214.4 L244.3 209.2 L244.0 204.0 L244.3 198.8 L245.1 193.6 L246.4 188.5 L248.3 183.7 L250.7 179.0 L253.5 174.6 L256.8 170.5 L260.5 166.8 L264.6 163.5 L269.0 160.7 L273.7 158.3 L278.5 156.4 L283.6 155.1 L288.8 154.3 L294.0 154.0 L299.2 154.3 L304.4 155.1 L309.5 156.4 L314.3 158.3 L319.0 160.7 L323.4 163.5 L327.5 166.8 L331.2 170.5 L334.5 174.6 L337.3 179.0 L339.7 183.7 L341.6 188.5 L342.9 193.6 L343.7 198.8 Z M331.8 200.0 L331.2 196.1 L330.1 192.3 L328.7 188.5 L326.9 185.0 L324.7 181.7 L322.2 178.6 L319.4 175.8 L316.3 173.3 L313.0 171.1 L309.5 169.3 L305.7 167.9 L301.9 166.8 L298.0 166.2 L294.0 166.0 L290.0 166.2 L286.1 166.8 L282.3 167.9 L278.5 169.3 L275.0 171.1 L271.7 173.3 L268.6 175.8 L265.8 178.6 L263.3 181.7 L261.1 185.0 L259.3 188.5 L257.9 192.3 L256.8 196.1 L256.2 200.0 L256.0 204.0 L256.2 208.0 L256.8 211.9 L257.9 215.7 L259.3 219.5 L261.1 223.0 L263.3 226.3 L265.8 229.4 L268.6 232.2 L271.7 234.7 L275.0 236.9 L278.5 238.7 L282.3 240.1 L286.1 241.2 L290.0 241.8 L294.0 242.0 L298.0 241.8 L301.9 241.2 L305.7 240.1 L309.5 238.7 L313.0 236.9 L316.3 234.7 L319.4 232.2 L322.2 229.4 L324.7 226.3 L326.9 223.0 L328.7 219.5 L330.1 215.7 L331.2 211.9 L331.8 208.0 L332.0 204.0 Z"/>
  <circle class="fillable" fill="#ffffff" cx="294" cy="204" r="38" stroke-width="3"/>
  <path fill="none" stroke-width="2.5" d="M294 204 L332.0 204.0 M294 204 L320.9 230.9 M294 204 L294.0 242.0 M294 204 L267.1 230.9 M294 204 L256.0 204.0 M294 204 L267.1 177.1 M294 204 L294.0 166.0 M294 204 L320.9 177.1"/>
  <circle class="fillable" fill="#ffffff" cx="294" cy="204" r="8" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M109.6 207.4 L170.6 143.4 A5.0 5.0 0 0 1 163.4 136.6 L102.4 200.6 A5.0 5.0 0 0 1 109.6 207.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M105.6 209.0 L183.6 215.0 A5.0 5.0 0 0 1 184.4 205.0 L106.4 199.0 A5.0 5.0 0 0 1 105.6 209.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M271.4 161.9 L289.4 205.9 A5.0 5.0 0 0 1 298.6 202.1 L280.6 158.1 A5.0 5.0 0 0 1 271.4 161.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M167.0 146.0 L270.0 146.0 A6.0 6.0 0 0 1 270.0 134.0 L167.0 134.0 A6.0 6.0 0 0 1 167.0 146.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M186.9 215.3 L278.9 165.3 A6.0 6.0 0 0 1 273.1 154.7 L181.1 204.7 A6.0 6.0 0 0 1 186.9 215.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M158.2 127.4 L178.2 211.4 A6.0 6.0 0 0 1 189.8 208.6 L169.8 124.6 A6.0 6.0 0 0 1 158.2 127.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M261.2 127.6 L269.2 161.6 A7.0 7.0 0 0 1 282.8 158.4 L274.8 124.4 A7.0 7.0 0 0 1 261.2 127.6 Z"/>
  <circle class="fillable" fill="#ffffff" cx="184" cy="210" r="18"/>
  <path fill="none" stroke-width="6" d="M162 128 L160 112"/>
  <path class="fillable" fill="#ffffff" d="M134 108 Q136 98 160 100 Q184 102 186 108 Q180 116 160 114 Q140 116 134 108 Z"/>
  <path class="fillable" fill="#ffffff" d="M272.9 127.0 L266.9 99.0 A5.0 5.0 0 0 1 257.1 101.0 L263.1 129.0 A5.0 5.0 0 0 1 272.9 127.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M262 96 Q248 88 232 92 Q226 96 230 102 Q246 100 262 106 Z"/>
  <path fill="none" d="M318 106 L322 80"/>
  <path class="fillable" fill="#ffffff" d="M322.0 62.0 C327.4 46.6 344.5 59.0 331.5 68.9 C347.9 69.3 341.3 89.4 327.9 80.1 C332.6 95.7 311.4 95.7 316.1 80.1 C302.7 89.4 296.1 69.3 312.5 68.9 C299.5 59.0 316.6 46.6 322.0 62.0 Z"/>
  <circle class="fillable" fill="#ffffff" cx="322" cy="72" r="8"/>
  <path class="fillable" fill="#ffffff" d="M300 106 Q290 84 302 76 Q312 90 306 106 Z"/>
  <path class="fillable" fill="#ffffff" d="M276 112 L334 112 L328 156 L282 156 Z"/>
  <path fill="none" stroke-width="3" d="M278 127 L332 127 M280 142 L330 142 M296 112 L297 156 M314 112 L313 156"/>
  <rect class="fillable" fill="#ffffff" x="272" y="104" width="66" height="12" rx="5"/>
  <path fill="none" stroke-width="6" d="M184 210 L198 238"/>
  <rect class="fillable" fill="#ffffff" x="186" y="234" width="26" height="9" rx="3" stroke-width="3"/>
  <circle fill="#1a1a1a" stroke="none" cx="184" cy="210" r="4"/>
</g>
''')

add('sailboat', '⛵ 帆船', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="58" cy="52" r="26"/>
  <path class="fillable" fill="#ffffff" d="M290 60 Q290 42 310 44 Q318 28 338 34 Q356 26 362 44 Q380 46 376 60 Z"/>
  <path fill="none" stroke-width="3" d="M110 90 Q118 82 126 90 Q134 82 142 90"/>
  <path class="fillable" fill="#ffffff" d="M0 222 Q25 212 50 222 Q75 232 100 222 Q125 212 150 222 Q175 232 200 222 Q225 212 250 222 Q275 232 300 222 Q325 212 350 222 Q375 232 400 222 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="194" y="30" width="10" height="190" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M204 32 Q222 26 240 36 Q222 40 214 50 L204 48 Z"/>
  <path class="fillable" fill="#ffffff" d="M190 54 Q150 110 92 186 L142 186 Q174 120 190 54 Z"/>
  <path class="fillable" fill="#ffffff" d="M190 54 Q174 120 142 186 L190 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M208.0 64.0 L208.0 64.0 L211.6 67.1 L215.2 70.3 L218.7 73.6 L222.2 76.9 L225.7 80.3 L229.1 83.7 L232.5 87.2 L235.8 90.8 L239.1 94.5 L242.4 98.2 L245.7 102.0 L248.9 105.9 L252.0 109.8 L255.2 113.8 L258.3 117.9 L261.3 122.0 L208.0 128.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M208.0 128.0 L261.3 122.0 L262.4 123.4 L263.4 124.9 L264.5 126.3 L265.5 127.8 L266.5 129.3 L267.6 130.8 L268.6 132.2 L269.6 133.7 L270.6 135.2 L271.6 136.8 L272.6 138.3 L273.6 139.8 L274.6 141.3 L275.6 142.9 L276.6 144.4 L277.6 146.0 L208.0 152.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M208.0 152.0 L277.6 146.0 L279.1 148.4 L280.5 150.7 L282.0 153.1 L283.4 155.6 L284.9 158.0 L286.3 160.5 L287.7 162.9 L289.1 165.4 L290.5 167.9 L291.9 170.5 L293.3 173.0 L294.6 175.6 L296.0 178.1 L297.3 180.7 L298.7 183.4 L300.0 186.0 L208.0 186.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M70 194 L330 194 Q326 206 312 212 L88 212 Q74 206 70 194 Z"/>
  <path class="fillable" fill="#ffffff" d="M88 212 L312 212 Q296 240 270 246 L130 246 Q104 240 88 212 Z"/>
  <circle class="fillable" fill="#ffffff" cx="150" cy="228" r="8" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="228" r="8" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="250" cy="228" r="8" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M0 252 Q33 240 66 252 Q100 264 133 252 Q166 240 200 252 Q233 264 266 252 Q300 240 333 252 Q366 264 400 252 L400 300 L0 300 Z"/>
</g>
''')

add('helicopter', '🚁 直升机', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M330 122 Q330 104 350 106 Q358 90 376 96 Q392 92 392 108 Q396 122 384 122 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 262 Q60 236 130 248 Q200 260 270 246 Q340 232 400 254 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 130 Q110 126 56 116 Q46 114 46 124 Q46 134 56 136 Q110 150 170 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M58 118 Q46 96 40 80 Q52 78 62 88 Q72 104 74 120 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="46" cy="124" rx="7" ry="28" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="46" cy="124" r="6" stroke-width="3"/>
  <path fill="none" stroke-width="5" d="M170 214 L162 236 M260 214 L268 236"/>
  <path class="fillable" fill="#ffffff" d="M118 236 L300 236 Q318 236 318 226 Q324 226 324 232 Q322 246 300 246 L118 246 Q110 246 110 241 Q110 236 118 236 Z"/>
  <rect class="fillable" fill="#ffffff" x="206" y="52" width="16" height="26" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M214 46 Q150 38 64 44 Q54 46 54 52 Q54 58 64 58 Q150 62 214 58 Z"/>
  <path class="fillable" fill="#ffffff" d="M214 46 Q278 38 364 44 Q374 46 374 52 Q374 58 364 58 Q278 62 214 58 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="214" cy="52" rx="16" ry="10"/>
  <path class="fillable" fill="#ffffff" d="M150 112 Q156 76 214 74 Q290 74 314 130 Q328 168 300 200 Q276 220 220 220 L172 220 Q140 218 140 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M232 86 Q284 88 302 134 Q306 146 294 146 L240 146 Q230 146 230 136 L230 96 Q230 86 232 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M166 110 Q168 90 196 88 L216 88 L216 196 L170 196 Q164 196 164 188 Z" stroke-width="3"/>
  <path class="fillable" fill="#ffffff" d="M174 112 Q176 98 196 98 L206 98 L206 138 L174 138 Z" stroke-width="3"/>
  <circle fill="#1a1a1a" stroke="none" cx="208" cy="166" r="4"/>
  <path class="fillable" fill="#ffffff" d="M220 168 L318 168 Q314 182 304 194 L220 194 Z" stroke-width="3"/>
  <circle class="fillable" fill="#ffffff" cx="268" cy="124" r="18"/>
  <path class="fillable" fill="#ffffff" d="M250 120 Q252 100 268 100 Q284 100 286 120 Q276 112 268 114 Q258 112 250 120 Z"/>
  <circle fill="#1a1a1a" stroke="none" cx="262" cy="124" r="3"/>
  <circle fill="#1a1a1a" stroke="none" cx="276" cy="124" r="3"/>
  <path fill="none" stroke-width="2.5" d="M263 132 Q269 137 275 132"/>
</g>
''')

# --- Nature: +3 ---
add('cactus', '🌵 仙人掌', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="340" cy="52" r="24"/>
  <path class="fillable" fill="#ffffff" d="M 38 74 Q 38 54 60 56 Q 68 38 90 44 Q 108 36 116 56 Q 134 58 130 74 Z"/>
  <path class="fillable" fill="#ffffff" d="M 214 252 Q 300 186 400 232 L 400 262 L 214 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M 0 250 Q 100 228 200 246 Q 300 262 400 238 L 400 300 L 0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M 168 170 L 142 170 Q 126 170 126 154 L 126 116 Q 126 102 140 102 Q 154 102 154 116 L 154 148 L 168 148 Z"/>
  <path class="fillable" fill="#ffffff" d="M 232 150 L 258 150 Q 274 150 274 134 L 274 100 Q 274 86 260 86 Q 246 86 246 100 L 246 128 L 232 128 Z"/>
  <path class="fillable" fill="#ffffff" d="M 161 204 L 161 104 Q 161 64 200 64 Q 239 64 239 104 L 239 204 Z"/>
  <path fill="none" stroke-width="3" d="M 126 124 L 118 120 M 126 146 L 118 150 M 154 124 L 162 120 M 274 108 L 282 104 M 274 128 L 282 132 M 161 112 L 153 108 M 161 186 L 153 190 M 239 176 L 247 172 M 239 196 L 247 200"/>
  <path fill="none" stroke-width="3" d="M 184 164 L 184 196 M 216 164 L 216 196 M 140 112 L 140 156 M 260 98 L 260 140"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="40" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="211.4" cy="48.3" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="207.1" cy="61.7" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="192.9" cy="61.7" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="188.6" cy="48.3" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="52" r="8"/>
  <path class="fillable" fill="#ffffff" d="M 140 196 L 260 196 Q 266 196 266 204 L 266 212 Q 266 218 260 218 L 140 218 Q 134 218 134 212 L 134 204 Q 134 196 140 196 Z"/>
  <path class="fillable" fill="#ffffff" d="M 146 218 L 254 218 L 242 262 Q 240 266 234 266 L 166 266 Q 160 266 158 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M 150 232 L 250 232 L 246.4 246 L 153.6 246 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="185" cy="116" rx="7" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="215" cy="116" rx="7" ry="9"/>
  <circle fill="#1a1a1a" stroke="none" cx="186" cy="118" r="4.6"/>
  <circle fill="#ffffff" stroke="none" cx="187.8" cy="115.7" r="1.8"/>
  <circle fill="#1a1a1a" stroke="none" cx="216" cy="118" r="4.6"/>
  <circle fill="#ffffff" stroke="none" cx="217.8" cy="115.7" r="1.8"/>
  <path fill="none" stroke-width="3" d="M 193 136 Q 200 142.3 207 136"/>
  <ellipse class="fillable" fill="#ffffff" cx="176" cy="135" rx="7" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="224" cy="135" rx="7" ry="5"/>
</g>
''')

add('palm_island', '🏝️ 椰子树小岛', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="330" cy="54" r="24"/>
  <path class="fillable" fill="#ffffff" d="M 28 78 Q 28 58 50 60 Q 58 42 80 48 Q 98 40 106 60 Q 124 62 120 78 Z"/>
  <path fill="none" stroke-width="3" d="M 262 92 Q 270 84 278 92 Q 286 84 294 92"/>
  <path class="fillable" fill="#ffffff" d="M 0 204 Q 50 192 100 204 Q 150 216 200 204 Q 250 192 300 204 Q 350 216 400 204 L 400 300 L 0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M 40 250 Q 200 150 360 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M 211 214 L 215.7 190.1 Q 229.6 185.1 243.5 190.1 L 241 214 Q 226 209 211 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M 215.3 192.7 L 216.6 168.8 Q 229.5 163.8 242.3 168.8 L 243.3 192.7 Q 229.3 187.7 215.3 192.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M 216.7 171.3 L 212.2 147.4 Q 224 142.4 235.9 147.4 L 242.7 171.3 Q 229.7 166.3 216.7 171.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M 213 150 L 201.9 126.1 Q 212.7 121.1 223.6 126.1 L 237 150 Q 225 145 213 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M 203.4 128.7 L 186.6 104.8 Q 196.5 99.8 206.4 104.8 L 225.4 128.7 Q 214.4 123.7 203.4 128.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M 188.7 107.3 L 168.8 83.4 Q 177.7 78.4 186.6 83.4 L 208.7 107.3 Q 198.7 102.3 188.7 107.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M 180 86 Q 124.2 109.4 92 142 Q 147.8 146.6 180 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M 180 86 Q 137.5 71.1 92 80 Q 134.5 114.9 180 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M 180 86 Q 176.6 48.9 140 26 Q 143.4 71.1 180 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M 180 86 Q 222.1 76.1 236 30 Q 193.9 47.9 180 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M 180 86 Q 232.6 111.8 280 74 Q 227.4 68.2 180 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M 180 86 Q 214 145 270 138 Q 236 107 180 86 Z"/>
  <path fill="none" stroke-width="2.5" d="M 180 86 Q 136 128 92 142 M 180 86 Q 136 93 92 80 M 180 86 Q 160 60 140 26 M 180 86 Q 208 62 236 30 M 180 86 Q 230 90 280 74 M 180 86 Q 225 126 270 138"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="98" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="190" cy="98" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="106" r="10"/>
  <path class="fillable" fill="#ffffff" d="M 292.8 210.2 L 295.4 220.8 L 305.8 223.8 L 296.6 229.5 L 297 240.4 L 288.7 233.4 L 278.5 237.1 L 282.6 227 L 275.9 218.5 L 286.7 219.3 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="116" cy="232" rx="18" ry="10"/>
  <path fill="none" stroke-width="2.5" d="M 104 230 Q 116 222 128 230"/>
  <path class="fillable" fill="#ffffff" d="M 0 252 Q 50 240 100 252 Q 150 264 200 252 Q 250 240 300 252 Q 350 264 400 252 L 400 300 L 0 300 Z"/>
  <path fill="none" stroke-width="3" d="M 30 274 Q 50 266 70 274 M 170 280 Q 190 272 210 280 M 310 276 Q 330 268 350 276"/>
</g>
''')

add('mushroom_garden', '🍄 蘑菇林', 'nature', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="358" cy="44" r="22"/>
  <path class="fillable" fill="#ffffff" d="M 20 68 Q 20 50 39.8 51.8 Q 47 35.6 66.8 41 Q 83 33.8 90.2 51.8 Q 106.4 53.6 102.8 68 Z"/>
  <path class="fillable" fill="#ffffff" d="M 0 250 Q 100 228 200 246 Q 300 262 400 238 L 400 300 L 0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M 70 196 Q 66 228 64 254 Q 86 262 108 254 Q 104 228 100 196 Z"/>
  <path class="fillable" fill="#ffffff" d="M 36 198 Q 36 150 85 146 Q 134 150 134 198 Q 85 210 36 198 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="66" cy="172" rx="11" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="104" cy="168" rx="9" ry="7"/>
  <path class="fillable" fill="#ffffff" d="M 304 186 Q 300 222 298 252 Q 322 260 346 252 Q 344 222 340 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M 276 188 Q 278 128 322 126 Q 366 128 368 188 Q 322 198 276 188 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="304" cy="156" rx="10" ry="12"/>
  <ellipse class="fillable" fill="#ffffff" cx="342" cy="160" rx="9" ry="11"/>
  <path class="fillable" fill="#ffffff" d="M 164 126 Q 156 196 152 252 Q 200 266 248 252 Q 244 196 236 126 Z"/>
  <path class="fillable" fill="#ffffff" d="M 106 132 Q 104 46 200 42 Q 296 46 294 132 Q 200 152 106 132 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="152" cy="92" rx="18" ry="13" transform="rotate(-20 152 92)"/>
  <ellipse class="fillable" fill="#ffffff" cx="204" cy="70" rx="20" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="254" cy="98" rx="17" ry="12" transform="rotate(20 254 98)"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="118" rx="13" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="132" cy="122" rx="9" ry="6" transform="rotate(-10 132 122)"/>
  <ellipse class="fillable" fill="#ffffff" cx="268" cy="124" rx="9" ry="6" transform="rotate(10 268 124)"/>
  <ellipse class="fillable" fill="#ffffff" cx="182" cy="182" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="218" cy="182" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="183" cy="184" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="185.4" cy="181" r="2.1"/>
  <circle fill="#1a1a1a" stroke="none" cx="219" cy="184" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="221.4" cy="181" r="2.1"/>
  <path fill="none" stroke-width="3" d="M 192 204 Q 200 211.2 208 204"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="200" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="230" cy="200" rx="8" ry="5"/>
  <path fill="none" stroke-width="3" d="M 26 262 Q 24 252 18 248 M 32 262 Q 34 250 30 242 M 38 262 Q 42 252 48 250 M 126 264 Q 124 254 118 250 M 132 264 Q 134 252 130 244 M 138 264 Q 142 254 148 252 M 262 268 Q 260 258 254 254 M 268 268 Q 270 256 266 248 M 274 268 Q 278 258 284 256 M 370 258 Q 368 248 362 244 M 376 258 Q 378 246 374 238 M 382 258 Q 386 248 392 246"/>
</g>
''')

# --- Food: +4 ---
add('candy', '🍬 一堆糖果', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M 0 252 Q 100 240 200 250 Q 300 260 400 246 L 400 300 L 0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M 178.7 95.8 Q 160.8 77 144.7 82.3 Q 157.5 99.5 151.3 120.1 Q 168.3 119.5 178.7 95.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M 221.3 88.2 Q 231.7 64.5 248.7 63.9 Q 242.5 84.5 255.3 101.7 Q 239.2 107 221.3 88.2 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="92" rx="30" ry="20.4" transform="rotate(-10 200 92)"/>
  <path fill="none" stroke-width="3" d="M 187.2 74.8 Q 182.3 95.1 193.9 112.6 M 206.1 71.4 Q 201.2 91.8 212.8 109.2"/>
  <circle class="fillable" fill="#ffffff" cx="146" cy="132" r="25"/>
  <path fill="none" stroke-width="3" d="M 143.5 134.5 Q 143.5 127 149.8 127 Q 157.2 127 157.2 134.5 Q 157.2 144.5 146 144.5 Q 133.5 144.5 133.5 132 Q 133.5 117 148.5 117"/>
  <circle class="fillable" fill="#ffffff" cx="254" cy="130" r="25"/>
  <path fill="none" stroke-width="3" d="M 251.5 132.5 Q 251.5 125 257.8 125 Q 265.2 125 265.2 132.5 Q 265.2 142.5 254 142.5 Q 241.5 142.5 241.5 130 Q 241.5 115 256.5 115"/>
  <path class="fillable" fill="#ffffff" d="M 114.5 160.9 Q 108.7 136.7 92.7 133.4 Q 95.1 153.8 80.2 168 Q 94.5 175.7 114.5 160.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M 153.5 175.1 Q 173.5 160.3 187.8 168 Q 172.9 182.2 175.3 202.6 Q 159.3 199.3 153.5 175.1 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="134" cy="168" rx="28.7" ry="19.5" transform="rotate(20 134 168)"/>
  <path fill="none" stroke-width="3" d="M 131.6 147.6 Q 117.8 162.1 119.1 182.1 M 148.9 153.9 Q 135.1 168.4 136.4 188.4"/>
  <path class="fillable" fill="#ffffff" d="M 248.3 172.4 Q 228.8 157 214.2 164.1 Q 228.6 178.8 225.6 199.1 Q 241.6 196.3 248.3 172.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M 287.7 159.6 Q 294.4 135.7 310.4 132.9 Q 307.4 153.2 321.8 167.9 Q 307.2 175 287.7 159.6 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="268" cy="166" rx="28.7" ry="19.5" transform="rotate(-18 268 166)"/>
  <path fill="none" stroke-width="3" d="M 253.6 151.3 Q 251.6 171.3 264.9 186.3 M 271.1 145.7 Q 269 165.7 282.4 180.7"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="146" r="31"/>
  <ellipse class="fillable" fill="#ffffff" cx="188" cy="142" rx="6" ry="7.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="212" cy="142" rx="6" ry="7.5"/>
  <circle fill="#1a1a1a" stroke="none" cx="189" cy="144" r="4"/>
  <circle fill="#ffffff" stroke="none" cx="190.6" cy="142" r="1.8"/>
  <circle fill="#1a1a1a" stroke="none" cx="213" cy="144" r="4"/>
  <circle fill="#ffffff" stroke="none" cx="214.6" cy="142" r="1.8"/>
  <path fill="none" stroke-width="3" d="M 193 154 Q 200 160.3 207 154"/>
  <ellipse class="fillable" fill="#ffffff" cx="181" cy="154" rx="5" ry="3.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="219" cy="154" rx="5" ry="3.5"/>
  <path class="fillable" fill="#ffffff" d="M 166 250 L 160 264 Q 200 272 240 264 L 234 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M 84 180 Q 90 252 200 254 Q 310 252 316 180 Q 200 208 84 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M 98 216 Q 200 240 302 216 L 296 230 Q 200 254 104 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M 80 178 Q 200 206 320 178 Q 324 188 316 192 Q 200 220 84 192 Q 76 188 80 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M 32.2 254.5 Q 17.8 238.4 4.2 242.3 Q 14.4 257 8.7 274 Q 22.8 274 32.2 254.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M 67.8 249.5 Q 77.2 230 91.3 230 Q 85.6 247 95.8 261.7 Q 82.2 265.6 67.8 249.5 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="50" cy="252" rx="25" ry="17" transform="rotate(-8 50 252)"/>
  <path fill="none" stroke-width="3" d="M 39.9 237.3 Q 35.1 254.1 44.3 269 M 55.7 235 Q 51 251.9 60.1 266.7"/>
  <circle class="fillable" fill="#ffffff" cx="356" cy="252" r="19"/>
  <path fill="none" stroke-width="3" d="M 354.1 253.9 Q 354.1 248.2 358.9 248.2 Q 364.6 248.2 364.6 253.9 Q 364.6 261.5 356 261.5 Q 346.5 261.5 346.5 252 Q 346.5 240.6 357.9 240.6"/>
</g>
''')

add('cookies', '🍪 巧克力饼干', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 244 Q200 232 400 244 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M336 110 L344 252 Q362 258 380 252 L388 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M339 146 Q362 154 385 146 L378 250 Q362 256 346 250 Z"/>
  <path fill="none" stroke-width="3" d="M370 110 L378 64 Q380 58 386 60 L382 110"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="252" rx="150" ry="22"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="250" rx="108" ry="13"/>
  <path class="fillable" fill="#ffffff" d="M164 198 L164 214 C164 242 324 242 324 214 L324 198 C324 226 164 226 164 198 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 168 L164 184 C164 212 324 212 324 184 L324 168 C324 196 164 196 164 168 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 138 L164 154 C164 182 324 182 324 154 L324 138 C324 166 164 166 164 138 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 108 L164 124 C164 152 324 152 324 124 L324 108 C324 136 164 136 164 108 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="244" cy="108" rx="80" ry="21"/>
  <path class="fillable" fill="#ffffff" d="M 201 106 Q 202 99 210 99 Q 218 99 219 106 Q 210 110 201 106 Z"/>
  <path class="fillable" fill="#ffffff" d="M 235 98 Q 236 91 244 91 Q 252 91 253 98 Q 244 102 235 98 Z"/>
  <path class="fillable" fill="#ffffff" d="M 269 106 Q 270 99 278 99 Q 286 99 287 106 Q 278 110 269 106 Z"/>
  <path class="fillable" fill="#ffffff" d="M 219 119 Q 220 112 228 112 Q 236 112 237 119 Q 228 123 219 119 Z"/>
  <path class="fillable" fill="#ffffff" d="M 253 119 Q 254 112 262 112 Q 270 112 271 119 Q 262 123 253 119 Z"/>
  <circle class="fillable" fill="#ffffff" cx="108" cy="186" r="66"/>
  <path class="fillable" fill="#ffffff" d="M 79.9 146.5 Q 75.5 137.4 83.6 133.4 Q 92.4 131.3 94.9 141 Q 89.1 148.5 79.9 146.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M 125.1 144.2 Q 128.4 134.8 137 137.7 Q 144.7 142.4 139.6 151 Q 130.2 152.2 125.1 144.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M 51.3 211.9 Q 57 203.6 64.5 208.6 Q 70.8 215.2 63.6 222.2 Q 54.2 220.9 51.3 211.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M 155.1 221.5 Q 149.2 213.3 156.5 207.9 Q 164.8 204.3 168.9 213.5 Q 164.5 221.8 155.1 221.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M 99.4 240.6 Q 100.2 230.5 109.2 231.1 Q 117.9 233.7 115.2 243.3 Q 106.4 246.9 99.4 240.6 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="92" cy="180" rx="7.5" ry="9.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="124" cy="180" rx="7.5" ry="9.5"/>
  <circle fill="#1a1a1a" stroke="none" cx="93" cy="182" r="5"/>
  <circle fill="#ffffff" stroke="none" cx="95" cy="179.5" r="1.8"/>
  <circle fill="#1a1a1a" stroke="none" cx="125" cy="182" r="5"/>
  <circle fill="#ffffff" stroke="none" cx="127" cy="179.5" r="1.8"/>
  <path fill="none" stroke-width="3" d="M100 198 Q108 205.2 116 198"/>
  <ellipse class="fillable" fill="#ffffff" cx="78" cy="197" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="138" cy="197" rx="8" ry="5"/>
</g>
''')

add('watermelon', '🍉 西瓜', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M 16 64 Q 16 46 35.8 47.8 Q 43 31.6 62.8 37 Q 79 29.8 86.2 47.8 Q 102.4 49.6 98.8 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="318" cy="212" rx="64" ry="44"/>
  <path class="fillable" fill="#ffffff" d="M296 172.7 Q258 212 296 251.3 Q280 212 296 172.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 172.7 Q378 212 340 251.3 Q356 212 340 172.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M318 168 Q302 212 318 256 Q334 212 318 168 Z"/>
  <path fill="none" stroke-width="3" d="M318 168 Q314 156 324 152"/>
  <path class="fillable" fill="#ffffff" d="M88 112 L18 222 Q88 258 158 222 Z"/>
  <path class="fillable" fill="#ffffff" d="M 88 113.2 L 25 212.2 Q 88 244.6 151 212.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M 88 114.2 L 30.6 204.4 Q 88 233.9 145.4 204.4 Z"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="88" cy="150" rx="3" ry="5"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="70" cy="188" rx="3" ry="5"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="106" cy="188" rx="3" ry="5"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="88" cy="214" rx="3" ry="5"/>
  <path class="fillable" fill="#ffffff" d="M200 52 L96 214 Q200 266 304 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M 200 53.2 L 106.4 199 Q 200 245.8 293.6 199 Z"/>
  <path class="fillable" fill="#ffffff" d="M 200 54.2 L 114.7 187 Q 200 229.6 285.3 187 Z"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="200" cy="96" rx="3.2" ry="5.5"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="152" cy="188" rx="3.2" ry="5.5"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="248" cy="188" rx="3.2" ry="5.5"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="176" cy="210" rx="3.2" ry="5.5"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="224" cy="210" rx="3.2" ry="5.5"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="200" cy="216" rx="3.2" ry="5.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="182" cy="146" rx="8" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="218" cy="146" rx="8" ry="10"/>
  <circle fill="#1a1a1a" stroke="none" cx="183" cy="148" r="5.3"/>
  <circle fill="#ffffff" stroke="none" cx="185.1" cy="145.4" r="1.9"/>
  <circle fill="#1a1a1a" stroke="none" cx="219" cy="148" r="5.3"/>
  <circle fill="#ffffff" stroke="none" cx="221.1" cy="145.4" r="1.9"/>
  <path fill="none" stroke-width="3" d="M192 166 Q200 173.2 208 166"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="163" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="230" cy="163" rx="8" ry="5"/>
</g>
''')

add('lollipop', '🍭 棒棒糖', 'food', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M 18 66 Q 18 47 38.9 48.9 Q 46.5 31.8 67.4 37.5 Q 84.5 29.9 92.1 48.9 Q 109.2 50.8 105.4 66 Z"/>
  <circle class="fillable" fill="#ffffff" cx="360" cy="44" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M72 180 L84 180 L84 254 L72 254 Z"/>
  <circle class="fillable" fill="#ffffff" cx="78" cy="148" r="38"/>
  <circle class="fillable" fill="#ffffff" cx="78" cy="148" r="26"/>
  <circle class="fillable" fill="#ffffff" cx="78" cy="148" r="13"/>
  <path class="fillable" fill="#ffffff" d="M316 176 L328 176 L328 256 L316 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M 322 183.7 C 306.7 168.4 276 153.1 276 131.6 C 276 110.1 306.7 104 322 125.5 C 337.3 104 368 110.1 368 131.6 C 368 153.1 337.3 168.4 322 183.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M 322 168.5 C 312.7 159.2 294 149.9 294 136.8 C 294 123.7 312.7 120 322 133.1 C 331.3 120 350 123.7 350 136.8 C 350 149.9 331.3 159.2 322 168.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M193 168 L207 168 L207 254 L193 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 104 Q164.4 79.1 200 34 A70 70 0 0 1 249.5 54.5 Q192.5 61.3 200 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 104 Q192.5 61.3 249.5 54.5 A70 70 0 0 1 270 104 Q224.9 68.4 200 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 104 Q224.9 68.4 270 104 A70 70 0 0 1 249.5 153.5 Q242.7 96.5 200 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 104 Q242.7 96.5 249.5 153.5 A70 70 0 0 1 200 174 Q235.6 128.9 200 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 104 Q235.6 128.9 200 174 A70 70 0 0 1 150.5 153.5 Q207.5 146.7 200 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 104 Q207.5 146.7 150.5 153.5 A70 70 0 0 1 130 104 Q175.1 139.6 200 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 104 Q175.1 139.6 130 104 A70 70 0 0 1 150.5 54.5 Q157.3 111.5 200 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 104 Q157.3 111.5 150.5 54.5 A70 70 0 0 1 200 34 Q164.4 79.1 200 104 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="104" r="14"/>
  <path class="fillable" fill="#ffffff" d="M200 198 Q172 176 166 194 Q166 214 200 198 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 198 Q228 176 234 194 Q234 214 200 198 Z"/>
  <path fill="none" stroke-width="3" d="M196 202 Q188 216 180 224 M204 202 Q212 216 220 224"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="198" rx="8" ry="9"/>
</g>
''')

# --- Other: +3 ---
add('gift_stack', '🎁 礼物堆', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M32 210 L92 210 L92 254 L32 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M26 198 L98 198 L98 212 L26 212 Z"/>
  <path class="fillable" fill="#ffffff" d="M54 198 L68 198 L68 254 L54 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M312 212 L376 212 L376 252 L312 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M306 200 L382 200 L382 214 L306 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M337 200 L351 200 L351 252 L337 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M344 198 Q320 176 314 190 Q314 204 344 198 Z"/>
  <path class="fillable" fill="#ffffff" d="M344 198 Q368 176 374 190 Q374 204 344 198 Z"/>
  <circle class="fillable" fill="#ffffff" cx="344" cy="197" r="7"/>
  <path class="fillable" fill="#ffffff" d="M112 188 L288 188 L288 254 L112 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M104 170 L296 170 L296 190 L104 190 Z"/>
  <path class="fillable" fill="#ffffff" d="M189 170 L211 170 L211 254 L189 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M136 130 L264 130 L264 172 L136 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 114 L270 114 L270 132 L130 132 Z"/>
  <path class="fillable" fill="#ffffff" d="M136 146 L264 146 L264 160 L136 160 Z"/>
  <path class="fillable" fill="#ffffff" d="M162 84 L238 84 L238 116 L162 116 Z"/>
  <path class="fillable" fill="#ffffff" d="M156 70 L244 70 L244 86 L156 86 Z"/>
  <path class="fillable" fill="#ffffff" d="M192 70 L208 70 L208 116 L192 116 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 68 Q168 36 158 56 Q154 76 200 68 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 68 Q232 36 242 56 Q246 76 200 68 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="66" rx="10" ry="9"/>
</g>
''')

add('fireworks', '🎆 烟花', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M76 22 Q44 26 44 54 Q46 82 76 84 Q58 72 58 53 Q58 34 76 22 Z"/>
  <path class="fillable" fill="#ffffff" d="M372 19 L374.9 26 L382.5 26.6 L376.8 31.5 L378.5 38.9 L372 35 L365.5 38.9 L367.2 31.5 L361.5 26.6 L369.1 26 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 21 L198.4 26.8 L204.6 27.2 L199.8 31.2 L201.3 37.3 L196 34 L190.7 37.3 L192.2 31.2 L187.4 27.2 L193.6 26.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M122 46 L128.9 66.2 L145 52.2 L140.9 73.1 L161.8 69 L147.8 85.1 L168 92 L147.8 98.9 L161.8 115 L140.9 110.9 L145 131.8 L128.9 117.8 L122 138 L115.1 117.8 L99 131.8 L103.1 110.9 L82.2 115 L96.2 98.9 L76 92 L96.2 85.1 L82.2 69 L103.1 73.1 L99 52.2 L115.1 66.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M131.2 69.9 L130.5 83.5 L144.1 82.8 L134 92 L144.1 101.2 L130.5 100.5 L131.2 114.1 L122 104 L112.8 114.1 L113.5 100.5 L99.9 101.2 L110 92 L99.9 82.8 L113.5 83.5 L112.8 69.9 L122 80 Z"/>
  <circle class="fillable" fill="#ffffff" cx="122" cy="92" r="7.4"/>
  <path class="fillable" fill="#ffffff" d="M310.9 33.7 L312.5 56.9 L333.4 46.6 L323.1 67.5 L346.3 69.1 L327 82 L346.3 94.9 L323.1 96.5 L333.4 117.4 L312.5 107.1 L310.9 130.3 L298 111 L285.1 130.3 L283.5 107.1 L262.6 117.4 L272.9 96.5 L249.7 94.9 L269 82 L249.7 69.1 L272.9 67.5 L262.6 46.6 L283.5 56.9 L285.1 33.7 L298 53 Z"/>
  <path class="fillable" fill="#ffffff" d="M313.8 61.4 L309.3 75.5 L323.8 78.6 L310.6 85.4 L318.6 97.8 L304.5 93.3 L301.4 107.8 L294.6 94.6 L282.2 102.6 L286.7 88.5 L272.2 85.4 L285.4 78.6 L277.4 66.2 L291.5 70.7 L294.6 56.2 L301.4 69.4 Z"/>
  <circle class="fillable" fill="#ffffff" cx="298" cy="82" r="8"/>
  <path class="fillable" fill="#ffffff" d="M214 112 L219 124.6 L230.5 117.3 L227.1 130.5 L240.6 131.3 L230.2 140 L240.6 148.7 L227.1 149.5 L230.5 162.7 L219 155.4 L214 168 L209 155.4 L197.5 162.7 L200.9 149.5 L187.4 148.7 L197.8 140 L187.4 131.3 L200.9 130.5 L197.5 117.3 L209 124.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M219.6 126.5 L219.1 134.9 L227.5 134.4 L221.3 140 L227.5 145.6 L219.1 145.1 L219.6 153.5 L214 147.3 L208.4 153.5 L208.9 145.1 L200.5 145.6 L206.7 140 L200.5 134.4 L208.9 134.9 L208.4 126.5 L214 132.7 Z"/>
  <circle class="fillable" fill="#ffffff" cx="214" cy="140" r="4.5"/>
  <path fill="none" stroke-width="3" d="M122 39 L122 29 M148.5 46.1 L153.5 37.4 M167.9 65.5 L176.6 60.5 M175 92 L185 92 M167.9 118.5 L176.6 123.5 M148.5 137.9 L153.5 146.6 M122 145 L122 155 M95.5 137.9 L90.5 146.6 M76.1 118.5 L67.4 123.5 M69 92 L59 92 M76.1 65.5 L67.4 60.5 M95.5 46.1 L90.5 37.4 M312.8 26.9 L315.3 17.3 M338.3 41.7 L345.4 34.6 M353.1 67.2 L362.7 64.7 M353.1 96.8 L362.7 99.3 M338.3 122.3 L345.4 129.4 M312.8 137.1 L315.3 146.7 M283.2 137.1 L280.7 146.7 M257.7 122.3 L250.6 129.4 M242.9 96.8 L233.3 99.3 M242.9 67.2 L233.3 64.7 M257.7 41.7 L250.6 34.6 M283.2 26.9 L280.7 17.3 M214 105 L214 95 M234.6 111.7 L240.5 103.6 M247.3 129.2 L256.8 126.1 M247.3 150.8 L256.8 153.9 M234.6 168.3 L240.5 176.4 M214 175 L214 185 M193.4 168.3 L187.5 176.4 M180.7 150.8 L171.2 153.9 M180.7 129.2 L171.2 126.1 M193.4 111.7 L187.5 103.6"/>
  <path fill="none" stroke-width="3" d="M122 160 Q116 150 120 140 M298 158 Q304 150 300 134"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q200 248 400 258 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M12 262 L12 182 L46 160 L80 182 L80 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M84 168 L150 168 L150 262 L84 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M154 262 L154 196 Q188 172 222 196 L222 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M244 160 L312 160 L312 262 L244 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M316 192 L388 192 L388 262 L316 262 Z"/>
  <path fill="none" stroke-width="3" d="M24 196 L38 196 L38 210 L24 210 Z M52 196 L66 196 L66 210 L52 210 Z M24 224 L38 224 L38 238 L24 238 Z M52 224 L66 224 L66 238 L52 238 Z M96 180 L110 180 L110 194 L96 194 Z M124 180 L138 180 L138 194 L124 194 Z M96 206 L110 206 L110 220 L96 220 Z M124 206 L138 206 L138 220 L124 220 Z M96 232 L110 232 L110 246 L96 246 Z M124 232 L138 232 L138 246 L124 246 Z M166 208 L180 208 L180 222 L166 222 Z M198 208 L212 208 L212 222 L198 222 Z M166 234 L180 234 L180 248 L166 248 Z M198 234 L212 234 L212 248 L198 248 Z M256 172 L270 172 L270 186 L256 186 Z M284 172 L298 172 L298 186 L284 186 Z M256 198 L270 198 L270 212 L256 212 Z M284 198 L298 198 L298 212 L284 212 Z M256 224 L270 224 L270 238 L256 238 Z M284 224 L298 224 L298 238 L284 238 Z M328 204 L342 204 L342 218 L328 218 Z M360 204 L374 204 L374 218 L360 218 Z M328 230 L342 230 L342 244 L328 244 Z M360 230 L374 230 L374 244 L360 244 Z"/>
  <path fill="none" stroke-width="3" d="M222 262 L222 222 L244 222"/>
</g>
''')

add('balloon_bunch', '🎈 一束气球', 'other', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="364" cy="40" r="20"/>
  <path class="fillable" fill="#ffffff" d="M 10 194 Q 10 177 28.7 178.7 Q 35.5 163.4 54.2 168.5 Q 69.5 161.7 76.3 178.7 Q 91.6 180.4 88.2 194 Z"/>
  <path class="fillable" fill="#ffffff" d="M 308 224 Q 308 208 325.6 209.6 Q 332 195.2 349.6 200 Q 364 193.6 370.4 209.6 Q 384.8 211.2 381.6 224 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path fill="none" stroke-width="2.5" d="M136 128 Q161.6 181 200 214 M200 110 Q200 172 200 214 M264 128 Q238.4 181 200 214 M124 184 Q154.4 209 200 214 M200 178 Q200 206 200 214 M276 184 Q245.6 209 200 214"/>
  <path class="fillable" fill="#ffffff" d="M136 120 C98.5 90 98.5 40 136 40 C173.5 40 173.5 90 136 120 Z"/>
  <path fill="#ffffff" stroke-width="3" d="M136 119 L130 128 L142 128 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 102 C162.5 72 162.5 22 200 22 C237.5 22 237.5 72 200 102 Z"/>
  <path fill="#ffffff" stroke-width="3" d="M200 101 L194 110 L206 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M264 120 C226.5 90 226.5 40 264 40 C301.5 40 301.5 90 264 120 Z"/>
  <path fill="#ffffff" stroke-width="3" d="M264 119 L258 128 L270 128 Z"/>
  <path class="fillable" fill="#ffffff" d="M124 176 C86.5 146 86.5 96 124 96 C161.5 96 161.5 146 124 176 Z"/>
  <path fill="#ffffff" stroke-width="3" d="M124 175 L118 184 L130 184 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 170 C162.5 140 162.5 90 200 90 C237.5 90 237.5 140 200 170 Z"/>
  <path fill="#ffffff" stroke-width="3" d="M200 169 L194 178 L206 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M276 176 C238.5 146 238.5 96 276 96 C313.5 96 313.5 146 276 176 Z"/>
  <path fill="#ffffff" stroke-width="3" d="M276 175 L270 184 L282 184 Z"/>
  <path fill="none" stroke-width="3" d="M102 134 Q104 112 120 106 M178 128 Q180 106 196 100 M254 134 Q256 112 272 106 M114 78 Q116 56 132 50 M242 78 Q244 56 260 50 M178 60 Q180 38 196 32"/>
  <ellipse class="fillable" fill="#ffffff" cx="187" cy="132" rx="6" ry="7.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="213" cy="132" rx="6" ry="7.5"/>
  <circle fill="#1a1a1a" stroke="none" cx="188" cy="134" r="4"/>
  <circle fill="#ffffff" stroke="none" cx="189.6" cy="132" r="1.8"/>
  <circle fill="#1a1a1a" stroke="none" cx="214" cy="134" r="4"/>
  <circle fill="#ffffff" stroke="none" cx="215.6" cy="132" r="1.8"/>
  <path fill="none" stroke-width="3" d="M194 145 Q200 150.4 206 145"/>
  <ellipse class="fillable" fill="#ffffff" cx="179" cy="145" rx="6" ry="4"/>
  <ellipse class="fillable" fill="#ffffff" cx="221" cy="145" rx="6" ry="4"/>
  <path class="fillable" fill="#ffffff" d="M180 226 L220 226 L220 256 L180 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M176 218 L224 218 L224 228 L176 228 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 216 Q180 200 176 212 Q176 224 200 216 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 216 Q220 200 224 212 Q224 224 200 216 Z"/>
  <circle fill="#ffffff" stroke-width="3" cx="200" cy="216" r="6"/>
</g>
''')

# --- People (10) ---
add('family', '👨‍👩‍👧 一家四口', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="46" r="22"/>
  <path class="fillable" fill="#ffffff" d="M 18 66 Q 18 48 37.8 49.8 Q 45 33.6 64.8 39 Q 81 31.8 88.2 49.8 Q 104.4 51.6 100.8 66 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 252 Q100 236 200 248 Q300 260 400 244 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M 51.6 241.2 L 52.8 256.8 L 64.2 256.8 L 64.8 241.2 Z M 67.2 241.2 L 67.8 256.8 L 79.2 256.8 L 80.4 241.2 Z"/>
  <path class="fillable" fill="#ffffff" d="M 46.8 262.8 Q 46.8 255.6 56.4 255.6 Q 64.8 255.6 64.8 262.8 Z M 67.2 262.8 Q 67.2 255.6 75.6 255.6 Q 85.2 255.6 85.2 262.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M 45.6 243.6 Q 44.4 232.8 46.8 224.4 Q 42 228 37.2 231 Q 28.8 231.6 27.6 223.2 Q 37.2 211.2 51.6 206.4 Q 66 201.6 80.4 206.4 Q 94.8 211.2 104.4 223.2 Q 103.2 231.6 94.8 231 Q 90 228 85.2 224.4 Q 87.6 232.8 86.4 243.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M 99.6 174 C 99.6 192.5 84.5 207.6 66 207.6 C 47.5 207.6 32.4 192.5 32.4 174 C 32.4 155.5 47.5 140.4 66 140.4 C 84.5 140.4 99.6 155.5 99.6 174 Z M 36 228 C 36 231.3 33.3 234 30 234 C 26.7 234 24 231.3 24 228 C 24 224.7 26.7 222 30 222 C 33.3 222 36 224.7 36 228 Z M 108 228 C 108 231.3 105.3 234 102 234 C 98.7 234 96 231.3 96 228 C 96 224.7 98.7 222 102 222 C 105.3 222 108 224.7 108 228 Z"/>
  <path class="fillable" fill="#ffffff" d="M 33.6 171.6 Q 31.2 140.4 66 138 Q 100.8 140.4 98.4 171.6 Q 92.4 157.2 82.8 156 Q 74.4 162 66 154.8 Q 57.6 162 49.2 156 Q 38.4 158.4 33.6 171.6 Z"/>
  <path fill="none" stroke-width="3" d="M 66 138 Q 68.4 129.6 75.6 130.8"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="54" cy="181.2" rx="3" ry="4.2"/>
  <circle fill="#ffffff" stroke="none" cx="54.9" cy="179.7" r="1.2"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="78" cy="181.2" rx="3" ry="4.2"/>
  <circle fill="#ffffff" stroke="none" cx="78.9" cy="179.7" r="1.2"/>
  <path fill="none" stroke-width="3" d="M 61.2 192 Q 66 196.3 70.8 192"/>
  <path class="fillable" fill="#ffffff" d="M 137.8 232.5 L 139.5 254.3 L 155.5 254.3 L 156.3 232.5 Z M 159.7 232.5 L 160.5 254.3 L 176.5 254.3 L 178.2 232.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M 131.1 262.7 Q 131.1 252.6 144.6 252.6 Q 156.3 252.6 156.3 262.7 Z M 159.7 262.7 Q 159.7 252.6 171.4 252.6 Q 184.9 252.6 184.9 262.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M 129.4 235.8 Q 127.8 220.7 131.1 209 Q 124.4 214 117.7 218.2 Q 105.9 219 104.2 207.3 Q 117.7 190.5 137.8 183.8 Q 158 177 178.2 183.8 Q 198.3 190.5 211.8 207.3 Q 210.1 219 198.3 218.2 Q 191.6 214 184.9 209 Q 188.2 220.7 186.6 235.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M 205 138.4 C 205 164.4 184 185.4 158 185.4 C 132 185.4 111 164.4 111 138.4 C 111 112.4 132 91.4 158 91.4 C 184 91.4 205 112.4 205 138.4 Z M 116 214 C 116 218.6 112.2 222.4 107.6 222.4 C 103 222.4 99.2 218.6 99.2 214 C 99.2 209.4 103 205.6 107.6 205.6 C 112.2 205.6 116 209.4 116 214 Z M 216.8 214 C 216.8 218.6 213 222.4 208.4 222.4 C 203.8 222.4 200 218.6 200 214 C 200 209.4 203.8 205.6 208.4 205.6 C 213 205.6 216.8 209.4 216.8 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M 112.6 135 Q 109.3 89.7 158 88 Q 206.7 89.7 203.4 135 Q 200 114.9 188.2 109.8 Q 169.8 118.2 153 108.2 Q 134.5 118.2 122.7 113.2 Q 116 121.6 112.6 135 Z"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="141.2" cy="148.5" rx="4.2" ry="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="142.5" cy="146.4" r="1.7"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="174.8" cy="148.5" rx="4.2" ry="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="176.1" cy="146.4" r="1.7"/>
  <path fill="none" stroke-width="3" d="M 151.3 163.6 Q 158 169.6 164.7 163.6"/>
  <path class="fillable" fill="#ffffff" d="M 208.8 144 Q 204 96 252 92.8 Q 300 96 295.2 144 L 303.2 200 Q 287.2 209.6 274.4 196.8 L 229.6 196.8 Q 216.8 209.6 200.8 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M 237.6 246.4 L 237.6 256 L 248.8 256 L 248.8 246.4 Z M 255.2 246.4 L 255.2 256 L 266.4 256 L 266.4 246.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M 226.4 262.4 Q 226.4 252.8 239.2 252.8 Q 250.4 252.8 250.4 262.4 Z M 253.6 262.4 Q 253.6 252.8 264.8 252.8 Q 277.6 252.8 277.6 262.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M 212 246.4 Q 220 225.6 226.4 211.2 Q 220 216 213.6 220 Q 202.4 220.8 200.8 209.6 Q 213.6 193.6 232.8 187.2 Q 252 180.8 271.2 187.2 Q 290.4 193.6 303.2 209.6 Q 301.6 220.8 290.4 220 Q 284 216 277.6 211.2 Q 284 225.6 292 246.4 Q 252 254.4 212 246.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M 296.8 144 C 296.8 168.7 276.7 188.8 252 188.8 C 227.3 188.8 207.2 168.7 207.2 144 C 207.2 119.3 227.3 99.2 252 99.2 C 276.7 99.2 296.8 119.3 296.8 144 Z M 212 216 C 212 220.4 208.4 224 204 224 C 199.6 224 196 220.4 196 216 C 196 211.6 199.6 208 204 208 C 208.4 208 212 211.6 212 216 Z M 308 216 C 308 220.4 304.4 224 300 224 C 295.6 224 292 220.4 292 216 C 292 211.6 295.6 208 300 208 C 304.4 208 308 211.6 308 216 Z"/>
  <path class="fillable" fill="#ffffff" d="M 207.2 147.2 Q 205.6 100.8 252 97.6 Q 298.4 100.8 296.8 147.2 Q 290.4 123.2 271.2 116.8 Q 248.8 129.6 226.4 120 Q 212 129.6 207.2 147.2 Z"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="236" cy="153.6" rx="4" ry="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="237.2" cy="151.6" r="1.6"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="268" cy="153.6" rx="4" ry="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="269.2" cy="151.6" r="1.6"/>
  <path fill="none" stroke-width="3" d="M 245.6 168 Q 252 173.8 258.4 168"/>
  <path class="fillable" fill="#ffffff" d="M 314 158.4 C 314 165 308.6 170.4 302 170.4 C 295.4 170.4 290 165 290 158.4 C 290 151.8 295.4 146.4 302 146.4 C 308.6 146.4 314 151.8 314 158.4 Z M 386 158.4 C 386 165 380.6 170.4 374 170.4 C 367.4 170.4 362 165 362 158.4 C 362 151.8 367.4 146.4 374 146.4 C 380.6 146.4 386 151.8 386 158.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M 327.2 250.8 L 327.2 258 L 335.6 258 L 335.6 250.8 Z M 340.4 250.8 L 340.4 258 L 348.8 258 L 348.8 250.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M 318.8 262.8 Q 318.8 255.6 328.4 255.6 Q 336.8 255.6 336.8 262.8 Z M 339.2 262.8 Q 339.2 255.6 347.6 255.6 Q 357.2 255.6 357.2 262.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M 308 250.8 Q 314 235.2 318.8 224.4 Q 314 228 309.2 231 Q 300.8 231.6 299.6 223.2 Q 309.2 211.2 323.6 206.4 Q 338 201.6 352.4 206.4 Q 366.8 211.2 376.4 223.2 Q 375.2 231.6 366.8 231 Q 362 228 357.2 224.4 Q 362 235.2 368 250.8 Q 338 256.8 308 250.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M 371.6 174 C 371.6 192.5 356.5 207.6 338 207.6 C 319.5 207.6 304.4 192.5 304.4 174 C 304.4 155.5 319.5 140.4 338 140.4 C 356.5 140.4 371.6 155.5 371.6 174 Z M 308 228 C 308 231.3 305.3 234 302 234 C 298.7 234 296 231.3 296 228 C 296 224.7 298.7 222 302 222 C 305.3 222 308 224.7 308 228 Z M 380 228 C 380 231.3 377.3 234 374 234 C 370.7 234 368 231.3 368 228 C 368 224.7 370.7 222 374 222 C 377.3 222 380 224.7 380 228 Z"/>
  <path class="fillable" fill="#ffffff" d="M 304.4 174 Q 303.2 140.4 338 139.2 Q 372.8 140.4 371.6 174 Q 365.6 156 352.4 154.8 Q 345.2 163.2 338 156 Q 330.8 163.2 323.6 154.8 Q 310.4 156 304.4 174 Z"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="326" cy="181.2" rx="3" ry="4.2"/>
  <circle fill="#ffffff" stroke="none" cx="326.9" cy="179.7" r="1.2"/>
  <ellipse fill="#1a1a1a" stroke="none" cx="350" cy="181.2" rx="3" ry="4.2"/>
  <circle fill="#ffffff" stroke="none" cx="350.9" cy="179.7" r="1.2"/>
  <path fill="none" stroke-width="3" d="M 333.2 192 Q 338 196.3 342.8 192"/>
</g>
''')

add('baby', '👶 小宝宝', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="46" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M36 204 L92 204 L92 256 L36 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M 47.7 148.8 L 97.2 155.7 L 90.3 205.2 L 40.8 198.3 Z"/>
  <path fill="none" stroke-width="3" d="M38 216 L56 216 M72 232 L84 232"/>
  <circle class="fillable" fill="#ffffff" cx="340" cy="226" r="32"/>
  <path class="fillable" fill="#ffffff" d="M318 203 Q340 226 318 249 L330 256 Q352 226 330 196 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 250 Q138 200 166 172 L234 172 Q262 200 250 250 Q200 262 150 250 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="248" rx="30" ry="15" transform="rotate(-12 150 248)"/>
  <ellipse class="fillable" fill="#ffffff" cx="250" cy="248" rx="30" ry="15" transform="rotate(12 250 248)"/>
  <ellipse class="fillable" fill="#ffffff" cx="122" cy="252" rx="13" ry="15" transform="rotate(-12 122 252)"/>
  <ellipse class="fillable" fill="#ffffff" cx="278" cy="252" rx="13" ry="15" transform="rotate(12 278 252)"/>
  <path class="fillable" fill="#ffffff" d="M174 174 Q200 170 226 174 Q228 204 200 208 Q172 204 174 174 Z"/>
  <path class="fillable" fill="#ffffff" d="M 108.7 156.3 L 117.3 151.3 L 145.3 199.7 L 136.7 204.7 Z"/>
  <circle class="fillable" fill="#ffffff" cx="114" cy="150" r="17"/>
  <path fill="none" stroke-width="2.5" d="M104 142 L124 158 M104 158 L124 142"/>
  <path class="fillable" fill="#ffffff" d="M172 182 Q150 190 140 210 Q146 222 158 218 Q166 202 180 198 Z"/>
  <circle class="fillable" fill="#ffffff" cx="146" cy="214" r="11"/>
  <path class="fillable" fill="#ffffff" d="M 228 182 Q 250 190 256 212 Q 250 224 238 220 Q 232 202 220 198 Z"/>
  <circle class="fillable" fill="#ffffff" cx="250" cy="218" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="136" cy="120" r="12"/>
  <circle class="fillable" fill="#ffffff" cx="264" cy="120" r="12"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="112" r="64"/>
  <path fill="none" stroke-width="3" d="M200 48 Q188 32 202 26 Q216 24 216 36 Q214 46 204 42"/>
  <ellipse class="fillable" fill="#ffffff" cx="178" cy="116" rx="10" ry="12"/>
  <ellipse class="fillable" fill="#ffffff" cx="222" cy="116" rx="10" ry="12"/>
  <circle fill="#1a1a1a" stroke="none" cx="179" cy="118" r="6.6"/>
  <circle fill="#ffffff" stroke="none" cx="181.6" cy="114.7" r="2.4"/>
  <circle fill="#1a1a1a" stroke="none" cx="223" cy="118" r="6.6"/>
  <circle fill="#ffffff" stroke="none" cx="225.6" cy="114.7" r="2.4"/>
  <ellipse class="fillable" fill="#ffffff" cx="162" cy="136" rx="10" ry="6.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="238" cy="136" rx="10" ry="6.5"/>
  <path class="fillable" fill="#ffffff" stroke-width="3" d="M190 140 Q200 154 210 140 Z"/>
</g>
''')

add('chef', '👨‍🍳 厨师', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M 16 64 Q 16 46 35.8 47.8 Q 43 31.6 62.8 37 Q 79 29.8 86.2 47.8 Q 102.4 49.6 98.8 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 220 L179 248 L197 248 L198 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 220 L203 248 L221 248 L222 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M168 256 Q168 244 184 244 Q198 244 198 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 256 Q202 244 216 244 Q232 244 232 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M166 226 Q162 190 174 164 Q200 156 226 164 Q238 190 234 226 Z"/>
  <path class="fillable" fill="#ffffff" d="M184 162 L216 162 L200 188 Z"/>
  <path fill="none" stroke-width="7" d="M190 196 L190 196 M210 196 L210 196 M190 214 L190 214 M210 214 L210 214"/>
  <path class="fillable" fill="#ffffff" d="M178 166 Q156 174 146 202 Q152 212 162 208 Q168 190 182 184 Z"/>
  <circle class="fillable" fill="#ffffff" cx="153" cy="211" r="10"/>
  <path class="fillable" fill="#ffffff" d="M268 196 L314 184 L318 194 L272 208 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="338" cy="182" rx="34" ry="18" transform="rotate(-12 338 182)"/>
  <path class="fillable" fill="#ffffff" d="M318 178 Q330 164 344 170 Q362 168 358 184 Q352 196 336 192 Q318 194 318 178 Z"/>
  <circle class="fillable" fill="#ffffff" cx="338" cy="180" r="8"/>
  <path class="fillable" fill="#ffffff" d="M222 168 Q248 176 262 194 Q258 206 248 206 Q238 192 218 186 Z"/>
  <circle class="fillable" fill="#ffffff" cx="270" cy="198" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="145" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="255" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="56"/>
  <path class="fillable" fill="#ffffff" d="M146 104 Q144 80 162 74 L238 74 Q256 80 254 104 Q246 90 234 88 L166 88 Q154 90 146 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M156 54 Q130 48 136 28 Q144 12 164 18 Q176 6 200 10 Q224 6 236 18 Q256 12 264 28 Q270 48 244 54 Z"/>
  <path class="fillable" fill="#ffffff" d="M152 82 Q200 70 248 82 L246 54 Q200 46 154 54 Z"/>
  <path fill="none" stroke-width="3" d="M176 30 Q182 40 180 50 M224 30 Q218 40 220 50"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="120" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="183.4" cy="119" r="2.1"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="223.4" cy="119" r="2.1"/>
  <path fill="none" stroke-width="3" d="M191 142 Q200 150.1 209 142"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="138" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="138" rx="9" ry="6"/>
</g>
''')

add('doctor', '👩‍⚕️ 医生', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M 16 64 Q 16 46 35.8 47.8 Q 43 31.6 62.8 37 Q 79 29.8 86.2 47.8 Q 102.4 49.6 98.8 64 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 220 L179 248 L197 248 L198 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 220 L203 248 L221 248 L222 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M168 256 Q168 244 184 244 Q198 244 198 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 256 Q202 244 216 244 Q232 244 232 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 166 L220 166 L220 232 L180 232 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 170 L204 170 L208 200 L200 210 L192 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 238 Q158 194 174 166 L192 162 L196 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M 236 238 Q 242 194 226 166 L 208 162 L 204 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M212 200 L228 200 L228 214 L212 214 Z"/>
  <path fill="none" stroke-width="2.5" d="M214 200 L214 192 M220 200 L220 190"/>
  <path fill="none" stroke-width="3" d="M180 168 Q170 192 178 206"/>
  <circle class="fillable" fill="#ffffff" cx="179" cy="212" r="8"/>
  <path class="fillable" fill="#ffffff" d="M126 222 L180 222 Q184 222 184 226 L184 256 Q184 260 180 260 L126 260 Q122 260 122 256 L122 226 Q122 222 126 222 Z"/>
  <path fill="none" stroke-width="3" d="M140 222 L140 212 Q140 204 148 204 L158 204 Q166 204 166 212 L166 222"/>
  <path class="fillable" fill="#ffffff" d="M 148 228 L 158 228 L 158 236 L 166 236 L 166 246 L 158 246 L 158 254 L 148 254 L 148 246 L 140 246 L 140 236 L 148 236 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 166 Q156 174 146 202 Q152 212 162 208 Q168 190 182 184 Z"/>
  <circle class="fillable" fill="#ffffff" cx="153" cy="211" r="10"/>
  <path class="fillable" fill="#ffffff" d="M 222 166 Q 244 174 254 202 Q 248 212 238 208 Q 232 190 218 184 Z"/>
  <circle class="fillable" fill="#ffffff" cx="247" cy="211" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="145" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="255" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="56"/>
  <path class="fillable" fill="#ffffff" d="M144 112 Q140 52 200 50 Q262 52 256 112 Q252 88 238 80 Q212 94 182 78 Q158 86 144 112 Z"/>
  <path fill="none" stroke-width="3" d="M150 82 Q200 66 250 82"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="70" r="13"/>
  <path fill="none" stroke-width="2.5" d="M194 66 Q198 62 204 64"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="120" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="183.4" cy="119" r="2.1"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="223.4" cy="119" r="2.1"/>
  <path fill="none" stroke-width="3" d="M191 142 Q200 150.1 209 142"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="138" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="138" rx="9" ry="6"/>
</g>
''')

add('fireman', '👨‍🚒 消防员', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M312 256 L312 200 Q312 186 334 184 Q356 186 356 200 L356 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M318 186 Q320 168 334 166 Q348 168 350 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 206 L312 206 L312 226 L300 226 Z"/>
  <path class="fillable" fill="#ffffff" d="M304 248 L364 248 L364 260 L304 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M176 230 L176 258 Q186 262 199 258 L198 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 230 L201 258 Q214 262 224 258 L224 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M166 226 Q162 190 174 164 Q200 156 226 164 Q238 190 234 226 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 204 L235 204 L235 216 L165 216 Z"/>
  <path fill="none" stroke-width="3" d="M182 166 L200 182 L218 166"/>
  <path class="fillable" fill="#ffffff" d="M178 166 Q156 174 146 202 Q152 212 162 208 Q168 190 182 184 Z"/>
  <circle class="fillable" fill="#ffffff" cx="153" cy="211" r="10"/>
  <path class="fillable" fill="#ffffff" d="M244 206 Q250 262 304 224 L304 210 Q262 238 258 204 Z"/>
  <path class="fillable" fill="#ffffff" d="M 266.1 164.4 L 279.9 172.4 L 261.9 203.6 L 248.1 195.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M276.7 163.3 Q289.2 109.3 328.1 67.8 Q326.1 51 311.9 60.2 Q279.4 104.8 271.3 160.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M275.8 164.4 Q317.6 123.8 372.1 100 Q378.7 82.3 359.9 84 Q310.3 114.3 272.2 159.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M274.6 164.9 Q328.5 148.5 385.8 148.8 Q398.1 137.2 382.2 131.2 Q326.4 137.9 273.4 159.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M222 168 Q244 172 256 192 Q252 204 242 204 Q234 192 218 186 Z"/>
  <circle class="fillable" fill="#ffffff" cx="252" cy="200" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="145" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="255" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="56"/>
  <path class="fillable" fill="#ffffff" d="M142 100 Q140 40 200 38 Q260 40 258 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M126 100 Q200 84 274 100 Q280 112 266 112 Q200 98 134 112 Q120 112 126 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M186 48 L214 48 L216 70 Q200 84 184 70 Z"/>
  <path fill="none" stroke-width="3" d="M200 40 L200 46 M152 60 Q174 46 186 48 M248 60 Q226 46 214 48"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="120" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="183.4" cy="119" r="2.1"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="223.4" cy="119" r="2.1"/>
  <path fill="none" stroke-width="3" d="M191 142 Q200 150.1 209 142"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="138" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="138" rx="9" ry="6"/>
</g>
''')

add('astronaut', '👨‍🚀 宇航员', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M86 58 C86 71.3 75.3 82 62 82 C48.7 82 38 71.3 38 58 C38 44.7 48.7 34 62 34 C75.3 34 86 44.7 86 58 Z"/>
  <path class="fillable" fill="#ffffff" d="M26 70 Q16 56 62 48 Q108 42 98 56 Q96 64 86 66 Q96 58 80 58 Q50 58 38 66 Q30 72 26 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M352 28 L355.2 35.6 L363.4 36.3 L357.2 41.7 L359.1 49.7 L352 45.5 L344.9 49.7 L346.8 41.7 L340.6 36.3 L348.8 35.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 87 L302.4 92.8 L308.6 93.2 L303.8 97.2 L305.3 103.3 L300 100 L294.7 103.3 L296.2 97.2 L291.4 93.2 L297.6 92.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 246 Q100 232 200 244 Q300 256 400 238 L400 300 L0 300 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="70" cy="268" rx="26" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="330" cy="272" rx="30" ry="9"/>
  <path fill="none" stroke-width="5" d="M298 254 L298 126"/>
  <path class="fillable" fill="#ffffff" d="M300 128 Q320 120 338 128 Q356 136 372 128 L372 162 Q356 170 338 162 Q320 154 300 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M334 135 L336.6 141.4 L343.5 141.9 L338.3 146.4 L339.9 153.1 L334 149.5 L328.1 153.1 L329.7 146.4 L324.5 141.9 L331.4 141.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 168 L250 168 Q256 168 256 174 L256 222 Q256 228 250 228 L150 228 Q144 228 144 222 L144 174 Q144 168 150 168 Z"/>
  <path class="fillable" fill="#ffffff" d="M174 222 L174 248 L198 248 L198 222 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 222 L202 248 L226 248 L226 222 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 258 Q164 242 184 242 Q200 242 200 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 258 Q200 242 216 242 Q236 242 236 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 230 Q156 190 172 164 Q200 156 228 164 Q244 190 240 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M182 184 L218 184 L218 210 L182 210 Z"/>
  <path fill="none" stroke-width="4" d="M190 197 L196 197 M204 197 L210 197"/>
  <path class="fillable" fill="#ffffff" d="M176 170 Q150 162 140 134 Q146 122 158 126 Q164 146 184 154 Z"/>
  <circle class="fillable" fill="#ffffff" cx="148" cy="124" r="12"/>
  <path class="fillable" fill="#ffffff" d="M224 168 Q252 180 274 196 Q272 210 262 208 Q244 196 218 186 Z"/>
  <circle class="fillable" fill="#ffffff" cx="282" cy="200" r="12"/>
  <path fill="none" stroke-width="3" d="M282 200 L298 200"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="106" r="66"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="112" r="48"/>
  <path class="fillable" fill="#ffffff" d="M152 112 Q150 66 200 64 Q250 66 248 112 Q240 92 224 88 Q204 96 182 86 Q160 92 152 112 Z"/>
  <path fill="none" stroke-width="4" d="M200 40 L200 26"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="20" r="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="182" cy="122" rx="8.5" ry="10.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="218" cy="122" rx="8.5" ry="10.5"/>
  <circle fill="#1a1a1a" stroke="none" cx="183" cy="124" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="185.2" cy="121.2" r="2"/>
  <circle fill="#1a1a1a" stroke="none" cx="219" cy="124" r="5.6"/>
  <circle fill="#ffffff" stroke="none" cx="221.2" cy="121.2" r="2"/>
  <path fill="none" stroke-width="3" d="M192 142 Q200 149.2 208 142"/>
  <ellipse class="fillable" fill="#ffffff" cx="168" cy="138" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="232" cy="138" rx="8" ry="5"/>
  <path fill="none" stroke-width="3" d="M232 62 Q250 70 258 90"/>
</g>
''')

add('superhero', '🦸 超级英雄', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M 18 66 Q 18 48 37.8 49.8 Q 45 33.6 64.8 39 Q 81 31.8 88.2 49.8 Q 104.4 51.6 100.8 66 Z"/>
  <path class="fillable" fill="#ffffff" d="M 314 170 Q 314 155 330.5 156.5 Q 336.5 143 353 147.5 Q 366.5 141.5 372.5 156.5 Q 386 158 383 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M172 166 Q136 206 120 260 Q160 248 200 258 Q240 248 280 260 Q264 206 228 166 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 220 L179 248 L197 248 L198 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 220 L203 248 L221 248 L222 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M176 230 L176 258 Q186 262 199 258 L198 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 230 L201 258 Q214 262 224 258 L224 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M166 226 Q162 190 174 164 Q200 156 226 164 Q238 190 234 226 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 177 L204.1 186.3 L214.3 187.4 L206.7 194.2 L208.8 204.1 L200 199 L191.2 204.1 L193.3 194.2 L185.7 187.4 L195.9 186.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M167 212 L233 212 L233 224 L167 224 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 166 Q152 176 150 200 Q158 210 168 204 Q168 190 182 184 Z"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="206" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="145" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="255" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="56"/>
  <path class="fillable" fill="#ffffff" d="M224 172 Q268 172 290 124 Q286 112 274 114 Q258 150 220 158 Z"/>
  <circle class="fillable" fill="#ffffff" cx="282" cy="112" r="13"/>
  <path fill="none" stroke-width="2.5" d="M275 104 L289 104 M274 111 L290 111"/>
  <path class="fillable" fill="#ffffff" d="M144 112 Q140 52 200 48 Q262 52 256 112 Q250 84 232 78 Q212 72 202 84 Q190 70 168 78 Q150 86 144 112 Z"/>
  <path fill="none" stroke-width="3" d="M202 50 Q194 36 206 32 Q216 32 212 42"/>
  <path class="fillable" fill="#ffffff" d="M156 112 Q178 98 200 110 Q222 98 244 112 Q248 128 232 134 Q214 136 200 124 Q186 136 168 134 Q152 128 156 112 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="120" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="183.4" cy="119" r="2.1"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="223.4" cy="119" r="2.1"/>
  <path fill="none" stroke-width="3" d="M191 142 Q200 150.1 209 142"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="138" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="138" rx="9" ry="6"/>
</g>
''')

add('painter', '🎨 画家', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M282 168 L262 256 L274 256 L294 168 Z M348 168 L368 256 L356 256 L336 168 Z"/>
  <path class="fillable" fill="#ffffff" d="M262 70 L370 70 L370 162 L262 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 156 Q300 116 330 140 Q348 128 364 156 Z"/>
  <circle class="fillable" fill="#ffffff" cx="336" cy="98" r="14"/>
  <path class="fillable" fill="#ffffff" d="M256 160 L376 160 L376 172 L256 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M 143 220 L 144 248 L 162 248 L 163 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M 167 220 L 168 248 L 186 248 L 187 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M 133 256 Q 133 244 149 244 Q 163 244 163 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M 167 256 Q 167 244 181 244 Q 197 244 197 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M 127 236 Q 123 190 139 164 Q 165 156 191 164 Q 207 190 203 236 Z"/>
  <path fill="none" stroke-width="3" d="M 145 166 L 165 184 L 185 166"/>
  <path class="fillable" fill="#ffffff" d="M 143 166 Q 121 174 111 202 Q 117 212 127 208 Q 133 190 147 184 Z"/>
  <path class="fillable" fill="#ffffff" d="M 63 190 Q 83 172 115 178 Q 135 184 131 202 Q 125 212 133 222 Q 125 238 93 236 Q 59 232 55 212 Q 53 198 63 190 Z"/>
  <circle class="fillable" fill="#ffffff" cx="75" cy="198" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="97" cy="189" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="81" cy="220" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="125" cy="211" r="10"/>
  <path class="fillable" fill="#ffffff" d="M 240.8 117.5 L 246 123.6 L 209.2 154.5 L 204 148.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M 247 118 Q 257 106 265 110 Q 263 120 251 126 Z"/>
  <path class="fillable" fill="#ffffff" d="M 187 168 Q 213 168 227 150 Q 225 138 215 140 Q 205 152 183 156 Z"/>
  <circle class="fillable" fill="#ffffff" cx="222" cy="142" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="165" cy="110" r="56"/>
  <path class="fillable" fill="#ffffff" d="M 107 124 Q 101 60 165 58 Q 229 60 223 124 Q 217 96 203 88 L 127 88 Q 113 96 107 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M 113 74 Q 113 38 169 38 Q 223 40 223 76 Q 165 60 113 74 Z"/>
  <path fill="none" stroke-width="4" d="M 171 38 L 175 28"/>
  <ellipse class="fillable" fill="#ffffff" cx="145" cy="120" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="185" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="146" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="148.4" cy="119" r="2.1"/>
  <circle fill="#1a1a1a" stroke="none" cx="186" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="188.4" cy="119" r="2.1"/>
  <path fill="none" stroke-width="3" d="M 156 142 Q 165 150.1 174 142"/>
  <ellipse class="fillable" fill="#ffffff" cx="129" cy="138" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="201" cy="138" rx="9" ry="6"/>
</g>
''')

add('ballerina', '🩰 芭蕾舞者', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 250 Q200 240 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M10 10 L84 10 Q70 90 92 186 Q52 196 10 184 Z"/>
  <path class="fillable" fill="#ffffff" d="M 390 10 L 316 10 Q 330 90 308 186 Q 348 196 390 184 Z"/>
  <path fill="none" stroke-width="3" d="M30 20 Q34 100 26 176 M56 20 Q56 100 66 186 M370 20 Q366 100 374 176 M344 20 Q344 100 334 186"/>
  <path class="fillable" fill="#ffffff" d="M185 226 L186 252 L196 252 L196 226 Z"/>
  <path class="fillable" fill="#ffffff" d="M204 226 L204 252 L214 252 L215 226 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="183" cy="255" rx="13" ry="6.5" transform="rotate(20 183 255)"/>
  <ellipse class="fillable" fill="#ffffff" cx="217" cy="255" rx="13" ry="6.5" transform="rotate(-20 217 255)"/>
  <path fill="none" stroke-width="2.5" d="M186 238 L196 246 M196 238 L186 246 M204 238 L214 246 M214 238 L204 246"/>
  <path class="fillable" fill="#ffffff" d="M124 214 Q140 190 200 194 Q260 190 276 214 Q262 236 200 232 Q138 236 124 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 216 Q172 190 180 166 Q200 160 220 166 Q228 190 222 216 Z"/>
  <path class="fillable" fill="#ffffff" d="M144 210 Q200 198 256 210 Q264 224 248 226 Q240 236 224 230 Q212 240 200 232 Q188 240 176 230 Q160 236 152 226 Q136 224 144 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M182 176 Q150 176 126 160 Q112 156 116 144 Q122 134 134 142 Q156 158 184 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M 218 176 Q 250 176 274 160 Q 288 156 284 144 Q 278 134 266 142 Q 244 158 216 162 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="50" r="20"/>
  <circle class="fillable" fill="#ffffff" cx="145" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="255" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="56"/>
  <path class="fillable" fill="#ffffff" d="M144 116 Q140 58 200 56 Q260 58 256 116 Q250 88 230 80 Q206 92 172 80 Q150 88 144 116 Z"/>
  <path class="fillable" fill="#ffffff" d="M176 64 L182 46 L192 58 L200 40 L208 58 L218 46 L224 64 Q200 56 176 64 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="120" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="183.4" cy="119" r="2.1"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="223.4" cy="119" r="2.1"/>
  <path fill="none" stroke-width="3" d="M191 142 Q200 150.1 209 142"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="138" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="138" rx="9" ry="6"/>
</g>
''')

add('prince', '🤴 王子', 'people', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 228 200 246 Q300 262 400 238 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M26 122 L84 122 L84 252 L26 252 Z"/>
  <path class="fillable" fill="#ffffff" d="M18 124 L55 66 L92 124 Z"/>
  <path fill="none" stroke-width="3" d="M55 66 L55 42"/>
  <path class="fillable" fill="#ffffff" d="M55 42 L76 48 L55 56 Z"/>
  <path fill="none" stroke-width="3" d="M46 160 Q46 148 55 148 Q64 148 64 160 L64 176 L46 176 Z M42 252 L42 224 Q42 210 55 210 Q68 210 68 224 L68 252"/>
  <path class="fillable" fill="#ffffff" d="M172 166 Q138 210 130 258 L270 258 Q262 210 228 166 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 220 L179 248 L197 248 L198 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 220 L203 248 L221 248 L222 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M176 230 L176 258 Q186 262 199 258 L198 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M202 230 L201 258 Q214 262 224 258 L224 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M166 226 Q162 190 174 164 Q200 156 226 164 Q238 190 234 226 Z"/>
  <path class="fillable" fill="#ffffff" d="M167 210 L233 210 L233 222 L167 222 Z"/>
  <path fill="#ffffff" stroke-width="3" d="M193 209 L207 209 L207 223 L193 223 Z"/>
  <path fill="none" stroke-width="3" d="M200 180 L200 208"/>
  <path class="fillable" fill="#ffffff" d="M178 166 Q156 174 146 202 Q152 212 162 208 Q168 190 182 184 Z"/>
  <circle class="fillable" fill="#ffffff" cx="153" cy="211" r="10"/>
  <path class="fillable" fill="#ffffff" d="M 262.2 129.3 L 271.9 131.7 L 243.4 246.2 L 233.7 243.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M 222 166 Q 244 174 254 202 Q 248 212 238 208 Q 232 190 218 184 Z"/>
  <circle class="fillable" fill="#ffffff" cx="247" cy="211" r="10"/>
  <path class="fillable" fill="#ffffff" d="M162 176 Q200 192 238 176 Q244 162 230 158 Q200 170 170 158 Q156 162 162 176 Z"/>
  <circle class="fillable" fill="#ffffff" cx="145" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="255" cy="120" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="56"/>
  <path class="fillable" fill="#ffffff" d="M144 114 Q140 60 200 56 Q260 60 256 114 Q252 88 238 82 Q218 92 200 82 Q182 92 162 82 Q148 88 144 114 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 70 L162 32 L180 52 L200 26 L220 52 L238 32 L242 70 Q200 60 158 70 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="56" r="7"/>
  <circle class="fillable" fill="#ffffff" cx="271" cy="116" r="14"/>
  <path fill="none" stroke-width="2.5" d="M271 109 L272.9 113.4 L277.7 113.8 L274 117 L275.1 121.7 L271 119.2 L266.9 121.7 L268 117 L264.3 113.8 L269.1 113.4 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="120" rx="9" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="120" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="181" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="183.4" cy="119" r="2.1"/>
  <circle fill="#1a1a1a" stroke="none" cx="221" cy="122" r="5.9"/>
  <circle fill="#ffffff" stroke="none" cx="223.4" cy="119" r="2.1"/>
  <path fill="none" stroke-width="3" d="M191 142 Q200 150.1 209 142"/>
  <ellipse class="fillable" fill="#ffffff" cx="164" cy="138" rx="9" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="138" rx="9" ry="6"/>
</g>
''')

# --- Bug / Birds (10) ---
add('bird_perched', '🐦 小鸟', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="52" r="24"/>
  <path class="fillable" fill="#ffffff" d="M0 254 Q100 240 200 254 Q300 268 400 248 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M40 262 Q48 180 44 104 L80 104 Q74 180 84 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M16 104 Q2 74 30 62 Q32 30 66 34 Q92 18 108 46 Q136 52 126 82 Q134 108 100 112 Q56 122 16 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M76 194 Q200 182 352 190 Q366 200 352 208 Q200 204 78 220 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="352" cy="170" rx="26" ry="11" transform="rotate(-50 352 170)"/>
  <path fill="none" stroke-width="2.5" d="M350 192 L362 152"/>
  <path class="fillable" fill="#ffffff" d="M292 206 Q300 232 330 236 Q324 212 300 204 Z"/>
  <path fill="none" stroke-width="2.5" d="M296 208 Q306 222 324 232"/>
  <path class="fillable" fill="#ffffff" d="M156 160 Q118 160 98 186 Q124 192 136 184 Q130 200 152 196 Q168 186 170 176 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="204" cy="146" rx="60" ry="48"/>
  <ellipse class="fillable" fill="#ffffff" cx="214" cy="160" rx="34" ry="30"/>
  <path class="fillable" fill="#ffffff" d="M150 136 Q170 118 198 136 Q202 166 178 182 Q150 184 146 164 Q144 148 150 136 Z"/>
  <path fill="none" stroke-width="2.5" d="M160 160 Q172 164 184 156 M156 172 Q168 176 180 170"/>
  <path class="fillable" fill="#ffffff" d="M184 186 L182 200 Q190 206 198 200 L196 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M222 186 L220 200 Q228 206 236 200 L234 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 52 Q198 30 214 20 Q214 34 226 50 Z"/>
  <circle class="fillable" fill="#ffffff" cx="216" cy="94" r="44"/>
  <ellipse class="fillable" fill="#ffffff" cx="198" cy="88" rx="10" ry="12"/>
  <circle fill="#1a1a1a" stroke="none" cx="199" cy="89" r="6.0"/>
  <circle fill="#ffffff" stroke="none" cx="201.4" cy="86.3" r="2.3"/>
  <ellipse class="fillable" fill="#ffffff" cx="234" cy="88" rx="10" ry="12"/>
  <circle fill="#1a1a1a" stroke="none" cx="235" cy="89" r="6.0"/>
  <circle fill="#ffffff" stroke="none" cx="237.4" cy="86.3" r="2.3"/>
  <path class="fillable" fill="#ffffff" d="M206 104 Q216 98 228 104 L217 120 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="186" cy="110" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="248" cy="110" rx="8" ry="5"/>
</g>
''')

add('bee_flower', '🐝 蜜蜂', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M26.0 67.0 Q26.0 49.0 45.8 50.8 Q53.0 34.6 72.8 40.0 Q89.0 32.8 96.2 50.8 Q112.4 52.6 108.8 67.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 256 Q300 270 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M72 260 Q70 230 74 200 L80 200 Q78 230 80 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M76 236 Q50 220 40 232 Q56 246 76 240 Z"/>
  <circle class="fillable" fill="#ffffff" cx="74.0" cy="162.0" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="96.8" cy="178.6" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="88.1" cy="205.4" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="59.9" cy="205.4" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="51.2" cy="178.6" r="17"/>
  <circle class="fillable" fill="#ffffff" cx="74" cy="186" r="14"/>
  <path class="fillable" fill="#ffffff" d="M336 260 Q334 230 338 196 L344 196 Q342 230 344 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M342 232 Q368 214 376 228 Q362 242 342 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M314 176 Q312 206 340 208 Q368 206 366 176 L356 188 L340 170 L326 188 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="160" cy="74" rx="30" ry="44" transform="rotate(-25 160 74)"/>
  <ellipse class="fillable" fill="#ffffff" cx="204" cy="70" rx="28" ry="42" transform="rotate(20 204 70)"/>
  <path fill="none" stroke-width="2.5" d="M162 60 Q166 80 172 100 M200 56 Q200 76 196 96"/>
  <path class="fillable" fill="#ffffff" d="M118 126 L92 134 L118 144 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="188" cy="132" rx="74" ry="52"/>
  <path class="fillable" fill="#ffffff" d="M136 95.0 A74 52 0 0 1 160 83.9 Q174 132 160 180.1 A74 52 0 0 1 136 169.0 Q150 132 136 95.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 80.0 A74 52 0 0 1 212 82.8 Q226 132 212 181.2 A74 52 0 0 1 188 184.0 Q202 132 188 80.0 Z"/>
  <path fill="none" stroke-width="3" d="M262 82 Q252 52 236 46"/>
  <path fill="none" stroke-width="3" d="M286 80 Q300 52 318 50"/>
  <circle class="fillable" fill="#ffffff" cx="234" cy="44" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="320" cy="48" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="272" cy="118" r="42"/>
  <ellipse class="fillable" fill="#ffffff" cx="256" cy="110" rx="10" ry="12"/>
  <circle fill="#1a1a1a" stroke="none" cx="257" cy="111" r="6.0"/>
  <circle fill="#ffffff" stroke="none" cx="259.4" cy="108.3" r="2.3"/>
  <ellipse class="fillable" fill="#ffffff" cx="290" cy="110" rx="10" ry="12"/>
  <circle fill="#1a1a1a" stroke="none" cx="291" cy="111" r="6.0"/>
  <circle fill="#ffffff" stroke="none" cx="293.4" cy="108.3" r="2.3"/>
  <path fill="none" stroke-width="3" d="M262 134 Q273 146 284 134"/>
  <ellipse class="fillable" fill="#ffffff" cx="246" cy="132" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="300" cy="132" rx="8" ry="5"/>
</g>
''')

add('dragonfly', '🪲 蜻蜓', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="354" cy="46" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 262 Q60 250 120 260 Q180 270 240 258 Q320 248 400 260 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M24 266 Q22 220 30 180 L36 180 Q32 220 34 264 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="33" cy="172" rx="8" ry="22"/>
  <path class="fillable" fill="#ffffff" d="M362 264 Q358 224 366 196 L372 196 Q368 226 372 262 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="369" cy="188" rx="8" ry="20"/>
  <path class="fillable" fill="#ffffff" d="M44 264 Q50 236 70 222 Q60 244 58 264 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="171.0" cy="90.5" rx="75.0" ry="22" transform="rotate(-150 171.0 90.5)"/>
  <ellipse class="fillable" fill="#ffffff" cx="215.4" cy="77.0" rx="55.0" ry="20" transform="rotate(-112 215.4 77.0)"/>
  <ellipse class="fillable" fill="#ffffff" cx="171.0" cy="165.5" rx="75.0" ry="22" transform="rotate(150 171.0 165.5)"/>
  <ellipse class="fillable" fill="#ffffff" cx="215.4" cy="179.0" rx="55.0" ry="20" transform="rotate(112 215.4 179.0)"/>
  <path fill="none" stroke-width="2.5" d="M223.9 121.0 L118.2 60.0"/>
  <path fill="none" stroke-width="2.5" d="M230.8 115.0 L200.0 39.0"/>
  <path fill="none" stroke-width="2.5" d="M223.9 135.0 L118.2 196.0"/>
  <path fill="none" stroke-width="2.5" d="M230.8 141.0 L200.0 217.0"/>
  <ellipse class="fillable" fill="#ffffff" cx="88" cy="135" rx="11" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="108" cy="134" rx="12" ry="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="131" cy="133" rx="13" ry="10"/>
  <ellipse class="fillable" fill="#ffffff" cx="155" cy="132" rx="14" ry="11"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="131" rx="15" ry="12"/>
  <ellipse class="fillable" fill="#ffffff" cx="206" cy="130" rx="16" ry="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="236" cy="128" rx="28" ry="22"/>
  <circle class="fillable" fill="#ffffff" cx="282" cy="124" r="34"/>
  <ellipse class="fillable" fill="#ffffff" cx="272" cy="108" rx="13" ry="15"/>
  <circle fill="#1a1a1a" stroke="none" cx="274" cy="109" r="7.8"/>
  <circle fill="#ffffff" stroke="none" cx="277.1" cy="105.5" r="3.0"/>
  <ellipse class="fillable" fill="#ffffff" cx="302" cy="112" rx="11" ry="14"/>
  <circle fill="#1a1a1a" stroke="none" cx="304" cy="113" r="6.6"/>
  <circle fill="#ffffff" stroke="none" cx="306.6" cy="110.0" r="2.5"/>
  <path fill="none" stroke-width="3" d="M280 138 Q290 148 300 138"/>
  <ellipse class="fillable" fill="#ffffff" cx="266" cy="134" rx="7" ry="4.5"/>
</g>
''')

add('ladybug_leaf', '🐞 瓢虫', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="52" r="24"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 256 Q300 270 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M22 238 Q120 120 376 150 Q200 186 22 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M22 238 Q200 186 376 150 Q300 268 22 238 Z"/>
  <path fill="none" stroke-width="2.5" d="M90 220 Q104 196 100 178 M300 166 Q320 158 330 142 M100 222 Q120 240 140 244 M300 172 Q320 196 340 194"/>
  <path class="fillable" fill="#ffffff" d="M24 238 Q12 250 4 270 L12 272 Q18 252 30 242 Z"/>
  <path fill="none" stroke-width="5" d="M150 140 Q136 132 128 138 M146 172 Q130 172 124 180 M156 202 Q142 208 140 218 M270 140 Q284 132 292 138 M274 172 Q290 172 296 180 M264 202 Q278 208 280 218"/>
  <path fill="none" stroke-width="3" d="M196 66 Q184 36 166 34 M224 66 Q236 36 254 34"/>
  <circle class="fillable" fill="#ffffff" cx="164" cy="34" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="256" cy="34" r="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="210" cy="160" rx="68" ry="62"/>
  <path class="fillable" fill="#ffffff" d="M208 100 Q144 100 144 160 Q146 214 204 220 Q198 160 208 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M212 100 Q276 100 276 160 Q274 214 216 220 Q222 160 212 100 Z"/>
  <circle class="fillable" fill="#ffffff" cx="176" cy="140" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="176" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="186" cy="196" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="244" cy="140" r="11"/>
  <circle class="fillable" fill="#ffffff" cx="260" cy="176" r="10"/>
  <circle class="fillable" fill="#ffffff" cx="234" cy="196" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="210" cy="86" r="36"/>
  <ellipse class="fillable" fill="#ffffff" cx="196" cy="82" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="197" cy="83" r="5.4"/>
  <circle fill="#ffffff" stroke="none" cx="199.2" cy="80.6" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="224" cy="82" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="225" cy="83" r="5.4"/>
  <circle fill="#ffffff" stroke="none" cx="227.2" cy="80.6" r="2.1"/>
  <path fill="none" stroke-width="3" d="M200 100 Q210 108 220 100"/>
  <ellipse class="fillable" fill="#ffffff" cx="186" cy="98" rx="6" ry="4"/>
  <ellipse class="fillable" fill="#ffffff" cx="234" cy="98" rx="6" ry="4"/>
</g>
''')

add('snail', '🐌 蜗牛', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="56" cy="46" r="22"/>
  <path class="fillable" fill="#ffffff" d="M196.0 55.0 Q196.0 37.0 215.8 38.8 Q223.0 22.6 242.8 28.0 Q259.0 20.8 266.2 38.8 Q282.4 40.6 278.8 55.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 256 Q300 270 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M40 262 L44 230 L62 230 L66 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M22 232 Q24 196 53 194 Q84 196 86 232 Z"/>
  <circle class="fillable" fill="#ffffff" cx="40" cy="214" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="66" cy="208" r="7"/>
  <path fill="none" stroke-width="4" d="M318 124 Q312 100 300 78 M342 124 Q350 100 364 80"/>
  <path class="fillable" fill="#ffffff" d="M86 254 Q70 254 72 242 Q78 230 110 230 L280 226 Q298 222 300 196 Q300 148 324 124 Q356 116 370 148 Q378 196 352 230 Q330 254 290 254 Z"/>
  <path fill="none" stroke-width="3" d="M110 244 L280 240"/>
  <circle class="fillable" fill="#ffffff" cx="186" cy="148" r="80"/>
  <circle class="fillable" fill="#ffffff" cx="194" cy="142" r="56"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="138" r="33"/>
  <circle class="fillable" fill="#ffffff" cx="204" cy="136" r="13"/>
  <ellipse class="fillable" fill="#ffffff" cx="298" cy="74" rx="15" ry="15"/>
  <circle fill="#1a1a1a" stroke="none" cx="299" cy="75" r="9.0"/>
  <circle fill="#ffffff" stroke="none" cx="302.6" cy="71.0" r="3.4"/>
  <ellipse class="fillable" fill="#ffffff" cx="366" cy="76" rx="15" ry="15"/>
  <circle fill="#1a1a1a" stroke="none" cx="367" cy="77" r="9.0"/>
  <circle fill="#ffffff" stroke="none" cx="370.6" cy="73.0" r="3.4"/>
  <path fill="none" stroke-width="3" d="M328 162 Q338 172 350 162"/>
  <ellipse class="fillable" fill="#ffffff" cx="322" cy="150" rx="6" ry="4"/>
  <ellipse class="fillable" fill="#ffffff" cx="358" cy="150" rx="6" ry="4"/>
</g>
''')

add('frog', '🐸 青蛙', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="46" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 236 Q100 226 200 236 Q300 246 400 232 L400 300 L0 300 Z"/>
  <path fill="none" stroke-width="3" d="M30 284 Q50 276 70 284 M330 284 Q350 276 370 284 M170 290 Q190 282 210 290"/>
  <path class="fillable" fill="#ffffff" d="M200 254 L348.5 258.2 A150 30 0 1 1 348.5 249.8 Z"/>
  <path class="fillable" fill="#ffffff" d="M52 232 L12.6 234.1 A40 12 0 1 1 12.6 229.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M52 226 Q36 200 46 186 Q52 200 52 210 Q56 190 70 182 Q74 206 60 226 Z"/>
  <path class="fillable" fill="#ffffff" d="M52 226 Q34 214 26 200 Q44 200 54 214 Z"/>
  <path class="fillable" fill="#ffffff" d="M354 224 L320.5 222.3 A34 10 0 1 1 320.5 225.7 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="138" cy="214" rx="40" ry="28" transform="rotate(-15 138 214)"/>
  <ellipse class="fillable" fill="#ffffff" cx="262" cy="214" rx="40" ry="28" transform="rotate(15 262 214)"/>
  <path class="fillable" fill="#ffffff" d="M100 244 Q104 230 126 236 Q140 244 130 252 Q110 256 100 244 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 244 Q296 230 274 236 Q260 244 270 252 Q290 256 300 244 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="192" rx="60" ry="52"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="204" rx="38" ry="34"/>
  <path class="fillable" fill="#ffffff" d="M150 168 Q136 208 150 240 Q162 252 176 244 Q164 212 172 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 168 Q264 208 250 240 Q238 252 224 244 Q236 212 228 178 Z"/>
  <circle class="fillable" fill="#ffffff" cx="158" cy="74" r="30"/>
  <circle class="fillable" fill="#ffffff" cx="242" cy="74" r="30"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="122" rx="86" ry="56"/>
  <ellipse class="fillable" fill="#ffffff" cx="158" cy="70" rx="19" ry="19"/>
  <circle fill="#1a1a1a" stroke="none" cx="160" cy="72" r="10.0"/>
  <circle fill="#ffffff" stroke="none" cx="164.0" cy="67.5" r="3.8"/>
  <ellipse class="fillable" fill="#ffffff" cx="242" cy="70" rx="19" ry="19"/>
  <circle fill="#1a1a1a" stroke="none" cx="240" cy="72" r="10.0"/>
  <circle fill="#ffffff" stroke="none" cx="244.0" cy="67.5" r="3.8"/>
  <circle fill="none" cx="192" cy="112" r="2.5"/>
  <circle fill="none" cx="208" cy="112" r="2.5"/>
  <path fill="none" stroke-width="4" d="M150 132 Q200 166 250 132"/>
  <ellipse class="fillable" fill="#ffffff" cx="136" cy="134" rx="11" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="264" cy="134" rx="11" ry="7"/>
</g>
''')

add('spider_web', '🕷️ 蜘蛛网', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 262 Q100 254 200 262 Q300 270 400 256 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M232.1 58.4 Q251.1 84.9 277.6 103.9 L244.3 117.6 Q229.2 106.8 218.4 91.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M245.2 27.0 Q271.8 64.2 309.0 90.8 L277.6 103.9 Q251.1 84.9 232.1 58.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M277.6 103.9 Q272.2 136.0 277.6 168.1 L244.3 154.4 Q241.3 136.0 244.3 117.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M309.0 90.8 Q301.5 136.0 309.0 181.2 L277.6 168.1 Q272.2 136.0 277.6 103.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M277.6 168.1 Q251.1 187.1 232.1 213.6 L218.4 180.3 Q229.2 165.2 244.3 154.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M309.0 181.2 Q271.8 207.8 245.2 245.0 L232.1 213.6 Q251.1 187.1 277.6 168.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M232.1 213.6 Q200.0 208.2 167.9 213.6 L181.6 180.3 Q200.0 177.3 218.4 180.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M245.2 245.0 Q200.0 237.5 154.8 245.0 L167.9 213.6 Q200.0 208.2 232.1 213.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M167.9 213.6 Q148.9 187.1 122.4 168.1 L155.7 154.4 Q170.8 165.2 181.6 180.3 Z"/>
  <path class="fillable" fill="#ffffff" d="M154.8 245.0 Q128.2 207.8 91.0 181.2 L122.4 168.1 Q148.9 187.1 167.9 213.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M122.4 168.1 Q127.8 136.0 122.4 103.9 L155.7 117.6 Q158.7 136.0 155.7 154.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M91.0 181.2 Q98.5 136.0 91.0 90.8 L122.4 103.9 Q127.8 136.0 122.4 168.1 Z"/>
  <path class="fillable" fill="#ffffff" d="M122.4 103.9 Q148.9 84.9 167.9 58.4 L181.6 91.7 Q170.8 106.8 155.7 117.6 Z"/>
  <path class="fillable" fill="#ffffff" d="M91.0 90.8 Q128.2 64.2 154.8 27.0 L167.9 58.4 Q148.9 84.9 122.4 103.9 Z"/>
  <path class="fillable" fill="#ffffff" d="M167.9 58.4 Q200.0 63.8 232.1 58.4 L218.4 91.7 Q200.0 94.7 181.6 91.7 Z"/>
  <path class="fillable" fill="#ffffff" d="M154.8 27.0 Q200.0 34.5 245.2 27.0 L232.1 58.4 Q200.0 63.8 167.9 58.4 Z"/>
  <path class="fillable" fill="#ffffff" d="M218.4 91.7 Q229.2 106.8 244.3 117.6 Q241.3 136.0 244.3 154.4 Q229.2 165.2 218.4 180.3 Q200.0 177.3 181.6 180.3 Q170.8 165.2 155.7 154.4 Q158.7 136.0 155.7 117.6 Q170.8 106.8 181.6 91.7 Q200.0 94.7 218.4 91.7 Z"/>
  <path fill="none" stroke-width="2.5" d="M200.0 136.0 L247.5 21.4 M200.0 136.0 L314.6 88.5 M200.0 136.0 L314.6 183.5 M200.0 136.0 L247.5 250.6 M200.0 136.0 L152.5 250.6 M200.0 136.0 L85.4 183.5 M200.0 136.0 L85.4 88.5 M200.0 136.0 L152.5 21.4"/>
  <path fill="none" stroke-width="5" d="M170 118 Q122 80 102 112"/>
  <path fill="none" stroke-width="5" d="M170 134 Q118 106 100 146"/>
  <path fill="none" stroke-width="5" d="M170 150 Q114 134 98 174"/>
  <path fill="none" stroke-width="5" d="M170 166 Q110 164 96 198"/>
  <path fill="none" stroke-width="5" d="M230 118 Q278 80 298 112"/>
  <path fill="none" stroke-width="5" d="M230 134 Q282 106 300 146"/>
  <path fill="none" stroke-width="5" d="M230 150 Q286 134 302 174"/>
  <path fill="none" stroke-width="5" d="M230 166 Q290 164 304 198"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="140" rx="46" ry="44"/>
  <path class="fillable" fill="#ffffff" d="M168 104 Q170 86 186 92 Q192 98 200 100 Q194 112 176 114 Q166 112 168 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M232 104 Q230 86 214 92 Q208 98 200 100 Q206 112 224 114 Q234 112 232 104 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="101" r="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="184" cy="134" rx="11" ry="13"/>
  <circle fill="#1a1a1a" stroke="none" cx="185" cy="135" r="6.6"/>
  <circle fill="#ffffff" stroke="none" cx="187.6" cy="132.0" r="2.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="216" cy="134" rx="11" ry="13"/>
  <circle fill="#1a1a1a" stroke="none" cx="215" cy="135" r="6.6"/>
  <circle fill="#ffffff" stroke="none" cx="217.6" cy="132.0" r="2.5"/>
  <path fill="none" stroke-width="3" d="M190 156 Q200 164 210 156"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="152" rx="7" ry="4.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="230" cy="152" rx="7" ry="4.5"/>
</g>
''')

add('hummingbird', '🐦 蜂鸟', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="52" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 256 Q300 270 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M338 262 Q334 200 328 130 L336 130 Q342 200 346 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M340 230 Q366 206 384 214 Q370 238 342 238 Z"/>
  <path class="fillable" fill="#ffffff" d="M332 200 Q306 186 294 196 Q310 212 334 208 Z"/>
  <circle class="fillable" fill="#ffffff" cx="344.1" cy="90.6" r="18"/>
  <circle class="fillable" fill="#ffffff" cx="352.8" cy="117.4" r="18"/>
  <circle class="fillable" fill="#ffffff" cx="330.0" cy="134.0" r="18"/>
  <circle class="fillable" fill="#ffffff" cx="307.2" cy="117.4" r="18"/>
  <circle class="fillable" fill="#ffffff" cx="315.9" cy="90.6" r="18"/>
  <circle class="fillable" fill="#ffffff" cx="330" cy="110" r="14"/>
  <path class="fillable" fill="#ffffff" d="M120 178 Q84 196 70 230 Q94 226 104 214 Q100 236 118 232 Q132 214 142 196 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 120 Q120 70 128 26 Q156 44 166 72 Q178 46 196 40 Q204 80 192 118 Z"/>
  <path fill="none" stroke-width="2.5" d="M146 52 Q160 84 176 110 M190 54 Q190 84 186 110"/>
  <path class="fillable" fill="#ffffff" d="M204 104 Q150 104 128 146 Q112 184 128 200 Q160 210 204 178 Q240 150 236 124 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="188" cy="168" rx="36" ry="17" transform="rotate(-38 188 168)"/>
  <path class="fillable" fill="#ffffff" d="M170 140 Q130 146 112 178 Q146 184 172 162 Z"/>
  <path class="fillable" fill="#ffffff" d="M248 110 L300 112 L248 122 Z"/>
  <circle class="fillable" fill="#ffffff" cx="220" cy="112" r="32"/>
  <ellipse class="fillable" fill="#ffffff" cx="226" cy="104" rx="9" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="228" cy="105" r="5.4"/>
  <circle fill="#ffffff" stroke="none" cx="230.2" cy="102.6" r="2.1"/>
  <ellipse class="fillable" fill="#ffffff" cx="216" cy="126" rx="7" ry="4.5"/>
</g>
''')

add('caterpillar', '🐛 毛毛虫', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="150" cy="48" r="22"/>
  <path class="fillable" fill="#ffffff" d="M20.0 67.0 Q20.0 49.0 39.8 50.8 Q47.0 34.6 66.8 40.0 Q83.0 32.8 90.2 50.8 Q106.4 52.6 102.8 67.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 256 Q300 270 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 254 Q330 220 372 222 Q360 254 300 254 Z"/>
  <path fill="none" stroke-width="2.5" d="M304 252 Q336 236 366 226"/>
  <ellipse class="fillable" fill="#ffffff" cx="66" cy="242" rx="12" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="116" cy="231" rx="12" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="223" rx="12" ry="8"/>
  <ellipse class="fillable" fill="#ffffff" cx="226" cy="230" rx="12" ry="8"/>
  <circle class="fillable" fill="#ffffff" cx="66" cy="214" r="30"/>
  <circle class="fillable" fill="#ffffff" cx="116" cy="200" r="33"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="190" r="35"/>
  <circle class="fillable" fill="#ffffff" cx="226" cy="196" r="36"/>
  <ellipse class="fillable" fill="#ffffff" cx="66" cy="200.5" rx="9.6" ry="6.6"/>
  <ellipse class="fillable" fill="#ffffff" cx="116" cy="185.15" rx="10.56" ry="7.26"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="174.25" rx="11.200000000000001" ry="7.7"/>
  <ellipse class="fillable" fill="#ffffff" cx="226" cy="179.8" rx="11.52" ry="7.92"/>
  <path fill="none" stroke-width="3" d="M264 104 Q250 66 236 58 M300 104 Q312 66 330 58"/>
  <circle class="fillable" fill="#ffffff" cx="234" cy="56" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="332" cy="56" r="9"/>
  <ellipse class="fillable" fill="#ffffff" cx="296" cy="184" rx="12" ry="8"/>
  <circle class="fillable" fill="#ffffff" cx="282" cy="146" r="52"/>
  <ellipse class="fillable" fill="#ffffff" cx="264" cy="138" rx="11" ry="14"/>
  <circle fill="#1a1a1a" stroke="none" cx="265" cy="139" r="6.6"/>
  <circle fill="#ffffff" stroke="none" cx="267.6" cy="136.0" r="2.5"/>
  <ellipse class="fillable" fill="#ffffff" cx="300" cy="138" rx="11" ry="14"/>
  <circle fill="#1a1a1a" stroke="none" cx="301" cy="139" r="6.6"/>
  <circle fill="#ffffff" stroke="none" cx="303.6" cy="136.0" r="2.5"/>
  <path fill="none" stroke-width="3" d="M268 164 Q282 176 296 164"/>
  <ellipse class="fillable" fill="#ffffff" cx="248" cy="160" rx="8" ry="5"/>
  <ellipse class="fillable" fill="#ffffff" cx="316" cy="160" rx="8" ry="5"/>
</g>
''')

add('parrot', '🦜 鹦鹉', 'bug', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="56" cy="46" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 244 200 258 Q300 272 400 252 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 264 Q338 180 334 110 L368 110 Q364 180 376 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M300 112 Q290 80 316 72 Q322 42 352 46 Q380 40 388 66 Q404 84 392 104 Q380 122 350 118 Q320 126 300 112 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 196 Q120 236 104 278 Q120 284 132 272 Q150 236 172 204 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 200 Q146 244 140 284 Q156 290 164 278 Q172 240 184 206 Z"/>
  <path class="fillable" fill="#ffffff" d="M40 196 Q200 186 336 178 L338 200 Q200 206 42 214 Q32 206 40 196 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="60" cy="178" rx="22" ry="10" transform="rotate(-30 60 178)"/>
  <ellipse class="fillable" fill="#ffffff" cx="186" cy="146" rx="50" ry="62" transform="rotate(18 186 146)"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="158" rx="26" ry="40" transform="rotate(18 200 158)"/>
  <path class="fillable" fill="#ffffff" d="M168 194 L166 206 Q176 212 184 206 L182 194 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 192 L194 204 Q204 210 212 204 L210 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 110 Q190 106 198 146 Q200 190 164 222 Q140 200 138 158 Q138 124 158 110 Z"/>
  <path fill="none" stroke-width="2.5" d="M150 160 Q166 164 182 156 M150 184 Q166 188 180 180"/>
  <path class="fillable" fill="#ffffff" d="M186 56 Q166 36 172 18 Q186 30 196 44 Q194 22 210 12 Q214 30 208 46 Z"/>
  <circle class="fillable" fill="#ffffff" cx="214" cy="88" r="44"/>
  <ellipse class="fillable" fill="#ffffff" cx="230" cy="86" rx="22" ry="18"/>
  <ellipse class="fillable" fill="#ffffff" cx="228" cy="82" rx="10" ry="11"/>
  <circle fill="#1a1a1a" stroke="none" cx="230" cy="83" r="6.0"/>
  <circle fill="#ffffff" stroke="none" cx="232.4" cy="80.3" r="2.3"/>
  <path class="fillable" fill="#ffffff" d="M248 68 Q284 64 290 98 Q292 118 278 126 Q278 108 254 104 Z"/>
  <path class="fillable" fill="#ffffff" d="M254 104 Q274 110 272 122 Q260 128 248 116 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="210" cy="108" rx="8" ry="5"/>
</g>
''')

# --- Buildings (10) ---
add('village_house', '🏠 小村屋', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="52" r="24"/>
  <path class="fillable" fill="#ffffff" d="M26.0 63.0 Q26.0 45.0 45.8 46.8 Q53.0 30.6 72.8 36.0 Q89.0 28.8 96.2 46.8 Q112.4 48.6 108.8 63.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 244 200 258 Q300 272 400 252 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M38 262 L44 196 L62 196 L68 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M14 200 Q4 168 26 156 Q30 126 56 130 Q84 122 92 152 Q106 176 88 200 Q56 214 14 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 108 L250 54 L280 54 L280 128 Z"/>
  <circle class="fillable" fill="#ffffff" cx="270" cy="40" r="13"/>
  <circle class="fillable" fill="#ffffff" cx="288" cy="22" r="10"/>
  <path class="fillable" fill="#ffffff" d="M118 254 L118 140 L282 140 L282 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M92 148 Q86 140 96 132 L196 52 Q200 48 204 52 L304 132 Q314 140 308 148 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="108" r="16"/>
  <path fill="none" stroke-width="2.5" d="M184 108 L216 108 M200 92 L200 124"/>
  <path class="fillable" fill="#ffffff" d="M178 254 L178 204 Q178 180 200 180 Q222 180 222 204 L222 254 Z"/>
  <circle fill="none" cx="212" cy="220" r="3"/>
  <path class="fillable" fill="#ffffff" d="M132 170 L164 170 L164 210 L132 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M236 170 L268 170 L268 210 L236 210 Z"/>
  <path fill="none" stroke-width="2.5" d="M148 170 L148 210 M132 190 L164 190 M252 170 L252 210 M236 190 L268 190"/>
  <path class="fillable" fill="#ffffff" d="M126 214 L170 214 L170 224 L126 224 Z"/>
  <path class="fillable" fill="#ffffff" d="M230 214 L274 214 L274 224 L230 224 Z"/>
  <path class="fillable" fill="#ffffff" d="M184 300 Q190 276 180 256 L220 256 Q212 276 224 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M94 258 Q86 232 106 228 Q114 212 130 224 Q144 222 146 240 Q152 258 136 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M254 258 Q248 238 266 232 Q276 216 292 228 Q312 226 310 246 Q316 258 300 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M318 222 L398 222 L398 234 L318 234 Z"/>
  <path class="fillable" fill="#ffffff" d="M324 254 L324 212 L331 202 L338 212 L338 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M346 254 L346 212 L353 202 L360 212 L360 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M368 254 L368 212 L375 202 L382 212 L382 254 Z"/>
</g>
''')

add('school', '🏫 学校', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="362" cy="42" r="20"/>
  <path class="fillable" fill="#ffffff" d="M250.0 44.5 Q250.0 29.5 266.5 31.0 Q272.5 17.5 289.0 22.0 Q302.5 16.0 308.5 31.0 Q322.0 32.5 319.0 44.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 260 Q100 246 200 260 Q300 274 400 254 L400 300 L0 300 Z"/>
  <path fill="none" stroke-width="4" d="M60 140 L60 40"/>
  <path class="fillable" fill="#ffffff" d="M60 42 Q84 36 100 50 Q84 64 60 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M56 254 L56 150 L170 150 L170 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M230 254 L230 150 L344 150 L344 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M46 154 L50 136 L172 136 L172 154 Z"/>
  <path class="fillable" fill="#ffffff" d="M228 154 L228 136 L350 136 L354 154 Z"/>
  <path class="fillable" fill="#ffffff" d="M78 166 L106 166 L106 204 L78 204 Z"/>
  <path fill="none" stroke-width="2.5" d="M92 166 L92 204 M78 185 L106 185"/>
  <path class="fillable" fill="#ffffff" d="M128 166 L156 166 L156 204 L128 204 Z"/>
  <path fill="none" stroke-width="2.5" d="M142 166 L142 204 M128 185 L156 185"/>
  <path class="fillable" fill="#ffffff" d="M250 166 L278 166 L278 204 L250 204 Z"/>
  <path fill="none" stroke-width="2.5" d="M264 166 L264 204 M250 185 L278 185"/>
  <path class="fillable" fill="#ffffff" d="M300 166 L328 166 L328 204 L300 204 Z"/>
  <path fill="none" stroke-width="2.5" d="M314 166 L314 204 M300 185 L328 185"/>
  <path class="fillable" fill="#ffffff" d="M162 254 L162 84 L238 84 L238 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M152 90 Q146 84 154 78 L196 30 Q200 26 204 30 L246 78 Q254 84 248 90 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="118" r="22"/>
  <path fill="none" stroke-width="3" d="M200 118 L200 104 M200 118 L210 124"/>
  <path class="fillable" fill="#ffffff" d="M176 254 L176 186 Q176 166 200 166 Q224 166 224 186 L224 254 Z"/>
  <path fill="none" stroke-width="3" d="M200 168 L200 254"/>
  <path class="fillable" fill="#ffffff" d="M164 254 L236 254 L242 268 L158 268 Z"/>
  <path class="fillable" fill="#ffffff" d="M172 300 L180 268 L220 268 L228 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M16 262 Q8 236 28 230 Q36 214 52 226 Q66 228 64 248 Q68 262 54 264 Z"/>
  <path class="fillable" fill="#ffffff" d="M336 262 Q332 240 350 232 Q360 216 376 228 Q394 230 390 248 Q394 262 380 264 Z"/>
</g>
''')

add('lighthouse', '🗼 灯塔', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M24.0 57.0 Q24.0 39.0 43.8 40.8 Q51.0 24.6 70.8 30.0 Q87.0 22.8 94.2 40.8 Q110.4 42.6 106.8 57.0 Z"/>
  <circle class="fillable" fill="#ffffff" cx="344" cy="50" r="24"/>
  <path class="fillable" fill="#ffffff" d="M0 232 Q50 222 100 232 Q150 242 200 232 Q250 222 300 232 Q350 242 400 230 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M310 236 L370 236 Q366 252 350 254 L330 254 Q314 252 310 236 Z"/>
  <path fill="none" stroke-width="3" d="M340 236 L340 170"/>
  <path class="fillable" fill="#ffffff" d="M344 172 L344 230 L376 230 Q370 196 344 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M336 182 L336 230 L312 230 Q318 204 336 182 Z"/>
  <path class="fillable" fill="#ffffff" d="M152.0 250 L157.0 215 L243.0 215 L248.0 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M157.0 215 L162.0 180 L238.0 180 L243.0 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M162.0 180 L167.0 145 L233.0 145 L238.0 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M167.0 145 L172.0 110 L228.0 110 L233.0 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M188 250 L188 224 Q188 214 200 214 Q212 214 212 224 L212 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M192 164 Q192 154 200 154 Q208 154 208 164 L208 172 L192 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 60 L220 60 L220 100 L180 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M187 66 L213 66 L213 94 L187 94 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 100 L242 100 L242 112 L158 112 Z"/>
  <path fill="none" stroke-width="3" d="M172 100 L172 88 L228 88 L228 100 M186 88 L186 100 M200 88 L200 100 M214 88 L214 100"/>
  <path class="fillable" fill="#ffffff" d="M172 62 Q174 30 200 28 Q226 30 228 62 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="22" r="8"/>
  <path class="fillable" fill="#ffffff" d="M110 262 Q104 240 126 234 Q146 222 164 236 L164 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M236 262 L236 238 Q252 222 270 236 Q294 236 290 262 Z"/>
  <path fill="none" stroke-width="3" d="M140 246 L148 256 M262 240 L270 254"/>
  <path class="fillable" fill="#ffffff" d="M0 270 Q60 258 120 262 Q200 270 290 262 Q350 256 400 268 L400 300 L0 300 Z"/>
  <path fill="none" stroke-width="3" d="M60 200 Q70 190 80 200 Q90 190 100 200 M260 150 Q270 140 280 150 Q290 140 300 150"/>
</g>
''')

add('barn', '🏚️ 谷仓', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="52" r="24"/>
  <path class="fillable" fill="#ffffff" d="M150.0 48.0 Q150.0 32.0 167.6 33.6 Q174.0 19.2 191.6 24.0 Q206.0 17.6 212.4 33.6 Q226.8 35.2 223.6 48.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 256 Q300 270 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M30 254 L30 104 L92 104 L92 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M26 106 Q30 58 61 58 Q92 58 96 106 Z"/>
  <path class="fillable" fill="#ffffff" d="M30 160 L92 160 L92 172 L30 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M108 254 L108 146 L292 146 L292 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M92 156 Q88 148 94 142 L122 92 L196 56 Q200 54 204 56 L278 92 L306 142 Q312 148 308 156 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 94 L220 94 L220 132 L180 132 Z"/>
  <path fill="none" stroke-width="3" d="M180 94 L220 132 M220 94 L180 132"/>
  <path class="fillable" fill="#ffffff" d="M156 176 L244 176 L244 186 L156 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 254 L160 186 L200 186 L200 254 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 254 L200 186 L240 186 L240 254 Z"/>
  <path fill="none" stroke-width="3" d="M160 186 L200 254 M200 186 L160 254 M200 186 L240 254 M240 186 L200 254"/>
  <path class="fillable" fill="#ffffff" d="M120 180 L146 180 L146 206 L120 206 Z"/>
  <path class="fillable" fill="#ffffff" d="M254 180 L280 180 L280 206 L254 206 Z"/>
  <path class="fillable" fill="#ffffff" d="M296 222 L396 222 L396 232 L296 232 Z"/>
  <path class="fillable" fill="#ffffff" d="M312 256 L312 206 L324 206 L324 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M346 256 L346 206 L358 206 L358 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M380 256 L380 206 L392 206 L392 256 Z"/>
</g>
''')

add('igloo', '🛖 冰屋', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="44" r="22"/>
  <path class="fillable" fill="#ffffff" d="M28.0 57.0 Q28.0 39.0 47.8 40.8 Q55.0 24.6 74.8 30.0 Q91.0 22.8 98.2 40.8 Q114.4 42.6 110.8 57.0 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 236 Q100 226 200 238 Q300 248 400 232 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M54.0 244 A146 134 0 0 1 58.8 210 L115.3 210 L115.3 244 Z"/>
  <path class="fillable" fill="#ffffff" d="M115.3 244 L115.3 210 L171.8 210 L171.8 244 Z"/>
  <path class="fillable" fill="#ffffff" d="M171.8 244 L171.8 210 L228.2 210 L228.2 244 Z"/>
  <path class="fillable" fill="#ffffff" d="M228.2 244 L228.2 210 L284.7 210 L284.7 244 Z"/>
  <path class="fillable" fill="#ffffff" d="M284.7 244 L284.7 210 L341.2 210 A146 134 0 0 1 346.0 244 Z"/>
  <path class="fillable" fill="#ffffff" d="M58.8 210 A146 134 0 0 1 72.9 178 L149.2 178 L149.2 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M149.2 210 L149.2 178 L200.0 178 L200.0 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M200.0 210 L200.0 178 L250.8 178 L250.8 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M250.8 210 L250.8 178 L327.1 178 A146 134 0 0 1 341.2 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M72.9 178 A146 134 0 0 1 95.9 150 L148.0 150 L148.0 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M148.0 178 L148.0 150 L200.0 150 L200.0 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M200.0 178 L200.0 150 L252.0 150 L252.0 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M252.0 178 L252.0 150 L304.1 150 A146 134 0 0 1 327.1 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M95.9 150 A146 134 0 0 1 130.8 126 L179.2 126 L179.2 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M179.2 150 L179.2 126 L220.8 126 L220.8 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M220.8 150 L220.8 126 L269.2 126 A146 134 0 0 1 304.1 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M130.8 126 A146 134 0 0 1 269.2 126 Z"/>
  <path class="fillable" fill="#ffffff" d="M152 262 L152 222 Q152 182 200 182 Q248 182 248 222 L248 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M172 262 L172 228 Q172 204 200 204 Q228 204 228 228 L228 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 262 Q90 252 140 262 L260 262 Q320 252 400 260 L400 300 L0 300 Z"/>
</g>
''')

add('treehouse', '🌳 树屋', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="360" cy="36" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 244 200 258 Q300 272 400 252 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M168 262 Q178 200 176 120 L224 120 Q222 200 236 262 Q216 254 200 262 Q184 254 168 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 150 Q30 136 40 106 Q30 70 64 60 Q74 24 116 28 Q130 52 120 80 Q140 110 120 150 Q90 164 60 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M280 150 Q250 160 276 110 Q262 80 284 50 Q320 22 340 60 Q370 70 362 106 Q372 140 340 150 Q310 164 280 150 Z"/>
  <path class="fillable" fill="#ffffff" d="M116 30 Q150 6 200 12 Q252 6 284 50 Q262 80 276 110 Q260 140 200 140 Q140 140 120 150 Q140 110 120 80 Q130 52 116 30 Z"/>
  <circle class="fillable" fill="#ffffff" cx="76" cy="96" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="330" cy="92" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="132" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="340" cy="128" r="9"/>
  <path class="fillable" fill="#ffffff" d="M150 190 L176 230 L182 222 L160 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 190 L224 230 L218 222 L240 186 Z"/>
  <path class="fillable" fill="#ffffff" d="M112 176 L288 176 L288 192 L112 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M144 176 L144 118 L256 118 L256 176 Z"/>
  <path class="fillable" fill="#ffffff" d="M128 124 Q122 118 130 112 L196 68 Q200 64 204 68 L270 112 Q278 118 272 124 Z"/>
  <path fill="none" stroke-width="3" d="M200 66 L200 44"/>
  <path class="fillable" fill="#ffffff" d="M200 44 L226 52 L200 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 176 L164 138 Q164 126 178 126 Q192 126 192 138 L192 176 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 134 L242 134 L242 160 L210 160 Z"/>
  <path fill="none" stroke-width="2.5" d="M226 134 L226 160 M210 147 L242 147"/>
  <path fill="none" stroke-width="4" d="M262 192 L270 258 M290 192 L298 258 M265 212 L293 212 M268 232 L296 232 M270 250 L298 250"/>
  <path fill="none" stroke-width="3" d="M84 154 L84 218 M116 156 L116 218"/>
  <path class="fillable" fill="#ffffff" d="M74 218 L126 218 L126 228 L74 228 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 258 Q324 236 342 232 Q352 216 368 228 Q386 228 384 246 Q390 258 376 260 Z"/>
</g>
''')

add('skyscraper', '🏢 高楼', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="358" cy="40" r="20"/>
  <path class="fillable" fill="#ffffff" d="M18.0 55.5 Q18.0 38.5 36.7 40.2 Q43.5 24.9 62.2 30.0 Q77.5 23.2 84.3 40.2 Q99.6 41.9 96.2 55.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 244 200 258 Q300 272 400 252 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M44 258 L44 126 L136 126 L136 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M38 128 Q38 92 90 88 Q142 92 142 128 Z"/>
  <path fill="none" stroke-width="3" d="M200 42 L200 14"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="12" r="6"/>
  <path class="fillable" fill="#ffffff" d="M146 258 L146 62 L254 62 L254 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 66 L200 40 L260 66 Z"/>
  <path class="fillable" fill="#ffffff" d="M264 258 L264 108 L356 108 L356 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M258 110 L362 110 L362 98 L258 98 Z"/>
  <path class="fillable" fill="#ffffff" d="M296 98 L296 78 Q310 70 324 78 L324 98 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 82 L184 82 Q188 82 188 86 L188 108 Q188 112 184 112 L164 112 Q160 112 160 108 L160 86 Q160 82 164 82 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 82 L230 82 Q234 82 234 86 L234 108 Q234 112 230 112 L210 112 Q206 112 206 108 L206 86 Q206 82 210 82 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 126 L184 126 Q188 126 188 130 L188 152 Q188 156 184 156 L164 156 Q160 156 160 152 L160 130 Q160 126 164 126 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 126 L230 126 Q234 126 234 130 L234 152 Q234 156 230 156 L210 156 Q206 156 206 152 L206 130 Q206 126 210 126 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 170 L184 170 Q188 170 188 174 L188 196 Q188 200 184 200 L164 200 Q160 200 160 196 L160 174 Q160 170 164 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 170 L230 170 Q234 170 234 174 L234 196 Q234 200 230 200 L210 200 Q206 200 206 196 L206 174 Q206 170 210 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 142 L76 142 Q80 142 80 146 L80 164 Q80 168 76 168 L60 168 Q56 168 56 164 L56 146 Q56 142 60 142 Z"/>
  <path class="fillable" fill="#ffffff" d="M96 142 L112 142 Q116 142 116 146 L116 164 Q116 168 112 168 L96 168 Q92 168 92 164 L92 146 Q92 142 96 142 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 188 L76 188 Q80 188 80 192 L80 210 Q80 214 76 214 L60 214 Q56 214 56 210 L56 192 Q56 188 60 188 Z"/>
  <path class="fillable" fill="#ffffff" d="M96 188 L112 188 Q116 188 116 192 L116 210 Q116 214 112 214 L96 214 Q92 214 92 210 L92 192 Q92 188 96 188 Z"/>
  <path class="fillable" fill="#ffffff" d="M280 124 L298 124 Q302 124 302 128 L302 148 Q302 152 298 152 L280 152 Q276 152 276 148 L276 128 Q276 124 280 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M320 124 L338 124 Q342 124 342 128 L342 148 Q342 152 338 152 L320 152 Q316 152 316 148 L316 128 Q316 124 320 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M280 172 L298 172 Q302 172 302 176 L302 196 Q302 200 298 200 L280 200 Q276 200 276 196 L276 176 Q276 172 280 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M320 172 L338 172 Q342 172 342 176 L342 196 Q342 200 338 200 L320 200 Q316 200 316 196 L316 176 Q316 172 320 172 Z"/>
  <path class="fillable" fill="#ffffff" d="M184 258 L184 222 Q184 210 200 210 Q216 210 216 222 L216 258 Z"/>
  <path fill="none" stroke-width="3" d="M200 212 L200 258"/>
</g>
''')

add('windmill', '🏭 风车', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="40" r="22"/>
  <path class="fillable" fill="#ffffff" d="M12.0 59.5 Q12.0 42.5 30.7 44.2 Q37.5 28.9 56.2 34.0 Q71.5 27.2 78.3 44.2 Q93.6 45.9 90.2 59.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 256 Q100 242 200 256 Q300 270 400 250 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 258 L170 120 L230 120 L250 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M144 176 L256 176 L256 188 L144 188 Z"/>
  <path class="fillable" fill="#ffffff" d="M184 258 L184 232 Q184 218 200 218 Q216 218 216 232 L216 258 Z"/>
  <path class="fillable" fill="#ffffff" d="M194 194 L206 194 Q210 194 210 198 L210 206 Q210 210 206 210 L194 210 Q190 210 190 206 L190 198 Q190 194 194 194 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 124 Q160 74 200 72 Q240 74 240 124 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 86 L196 6 Q196 2 192 2 L174 2 Q170 2 170 6 L170 86 Z" transform="rotate(45 200 104)"/>
  <path fill="none" stroke-width="2.5" d="M170 30 L196 30 M170 58 L196 58 M183 2 L183 86" transform="rotate(45 200 104)"/>
  <path class="fillable" fill="#ffffff" d="M196 86 L196 6 Q196 2 192 2 L174 2 Q170 2 170 6 L170 86 Z" transform="rotate(135 200 104)"/>
  <path fill="none" stroke-width="2.5" d="M170 30 L196 30 M170 58 L196 58 M183 2 L183 86" transform="rotate(135 200 104)"/>
  <path class="fillable" fill="#ffffff" d="M196 86 L196 6 Q196 2 192 2 L174 2 Q170 2 170 6 L170 86 Z" transform="rotate(225 200 104)"/>
  <path fill="none" stroke-width="2.5" d="M170 30 L196 30 M170 58 L196 58 M183 2 L183 86" transform="rotate(225 200 104)"/>
  <path class="fillable" fill="#ffffff" d="M196 86 L196 6 Q196 2 192 2 L174 2 Q170 2 170 6 L170 86 Z" transform="rotate(315 200 104)"/>
  <path fill="none" stroke-width="2.5" d="M170 30 L196 30 M170 58 L196 58 M183 2 L183 86" transform="rotate(315 200 104)"/>
  <path fill="none" d="M200 104 L200 2" transform="rotate(45 200 104)"/>
  <path fill="none" d="M200 104 L200 2" transform="rotate(135 200 104)"/>
  <path fill="none" d="M200 104 L200 2" transform="rotate(225 200 104)"/>
  <path fill="none" d="M200 104 L200 2" transform="rotate(315 200 104)"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="104" r="12"/>
  <path fill="none" stroke-width="3" d="M60 262 L60 232"/>
  <path class="fillable" fill="#ffffff" d="M48 222 Q48 240 60 240 Q72 240 72 222 L66 230 L60 218 L54 230 Z"/>
  <path fill="none" stroke-width="3" d="M96 262 L96 232"/>
  <path class="fillable" fill="#ffffff" d="M84 222 Q84 240 96 240 Q108 240 108 222 L102 230 L96 218 L90 230 Z"/>
  <path fill="none" stroke-width="3" d="M320 262 L320 232"/>
  <path class="fillable" fill="#ffffff" d="M308 222 Q308 240 320 240 Q332 240 332 222 L326 230 L320 218 L314 230 Z"/>
</g>
''')

add('church', '⛪ 教堂', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="354" cy="40" r="20"/>
  <path class="fillable" fill="#ffffff" d="M18.0 51.5 Q18.0 34.5 36.7 36.2 Q43.5 20.9 62.2 26.0 Q77.5 19.2 84.3 36.2 Q99.6 37.9 96.2 51.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 244 200 258 Q300 272 400 252 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M48 262 L52 216 L64 216 L68 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M58 132 Q28 180 30 210 Q32 226 58 226 Q84 226 86 210 Q88 180 58 132 Z"/>
  <path class="fillable" fill="#ffffff" d="M332 262 L336 216 L348 216 L352 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M342 132 Q312 180 314 210 Q316 226 342 226 Q368 226 370 210 Q372 180 342 132 Z"/>
  <path fill="none" stroke-width="4" d="M200 34 L200 8 M190 18 L210 18"/>
  <path class="fillable" fill="#ffffff" d="M174 140 L174 72 L226 72 L226 140 Z"/>
  <path class="fillable" fill="#ffffff" d="M184 108 L184 92 Q184 82 200 82 Q216 82 216 92 L216 108 Z"/>
  <path class="fillable" fill="#ffffff" d="M192 106 Q192 94 200 94 Q208 94 208 106 Z"/>
  <path class="fillable" fill="#ffffff" d="M166 74 Q164 66 172 62 L198 34 Q200 32 202 34 L228 62 Q236 66 234 74 Z"/>
  <path class="fillable" fill="#ffffff" d="M112 256 L112 156 L288 156 L288 256 Z"/>
  <path class="fillable" fill="#ffffff" d="M98 162 Q92 156 98 150 L194 112 Q200 108 206 112 L302 150 Q308 156 302 162 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="170" r="14"/>
  <path fill="none" stroke-width="2.5" d="M186 170 L214 170 M200 156 L200 184"/>
  <path class="fillable" fill="#ffffff" d="M176 256 L176 214 Q176 190 200 190 Q224 190 224 214 L224 256 Z"/>
  <path fill="none" stroke-width="3" d="M200 192 L200 256"/>
  <path class="fillable" fill="#ffffff" d="M128 230 L128 196 Q128 182 142 182 Q156 182 156 196 L156 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M244 230 L244 196 Q244 182 258 182 Q272 182 272 196 L272 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M164 256 L236 256 L244 270 L156 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M172 300 L180 270 L220 270 L228 300 Z"/>
</g>
''')

add('hut', '🛖 茅草屋', 'building', '''
<g stroke="#1a1a1a" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="352" cy="42" r="22"/>
  <path class="fillable" fill="#ffffff" d="M20.0 57.5 Q20.0 40.5 38.7 42.2 Q45.5 26.9 64.2 32.0 Q79.5 25.2 86.3 42.2 Q101.6 43.9 98.2 57.5 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 258 Q100 244 200 258 Q300 272 400 252 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 262 Q340 200 322 120 L332 118 Q352 200 344 262 Z"/>
  <path class="fillable" fill="#ffffff" d="M326 120 Q300 100 270 112 Q290 88 326 108 Z"/>
  <path class="fillable" fill="#ffffff" d="M328 118 Q360 96 392 112 Q362 92 330 108 Z"/>
  <path class="fillable" fill="#ffffff" d="M326 114 Q310 80 286 74 Q320 70 332 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 114 Q350 80 378 76 Q346 70 328 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M124 256 L124 176 L276 176 L276 256 Q200 266 124 256 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="146" cy="232" rx="10" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="256" cy="214" rx="10" ry="7"/>
  <ellipse class="fillable" fill="#ffffff" cx="150" cy="200" rx="8" ry="6"/>
  <path class="fillable" fill="#ffffff" d="M174 260 L174 220 Q174 196 200 196 Q226 196 226 220 L226 260 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="252" cy="236" rx="12" ry="10"/>
  <path class="fillable" fill="#ffffff" d="M84 182 Q100.6 204 117.1 182 Q133.7 204 150.3 182 Q166.9 204 183.4 182 Q200.0 204 216.6 182 Q233.1 204 249.7 182 Q266.3 204 282.9 182 Q299.4 204 316.0 182 L200 60 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 150 Q200 132 280 150 L232 96 Q200 88 168 96 Z"/>
  <path fill="none" stroke-width="2.5" d="M144 122 L118 176 M176 110 L160 176 M200 104 L200 176 M224 110 L240 176 M256 122 L282 176"/>
  <path class="fillable" fill="#ffffff" d="M186 66 Q190 40 200 36 Q210 40 214 66 Z"/>
  <path class="fillable" fill="#ffffff" d="M28 262 Q20 236 42 230 Q52 214 70 226 Q90 228 86 248 Q92 262 76 264 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 300 Q186 280 176 262 L224 262 Q216 280 222 300 Z"/>
</g>
''')

# Sanity: make sure we have 100
assert len(TEMPLATES) == 100, f'expected 100 templates, got {len(TEMPLATES)}'
