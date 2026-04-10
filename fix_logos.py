import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Patterns to replace
sidebar_pattern = re.compile(r'<img src="fotos_originales/VARIACIONHORIZONTAL\.png".*?class=".*?"')
footer_pattern = re.compile(r'<img src="fotos_originales/VARIACIONVERTICAL\.png".*?class=".*?"')

# Admin pattern
admin_pattern = re.compile(r'<img src="fotos_originales/VARIACIONHORIZONTAL\.png" alt="Logo Borgil" class="h-10 w-auto brightness-0 invert">')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Sidebar Replacement
    content = sidebar_pattern.sub('<img src="fotos_originales/VARIACIONHORIZONTAL.png" alt="Logo Multiservicios Borgil" class="w-full h-auto max-h-24 object-contain transition-transform hover:scale-105 duration-300"', content)
    
    # 2. Footer Replacement
    content = footer_pattern.sub('<img src="fotos_originales/VARIACIONVERTICAL.png" alt="Logo BORGIL" class="h-20 w-auto"', content)
    
    # 3. Specific Admin Replacement
    content = admin_pattern.sub('<img src="fotos_originales/VARIACIONHORIZONTAL.png" alt="Logo Borgil" class="h-20 w-auto">', content)

    # Specific Service footer replacement (it has brightness-0)
    service_footer = re.compile(r'<img src="fotos_originales/VARIACIONHORIZONTAL\.png" alt="Logo BORGIL" class="h-12 w-auto brightness-0 invert opacity-80">')
    content = service_footer.sub('<img src="fotos_originales/VARIACIONHORIZONTAL.png" alt="Logo BORGIL" class="h-20 w-auto">', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Actualización de logos completada en todos los archivos HTML.")
