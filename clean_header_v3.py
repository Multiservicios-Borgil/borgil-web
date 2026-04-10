import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# The target header we want
new_header = """<!-- Barra de Contacto Superior (Limpia) -->
    <div class="fixed top-0 left-0 lg:left-72 right-0 bg-white shadow-md z-[50] py-4 px-8 flex flex-wrap justify-between items-center gap-6 border-b border-gray-100 font-sans">
        <div class="flex items-center gap-8">
            <div class="flex items-center gap-3">
                <span class="material-symbols-outlined text-primary text-2xl">mail</span>
                <span class="text-sm font-bold text-secondary">infoborgil@gmail.com</span>
            </div>
        </div>
        <div class="flex items-center gap-8">
            <a href="tel:976822343" class="flex items-center gap-3 group">
                <div class="w-10 h-10 bg-gray-50 rounded-full flex items-center justify-center group-hover:bg-primary transition-colors">
                    <span class="material-symbols-outlined text-primary text-xl group-hover:text-white">phone</span>
                </div>
                <span class="text-lg font-black text-secondary tracking-tighter">976 82 23 43</span>
            </a>
            <a href="https://wa.me/34623150111" class="flex items-center gap-3 bg-green-50 px-5 py-2.5 rounded-2xl border border-green-100 hover:bg-green-100 transition-all group border-2 border-green-200">
                <span class="material-symbols-outlined text-green-600 font-black text-2xl">smartphone</span>
                <span class="text-xl font-black text-green-700 tracking-tighter">623 150 111</span>
            </a>
        </div>
    </div>"""

# Regex to find ANY version of the header (including duplicated ones)
# We look for the start comment up to the point where the Hero or Sidebar ends.
# Basically from the first <!-- Barra de Contacto --> until it hits the <!-- Hero --> or similar.
full_cleanup_regex = re.compile(r'<!-- Barra de Contacto.*?<!-- Hero', re.DOTALL)
full_cleanup_regex_sat = re.compile(r'<!-- Barra de Contacto.*?<!-- Hero SAT', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the messy header area with our new one + the comment that was removed
    if 'Hero SAT' in content:
        content = full_cleanup_regex_sat.sub(new_header + '\n\n    <!-- Hero SAT', content)
    else:
        content = full_cleanup_regex.sub(new_header + '\n\n    <!-- Hero', content)
    
    # Also cleanup any stray Illueca
    content = re.sub(r'Illueca', 'Aragón', content, flags=re.IGNORECASE)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cabeceras saneadas en todos los archivos.")
