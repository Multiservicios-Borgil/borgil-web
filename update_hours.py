import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Hours pattern
# Match "Lunes a Viernes: ... </p>" and "Sábados: ... </p>"
pattern_mon_fri = re.compile(r'Lunes a Viernes:.*?</p>', re.IGNORECASE | re.DOTALL)
pattern_sat = re.compile(r'Sábados:.*?</p>', re.IGNORECASE | re.DOTALL)

new_mon_fri = 'Lunes a Viernes: 10:15 - 13:15 | 17:00 - 20:00</p>'
new_sat = 'Sábados: 10:15 - 13:15</p>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = pattern_mon_fri.sub(new_mon_fri, content)
    content = pattern_sat.sub(new_sat, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Horarios actualizados en toda la web.")
