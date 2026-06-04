import os

folder = "output"  # your HTML folder

files = sorted([f for f in os.listdir(folder) if f.endswith(".html")])

html = """<!DOCTYPE html>
<html>
<head>
    <title>RentIt - Chennai Rentals</title>
    <meta name="description" content="Browse rental properties in Chennai">
</head>
<body>

<h1>RentIt Property Listings</h1>
<ul>
"""

for file in files:
    name = file.replace("-", " ").replace(".html", "").title()
    html += f'<li><a href="{file}">{name}</a></li>\n'

html += """
</ul>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html generated with", len(files), "links")