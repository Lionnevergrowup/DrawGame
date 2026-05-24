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

# =============================================================================
# 50 more templates to bring totals to ≥10 per category (100 total)
# =============================================================================

# --- Ocean: +4 ---
add('shark', '🦈 鲨鱼', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke="#9bd0ff" stroke-width="2" stroke-dasharray="6 6" fill="none"><line x1="60" y1="0" x2="80" y2="60"/><line x1="300" y1="0" x2="320" y2="60"/></g>
  <path class="fillable" fill="#ffffff" d="M0 240 Q60 230 120 240 Q180 250 240 240 Q300 230 400 245 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 260 Q60 252 120 260 Q180 268 240 260 Q300 252 400 263"/><path d="M0 280 Q60 272 120 280 Q180 288 240 280 Q300 272 400 283"/></g>
  <path class="fillable" fill="#ffffff" d="M80 170 Q60 110 160 100 Q260 95 310 130 Q335 145 330 175 Q330 195 280 200 L100 200 Q70 200 80 170 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 175 Q360 160 380 130 Q360 175 348 185 Z"/>
  <path class="fillable" fill="#ffffff" d="M330 180 Q360 190 380 215 Q358 195 348 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 105 L160 50 L210 95 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 200 Q145 222 165 222 Q175 218 175 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M225 200 Q215 222 235 222 Q245 218 245 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M105 175 Q150 178 195 178 L195 195 Q150 200 105 195 Z"/>
  <g stroke-width="2" fill="none"><line x1="130" y1="160" x2="135" y2="180"/><line x1="145" y1="158" x2="150" y2="178"/><line x1="160" y1="156" x2="165" y2="176"/></g>
  <circle class="fillable" fill="#ffffff" cx="135" cy="140" r="8"/>
  <circle fill="#1a1a1a" cx="136" cy="142" r="3"/>
  <path class="fillable" fill="#ffffff" d="M80 178 Q100 185 145 188 L145 200 Q105 200 80 195 Z"/>
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M92 184 L96 192 L100 184 Z"/><path class="fillable" fill="#ffffff" d="M104 186 L108 194 L112 186 Z"/><path class="fillable" fill="#ffffff" d="M116 188 L120 196 L124 188 Z"/><path class="fillable" fill="#ffffff" d="M128 188 L132 196 L136 188 Z"/></g>
</g>
''')

add('seahorse', '🌊 海马', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke="#9bd0ff" stroke-width="2" stroke-dasharray="6 6" fill="none"><line x1="80" y1="0" x2="80" y2="50"/><line x1="320" y1="0" x2="320" y2="50"/></g>
  <path class="fillable" fill="#ffffff" d="M180 50 Q220 50 235 80 Q245 110 235 140 Q220 170 210 195 Q205 220 215 245 Q225 265 235 270 Q250 270 245 255 Q235 240 230 220 Q230 200 245 175 Q265 145 260 110 Q255 75 230 55 Q205 38 180 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M178 55 Q160 60 150 75 Q165 75 178 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 50 Q205 35 215 25 Q225 30 220 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M232 78 L242 70 L240 85 Z"/>
  <path class="fillable" fill="#ffffff" d="M232 100 L242 92 L240 107 Z"/>
  <path class="fillable" fill="#ffffff" d="M236 122 L246 114 L244 129 Z"/>
  <path class="fillable" fill="#ffffff" d="M232 145 L242 140 L237 158 Z"/>
  <path class="fillable" fill="#ffffff" d="M218 170 L228 165 L222 183 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 195 L220 192 L213 210 Z"/>
  <path class="fillable" fill="#ffffff" d="M213 220 L222 220 L215 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 105 Q275 100 290 115 Q275 120 255 120 Z"/>
  <circle class="fillable" fill="#ffffff" cx="218" cy="70" r="6"/>
  <circle fill="#1a1a1a" cx="220" cy="71" r="2.5"/>
  <g><circle class="fillable" fill="#ffffff" cx="100" cy="100" r="6"/><circle class="fillable" fill="#ffffff" cx="115" cy="80" r="4"/><circle class="fillable" fill="#ffffff" cx="320" cy="170" r="5"/><circle class="fillable" fill="#ffffff" cx="335" cy="190" r="3"/><circle class="fillable" fill="#ffffff" cx="90" cy="200" r="4"/></g>
</g>
''')

add('lobster', '🦞 龙虾', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="50" cy="280" r="3"/><circle class="fillable" fill="#ffffff" cx="350" cy="275" r="3"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="180" rx="50" ry="40"/>
  <path class="fillable" fill="#ffffff" d="M250 175 Q280 175 290 185 Q280 195 250 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 180 Q275 180 285 195 Q275 215 255 210 Q245 200 250 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 175 Q120 175 110 185 Q120 195 150 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 180 Q125 180 115 195 Q125 215 145 210 Q155 200 150 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M260 195 L325 220 L320 235 L255 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M310 218 Q335 220 340 235 Q325 240 318 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M305 230 Q330 232 332 245 Q318 250 312 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 195 L75 220 L80 235 L145 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M90 218 Q65 220 60 235 Q75 240 82 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M95 230 Q70 232 68 245 Q82 250 88 240 Z"/>
  <g stroke-width="2" fill="none"><line x1="170" y1="200" x2="160" y2="225"/><line x1="180" y1="205" x2="172" y2="232"/><line x1="190" y1="208" x2="186" y2="238"/><line x1="210" y1="208" x2="214" y2="238"/><line x1="220" y1="205" x2="228" y2="232"/><line x1="230" y1="200" x2="240" y2="225"/></g>
  <line x1="240" y1="160" x2="280" y2="135"/>
  <line x1="245" y1="170" x2="295" y2="160"/>
  <line x1="160" y1="160" x2="120" y2="135"/>
  <line x1="155" y1="170" x2="105" y2="160"/>
  <circle class="fillable" fill="#ffffff" cx="187" cy="170" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="213" cy="170" r="5"/>
  <circle fill="#1a1a1a" cx="188" cy="172" r="2"/>
  <circle fill="#1a1a1a" cx="214" cy="172" r="2"/>
  <g stroke-width="1.5" fill="none"><line x1="180" y1="155" x2="195" y2="155"/><line x1="205" y1="155" x2="220" y2="155"/></g>
</g>
''')

add('scuba', '🤿 潜水员', 'ocean', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke="#9bd0ff" stroke-width="2" stroke-dasharray="6 6" fill="none"><line x1="60" y1="0" x2="60" y2="60"/><line x1="200" y1="0" x2="200" y2="50"/><line x1="340" y1="0" x2="340" y2="60"/></g>
  <path class="fillable" fill="#ffffff" d="M0 260 Q100 250 200 260 Q300 270 400 255 L400 300 L0 300 Z"/>
  <circle class="fillable" fill="#ffffff" cx="190" cy="120" r="42"/>
  <circle class="fillable" fill="#ffffff" cx="190" cy="120" r="30"/>
  <path class="fillable" fill="#ffffff" d="M170 100 L185 100 L185 130 L170 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 100 L210 100 L210 130 L195 130 Z"/>
  <circle fill="#1a1a1a" cx="177" cy="115" r="2"/>
  <circle fill="#1a1a1a" cx="203" cy="115" r="2"/>
  <path fill="none" d="M180 140 Q190 145 200 140"/>
  <path class="fillable" fill="#ffffff" d="M195 158 L215 145 L222 155 L205 168 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="230" cy="135" r="6"/><circle class="fillable" fill="#ffffff" cx="245" cy="125" r="4"/><circle class="fillable" fill="#ffffff" cx="255" cy="115" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M150 170 L235 170 L240 240 L145 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 175 L150 175 L160 215 L145 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 175 L270 175 L260 215 L245 220 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 240 L155 280 L185 280 L185 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 240 L200 280 L230 280 L235 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 215 L160 215 L160 232 L130 232 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 215 L270 215 L270 232 L240 232 Z"/>
  <path class="fillable" fill="#ffffff" d="M245 175 L290 175 L290 230 L245 230 Z"/>
  <line x1="245" y1="195" x2="290" y2="195"/>
  <g><circle class="fillable" fill="#ffffff" cx="80" cy="100" r="7"/><circle class="fillable" fill="#ffffff" cx="100" cy="80" r="5"/><circle class="fillable" fill="#ffffff" cx="320" cy="120" r="6"/><circle class="fillable" fill="#ffffff" cx="335" cy="100" r="4"/></g>
</g>
''')

# --- Fantasy: +3 ---
add('witch', '🧙‍♀️ 女巫和扫帚', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="22"/>
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="120" cy="60" r="2.5"/><circle class="fillable" fill="#ffffff" cx="320" cy="80" r="2.5"/><circle class="fillable" fill="#ffffff" cx="370" cy="120" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M150 110 L250 95 L210 30 Z"/>
  <rect class="fillable" fill="#ffffff" x="148" y="108" width="105" height="12"/>
  <circle class="fillable" fill="#ffffff" cx="222" cy="65" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="150" r="35"/>
  <circle class="fillable" fill="#ffffff" cx="187" cy="148" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="213" cy="148" r="6"/>
  <circle fill="#1a1a1a" cx="188" cy="150" r="2.5"/>
  <circle fill="#1a1a1a" cx="214" cy="150" r="2.5"/>
  <path fill="none" d="M188 165 Q200 175 212 165"/>
  <path class="fillable" fill="#ffffff" d="M180 175 L155 235 L245 235 L220 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 235 L130 280 L270 280 L250 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 180 Q140 200 130 220 L155 225 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 180 Q260 200 270 220 L245 225 Z"/>
  <line x1="270" y1="250" x2="360" y2="180"/>
  <path class="fillable" fill="#ffffff" d="M340 180 L380 165 L390 175 L355 195 Z"/>
  <g stroke-width="1.5"><line x1="345" y1="188" x2="375" y2="178"/><line x1="350" y1="195" x2="380" y2="185"/><line x1="355" y1="202" x2="383" y2="192"/></g>
</g>
''')

add('fairy', '🧚 小仙女', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M50 40 L52 47 L60 47 L54 51 L56 59 L50 55 L44 59 L46 51 L40 47 L48 47 Z"/><path class="fillable" fill="#ffffff" d="M340 50 L342 57 L350 57 L344 61 L346 69 L340 65 L334 69 L336 61 L330 57 L338 57 Z"/><circle class="fillable" fill="#ffffff" cx="80" cy="120" r="3"/><circle class="fillable" fill="#ffffff" cx="320" cy="160" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M155 130 Q120 100 95 130 Q105 165 145 175 Q160 165 160 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M245 130 Q280 100 305 130 Q295 165 255 175 Q240 165 240 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 175 Q130 195 110 220 Q140 215 165 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 175 Q270 195 290 220 Q260 215 235 200 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="115" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="192" cy="113" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="208" cy="113" r="4"/>
  <circle fill="#1a1a1a" cx="193" cy="115" r="2"/>
  <circle fill="#1a1a1a" cx="209" cy="115" r="2"/>
  <path fill="none" d="M194 125 Q200 130 206 125"/>
  <path class="fillable" fill="#ffffff" d="M180 95 Q200 80 220 95 L220 100 Q200 92 180 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 145 L220 145 L230 175 L170 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 175 Q160 200 165 230 Q200 235 235 230 Q240 200 230 175 Z"/>
  <line x1="180" y1="180" x2="160" y2="200"/>
  <line x1="220" y1="180" x2="240" y2="200"/>
  <line x1="240" y1="200" x2="260" y2="170"/>
  <path class="fillable" fill="#ffffff" d="M255 162 L265 158 L268 170 L258 173 Z"/>
  <g stroke-width="1.5"><line x1="255" y1="155" x2="248" y2="148"/><line x1="265" y1="150" x2="270" y2="143"/><line x1="270" y1="160" x2="280" y2="160"/></g>
  <path class="fillable" fill="#ffffff" d="M195 230 L195 260 L180 260 Z"/>
  <path class="fillable" fill="#ffffff" d="M205 230 L205 260 L220 260 Z"/>
</g>
''')

