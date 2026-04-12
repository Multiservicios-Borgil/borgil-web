import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

gtm_head = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NX2NDNLK');</script>
<!-- End Google Tag Manager -->"""

gtm_body = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NX2NDNLK"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Insert in <head>
    if '<!-- Google Tag Manager -->' not in content:
        content = content.replace('<head>', '<head>\n    ' + gtm_head)
    
    # Insert in <body>
    if '<!-- Google Tag Manager (noscript) -->' not in content:
        # We try to put it right after <body> tag
        content = content.replace('<body', gtm_body + '\n<body', 1)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Google Tag Manager (GTM-NX2NDNLK) integrado en todas las páginas.")
