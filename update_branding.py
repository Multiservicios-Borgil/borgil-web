import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

sidebar_pattern = r'<div class="flex items-center gap-3 mb-[2-8]" onclick="location\.href=\'index\.html\'" style="cursor:pointer">.*?</div>'
replacement_sidebar = """<div class="flex items-center gap-3 mb-10" onclick="location.href='index.html'" style="cursor:pointer">
            <img src="logo-horizontal.png" alt="Multiservicios Borgil" class="h-24 w-auto object-contain">
        </div>"""

footer_pattern = r'<footer.*?</footer>'

# This script will be more surgical
for filename in html_files:
    print(f"Updating {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Sidebar Logo (more robust matching)
    content = re.sub(r'<div class="flex items-center gap-3 mb-\d+" onclick="location\.href=\'index\.html\'" style="cursor:pointer">.*?<img src=".*?".*?>.*?</div>', replacement_sidebar, content, flags=re.DOTALL)
    # Also match the old BORGIL text version if any left
    content = re.sub(r'<div class="flex items-center gap-3 mb-\d+" onclick="location\.href=\'index\.html\'" style="cursor:pointer">.*?BORGIL.*?</div>', replacement_sidebar, content, flags=re.DOTALL)
    
    # 2. Update Footer (surgical replacement of the logo part)
    # Match the old B square or any img src="logo..."
    content = re.sub(r'<div class="w-8 h-8 bg-primary rounded flex items-center justify-center font-black text-white text-xs">B</div>\s*<span class="font-black uppercase text-xs tracking-tighter text-secondary leading-none.*?</span>', '<img src="logo-white.png" alt="Multiservicios Borgil" class="h-16 w-auto">', content, flags=re.DOTALL)
    content = re.sub(r'<img src="logo-vertical\.png" alt="Multiservicios Borgil" class="h-\d+ w-auto brightness-0 invert">', '<img src="logo-white.png" alt="Multiservicios Borgil" class="h-24 w-auto">', content)
    content = re.sub(r'<img src="logo\.png" alt="Multiservicios Borgil" class="h-\d+ w-auto">', '<img src="logo-white.png" alt="Multiservicios Borgil" class="h-16 w-auto">', content)

    # 3. Favicon
    if '<link rel="icon"' in content:
        content = re.sub(r'<link rel="icon" type="image/png" href=".*?">', '<link rel="icon" type="image/png" href="logo-horizontal.png">', content)
    else:
        content = content.replace('</head>', '    <link rel="icon" type="image/png" href="logo-horizontal.png">\n</head>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done.")