add('genie_lamp', '🪔 神灯', 'fantasy', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="280" rx="120" ry="12"/>
  <path class="fillable" fill="#ffffff" d="M120 250 Q120 200 200 195 Q280 200 280 250 Q280 275 200 275 Q120 275 120 250 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="200" rx="55" ry="10"/>
  <rect class="fillable" fill="#ffffff" x="180" y="180" width="40" height="22" rx="3"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="180" rx="22" ry="6"/>
  <path class="fillable" fill="#ffffff" d="M280 220 Q325 200 335 235 Q320 245 295 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 230 Q90 222 85 245 Q100 250 122 245 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M150 235 Q180 240 220 235 Q250 240 270 235"/></g>
  <path class="fillable" fill="#ffffff" d="M195 178 Q185 160 195 145 Q205 130 200 110 Q220 125 215 150 Q230 165 220 178 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 110 Q210 95 200 80 Q190 65 200 50 Q220 65 215 85 Q220 100 210 110 Z"/>
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="160" cy="130" r="3"/><circle class="fillable" fill="#ffffff" cx="245" cy="120" r="3"/><circle class="fillable" fill="#ffffff" cx="170" cy="90" r="2.5"/><circle class="fillable" fill="#ffffff" cx="235" cy="80" r="2.5"/></g>
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="170" cy="240" r="3"/><circle class="fillable" fill="#ffffff" cx="200" cy="245" r="3"/><circle class="fillable" fill="#ffffff" cx="230" cy="240" r="3"/></g>
</g>
''')

# --- Vehicle: +3 ---
add('bicycle', '🚲 自行车', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 232 200 240 Q300 248 400 235 L400 300 L0 300 Z"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="220" r="48"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="220" r="48"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="220" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="300" cy="220" r="8"/>
  <g stroke-width="1.5" fill="none">
    <line x1="100" y1="172" x2="100" y2="268"/><line x1="52" y1="220" x2="148" y2="220"/>
    <line x1="100" y1="220" x2="135" y2="186"/><line x1="100" y1="220" x2="135" y2="254"/>
    <line x1="100" y1="220" x2="65" y2="186"/><line x1="100" y1="220" x2="65" y2="254"/>
    <line x1="300" y1="172" x2="300" y2="268"/><line x1="252" y1="220" x2="348" y2="220"/>
    <line x1="300" y1="220" x2="335" y2="186"/><line x1="300" y1="220" x2="335" y2="254"/>
    <line x1="300" y1="220" x2="265" y2="186"/><line x1="300" y1="220" x2="265" y2="254"/>
  </g>
  <line x1="100" y1="220" x2="200" y2="160"/>
  <line x1="200" y1="160" x2="300" y2="220"/>
  <line x1="200" y1="160" x2="200" y2="220"/>
  <line x1="200" y1="220" x2="300" y2="220"/>
  <line x1="200" y1="220" x2="100" y2="220"/>
  <line x1="220" y1="160" x2="240" y2="120"/>
  <path class="fillable" fill="#ffffff" d="M225 115 L255 115 L250 130 L230 130 Z"/>
  <line x1="100" y1="160" x2="120" y2="120"/>
  <rect class="fillable" fill="#ffffff" x="92" y="113" width="60" height="6"/>
  <line x1="100" y1="113" x2="100" y2="100"/>
  <line x1="140" y1="113" x2="140" y2="100"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="220" r="14"/>
  <line x1="186" y1="220" x2="184" y2="240"/>
  <line x1="214" y1="220" x2="216" y2="200"/>
  <rect class="fillable" fill="#ffffff" x="180" y="240" width="12" height="4"/>
  <rect class="fillable" fill="#ffffff" x="208" y="196" width="12" height="4"/>
  <path class="fillable" fill="#ffffff" d="M200 165 L205 145 L215 145 L210 165 Z"/>
</g>
''')

add('sailboat', '⛵ 帆船', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 50 Q295 35 315 40 Q335 30 350 50 Q365 50 360 65 L280 65 Q270 60 280 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 220 Q50 210 100 220 Q150 230 200 220 Q250 210 300 220 Q350 230 400 215 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 240 Q50 232 100 240 Q150 248 200 240 Q250 232 300 240 Q350 248 400 235"/><path d="M0 265 Q50 257 100 265 Q150 273 200 265 Q250 257 300 265 Q350 273 400 260"/></g>
  <path class="fillable" fill="#ffffff" d="M80 220 L320 220 L290 270 L110 270 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="140" cy="245" r="6"/><circle class="fillable" fill="#ffffff" cx="200" cy="245" r="6"/><circle class="fillable" fill="#ffffff" cx="260" cy="245" r="6"/></g>
  <line x1="200" y1="220" x2="200" y2="60"/>
  <path class="fillable" fill="#ffffff" d="M200 70 L290 200 L200 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 75 L110 200 L195 200 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="170" y1="130" x2="170" y2="200"/><line x1="140" y1="170" x2="140" y2="200"/><line x1="230" y1="130" x2="230" y2="200"/><line x1="260" y1="170" x2="260" y2="200"/></g>
  <rect class="fillable" fill="#ffffff" x="200" y="55" width="35" height="18"/>
  <path class="fillable" fill="#ffffff" d="M200 73 L235 73 L228 80 L207 80 Z"/>
</g>
''')

add('helicopter', '🚁 直升机', 'vehicle', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="60" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 55 Q295 40 315 45 Q335 35 350 55 Q365 60 360 70 L280 70 Q270 65 280 55 Z"/>
  <path class="fillable" fill="#ffffff" d="M70 200 Q70 130 200 130 Q300 130 320 175 L320 210 Q200 230 80 215 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="160" cy="170" rx="58" ry="32"/>
  <line x1="160" y1="138" x2="160" y2="155"/>
  <path class="fillable" fill="#ffffff" d="M150 135 L170 135 L175 140 L145 140 Z"/>
  <rect class="fillable" fill="#ffffff" x="225" y="160" width="65" height="30" rx="3"/>
  <g stroke-width="1.5" fill="none"><line x1="240" y1="160" x2="240" y2="190"/><line x1="255" y1="160" x2="255" y2="190"/><line x1="270" y1="160" x2="270" y2="190"/></g>
  <path class="fillable" fill="#ffffff" d="M320 175 L380 165 L382 195 L320 200 Z"/>
  <line x1="370" y1="170" x2="380" y2="155"/>
  <line x1="380" y1="155" x2="395" y2="160"/>
  <line x1="395" y1="160" x2="385" y2="175"/>
  <line x1="380" y1="155" x2="385" y2="175"/>
  <line x1="80" y1="215" x2="80" y2="240"/>
  <line x1="280" y1="215" x2="280" y2="240"/>
  <line x1="60" y1="240" x2="300" y2="240"/>
  <line x1="80" y1="220" x2="60" y2="240"/>
  <line x1="280" y1="220" x2="300" y2="240"/>
  <g><circle class="fillable" fill="#ffffff" cx="60" cy="240" r="4"/><circle class="fillable" fill="#ffffff" cx="300" cy="240" r="4"/></g>
  <path class="fillable" fill="#ffffff" d="M50 130 L160 138 L160 142 L50 138 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 138 L300 130 L300 134 L170 142 Z"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="138" r="5"/>
</g>
''')

# --- Nature: +3 ---
add('cactus', '🌵 仙人掌', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="345" cy="60" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q60 240 120 250 Q180 260 240 250 Q300 240 400 255 L400 300 L0 300 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M30 285 L40 275"/><path d="M55 290 L65 280"/><path d="M340 285 L350 275"/><path d="M365 285 L375 275"/></g>
  <path class="fillable" fill="#ffffff" d="M170 250 L170 130 Q170 110 190 110 L220 110 Q240 110 240 130 L240 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 170 L130 170 Q120 170 120 180 L120 220 Q120 230 130 230 L170 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 150 L280 150 Q290 150 290 160 L290 200 Q290 210 280 210 L240 210 Z"/>
  <g stroke-width="1.5" fill="none">
    <line x1="180" y1="140" x2="180" y2="145"/><line x1="200" y1="135" x2="200" y2="140"/><line x1="220" y1="140" x2="220" y2="145"/>
    <line x1="180" y1="180" x2="180" y2="185"/><line x1="200" y1="175" x2="200" y2="180"/><line x1="220" y1="180" x2="220" y2="185"/>
    <line x1="180" y1="220" x2="180" y2="225"/><line x1="200" y1="215" x2="200" y2="220"/><line x1="220" y1="220" x2="220" y2="225"/>
    <line x1="140" y1="190" x2="140" y2="195"/><line x1="160" y1="200" x2="160" y2="205"/>
    <line x1="260" y1="170" x2="260" y2="175"/><line x1="280" y1="180" x2="280" y2="185"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M205 110 Q200 95 210 92 Q218 95 215 110 Z"/>
  <circle class="fillable" fill="#ffffff" cx="138" cy="170" r="5"/>
  <circle class="fillable" fill="#ffffff" cx="278" cy="150" r="5"/>
  <path class="fillable" fill="#ffffff" d="M40 250 L40 200 Q40 188 50 188 Q60 188 60 200 L60 250 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="45" y1="210" x2="45" y2="215"/><line x1="55" y1="220" x2="55" y2="225"/></g>
  <path class="fillable" fill="#ffffff" d="M310 250 L310 215 Q310 208 320 208 Q330 208 330 215 L330 250 Z"/>
</g>
''')

add('palm_island', '🏝️ 椰子树小岛', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="22"/>
  <path class="fillable" fill="#ffffff" d="M0 220 Q40 215 80 220 Q120 225 160 220 Q200 215 240 220 Q280 225 320 220 Q360 215 400 220 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 240 Q40 235 80 240 Q120 245 160 240 Q200 235 240 240 Q280 245 320 240 Q360 235 400 240"/><path d="M0 265 Q40 260 80 265 Q120 270 160 265 Q200 260 240 265 Q280 270 320 265 Q360 260 400 265"/></g>
  <path class="fillable" fill="#ffffff" d="M70 240 Q200 220 330 240 Q330 260 200 260 Q70 260 70 240 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="150" cy="250" r="3"/><circle class="fillable" fill="#ffffff" cx="250" cy="250" r="3"/><circle class="fillable" fill="#ffffff" cx="200" cy="248" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M195 245 Q193 200 198 145 L210 145 Q207 200 205 245 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="198" y1="220" x2="207" y2="220"/><line x1="199" y1="200" x2="206" y2="200"/><line x1="200" y1="180" x2="205" y2="180"/></g>
  <path class="fillable" fill="#ffffff" d="M200 145 Q140 130 110 100 Q150 125 195 140 Q145 95 165 60 Q185 100 200 140 Q220 90 270 70 Q240 105 205 140 Q260 105 290 120 Q245 130 205 145 Q260 145 290 175 Q240 158 200 150 Q175 155 145 180 Q175 155 195 148 Z"/>
  <circle class="fillable" fill="#ffffff" cx="205" cy="155" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="192" cy="158" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="215" cy="162" r="5"/>
  <path class="fillable" fill="#ffffff" d="M340 240 L348 215 L356 240 Z"/>
  <line x1="348" y1="215" x2="348" y2="200"/>
  <path class="fillable" fill="#ffffff" d="M345 200 L360 205 L345 210 Z"/>
</g>
''')

