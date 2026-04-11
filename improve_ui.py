import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'admin.html']

# 1. Update Gallery Buttons (more visibility)
old_btn_left = 'class="absolute left-4 top-1/2 -translate-y-1/2 bg-white/10 hover:bg-white/20 text-white p-4 rounded-full transition-all z-[110]"'
new_btn_left = 'class="absolute left-2 sm:left-6 top-1/2 -translate-y-1/2 bg-white text-secondary hover:bg-primary hover:text-white p-4 sm:p-5 rounded-full transition-all z-[110] shadow-2xl"'

old_btn_right = 'class="absolute right-4 top-1/2 -translate-y-1/2 bg-white/10 hover:bg-white/20 text-white p-4 rounded-full transition-all z-[110]"'
new_btn_right = 'class="absolute right-2 sm:right-6 top-1/2 -translate-y-1/2 bg-white text-secondary hover:bg-primary hover:text-white p-4 sm:p-5 rounded-full transition-all z-[110] shadow-2xl"'

# 2. Update JS rendering for Description expansion and Price size
# Look for: <p class="text-secondary/50 text-sm mb-8 line-clamp-2">${prod.descripcion}</p>
desc_pattern = re.compile(r'<p class="text-secondary/50 text-sm mb-8 line-clamp-2">\$\{prod\.descripcion\}</p>')
new_desc = '<p title="${prod.descripcion.replace(/"/g, \'&quot;\')}" class="text-secondary/50 text-sm mb-8 line-clamp-2 hover:line-clamp-none transition-all cursor-help bg-white hover:bg-gray-50 p-2 rounded-xl border border-transparent hover:border-gray-100 hover:text-secondary hover:shadow-sm">${prod.descripcion}</p>'

# Look for: ${prod.precio_original ? `<span class="text-xs text-secondary/30 font-bold line-through ml-1">${prod.precio_original}</span>` : ''}
price_pattern = re.compile(r'\$\{prod\.precio_original \? `<span class="text-xs text-secondary/30 font-bold line-through ml-1">\$\{prod\.precio_original\}</span>` : \'\'\}')
new_price = '${prod.precio_original ? `<span class="text-3xl text-secondary/20 font-black line-through block mb-1">${prod.precio_original}</span>` : ""}'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply changes
    content = content.replace(old_btn_left, new_btn_left)
    content = content.replace(old_btn_right, new_btn_right)
    content = desc_pattern.sub(new_desc, content)
    content = price_pattern.sub(new_price, content)
    
    # Ensure transition-all for smoothness if not already there
    if 'fade-in {' not in content:
        content = content.replace('</style>', ' .line-clamp-none { -webkit-line-clamp: unset !important; display: block !important; }\n    </style>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Cambios de galería, descripción y precios aplicados.")
