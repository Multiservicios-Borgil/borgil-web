import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Header Replacement Pattern
# We match the entire "Barra de Contacto Superior" div
header_pattern = re.compile(r'<!-- Barra de Contacto Superior -->\s*<div class="fixed top-0.*?</div>', re.DOTALL)

# New Header HTML
new_header = """<!-- Barra de Contacto Superior (Mejorada) -->
    <div class="fixed top-0 left-0 lg:left-72 right-0 bg-white shadow-md z-[50] py-4 px-8 flex flex-wrap justify-between items-center gap-6 border-b border-gray-100">
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
            <a href="https://wa.me/34623150111" class="flex items-center gap-3 bg-green-50 px-5 py-2.5 rounded-2xl border border-green-100 hover:bg-green-100 transition-all group">
                <span class="material-symbols-outlined text-green-600 font-black">smartphone</span>
                <span class="text-lg font-black text-green-700 tracking-tighter">623 150 111</span>
            </a>
        </div>
    </div>"""

# Footer footer patterns
illueca_pattern = re.compile(r'Illueca\s*·?\s*Aranda\s*·?\s*Calatayud', re.IGNORECASE)
illueca_pattern_2 = re.compile(r'Illueca\s*\(Zaragoza\)', re.IGNORECASE)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace Header
    content = header_pattern.sub(new_header, content)
    
    # 2. Cleanup references to Illueca
    content = illueca_pattern.sub('Servicio en toda la Región', content)
    content = illueca_pattern_2.sub('Servicio Nacional', content)
    content = content.replace('Illueca · Calatayud · Aranda', 'Atención en toda la Comarca')
    content = content.replace('Illueca (ZGZ)', 'Aragón')

    # Also check for the specific footer block in index.html
    content = content.replace('<span class="text-[10px] font-black text-white/20 uppercase tracking-widest">Illueca · Calatayud · Aranda</span>', '<span class="text-[10px] font-black text-white/20 uppercase tracking-widest text-primary/40 text-center">Calidad y Servicio Garantizado</span>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cabecera mejorada y referencias a Illueca eliminadas.")