add('mushroom_garden', '🍄 蘑菇林', 'nature', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 232 200 240 Q300 248 400 235 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M30 285 L40 270"/><path d="M55 285 L65 270"/><path d="M340 285 L350 270"/><path d="M370 285 L380 270"/></g>
  <path class="fillable" fill="#ffffff" d="M120 200 Q120 130 200 130 Q280 130 280 200 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="155" cy="170" r="9"/><circle class="fillable" fill="#ffffff" cx="200" cy="155" r="11"/><circle class="fillable" fill="#ffffff" cx="245" cy="170" r="9"/><circle class="fillable" fill="#ffffff" cx="175" cy="190" r="7"/><circle class="fillable" fill="#ffffff" cx="225" cy="190" r="7"/></g>
  <path class="fillable" fill="#ffffff" d="M165 200 L165 250 Q165 260 200 260 Q235 260 235 250 L235 200 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="180" y1="210" x2="180" y2="255"/><line x1="200" y1="210" x2="200" y2="258"/><line x1="220" y1="210" x2="220" y2="255"/></g>
  <path class="fillable" fill="#ffffff" d="M40 250 Q40 220 75 220 Q110 220 110 250 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="60" cy="235" r="5"/><circle class="fillable" fill="#ffffff" cx="85" cy="232" r="6"/></g>
  <path class="fillable" fill="#ffffff" d="M60 250 L60 275 Q60 282 75 282 Q90 282 90 275 L90 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M310 260 Q310 240 335 240 Q360 240 360 260 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="325" cy="252" r="4"/><circle class="fillable" fill="#ffffff" cx="345" cy="250" r="4"/></g>
  <path class="fillable" fill="#ffffff" d="M325 260 L325 280 Q325 285 335 285 Q345 285 345 280 L345 260 Z"/>
  <g><path class="fillable" fill="#ffffff" d="M280 260 Q280 248 295 248 Q310 248 310 260 Z"/><path class="fillable" fill="#ffffff" d="M290 260 L290 275 L300 275 L300 260 Z"/></g>
</g>
''')

# --- Food: +4 ---
add('candy', '🍬 一堆糖果', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="270" rx="160" ry="15"/>
  <ellipse class="fillable" fill="#ffffff" cx="100" cy="200" rx="40" ry="22"/>
  <path class="fillable" fill="#ffffff" d="M60 200 L40 185 L40 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 200 L160 185 L160 215 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="80" y1="188" x2="80" y2="212"/><line x1="120" y1="188" x2="120" y2="212"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="280" cy="210" rx="42" ry="24"/>
  <path class="fillable" fill="#ffffff" d="M238 210 L218 195 L218 225 Z"/>
  <path class="fillable" fill="#ffffff" d="M322 210 L342 195 L342 225 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M258 200 Q280 215 302 200"/><path d="M258 220 Q280 205 302 220"/></g>
  <circle class="fillable" fill="#ffffff" cx="200" cy="160" r="28"/>
  <line x1="200" y1="132" x2="200" y2="100"/>
  <path class="fillable" fill="#ffffff" d="M195 100 L208 95 L208 110 L195 110 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M180 150 Q200 165 220 150"/><path d="M180 170 Q200 155 220 170"/></g>
  <path class="fillable" fill="#ffffff" d="M85 250 L80 230 L95 220 L100 230 L115 230 L120 240 Q110 255 95 252 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M90 240 L105 230"/><path d="M95 245 L110 240"/></g>
  <path class="fillable" fill="#ffffff" d="M315 250 Q310 230 325 220 Q330 215 335 225 Q345 230 340 245 Z"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="240" r="15"/>
  <g><circle class="fillable" fill="#ffffff" cx="178" cy="237" r="4"/><circle class="fillable" fill="#ffffff" cx="184" cy="244" r="3"/></g>
  <circle class="fillable" fill="#ffffff" cx="220" cy="245" r="13"/>
  <g><circle class="fillable" fill="#ffffff" cx="218" cy="242" r="3"/><circle class="fillable" fill="#ffffff" cx="224" cy="248" r="3"/></g>
  <circle class="fillable" fill="#ffffff" cx="245" cy="240" r="10"/>
</g>
''')

add('cookies', '🍪 巧克力饼干', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="265" rx="160" ry="15"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="220" rx="155" ry="32"/>
  <g stroke-width="1.5" fill="none"><line x1="60" y1="240" x2="340" y2="240"/></g>
  <circle class="fillable" fill="#ffffff" cx="115" cy="185" r="45"/>
  <g><circle class="fillable" fill="#ffffff" cx="100" cy="170" r="6"/><circle class="fillable" fill="#ffffff" cx="125" cy="178" r="5"/><circle class="fillable" fill="#ffffff" cx="135" cy="195" r="6"/><circle class="fillable" fill="#ffffff" cx="105" cy="200" r="5"/><circle class="fillable" fill="#ffffff" cx="118" cy="158" r="4"/><circle class="fillable" fill="#ffffff" cx="92" cy="190" r="4"/></g>
  <circle class="fillable" fill="#ffffff" cx="210" cy="170" r="50"/>
  <g><circle class="fillable" fill="#ffffff" cx="195" cy="155" r="6"/><circle class="fillable" fill="#ffffff" cx="220" cy="160" r="5"/><circle class="fillable" fill="#ffffff" cx="230" cy="180" r="6"/><circle class="fillable" fill="#ffffff" cx="200" cy="185" r="5"/><circle class="fillable" fill="#ffffff" cx="185" cy="175" r="4"/><circle class="fillable" fill="#ffffff" cx="215" cy="195" r="5"/><circle class="fillable" fill="#ffffff" cx="240" cy="165" r="4"/></g>
  <circle class="fillable" fill="#ffffff" cx="310" cy="190" r="42"/>
  <g><circle class="fillable" fill="#ffffff" cx="295" cy="180" r="5"/><circle class="fillable" fill="#ffffff" cx="320" cy="185" r="6"/><circle class="fillable" fill="#ffffff" cx="325" cy="200" r="4"/><circle class="fillable" fill="#ffffff" cx="300" cy="205" r="5"/><circle class="fillable" fill="#ffffff" cx="312" cy="170" r="4"/></g>
  <g><circle class="fillable" fill="#ffffff" cx="80" cy="250" r="4"/><circle class="fillable" fill="#ffffff" cx="170" cy="252" r="4"/><circle class="fillable" fill="#ffffff" cx="260" cy="250" r="4"/><circle class="fillable" fill="#ffffff" cx="350" cy="252" r="4"/></g>
</g>
''')

add('watermelon', '🍉 西瓜', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M50 70 A180 180 0 0 1 350 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M55 70 A175 175 0 0 1 345 70 L335 70 A165 165 0 0 0 65 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M65 70 A165 165 0 0 1 335 70 L325 70 A155 155 0 0 0 75 70 Z"/>
  <path class="fillable" fill="#ffffff" d="M75 70 A155 155 0 0 1 325 70 Z"/>
  <g>
    <ellipse class="fillable" fill="#1a1a1a" cx="110" cy="100" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="145" cy="90" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="180" cy="85" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="215" cy="85" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="250" cy="90" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="285" cy="100" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="130" cy="130" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="165" cy="125" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="200" cy="120" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="235" cy="125" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="270" cy="130" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="155" cy="160" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="195" cy="155" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="235" cy="160" rx="4" ry="6"/>
    <ellipse class="fillable" fill="#1a1a1a" cx="200" cy="200" rx="4" ry="6"/>
  </g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="240" rx="140" ry="14"/>
  <path class="fillable" fill="#ffffff" d="M70 260 Q200 250 330 260 L335 285 Q200 295 65 285 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="100" cy="278" r="3"/><circle class="fillable" fill="#ffffff" cx="160" cy="278" r="3"/><circle class="fillable" fill="#ffffff" cx="240" cy="278" r="3"/><circle class="fillable" fill="#ffffff" cx="300" cy="278" r="3"/></g>
</g>
''')

add('lollipop', '🍭 棒棒糖', 'food', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="50" cy="50" r="3"/><circle class="fillable" fill="#ffffff" cx="350" cy="60" r="3"/><circle class="fillable" fill="#ffffff" cx="80" cy="220" r="3"/></g>
  <rect class="fillable" fill="#ffffff" x="125" y="160" width="8" height="120"/>
  <rect class="fillable" fill="#ffffff" x="195" y="180" width="8" height="100"/>
  <rect class="fillable" fill="#ffffff" x="265" y="170" width="8" height="110"/>
  <circle class="fillable" fill="#ffffff" cx="129" cy="120" r="48"/>
  <path class="fillable" fill="#ffffff" d="M129 120 Q129 90 159 92 Q175 105 165 130 Q150 145 129 145 Q108 130 110 115 Q115 100 129 100 Q140 105 135 120 Z"/>
  <path class="fillable" fill="#ffffff" d="M129 120 Q129 95 149 90 Q160 92 156 105 Q145 115 135 118 Z"/>
  <circle class="fillable" fill="#ffffff" cx="199" cy="142" r="42"/>
  <path class="fillable" fill="#ffffff" d="M199 105 L208 132 L235 132 L213 148 L222 175 L199 158 L176 175 L185 148 L163 132 L190 132 Z"/>
  <circle class="fillable" fill="#ffffff" cx="269" cy="130" r="46"/>
  <g><circle class="fillable" fill="#ffffff" cx="250" cy="115" r="5"/><circle class="fillable" fill="#ffffff" cx="275" cy="110" r="5"/><circle class="fillable" fill="#ffffff" cx="295" cy="120" r="5"/><circle class="fillable" fill="#ffffff" cx="255" cy="140" r="5"/><circle class="fillable" fill="#ffffff" cx="285" cy="145" r="5"/><circle class="fillable" fill="#ffffff" cx="270" cy="130" r="5"/><circle class="fillable" fill="#ffffff" cx="240" cy="130" r="4"/><circle class="fillable" fill="#ffffff" cx="295" cy="135" r="4"/></g>
</g>
''')

# --- Other: +3 ---
add('gift_stack', '🎁 礼物堆', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="285" rx="180" ry="12"/>
  <rect class="fillable" fill="#ffffff" x="60" y="220" width="120" height="60"/>
  <rect class="fillable" fill="#ffffff" x="115" y="220" width="14" height="60"/>
  <rect class="fillable" fill="#ffffff" x="60" y="240" width="120" height="14"/>
  <path class="fillable" fill="#ffffff" d="M122 220 Q105 200 95 210 Q105 222 122 222 Z"/>
  <path class="fillable" fill="#ffffff" d="M122 220 Q139 200 149 210 Q139 222 122 222 Z"/>
  <rect class="fillable" fill="#ffffff" x="220" y="190" width="140" height="90"/>
  <rect class="fillable" fill="#ffffff" x="282" y="190" width="16" height="90"/>
  <rect class="fillable" fill="#ffffff" x="220" y="220" width="140" height="18"/>
  <path class="fillable" fill="#ffffff" d="M290 190 Q270 165 258 178 Q270 195 290 192 Z"/>
  <path class="fillable" fill="#ffffff" d="M290 190 Q310 165 322 178 Q310 195 290 192 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="240" y1="252" x2="250" y2="260"/><line x1="260" y1="252" x2="270" y2="260"/><line x1="320" y1="252" x2="330" y2="260"/></g>
  <rect class="fillable" fill="#ffffff" x="100" y="130" width="100" height="86"/>
  <rect class="fillable" fill="#ffffff" x="145" y="130" width="12" height="86"/>
  <rect class="fillable" fill="#ffffff" x="100" y="160" width="100" height="14"/>
  <path class="fillable" fill="#ffffff" d="M151 130 Q135 110 125 120 Q135 132 151 132 Z"/>
  <path class="fillable" fill="#ffffff" d="M151 130 Q167 110 177 120 Q167 132 151 132 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="110" y1="195" x2="120" y2="205"/><line x1="180" y1="195" x2="190" y2="205"/></g>
</g>
''')

