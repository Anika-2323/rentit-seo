import os

domain = "https://rentit-seo1.vercel.app"
folder = "output"

files = sorted([f for f in os.listdir(folder) if f.endswith(".html")])

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''

for file in files:
    xml += f"""
<url>
  <loc>{domain}/{file}</loc>
</url>
"""

xml += "\n</urlset>"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml)

print("Sitemap created with", len(files), "pages")