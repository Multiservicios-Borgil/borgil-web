import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Nuevo script de Analytics directo
gtag_script = \"\"\"<!-- Google tag (gtag.js) -->
<script async src=\"https://www.googletagmanager.com/gtag/js?id=G-68682PBMTQ\"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-68682PBMTQ');
</script>\"\"\"

# Patrón para encontrar y eliminar el GTM anterior
gtm_head_pattern = re.compile(r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->', re.DOTALL)
gtm_body_pattern = re.compile(r'<!-- Google Tag Manager \(noscript\) -->.*?<!-- End Google Tag Manager \(noscript\) -->', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar GTM por gtag en el head
    if '<!-- Google Tag Manager -->' in content:
        content = gtm_head_pattern.sub(gtag_script, content)
    elif 'G-68682PBMTQ' not in content:
        content = content.replace('<head>', '<head>\\n    ' + gtag_script)
    
    # Eliminar el noscript de GTM
    content = gtm_body_pattern.sub('', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(\"Google Analytics (gtag.js) instalado directamente en todas las páginas.\")