add('fireworks', '🎆 烟花', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="40" cy="180" r="2"/><circle class="fillable" fill="#ffffff" cx="370" cy="160" r="2"/></g>
  <path class="fillable" fill="#ffffff" d="M0 220 L50 220 L80 200 L120 220 L160 200 L200 220 L240 200 L280 220 L320 200 L360 220 L400 220 L400 300 L0 300 Z"/>
  <g stroke-width="1.5" fill="none">
    <rect class="fillable" fill="#ffffff" x="60" y="230" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="78" y="230" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="60" y="245" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="78" y="245" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="180" y="230" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="198" y="230" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="180" y="245" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="198" y="245" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="300" y="230" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="318" y="230" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="300" y="245" width="14" height="12"/>
    <rect class="fillable" fill="#ffffff" x="318" y="245" width="14" height="12"/>
  </g>
  <g>
    <circle class="fillable" fill="#ffffff" cx="100" cy="80" r="6"/>
    <g stroke-width="2"><line x1="100" y1="74" x2="100" y2="50"/><line x1="100" y1="86" x2="100" y2="110"/><line x1="94" y1="80" x2="70" y2="80"/><line x1="106" y1="80" x2="130" y2="80"/><line x1="96" y1="76" x2="80" y2="60"/><line x1="104" y1="76" x2="120" y2="60"/><line x1="96" y1="84" x2="80" y2="100"/><line x1="104" y1="84" x2="120" y2="100"/></g>
    <g><circle class="fillable" fill="#ffffff" cx="100" cy="48" r="3"/><circle class="fillable" fill="#ffffff" cx="100" cy="112" r="3"/><circle class="fillable" fill="#ffffff" cx="68" cy="80" r="3"/><circle class="fillable" fill="#ffffff" cx="132" cy="80" r="3"/><circle class="fillable" fill="#ffffff" cx="78" cy="58" r="3"/><circle class="fillable" fill="#ffffff" cx="122" cy="58" r="3"/><circle class="fillable" fill="#ffffff" cx="78" cy="102" r="3"/><circle class="fillable" fill="#ffffff" cx="122" cy="102" r="3"/></g>
  </g>
  <g>
    <circle class="fillable" fill="#ffffff" cx="240" cy="100" r="6"/>
    <g stroke-width="2"><line x1="240" y1="94" x2="240" y2="70"/><line x1="240" y1="106" x2="240" y2="130"/><line x1="234" y1="100" x2="210" y2="100"/><line x1="246" y1="100" x2="270" y2="100"/></g>
    <g><circle class="fillable" fill="#ffffff" cx="240" cy="68" r="3"/><circle class="fillable" fill="#ffffff" cx="240" cy="132" r="3"/><circle class="fillable" fill="#ffffff" cx="208" cy="100" r="3"/><circle class="fillable" fill="#ffffff" cx="272" cy="100" r="3"/></g>
  </g>
  <g>
    <circle class="fillable" fill="#ffffff" cx="340" cy="60" r="6"/>
    <g stroke-width="2"><line x1="340" y1="54" x2="340" y2="35"/><line x1="334" y1="60" x2="315" y2="60"/><line x1="346" y1="60" x2="365" y2="60"/><line x1="336" y1="56" x2="324" y2="44"/><line x1="344" y1="56" x2="356" y2="44"/></g>
    <g><circle class="fillable" fill="#ffffff" cx="340" cy="33" r="3"/><circle class="fillable" fill="#ffffff" cx="313" cy="60" r="3"/><circle class="fillable" fill="#ffffff" cx="367" cy="60" r="3"/></g>
  </g>
</g>
''')

add('balloon_bunch', '🎈 一束气球', 'other', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <ellipse class="fillable" fill="#ffffff" cx="100" cy="80" rx="32" ry="40"/>
  <path class="fillable" fill="#ffffff" d="M95 117 L100 124 L105 117 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="170" cy="60" rx="32" ry="40"/>
  <path class="fillable" fill="#ffffff" d="M165 97 L170 104 L175 97 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="240" cy="75" rx="32" ry="40"/>
  <path class="fillable" fill="#ffffff" d="M235 112 L240 119 L245 112 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="310" cy="100" rx="32" ry="40"/>
  <path class="fillable" fill="#ffffff" d="M305 137 L310 144 L315 137 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="135" cy="140" rx="28" ry="34"/>
  <path class="fillable" fill="#ffffff" d="M130 172 L135 178 L140 172 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="275" cy="150" rx="28" ry="34"/>
  <path class="fillable" fill="#ffffff" d="M270 182 L275 188 L280 182 Z"/>
  <g stroke-width="1.5" fill="none">
    <path d="M100 124 Q120 180 200 250"/>
    <path d="M170 104 Q180 170 200 250"/>
    <path d="M240 119 Q220 180 200 250"/>
    <path d="M310 144 Q260 200 200 250"/>
    <path d="M135 178 Q160 215 200 250"/>
    <path d="M275 188 Q240 220 200 250"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M190 250 L210 250 L210 280 L190 280 Z"/>
</g>
''')

# --- People (10) ---
add('family', '👨‍👩‍👧 一家四口', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="50" r="20"/>
  <path class="fillable" fill="#ffffff" d="M280 50 Q295 35 315 40 Q335 30 350 50 Q365 55 360 65 L280 65 Q270 60 280 50 Z"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <circle class="fillable" fill="#ffffff" cx="80" cy="115" r="22"/>
  <path class="fillable" fill="#ffffff" d="M62 100 L98 100 L102 80 L58 80 Z"/>
  <path class="fillable" fill="#ffffff" d="M62 135 L98 135 L108 215 L52 215 Z"/>
  <line x1="80" y1="135" x2="80" y2="215"/>
  <path class="fillable" fill="#ffffff" d="M58 215 L62 270 L80 270 L82 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M78 215 L80 270 L98 270 L102 215 Z"/>
  <circle fill="#1a1a1a" cx="74" cy="115" r="1.5"/><circle fill="#1a1a1a" cx="86" cy="115" r="1.5"/>
  <path fill="none" d="M74 125 Q80 130 86 125"/>
  <line x1="52" y1="170" x2="35" y2="190"/>
  <line x1="108" y1="170" x2="125" y2="180"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="115" r="22"/>
  <path class="fillable" fill="#ffffff" d="M148 105 L192 105 L195 85 L145 80 Q140 92 148 105 Z"/>
  <path class="fillable" fill="#ffffff" d="M148 135 Q150 215 152 215 L188 215 Q192 130 192 135 Q175 145 165 145 Q155 145 148 135 Z"/>
  <path class="fillable" fill="#ffffff" d="M152 215 Q140 285 160 270 L180 270 Q200 285 188 215 Z"/>
  <circle fill="#1a1a1a" cx="164" cy="115" r="1.5"/><circle fill="#1a1a1a" cx="176" cy="115" r="1.5"/>
  <path fill="none" d="M164 125 Q170 130 176 125"/>
  <line x1="142" y1="170" x2="125" y2="180"/>
  <line x1="198" y1="170" x2="220" y2="170"/>
  <circle class="fillable" fill="#ffffff" cx="245" cy="155" r="18"/>
  <path class="fillable" fill="#ffffff" d="M230 175 L260 175 L268 235 L223 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M225 235 L228 270 L245 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 235 L268 270 L268 235 Z"/>
  <circle fill="#1a1a1a" cx="240" cy="155" r="1.5"/><circle fill="#1a1a1a" cx="250" cy="155" r="1.5"/>
  <path fill="none" d="M240 165 Q245 168 250 165"/>
  <line x1="222" y1="200" x2="200" y2="170"/>
  <circle class="fillable" fill="#ffffff" cx="320" cy="180" r="14"/>
  <path class="fillable" fill="#ffffff" d="M308 192 L332 192 L335 235 L305 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M308 235 L310 265 L320 265 Z"/>
  <path class="fillable" fill="#ffffff" d="M325 235 L335 265 L335 235 Z"/>
  <circle fill="#1a1a1a" cx="316" cy="180" r="1.5"/><circle fill="#1a1a1a" cx="324" cy="180" r="1.5"/>
  <path fill="none" d="M316 187 Q320 190 324 187"/>
  <line x1="308" y1="210" x2="275" y2="200"/>
</g>
''')

add('baby', '👶 小宝宝', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 270 Q100 260 200 270 Q300 280 400 265 L400 300 L0 300 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="125" r="78"/>
  <path class="fillable" fill="#ffffff" d="M122 130 Q105 130 105 145 Q115 155 122 152 Z"/>
  <path class="fillable" fill="#ffffff" d="M278 130 Q295 130 295 145 Q285 155 278 152 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 60 Q170 50 178 56 Q180 65 175 70 Z"/>
  <circle class="fillable" fill="#ffffff" cx="178" cy="125" r="9"/>
  <circle class="fillable" fill="#ffffff" cx="222" cy="125" r="9"/>
  <circle fill="#1a1a1a" cx="180" cy="127" r="4"/>
  <circle fill="#1a1a1a" cx="222" cy="127" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="158" cy="155" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="242" cy="155" r="8"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="155" r="6"/>
  <path class="fillable" fill="#ffffff" d="M188 175 Q200 192 212 175 Q212 188 200 192 Q188 188 188 175 Z"/>
  <path fill="none" d="M195 180 L195 185"/>
  <path class="fillable" fill="#ffffff" d="M120 230 L160 215 L240 215 L280 230 L290 290 L110 290 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 215 L160 200 L240 200 L240 215 Z"/>
  <line x1="200" y1="200" x2="200" y2="290"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="245" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="175" cy="245" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="245" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="175" cy="265" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="265" r="4"/>
  <g><circle class="fillable" fill="#ffffff" cx="320" cy="60" r="6"/><circle class="fillable" fill="#ffffff" cx="340" cy="40" r="4"/><circle class="fillable" fill="#ffffff" cx="60" cy="100" r="4"/></g>
</g>
''')

add('chef', '👨‍🍳 厨师', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 260 Q100 252 200 260 Q300 268 400 255 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 80 Q120 80 120 60 Q120 40 140 40 Q145 25 165 30 Q180 18 200 30 Q220 18 235 30 Q255 25 260 40 Q280 40 280 60 Q280 80 260 80 Z"/>
  <rect class="fillable" fill="#ffffff" x="140" y="80" width="120" height="20"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="125" r="32"/>
  <circle fill="#1a1a1a" cx="190" cy="125" r="2.5"/>
  <circle fill="#1a1a1a" cx="210" cy="125" r="2.5"/>
  <path fill="none" d="M190 138 Q200 145 210 138"/>
  <path class="fillable" fill="#ffffff" d="M183 132 Q175 145 195 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M217 132 Q225 145 205 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M140 165 L260 165 L275 270 L125 270 Z"/>
  <line x1="200" y1="165" x2="200" y2="270"/>
  <g><circle class="fillable" fill="#ffffff" cx="175" cy="195" r="3"/><circle class="fillable" fill="#ffffff" cx="175" cy="215" r="3"/><circle class="fillable" fill="#ffffff" cx="175" cy="235" r="3"/><circle class="fillable" fill="#ffffff" cx="225" cy="195" r="3"/><circle class="fillable" fill="#ffffff" cx="225" cy="215" r="3"/><circle class="fillable" fill="#ffffff" cx="225" cy="235" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M125 220 L100 270 L130 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M275 220 L300 270 L270 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M260 165 L290 200 L310 195 L320 205 L295 230 L260 195 Z"/>
  <circle class="fillable" fill="#ffffff" cx="310" cy="200" r="12"/>
</g>
''')

add('doctor', '👩‍⚕️ 医生', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 260 Q100 252 200 260 Q300 268 400 255 L400 300 L0 300 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="42"/>
  <path class="fillable" fill="#ffffff" d="M158 100 Q165 65 200 60 Q235 65 242 100 L240 80 Q200 70 160 80 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 100 Q190 90 200 92 Q210 90 220 100 L218 92 Q200 86 182 92 Z"/>
  <circle fill="#1a1a1a" cx="188" cy="112" r="2.5"/>
  <circle fill="#1a1a1a" cx="212" cy="112" r="2.5"/>
  <rect class="fillable" fill="#ffffff" x="182" y="108" width="14" height="10" rx="2"/>
  <rect class="fillable" fill="#ffffff" x="204" y="108" width="14" height="10" rx="2"/>
  <line x1="196" y1="113" x2="204" y2="113"/>
  <path fill="none" d="M190 130 Q200 138 210 130"/>
  <path class="fillable" fill="#ffffff" d="M155 165 L245 165 L270 270 L130 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 165 L200 188 L230 165 L228 200 L172 200 Z"/>
  <path class="fillable" fill="#ffffff" d="M196 170 L204 170 L204 188 L196 188 Z"/>
  <path class="fillable" fill="#ffffff" d="M192 174 L208 174 L208 180 L192 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M130 270 L132 290 L155 290 Z"/>
  <path class="fillable" fill="#ffffff" d="M270 270 L268 290 L245 290 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 195 L130 220 L130 245 L150 240 L155 215 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="200" y1="180" x2="135" y2="230"/><circle class="fillable" fill="#ffffff" cx="130" cy="232" r="6"/></g>
  <rect class="fillable" fill="#ffffff" x="248" y="200" width="42" height="35" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="259" y="195" width="20" height="6"/>
  <line x1="269" y1="208" x2="269" y2="227"/>
  <line x1="259" y1="217" x2="279" y2="217"/>
</g>
''')

