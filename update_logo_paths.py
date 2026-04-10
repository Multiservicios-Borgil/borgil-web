import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Paths to update
# 1. Horizontal logo
h_pattern = re.compile(r'fotos_originales/VARIACIONHORIZONTAL\.png')
# 2. Vertical logo
v_pattern = re.compile(r'fotos_originales/VARIACIONVERTICAL\.png')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace paths
    content = h_pattern.sub('logo-horizontal.png', content)
    content = v_pattern.sub('logo-vertical.png', content)

    # Force large sizes (if I missed any in previous step or if they were reverted)
    # Sidebar max-h
    content = re.sub(r'max-h-1\d', 'max-h-32', content) # Change max-h-16 or similar to max-h-32
    # Footer h
    content = re.sub(r'h-20', 'h-40', content) # Change h-20 to h-40
    content = re.sub(r'h-24', 'h-40', content) # Change h-24 to h-40

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Actualización de rutas y tamaños de logos completada.")
