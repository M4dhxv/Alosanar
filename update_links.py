import os
import re

dir_path = "."
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

link_map = {
    "Home": "/",
    "Marketplace": "/marketplace.html",
    "Operations": "/operations.html",
    "Services": "/services.html",
    "About": "/about.html"
}

for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    for key, url in link_map.items():
        content = re.sub(
            r'<a([^>]*)href=["\'][^"\'>]*["\']([^>]*)>\s*' + key + r'\s*</a>',
            r'<a\1href="' + url + r'"\2>' + key + '</a>',
            content,
            flags=re.IGNORECASE
        )
    
    with open(file, 'w') as f:
        f.write(content)
        print(f"Updated {file}")