add('fireman', '👨‍🚒 消防员', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 260 Q100 252 200 260 Q300 268 400 255 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 95 Q158 65 200 60 Q242 65 242 95 L242 110 L158 110 Z"/>
  <rect class="fillable" fill="#ffffff" x="155" y="105" width="90" height="14"/>
  <path class="fillable" fill="#ffffff" d="M190 75 L210 75 L208 90 L192 90 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="135" r="22"/>
  <circle fill="#1a1a1a" cx="192" cy="133" r="2"/>
  <circle fill="#1a1a1a" cx="208" cy="133" r="2"/>
  <path fill="none" d="M193 145 Q200 150 207 145"/>
  <path class="fillable" fill="#ffffff" d="M150 162 L250 162 L268 270 L132 270 Z"/>
  <rect class="fillable" fill="#ffffff" x="135" y="195" width="130" height="14"/>
  <rect class="fillable" fill="#ffffff" x="135" y="235" width="130" height="14"/>
  <path class="fillable" fill="#ffffff" d="M132 270 L135 290 L165 290 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 270 L265 290 L235 290 Z"/>
  <rect class="fillable" fill="#ffffff" x="190" y="170" width="20" height="14"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="180" r="4"/>
  <path class="fillable" fill="#ffffff" d="M252 175 L290 165 Q310 165 315 175 L330 175 L330 195 L315 195 Q310 205 290 205 L280 205 L280 270 L252 270 Z"/>
  <line x1="290" y1="170" x2="290" y2="200"/>
  <line x1="300" y1="170" x2="300" y2="200"/>
  <path class="fillable" fill="#ffffff" d="M148 162 L120 195 L130 220 L150 215 L152 188 Z"/>
  <line x1="135" y1="180" x2="100" y2="160"/>
  <line x1="100" y1="160" x2="85" y2="170"/>
  <line x1="85" y1="170" x2="100" y2="180"/>
  <line x1="100" y1="180" x2="100" y2="160"/>
</g>
''')

add('astronaut', '👨‍🚀 宇航员', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><path class="fillable" fill="#ffffff" d="M40 50 L42 57 L50 57 L44 61 L46 69 L40 65 L34 69 L36 61 L30 57 L38 57 Z"/><path class="fillable" fill="#ffffff" d="M350 60 L352 67 L360 67 L354 71 L356 79 L350 75 L344 79 L346 71 L340 67 L348 67 Z"/><circle class="fillable" fill="#ffffff" cx="80" cy="200" r="3"/><circle class="fillable" fill="#ffffff" cx="320" cy="180" r="3"/><circle class="fillable" fill="#ffffff" cx="120" cy="80" r="2"/><circle class="fillable" fill="#ffffff" cx="280" cy="40" r="2"/></g>
  <circle class="fillable" fill="#ffffff" cx="200" cy="120" r="58"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="125" r="38"/>
  <circle fill="#1a1a1a" cx="190" cy="120" r="2"/>
  <circle fill="#1a1a1a" cx="210" cy="120" r="2"/>
  <path fill="none" d="M188 135 Q200 142 212 135"/>
  <path class="fillable" fill="#ffffff" d="M225 100 Q240 90 250 110 Q240 120 225 115 Z"/>
  <rect class="fillable" fill="#ffffff" x="150" y="172" width="100" height="100" rx="8"/>
  <rect class="fillable" fill="#ffffff" x="170" y="195" width="60" height="40" rx="3"/>
  <g stroke-width="1.5" fill="none"><line x1="180" y1="195" x2="180" y2="235"/><line x1="200" y1="195" x2="200" y2="235"/><line x1="220" y1="195" x2="220" y2="235"/></g>
  <circle class="fillable" fill="#ffffff" cx="180" cy="250" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="250" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="220" cy="250" r="4"/>
  <path class="fillable" fill="#ffffff" d="M150 180 L120 195 L120 240 L145 240 L150 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 180 L280 195 L280 240 L255 240 L250 230 Z"/>
  <rect class="fillable" fill="#ffffff" x="115" y="232" width="35" height="22" rx="4"/>
  <rect class="fillable" fill="#ffffff" x="250" y="232" width="35" height="22" rx="4"/>
  <path class="fillable" fill="#ffffff" d="M165 272 L165 285 L195 285 L195 272 Z"/>
  <path class="fillable" fill="#ffffff" d="M205 272 L205 285 L235 285 L235 272 Z"/>
</g>
''')

add('superhero', '🦸 超级英雄', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 270 Q100 262 200 270 Q300 278 400 263 L400 300 L0 300 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="100" r="32"/>
  <path class="fillable" fill="#ffffff" d="M170 88 L230 88 L235 102 L165 102 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="186" cy="98" rx="6" ry="4"/>
  <ellipse class="fillable" fill="#ffffff" cx="214" cy="98" rx="6" ry="4"/>
  <circle fill="#1a1a1a" cx="186" cy="98" r="2"/>
  <circle fill="#1a1a1a" cx="214" cy="98" r="2"/>
  <path fill="none" d="M188 118 Q200 125 212 118"/>
  <path class="fillable" fill="#ffffff" d="M150 138 L250 138 L268 240 L132 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M175 138 Q200 195 225 138 L228 165 Q200 220 172 165 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 165 L205 165 L210 185 L200 195 L190 185 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 138 L100 175 L100 240 L120 235 L150 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M250 138 L300 175 L300 240 L280 235 L250 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M132 240 L135 280 L165 280 L160 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 240 L265 280 L235 280 L240 240 Z"/>
  <rect class="fillable" fill="#ffffff" x="125" y="278" width="50" height="12" rx="3"/>
  <rect class="fillable" fill="#ffffff" x="225" y="278" width="50" height="12" rx="3"/>
  <path class="fillable" fill="#ffffff" d="M155 145 L80 235 L160 220 L130 280 L200 200 L270 280 L240 220 L320 235 L245 145 Z"/>
</g>
''')

add('painter', '🎨 画家', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 270 Q100 262 200 270 Q300 278 400 263 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 85 Q170 60 200 60 Q230 60 235 85 L235 95 L165 95 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="73" rx="14" ry="6"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="28"/>
  <circle fill="#1a1a1a" cx="192" cy="110" r="2"/>
  <circle fill="#1a1a1a" cx="208" cy="110" r="2"/>
  <path fill="none" d="M193 122 Q200 128 207 122"/>
  <path class="fillable" fill="#ffffff" d="M178 95 L188 90 L188 105 L178 105 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 145 L230 145 L242 250 L158 250 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="170" y1="180" x2="230" y2="180"/></g>
  <g><circle class="fillable" fill="#ffffff" cx="185" cy="165" r="3"/><circle class="fillable" fill="#ffffff" cx="200" cy="158" r="3"/><circle class="fillable" fill="#ffffff" cx="215" cy="165" r="3"/><circle class="fillable" fill="#ffffff" cx="190" cy="205" r="3"/><circle class="fillable" fill="#ffffff" cx="210" cy="205" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M158 250 L160 280 L185 280 Z"/>
  <path class="fillable" fill="#ffffff" d="M242 250 L240 280 L215 280 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 175 L110 215 L120 245 L150 220 L165 195 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="80" cy="220" rx="35" ry="22"/>
  <ellipse class="fillable" fill="#ffffff" cx="80" cy="220" rx="18" ry="12"/>
  <g><circle class="fillable" fill="#ffffff" cx="62" cy="218" r="4"/><circle class="fillable" fill="#ffffff" cx="80" cy="208" r="4"/><circle class="fillable" fill="#ffffff" cx="98" cy="218" r="4"/><circle class="fillable" fill="#ffffff" cx="68" cy="232" r="4"/><circle class="fillable" fill="#ffffff" cx="92" cy="232" r="4"/></g>
  <path class="fillable" fill="#ffffff" d="M242 175 L295 215 L290 230 L235 195 Z"/>
  <line x1="290" y1="225" x2="320" y2="245"/>
  <path class="fillable" fill="#ffffff" d="M318 240 L335 245 L335 255 L320 252 Z"/>
</g>
''')

add('ballerina', '🩰 芭蕾舞者', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 270 Q100 262 200 270 Q300 278 400 263 L400 300 L0 300 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="80" r="22"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="58" rx="14" ry="10"/>
  <line x1="200" y1="50" x2="200" y2="42"/>
  <path class="fillable" fill="#ffffff" d="M195 38 L205 38 L210 50 L190 50 Z"/>
  <circle fill="#1a1a1a" cx="194" cy="80" r="1.5"/>
  <circle fill="#1a1a1a" cx="206" cy="80" r="1.5"/>
  <path fill="none" d="M195 88 Q200 92 205 88"/>
  <path class="fillable" fill="#ffffff" d="M185 105 L215 105 L218 180 L182 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 175 Q200 165 245 175 Q255 200 240 215 Q200 220 160 215 Q145 200 155 175 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="170" y1="180" x2="165" y2="210"/><line x1="185" y1="178" x2="183" y2="215"/><line x1="200" y1="175" x2="200" y2="215"/><line x1="215" y1="178" x2="217" y2="215"/><line x1="230" y1="180" x2="235" y2="210"/></g>
  <path class="fillable" fill="#ffffff" d="M190 215 L195 270 L185 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M210 215 L205 270 L215 270 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="187" cy="280" rx="14" ry="6"/>
  <ellipse class="fillable" fill="#ffffff" cx="213" cy="280" rx="14" ry="6"/>
  <g stroke-width="1.5" fill="none"><path d="M180 285 Q188 290 195 285"/><path d="M205 285 Q213 290 220 285"/></g>
  <path class="fillable" fill="#ffffff" d="M185 115 Q140 140 100 110 Q120 145 175 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M215 115 Q260 140 300 110 Q280 145 225 145 Z"/>
</g>
''')

add('prince', '🤴 王子', 'people', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <path class="fillable" fill="#ffffff" d="M0 270 Q100 262 200 270 Q300 278 400 263 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 80 L168 50 L180 78 L195 45 L205 45 L220 78 L232 50 L242 80 Z"/>
  <circle class="fillable" fill="#ffffff" cx="170" cy="55" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="48" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="230" cy="55" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="110" r="32"/>
  <circle fill="#1a1a1a" cx="190" cy="108" r="2"/>
  <circle fill="#1a1a1a" cx="210" cy="108" r="2"/>
  <path fill="none" d="M192 122 Q200 128 208 122"/>
  <path fill="none" d="M180 95 Q190 92 198 95"/>
  <path fill="none" d="M220 95 Q210 92 202 95"/>
  <path class="fillable" fill="#ffffff" d="M170 142 L230 142 L240 175 L160 175 Z"/>
  <path class="fillable" fill="#ffffff" d="M160 175 L240 175 L255 250 L145 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M170 175 Q200 200 230 175 L228 195 Q200 215 172 195 Z"/>
  <path class="fillable" fill="#ffffff" d="M192 200 L208 200 L210 230 L190 230 Z"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="215" r="5"/>
  <path class="fillable" fill="#ffffff" d="M145 250 L150 280 L180 280 L175 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M255 250 L250 280 L220 280 L225 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 142 L295 180 L285 210 L235 175 Z"/>
  <rect class="fillable" fill="#ffffff" x="282" y="175" width="10" height="30"/>
  <path class="fillable" fill="#ffffff" d="M280 175 L295 175 L290 168 L285 168 Z"/>
  <path class="fillable" fill="#ffffff" d="M155 175 L130 230 L150 240 L165 200 Z"/>
</g>
''')

