import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll insert a center div before the phones div
# The header structure is: <div class="..."> <div class="left"> </div> <div class="right"> </div> </div>

# Search for the end of the first div block (email) and insert something
left_div_end = re.compile(r'(infoborgil@gmail.com</span>\s*</div>\s*</div>)', re.DOTALL)

middle_content = """
        <!-- Elemento Central para rellenar espacio -->
        <div class="hidden xl:flex items-center gap-4 bg-secondary/5 px-6 py-2 rounded-full border border-secondary/10">
            <span class="material-symbols-outlined text-primary text-xl">verified_user</span>
            <span class="text-[11px] font-black uppercase tracking-widest text-secondary/60">Servicio Técnico Oficial Multi-marca</span>
        </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already have a middle element to avoid double insertion
    if 'Servicio Técnico Oficial Multi-marca' not in content:
        content = left_div_end.sub(r'\1' + middle_content, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cabecera rellenada con badge central.")
