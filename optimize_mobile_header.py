import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll update the header classes to be relative on mobile and fixed only on LG
# class="fixed top-0 left-0 lg:left-72 right-0 bg-white shadow-md z-[50] py-4 px-8 flex flex-wrap justify-between items-center gap-6 border-b border-gray-100 font-sans"

old_header_start = re.compile(r'<div class="fixed top-0 left-0 lg:left-72 right-0 bg-white shadow-md z-\[50\] py-4 px-8 flex flex-wrap justify-between items-center gap-6 border-b border-gray-100 font-sans">')

new_header_container = '<div class="relative lg:fixed top-0 left-0 lg:left-72 right-0 bg-white shadow-md z-[50] py-4 px-4 sm:px-8 flex flex-wrap justify-center sm:justify-between items-center gap-4 sm:gap-6 border-b border-gray-100 font-sans">'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update container classes
    content = old_header_start.sub(new_header_container, content)
    
    # 2. Hide email on mobile
    content = content.replace('<div class="flex items-center gap-3">\n                <span class="material-symbols-outlined text-primary text-2xl">mail</span>', '<div class="hidden md:flex items-center gap-3">\n                <span class="material-symbols-outlined text-primary text-2xl">mail</span>')
    
    # 3. Smaller phones on mobile
    content = content.replace('text-lg font-black text-secondary tracking-tighter', 'text-sm sm:text-lg font-black text-secondary tracking-tighter')
    content = content.replace('text-xl font-black text-green-700 tracking-tighter', 'text-sm sm:text-xl font-black text-green-700 tracking-tighter')
    content = content.replace('w-10 h-10', 'w-8 h-8 sm:w-10 sm:h-10')
    content = content.replace('px-5 py-2.5', 'px-3 py-2 sm:px-5 sm:py-2.5')

    # 4. Remove negative margin from Stock Banner on mobile
    content = content.replace('class="py-12 px-8 -mt-12 relative z-20"', 'class="py-12 px-8 mt-0 lg:-mt-12 relative z-20"')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cabecera optimizada para dispositivos móviles.")