# --- Bug / Birds (10) ---
add('bird_perched', '🐦 小鸟', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M50 240 Q150 235 250 240 Q350 245 400 240"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="180" rx="60" ry="48"/>
  <circle class="fillable" fill="#ffffff" cx="265" cy="160" r="32"/>
  <path class="fillable" fill="#ffffff" d="M295 158 L320 155 L298 168 Z"/>
  <circle class="fillable" fill="#ffffff" cx="270" cy="155" r="6"/>
  <circle fill="#1a1a1a" cx="271" cy="156" r="3"/>
  <path class="fillable" fill="#ffffff" d="M155 165 Q120 150 110 170 Q130 185 170 180 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 195 Q130 195 110 215 Q135 220 175 210 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="135" y1="168" x2="125" y2="175"/><line x1="135" y1="200" x2="125" y2="208"/><line x1="160" y1="215" x2="155" y2="220"/></g>
  <path class="fillable" fill="#ffffff" d="M165 220 L155 245 L175 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M230 220 L240 245 L215 240 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="240" cy="200" r="3"/><circle class="fillable" fill="#ffffff" cx="225" cy="215" r="3"/><circle class="fillable" fill="#ffffff" cx="200" cy="215" r="3"/></g>
</g>
''')

add('bee_flower', '🐝 蜜蜂', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <g><path class="fillable" fill="#ffffff" d="M150 250 L150 200 L160 200 L160 250 Z"/><circle class="fillable" fill="#ffffff" cx="155" cy="180" r="15"/><circle class="fillable" fill="#ffffff" cx="155" cy="180" r="6"/><circle class="fillable" fill="#ffffff" cx="138" cy="170" r="10"/><circle class="fillable" fill="#ffffff" cx="172" cy="170" r="10"/><circle class="fillable" fill="#ffffff" cx="138" cy="190" r="10"/><circle class="fillable" fill="#ffffff" cx="172" cy="190" r="10"/></g>
  <g><path class="fillable" fill="#ffffff" d="M280 250 L280 200 L290 200 L290 250 Z"/><circle class="fillable" fill="#ffffff" cx="285" cy="180" r="15"/><circle class="fillable" fill="#ffffff" cx="285" cy="180" r="6"/><circle class="fillable" fill="#ffffff" cx="268" cy="170" r="10"/><circle class="fillable" fill="#ffffff" cx="302" cy="170" r="10"/><circle class="fillable" fill="#ffffff" cx="268" cy="190" r="10"/><circle class="fillable" fill="#ffffff" cx="302" cy="190" r="10"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="130" rx="50" ry="32"/>
  <rect class="fillable" fill="#ffffff" x="195" y="115" width="14" height="30"/>
  <rect class="fillable" fill="#ffffff" x="225" y="115" width="14" height="30"/>
  <rect class="fillable" fill="#ffffff" x="252" y="115" width="14" height="30"/>
  <circle class="fillable" fill="#ffffff" cx="178" cy="125" r="18"/>
  <circle fill="#1a1a1a" cx="175" cy="125" r="2.5"/>
  <circle fill="#1a1a1a" cx="183" cy="125" r="2.5"/>
  <path fill="none" d="M175 135 Q180 138 185 135"/>
  <line x1="170" y1="110" x2="160" y2="95"/>
  <line x1="183" y1="110" x2="190" y2="92"/>
  <path class="fillable" fill="#ffffff" d="M158 90 L162 92 L162 95 L158 93 Z"/>
  <path class="fillable" fill="#ffffff" d="M190 90 L194 88 L195 93 L191 95 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 100 Q175 80 165 100 Q180 115 205 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M240 100 Q265 80 275 100 Q260 115 235 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M268 138 L285 138 L282 148 L268 145 Z"/>
</g>
''')

add('dragonfly', '🪲 蜻蜓', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 232 200 240 Q300 248 400 235 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 260 Q100 252 200 260 Q300 268 400 255"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="180" rx="6" ry="65"/>
  <g stroke-width="1.5" fill="none"><line x1="194" y1="180" x2="194" y2="240"/><line x1="206" y1="180" x2="206" y2="240"/><line x1="194" y1="195" x2="206" y2="195"/><line x1="194" y1="210" x2="206" y2="210"/><line x1="194" y1="225" x2="206" y2="225"/></g>
  <circle class="fillable" fill="#ffffff" cx="200" cy="120" r="18"/>
  <circle class="fillable" fill="#ffffff" cx="188" cy="118" r="6"/>
  <circle class="fillable" fill="#ffffff" cx="212" cy="118" r="6"/>
  <circle fill="#1a1a1a" cx="188" cy="120" r="3"/>
  <circle fill="#1a1a1a" cx="212" cy="120" r="3"/>
  <path class="fillable" fill="#ffffff" d="M200 102 L196 92 L200 95 L204 92 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="135" cy="150" rx="50" ry="14" transform="rotate(-15 135 150)"/>
  <ellipse class="fillable" fill="#ffffff" cx="265" cy="150" rx="50" ry="14" transform="rotate(15 265 150)"/>
  <ellipse class="fillable" fill="#ffffff" cx="135" cy="180" rx="48" ry="12" transform="rotate(10 135 180)"/>
  <ellipse class="fillable" fill="#ffffff" cx="265" cy="180" rx="48" ry="12" transform="rotate(-10 265 180)"/>
  <g stroke-width="1.5" fill="none"><line x1="100" y1="148" x2="170" y2="148"/><line x1="230" y1="148" x2="300" y2="148"/><line x1="100" y1="178" x2="170" y2="178"/><line x1="230" y1="178" x2="300" y2="178"/></g>
</g>
''')

add('ladybug_leaf', '🐞 瓢虫', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 230 Q100 220 200 230 Q300 240 400 225 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M60 220 Q60 100 200 100 Q330 100 330 220 Q200 250 60 220 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M70 170 Q200 170 320 170"/><path d="M80 130 Q200 145 318 135"/><path d="M80 200 Q200 215 320 205"/></g>
  <line x1="100" y1="105" x2="60" y2="90"/>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="190" rx="60" ry="46"/>
  <line x1="220" y1="144" x2="220" y2="236"/>
  <g><circle class="fillable" fill="#ffffff" cx="190" cy="170" r="6"/><circle class="fillable" fill="#ffffff" cx="195" cy="195" r="6"/><circle class="fillable" fill="#ffffff" cx="185" cy="215" r="6"/><circle class="fillable" fill="#ffffff" cx="250" cy="170" r="6"/><circle class="fillable" fill="#ffffff" cx="255" cy="195" r="6"/><circle class="fillable" fill="#ffffff" cx="248" cy="215" r="6"/></g>
  <path class="fillable" fill="#ffffff" d="M160 165 Q220 150 280 165 L280 175 Q220 165 160 178 Z"/>
  <circle class="fillable" fill="#ffffff" cx="183" cy="160" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="195" cy="155" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="245" cy="155" r="4"/>
  <circle class="fillable" fill="#ffffff" cx="257" cy="160" r="4"/>
  <g stroke-width="1.5" fill="none"><line x1="170" y1="200" x2="155" y2="210"/><line x1="170" y1="215" x2="155" y2="225"/><line x1="270" y1="200" x2="285" y2="210"/><line x1="270" y1="215" x2="285" y2="225"/></g>
</g>
''')

add('snail', '🐌 蜗牛', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 268 Q100 260 200 268 Q300 276 400 263"/></g>
  <path class="fillable" fill="#ffffff" d="M60 240 Q60 215 180 215 L220 215 Q235 215 240 230 Q245 245 220 250 Q160 252 60 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M218 215 Q218 180 245 175"/>
  <line x1="218" y1="215" x2="252" y2="195"/>
  <line x1="252" y1="195" x2="254" y2="184"/>
  <circle class="fillable" fill="#ffffff" cx="254" cy="178" r="6"/>
  <circle fill="#1a1a1a" cx="255" cy="179" r="2.5"/>
  <line x1="230" y1="195" x2="225" y2="180"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="174" r="6"/>
  <circle fill="#1a1a1a" cx="226" cy="175" r="2.5"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="200" r="60"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="200" r="48"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="200" r="36"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="200" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="200" r="10"/>
  <path class="fillable" fill="#ffffff" d="M245 232 L255 232 L255 240 L245 240 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="285" cy="260" r="2.5"/><circle class="fillable" fill="#ffffff" cx="305" cy="262" r="2.5"/><circle class="fillable" fill="#ffffff" cx="325" cy="260" r="2.5"/></g>
</g>
''')

add('frog', '🐸 青蛙', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 270 Q100 262 200 270 Q300 278 400 263"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="240" rx="120" ry="22"/>
  <path class="fillable" fill="#ffffff" d="M80 240 L130 240 L130 235 L80 235 Z"/>
  <ellipse class="fillable" fill="#ffffff" cx="200" cy="175" rx="80" ry="60"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="125" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="125" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="160" cy="128" r="12"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="128" r="12"/>
  <circle fill="#1a1a1a" cx="160" cy="130" r="6"/>
  <circle fill="#1a1a1a" cx="240" cy="130" r="6"/>
  <circle fill="#ffffff" cx="158" cy="128" r="2"/>
  <circle fill="#ffffff" cx="238" cy="128" r="2"/>
  <path fill="none" d="M160 195 Q200 220 240 195"/>
  <circle class="fillable" fill="#ffffff" cx="175" cy="178" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="178" r="3"/>
  <path class="fillable" fill="#ffffff" d="M125 215 Q105 235 95 250 L120 255 L140 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M275 215 Q295 235 305 250 L280 255 L260 240 Z"/>
  <g><circle class="fillable" fill="#ffffff" cx="100" cy="255" r="4"/><circle class="fillable" fill="#ffffff" cx="110" cy="262" r="4"/><circle class="fillable" fill="#ffffff" cx="105" cy="270" r="4"/><circle class="fillable" fill="#ffffff" cx="295" cy="255" r="4"/><circle class="fillable" fill="#ffffff" cx="305" cy="262" r="4"/></g>
  <g><circle class="fillable" fill="#ffffff" cx="175" cy="165" r="2"/><circle class="fillable" fill="#ffffff" cx="195" cy="155" r="2"/><circle class="fillable" fill="#ffffff" cx="225" cy="160" r="2"/></g>
</g>
''')

add('spider_web', '🕷️ 蜘蛛网', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <line x1="20" y1="20" x2="380" y2="20"/>
  <line x1="20" y1="20" x2="20" y2="280"/>
  <line x1="380" y1="20" x2="380" y2="280"/>
  <g stroke-width="1.5" fill="none">
    <line x1="200" y1="150" x2="50" y2="20"/>
    <line x1="200" y1="150" x2="200" y2="20"/>
    <line x1="200" y1="150" x2="350" y2="20"/>
    <line x1="200" y1="150" x2="80" y2="50"/>
    <line x1="200" y1="150" x2="320" y2="50"/>
    <line x1="200" y1="150" x2="60" y2="160"/>
    <line x1="200" y1="150" x2="340" y2="160"/>
    <line x1="200" y1="150" x2="80" y2="260"/>
    <line x1="200" y1="150" x2="320" y2="260"/>
    <line x1="200" y1="150" x2="200" y2="280"/>
    <path d="M120 95 Q200 105 280 95"/>
    <path d="M100 140 Q200 145 300 140"/>
    <path d="M105 185 Q200 195 295 185"/>
    <path d="M130 230 Q200 235 270 230"/>
    <path d="M165 70 Q200 75 235 70"/>
  </g>
  <circle class="fillable" fill="#ffffff" cx="200" cy="160" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="140" r="14"/>
  <circle class="fillable" fill="#ffffff" cx="195" cy="135" r="2"/>
  <circle class="fillable" fill="#ffffff" cx="205" cy="135" r="2"/>
  <circle class="fillable" fill="#ffffff" cx="190" cy="140" r="2"/>
  <circle class="fillable" fill="#ffffff" cx="210" cy="140" r="2"/>
  <g stroke-width="2"><line x1="183" y1="145" x2="160" y2="125"/><line x1="180" y1="155" x2="150" y2="155"/><line x1="183" y1="170" x2="160" y2="185"/><line x1="190" y1="180" x2="175" y2="205"/><line x1="217" y1="145" x2="240" y2="125"/><line x1="220" y1="155" x2="250" y2="155"/><line x1="217" y1="170" x2="240" y2="185"/><line x1="210" y1="180" x2="225" y2="205"/></g>
</g>
''')

add('hummingbird', '🐦 蜂鸟', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <ellipse class="fillable" fill="#ffffff" cx="180" cy="160" rx="44" ry="24"/>
  <circle class="fillable" fill="#ffffff" cx="140" cy="148" r="18"/>
  <path class="fillable" fill="#ffffff" d="M122 145 L75 130 L122 152 Z"/>
  <circle fill="#1a1a1a" cx="138" cy="145" r="2"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="125" rx="30" ry="14" transform="rotate(-25 195 125)"/>
  <ellipse class="fillable" fill="#ffffff" cx="195" cy="195" rx="30" ry="14" transform="rotate(25 195 195)"/>
  <g stroke-width="1.5" fill="none"><line x1="175" y1="115" x2="215" y2="135"/><line x1="175" y1="205" x2="215" y2="185"/></g>
  <path class="fillable" fill="#ffffff" d="M218 165 L260 175 L218 185 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="225" y1="170" x2="255" y2="175"/><line x1="225" y1="180" x2="255" y2="175"/></g>
  <line x1="170" y1="178" x2="168" y2="195"/>
  <line x1="180" y1="178" x2="178" y2="195"/>
  <line x1="190" y1="178" x2="188" y2="195"/>
  <g><circle class="fillable" fill="#ffffff" cx="295" cy="200" r="22"/><line x1="295" y1="222" x2="295" y2="270"/><path class="fillable" fill="#ffffff" d="M295 270 Q280 280 290 285 L300 285 Q310 280 295 270 Z"/><g><circle class="fillable" fill="#ffffff" cx="280" cy="190" r="6"/><circle class="fillable" fill="#ffffff" cx="295" cy="180" r="6"/><circle class="fillable" fill="#ffffff" cx="310" cy="190" r="6"/><circle class="fillable" fill="#ffffff" cx="280" cy="210" r="6"/><circle class="fillable" fill="#ffffff" cx="310" cy="210" r="6"/><circle fill="#1a1a1a" cx="295" cy="200" r="3"/></g></g>
</g>
''')

