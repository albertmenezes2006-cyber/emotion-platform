#!/usr/bin/env python3
"""Adiciona Microsoft Clarity em todos os HTMLs"""
import os
from pathlib import Path

CLARITY_ID = "COLE_SEU_ID_AQUI"  # clarity.microsoft.com

SCRIPT = f"""
    <!-- Microsoft Clarity -->
    <script type="text/javascript">
        (function(c,l,a,r,i,t,y){{
            c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
            t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
            y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        }})(window, document, "clarity", "script", "{CLARITY_ID}");
    </script>"""

templates = Path("templates")
count = 0

for html in templates.glob("*.html"):
    content = html.read_text(encoding="utf-8")
    if "clarity.ms" not in content and "</head>" in content:
        content = content.replace("</head>", SCRIPT + "\n</head>")
        html.write_text(content, encoding="utf-8")
        count += 1
        print(f"✅ {html.name}")

print(f"\n✅ Clarity adicionado em {count} páginas")
print(f"📊 Acesse: clarity.microsoft.com para ver gravações")
