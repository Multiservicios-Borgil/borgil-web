import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Revertir Sidebar al original (Texto BORGIL + Icono Caja)
revert_sidebar = """<div class="flex items-center gap-3 mb-2" onclick="location.href='index.html'" style="cursor:pointer">
            <div class="w-8 h-8 bg-primary rounded-lg flex items-center justify-center"><span class="material-symbols-outlined text-white text-sm">home_repair_service</span></div>
            <div class="text-xl font-black uppercase tracking-tighter">BORGIL</div>
        </div>"""

for filename in html_files:
    print(f"Reverting {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Eliminar Favicon
    content = re.sub(r'\s*<link rel="icon" type="image/png" href="logo-horizontal\.png">', '', content)
    content = re.sub(r'\s*<link rel="icon" type="image/png" href="logo\.png">', '', content)

    # Revertir Sidebar
    content = re.sub(r'<div class="flex items-center gap-3 mb-\d+" onclick="location\.href=\'index\.html\'" style="cursor:pointer">.*?<img src="logo.*?".*?>.*?</div>', revert_sidebar, content, flags=re.DOTALL)

    # Revertir Footer (Volver al "B" cuadrado y el texto)
    revert_footer = """<div class="flex items-center gap-3">
                <div class="w-8 h-8 bg-primary rounded flex items-center justify-center font-black text-white text-xs">B</div>
                <span class="font-black uppercase text-xs tracking-tighter text-secondary leading-none text-[10px]">Multiservicios BORGIL</span>
            </div>"""
    
    content = re.sub(r'<img src="logo-white\.png" alt="Multiservicios Borgil" class="h-\d+ w-auto.*?>', revert_footer, content)
    content = re.sub(r'<div class="flex flex-col items-center gap-4">.*?<img src="logo-white\.png".*?>.*?</div>', revert_footer, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Reversion Done.")