add('caterpillar', '🐛 毛毛虫', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 220 Q40 215 80 220 Q120 225 160 220 Q200 215 240 220 Q280 225 320 220 Q360 215 400 220 L400 300 L0 300 Z"/>
  <circle class="fillable" fill="#ffffff" cx="60" cy="195" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="100" cy="195" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="140" cy="195" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="195" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="220" cy="195" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="260" cy="195" r="22"/>
  <circle class="fillable" fill="#ffffff" cx="305" cy="180" r="28"/>
  <g><circle class="fillable" fill="#ffffff" cx="298" cy="175" r="5"/><circle class="fillable" fill="#ffffff" cx="316" cy="175" r="5"/><circle fill="#1a1a1a" cx="298" cy="177" r="2.5"/><circle fill="#1a1a1a" cx="316" cy="177" r="2.5"/></g>
  <path fill="none" d="M298 190 Q307 198 316 190"/>
  <path class="fillable" fill="#ffffff" d="M302 190 L308 190 L305 194 Z"/>
  <line x1="298" y1="155" x2="290" y2="140"/>
  <line x1="316" y1="155" x2="324" y2="140"/>
  <circle class="fillable" fill="#ffffff" cx="290" cy="138" r="3"/>
  <circle class="fillable" fill="#ffffff" cx="324" cy="138" r="3"/>
  <g><circle class="fillable" fill="#ffffff" cx="80" cy="170" r="4"/><circle class="fillable" fill="#ffffff" cx="120" cy="170" r="4"/><circle class="fillable" fill="#ffffff" cx="160" cy="170" r="4"/><circle class="fillable" fill="#ffffff" cx="200" cy="170" r="4"/><circle class="fillable" fill="#ffffff" cx="240" cy="170" r="4"/></g>
  <g stroke-width="2"><line x1="60" y1="217" x2="60" y2="225"/><line x1="100" y1="217" x2="100" y2="225"/><line x1="140" y1="217" x2="140" y2="225"/><line x1="180" y1="217" x2="180" y2="225"/><line x1="220" y1="217" x2="220" y2="225"/><line x1="260" y1="217" x2="260" y2="225"/></g>
  <path class="fillable" fill="#ffffff" d="M40 218 L25 250 Q30 260 50 245 Z"/>
</g>
''')

add('parrot', '🦜 鹦鹉', 'bug', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <line x1="80" y1="250" x2="320" y2="250"/>
  <g stroke-width="2" fill="none"><line x1="100" y1="248" x2="105" y2="260"/><line x1="160" y1="248" x2="165" y2="260"/><line x1="220" y1="248" x2="225" y2="260"/><line x1="280" y1="248" x2="285" y2="260"/></g>
  <ellipse class="fillable" fill="#ffffff" cx="220" cy="170" rx="68" ry="58"/>
  <path class="fillable" fill="#ffffff" d="M152 180 Q120 180 110 200 Q120 210 145 205 Z"/>
  <path class="fillable" fill="#ffffff" d="M158 195 Q130 200 120 220 Q140 222 162 213 Z"/>
  <path class="fillable" fill="#ffffff" d="M162 210 Q140 215 132 230 Q148 230 168 222 Z"/>
  <circle class="fillable" fill="#ffffff" cx="265" cy="135" r="36"/>
  <path class="fillable" fill="#ffffff" d="M295 130 Q320 130 320 145 Q310 165 285 158 Z"/>
  <path class="fillable" fill="#ffffff" d="M295 145 Q315 155 310 170 Q295 168 285 158 Z"/>
  <circle class="fillable" fill="#ffffff" cx="265" cy="130" r="6"/>
  <circle fill="#1a1a1a" cx="266" cy="131" r="3"/>
  <path class="fillable" fill="#ffffff" d="M240 145 Q235 152 245 155 Q255 153 250 145 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 200 L200 215 L200 230 L180 215 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 215 L220 230 L220 245 L200 230 Z"/>
  <path class="fillable" fill="#ffffff" d="M220 230 L240 245 L240 250 L220 245 Z"/>
  <line x1="210" y1="225" x2="200" y2="248"/>
  <line x1="218" y1="232" x2="208" y2="248"/>
  <line x1="226" y1="240" x2="216" y2="250"/>
  <g><line x1="270" y1="225" x2="270" y2="248"/><line x1="270" y1="248" x2="265" y2="252"/><line x1="270" y1="248" x2="275" y2="252"/></g>
</g>
''')

# --- Buildings (10) ---
add('village_house', '🏠 小村屋', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 232 200 240 Q300 248 400 235 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="120" y="160" width="200" height="100"/>
  <path class="fillable" fill="#ffffff" d="M100 160 L220 80 L340 160 Z"/>
  <rect class="fillable" fill="#ffffff" x="260" y="100" width="22" height="30"/>
  <g><circle class="fillable" fill="#ffffff" cx="268" cy="90" r="5"/><circle class="fillable" fill="#ffffff" cx="275" cy="78" r="4"/><circle class="fillable" fill="#ffffff" cx="282" cy="68" r="3"/></g>
  <rect class="fillable" fill="#ffffff" x="200" y="200" width="50" height="60"/>
  <circle class="fillable" fill="#ffffff" cx="240" cy="232" r="3"/>
  <rect class="fillable" fill="#ffffff" x="135" y="180" width="38" height="38"/>
  <line x1="154" y1="180" x2="154" y2="218"/>
  <line x1="135" y1="199" x2="173" y2="199"/>
  <rect class="fillable" fill="#ffffff" x="275" y="180" width="38" height="38"/>
  <line x1="294" y1="180" x2="294" y2="218"/>
  <line x1="275" y1="199" x2="313" y2="199"/>
  <g stroke-width="1.5" fill="none"><line x1="120" y1="190" x2="200" y2="190"/><line x1="120" y1="230" x2="200" y2="230"/><line x1="250" y1="230" x2="320" y2="230"/><line x1="140" y1="180" x2="140" y2="190"/><line x1="180" y1="190" x2="180" y2="200"/></g>
  <path class="fillable" fill="#ffffff" d="M40 240 Q60 230 80 240 L80 270 L40 270 Z"/>
  <path class="fillable" fill="#ffffff" d="M30 250 Q60 220 90 250"/>
  <path class="fillable" fill="#ffffff" d="M340 230 L360 215 L360 245 L340 250 Z"/>
  <rect class="fillable" fill="#ffffff" x="349" y="226" width="4" height="20"/>
</g>
''')

add('school', '🏫 学校', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="60" y="160" width="280" height="110"/>
  <path class="fillable" fill="#ffffff" d="M50 160 L200 90 L350 160 Z"/>
  <rect class="fillable" fill="#ffffff" x="185" y="60" width="10" height="42"/>
  <rect class="fillable" fill="#ffffff" x="170" y="55" width="60" height="14" rx="3"/>
  <line x1="200" y1="60" x2="200" y2="90"/>
  <rect class="fillable" fill="#ffffff" x="178" y="120" width="44" height="40" rx="3"/>
  <g><line x1="200" y1="125" x2="200" y2="155"/><line x1="183" y1="135" x2="217" y2="135"/><circle fill="#1a1a1a" cx="190" cy="138" r="1"/></g>
  <rect class="fillable" fill="#ffffff" x="180" y="200" width="40" height="70"/>
  <circle class="fillable" fill="#ffffff" cx="210" cy="235" r="3"/>
  <rect class="fillable" fill="#ffffff" x="80" y="180" width="32" height="40"/>
  <line x1="96" y1="180" x2="96" y2="220"/>
  <line x1="80" y1="200" x2="112" y2="200"/>
  <rect class="fillable" fill="#ffffff" x="120" y="180" width="32" height="40"/>
  <line x1="136" y1="180" x2="136" y2="220"/>
  <line x1="120" y1="200" x2="152" y2="200"/>
  <rect class="fillable" fill="#ffffff" x="248" y="180" width="32" height="40"/>
  <line x1="264" y1="180" x2="264" y2="220"/>
  <line x1="248" y1="200" x2="280" y2="200"/>
  <rect class="fillable" fill="#ffffff" x="288" y="180" width="32" height="40"/>
  <line x1="304" y1="180" x2="304" y2="220"/>
  <line x1="288" y1="200" x2="320" y2="200"/>
  <rect class="fillable" fill="#ffffff" x="80" y="232" width="32" height="32"/>
  <rect class="fillable" fill="#ffffff" x="120" y="232" width="32" height="32"/>
  <rect class="fillable" fill="#ffffff" x="248" y="232" width="32" height="32"/>
  <rect class="fillable" fill="#ffffff" x="288" y="232" width="32" height="32"/>
  <rect class="fillable" fill="#ffffff" x="358" y="220" width="6" height="50"/>
  <path class="fillable" fill="#ffffff" d="M364 220 L398 225 L398 245 L364 240 Z"/>
</g>
''')

add('lighthouse', '🗼 灯塔', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 230 Q40 225 80 230 Q120 235 160 230 Q200 225 240 230 Q280 235 320 230 Q360 225 400 230 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M0 250 Q40 245 80 250 Q120 255 160 250 Q200 245 240 250 Q280 255 320 250 Q360 245 400 250"/><path d="M0 275 Q40 270 80 275 Q120 280 160 275 Q200 270 240 275 Q280 280 320 275 Q360 270 400 275"/></g>
  <path class="fillable" fill="#ffffff" d="M170 235 L155 250 L245 250 L230 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M175 235 L185 80 L215 80 L225 235 Z"/>
  <rect class="fillable" fill="#ffffff" x="178" y="180" width="44" height="22"/>
  <rect class="fillable" fill="#ffffff" x="180" y="130" width="40" height="22"/>
  <rect class="fillable" fill="#ffffff" x="180" y="100" width="40" height="22"/>
  <rect class="fillable" fill="#ffffff" x="195" y="200" width="10" height="35"/>
  <path class="fillable" fill="#ffffff" d="M175 80 L225 80 L235 65 L165 65 Z"/>
  <rect class="fillable" fill="#ffffff" x="180" y="40" width="40" height="25"/>
  <path class="fillable" fill="#ffffff" d="M180 40 L220 40 L210 20 L190 20 Z"/>
  <line x1="200" y1="20" x2="200" y2="10"/>
  <path class="fillable" fill="#ffffff" d="M195 10 L215 5 L210 18 Z"/>
  <g stroke-width="2" stroke-dasharray="6 4" fill="none" stroke="#aaa"><line x1="220" y1="55" x2="320" y2="20"/><line x1="220" y1="55" x2="320" y2="50"/><line x1="220" y1="55" x2="320" y2="80"/></g>
  <path class="fillable" fill="#ffffff" d="M100 235 L120 225 L135 235 Z"/>
  <path class="fillable" fill="#ffffff" d="M260 235 L280 225 L300 235 Z"/>
</g>
''')

add('barn', '🏚️ 谷仓', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 240 Q100 232 200 240 Q300 248 400 235 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 240 L120 160 L150 130 L250 130 L280 160 L280 240 Z"/>
  <path class="fillable" fill="#ffffff" d="M150 130 L150 110 L250 110 L250 130 Z"/>
  <rect class="fillable" fill="#ffffff" x="170" y="180" width="60" height="60"/>
  <line x1="200" y1="180" x2="200" y2="240"/>
  <path d="M170 180 L230 240" stroke-width="2"/>
  <path d="M230 180 L170 240" stroke-width="2"/>
  <rect class="fillable" fill="#ffffff" x="135" y="148" width="20" height="20"/>
  <line x1="145" y1="148" x2="145" y2="168"/>
  <line x1="135" y1="158" x2="155" y2="158"/>
  <rect class="fillable" fill="#ffffff" x="245" y="148" width="20" height="20"/>
  <line x1="255" y1="148" x2="255" y2="168"/>
  <line x1="245" y1="158" x2="265" y2="158"/>
  <rect class="fillable" fill="#ffffff" x="320" y="190" width="40" height="50"/>
  <path class="fillable" fill="#ffffff" d="M320 190 Q340 175 360 190 Z"/>
  <line x1="320" y1="210" x2="360" y2="210"/>
  <path class="fillable" fill="#ffffff" d="M40 240 L70 215 L100 240 Z"/>
  <g stroke-width="1.5" fill="none"><line x1="50" y1="232" x2="90" y2="232"/><line x1="55" y1="223" x2="85" y2="223"/></g>
</g>
''')

add('igloo', '🛖 冰屋', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><g transform="translate(60 60)" fill="none"><line x1="0" y1="-6" x2="0" y2="6"/><line x1="-6" y1="0" x2="6" y2="0"/><line x1="-4" y1="-4" x2="4" y2="4"/><line x1="-4" y1="4" x2="4" y2="-4"/></g><g transform="translate(330 80)" fill="none"><line x1="0" y1="-6" x2="0" y2="6"/><line x1="-6" y1="0" x2="6" y2="0"/></g><g transform="translate(150 50)" fill="none"><line x1="0" y1="-5" x2="0" y2="5"/><line x1="-5" y1="0" x2="5" y2="0"/></g></g>
  <circle class="fillable" fill="#ffffff" cx="290" cy="80" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M100 250 Q100 130 200 130 Q300 130 300 250 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M100 175 Q200 170 300 175"/><path d="M105 200 Q200 195 295 200"/><path d="M115 225 Q200 220 285 225"/></g>
  <line x1="125" y1="175" x2="120" y2="200"/>
  <line x1="160" y1="170" x2="155" y2="200"/>
  <line x1="200" y1="170" x2="200" y2="200"/>
  <line x1="240" y1="170" x2="245" y2="200"/>
  <line x1="275" y1="175" x2="280" y2="200"/>
  <line x1="140" y1="200" x2="138" y2="225"/>
  <line x1="180" y1="200" x2="180" y2="225"/>
  <line x1="220" y1="200" x2="220" y2="225"/>
  <line x1="260" y1="200" x2="262" y2="225"/>
  <line x1="135" y1="225" x2="135" y2="250"/>
  <line x1="265" y1="225" x2="265" y2="250"/>
  <line x1="190" y1="225" x2="190" y2="250"/>
  <line x1="210" y1="225" x2="210" y2="250"/>
  <path class="fillable" fill="#ffffff" d="M170 250 L170 215 Q170 200 200 200 Q230 200 230 215 L230 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M165 248 Q200 240 235 248 L240 256 Q200 262 160 256 Z"/>
</g>
''')

add('treehouse', '🌳 树屋', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 280 Q100 270 200 280 Q300 290 400 275 L400 300 L0 300 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 280 L175 130 L225 130 L220 280 Z"/>
  <g stroke-width="1.5" fill="none"><path d="M195 270 Q197 220 195 170 Q197 145 195 130"/><path d="M205 270 Q207 220 205 170 Q207 145 205 130"/></g>
  <line x1="180" y1="200" x2="135" y2="170"/>
  <line x1="220" y1="200" x2="265" y2="170"/>
  <line x1="180" y1="220" x2="145" y2="210"/>
  <line x1="220" y1="220" x2="255" y2="210"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="100" r="74"/>
  <circle class="fillable" fill="#ffffff" cx="135" cy="120" r="38"/>
  <circle class="fillable" fill="#ffffff" cx="265" cy="120" r="38"/>
  <circle class="fillable" fill="#ffffff" cx="180" cy="70" r="32"/>
  <circle class="fillable" fill="#ffffff" cx="225" cy="70" r="32"/>
  <rect class="fillable" fill="#ffffff" x="160" y="180" width="80" height="60"/>
  <path class="fillable" fill="#ffffff" d="M150 180 L200 145 L250 180 Z"/>
  <rect class="fillable" fill="#ffffff" x="190" y="210" width="20" height="30"/>
  <rect class="fillable" fill="#ffffff" x="168" y="195" width="14" height="14"/>
  <rect class="fillable" fill="#ffffff" x="218" y="195" width="14" height="14"/>
  <g stroke-width="1.5" fill="none"><line x1="240" y1="240" x2="278" y2="280"/><line x1="248" y1="232" x2="286" y2="272"/><line x1="240" y1="244" x2="278" y2="284"/><line x1="248" y1="248" x2="286" y2="288"/><line x1="256" y1="252" x2="294" y2="292"/></g>
  <line x1="160" y1="240" x2="125" y2="280"/>
  <path class="fillable" fill="#ffffff" d="M115 275 Q105 270 110 282 Q120 285 122 278 Z"/>
</g>
''')

add('skyscraper', '🏢 高楼', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <g stroke-width="1.5"><circle class="fillable" fill="#ffffff" cx="50" cy="40" r="3"/><circle class="fillable" fill="#ffffff" cx="80" cy="50" r="2"/><circle class="fillable" fill="#ffffff" cx="330" cy="40" r="3"/></g>
  <path class="fillable" fill="#ffffff" d="M0 270 Q100 262 200 270 Q300 278 400 263 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="140" y="60" width="120" height="210"/>
  <line x1="200" y1="50" x2="200" y2="60"/>
  <path class="fillable" fill="#ffffff" d="M195 50 L205 50 L208 35 L192 35 Z"/>
  <g><rect class="fillable" fill="#ffffff" x="150" y="75" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="180" y="75" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="210" y="75" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="238" y="75" width="14" height="20"/><rect class="fillable" fill="#ffffff" x="150" y="105" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="180" y="105" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="210" y="105" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="238" y="105" width="14" height="20"/><rect class="fillable" fill="#ffffff" x="150" y="135" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="180" y="135" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="210" y="135" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="238" y="135" width="14" height="20"/><rect class="fillable" fill="#ffffff" x="150" y="165" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="180" y="165" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="210" y="165" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="238" y="165" width="14" height="20"/><rect class="fillable" fill="#ffffff" x="150" y="195" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="180" y="195" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="210" y="195" width="22" height="20"/><rect class="fillable" fill="#ffffff" x="238" y="195" width="14" height="20"/></g>
  <rect class="fillable" fill="#ffffff" x="186" y="232" width="28" height="38"/>
  <circle class="fillable" fill="#ffffff" cx="208" cy="251" r="2"/>
  <rect class="fillable" fill="#ffffff" x="50" y="200" width="60" height="70"/>
  <g><rect class="fillable" fill="#ffffff" x="58" y="210" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="78" y="210" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="58" y="230" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="78" y="230" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="58" y="250" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="78" y="250" width="14" height="14"/></g>
  <rect class="fillable" fill="#ffffff" x="290" y="170" width="70" height="100"/>
  <g><rect class="fillable" fill="#ffffff" x="298" y="180" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="318" y="180" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="338" y="180" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="298" y="200" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="318" y="200" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="338" y="200" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="298" y="220" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="318" y="220" width="14" height="14"/><rect class="fillable" fill="#ffffff" x="338" y="220" width="14" height="14"/></g>
</g>
''')

add('windmill', '🏭 风车', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <g stroke-width="2" fill="none"><path d="M30 280 L40 265"/><path d="M340 280 L350 265"/></g>
  <path class="fillable" fill="#ffffff" d="M170 250 L185 90 L215 90 L230 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M180 110 L220 110 L222 130 L178 130 Z"/>
  <rect class="fillable" fill="#ffffff" x="190" y="210" width="20" height="40"/>
  <rect class="fillable" fill="#ffffff" x="185" y="170" width="30" height="22"/>
  <line x1="200" y1="170" x2="200" y2="192"/>
  <line x1="185" y1="181" x2="215" y2="181"/>
  <circle class="fillable" fill="#ffffff" cx="200" cy="90" r="10"/>
  <path class="fillable" fill="#ffffff" d="M200 90 L198 25 L208 25 L210 90 Z"/>
  <path class="fillable" fill="#ffffff" d="M205 25 L260 35 L260 45 L208 35 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 90 L255 92 L255 100 L200 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M205 100 L255 145 L250 155 L208 110 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 100 L145 155 L138 145 L195 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 90 L145 92 L145 100 L200 100 Z"/>
  <path class="fillable" fill="#ffffff" d="M195 90 L140 35 L140 45 L192 90 Z"/>
</g>
''')

add('church', '⛪ 教堂', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 260 Q100 252 200 260 Q300 268 400 255 L400 300 L0 300 Z"/>
  <rect class="fillable" fill="#ffffff" x="130" y="180" width="180" height="90"/>
  <path class="fillable" fill="#ffffff" d="M115 180 L220 130 L325 180 Z"/>
  <rect class="fillable" fill="#ffffff" x="190" y="110" width="40" height="55"/>
  <path class="fillable" fill="#ffffff" d="M190 110 L210 75 L230 110 Z"/>
  <rect class="fillable" fill="#ffffff" x="208" y="55" width="4" height="20"/>
  <rect class="fillable" fill="#ffffff" x="202" y="62" width="16" height="4"/>
  <path class="fillable" fill="#ffffff" d="M195 130 L195 145 Q205 138 215 145 L225 145 L225 130 Z"/>
  <path class="fillable" fill="#ffffff" d="M200 195 L200 250 Q200 265 220 265 Q240 265 240 250 L240 195 Q240 180 220 180 Q200 180 200 195 Z"/>
  <line x1="220" y1="195" x2="220" y2="265"/>
  <line x1="200" y1="225" x2="240" y2="225"/>
  <path class="fillable" fill="#ffffff" d="M150 200 Q150 190 165 190 Q180 190 180 200 L180 230 L150 230 Z"/>
  <line x1="165" y1="190" x2="165" y2="230"/>
  <line x1="150" y1="210" x2="180" y2="210"/>
  <path class="fillable" fill="#ffffff" d="M260 200 Q260 190 275 190 Q290 190 290 200 L290 230 L260 230 Z"/>
  <line x1="275" y1="190" x2="275" y2="230"/>
  <line x1="260" y1="210" x2="290" y2="210"/>
</g>
''')

add('hut', '🛖 茅草屋', 'building', '''
<g stroke="#1a1a1a" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
  <circle class="fillable" fill="#ffffff" cx="55" cy="55" r="20"/>
  <path class="fillable" fill="#ffffff" d="M0 250 Q100 240 200 250 Q300 260 400 245 L400 300 L0 300 Z"/>
  <g><rect class="fillable" fill="#ffffff" x="40" y="245" width="6" height="18"/><circle class="fillable" fill="#ffffff" cx="43" cy="238" r="14"/><rect class="fillable" fill="#ffffff" x="358" y="245" width="6" height="18"/><circle class="fillable" fill="#ffffff" cx="361" cy="238" r="14"/></g>
  <path class="fillable" fill="#ffffff" d="M120 180 L280 180 L290 250 L110 250 Z"/>
  <path class="fillable" fill="#ffffff" d="M120 180 L200 60 L280 180 Z"/>
  <g stroke-width="1.5" fill="none">
    <path d="M125 180 L135 175"/><path d="M145 180 L155 175"/><path d="M165 180 L175 175"/><path d="M185 180 L195 175"/><path d="M205 180 L215 175"/><path d="M225 180 L235 175"/><path d="M245 180 L255 175"/><path d="M265 180 L275 175"/>
    <path d="M140 160 L150 156"/><path d="M170 158 L180 154"/><path d="M200 158 L210 154"/><path d="M230 158 L240 154"/><path d="M260 160 L268 156"/>
    <path d="M155 130 L165 126"/><path d="M195 126 L205 122"/><path d="M235 130 L245 126"/>
    <path d="M175 100 L185 96"/><path d="M215 100 L225 96"/>
  </g>
  <path class="fillable" fill="#ffffff" d="M180 250 L180 215 Q180 200 200 200 Q220 200 220 215 L220 250 Z"/>
  <rect class="fillable" fill="#ffffff" x="135" y="205" width="22" height="22"/>
  <line x1="146" y1="205" x2="146" y2="227"/>
  <line x1="135" y1="216" x2="157" y2="216"/>
  <rect class="fillable" fill="#ffffff" x="243" y="205" width="22" height="22"/>
  <line x1="254" y1="205" x2="254" y2="227"/>
  <line x1="243" y1="216" x2="265" y2="216"/>
</g>
''')

# Sanity: make sure we have 100
assert len(TEMPLATES) == 100, f'expected 100 templates, got {len(TEMPLATES)}'
