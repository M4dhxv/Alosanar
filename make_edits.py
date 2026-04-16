import os
import re

dir_path = "/Users/madhavsharma/.gemini/antigravity/scratch/alosanar_website"
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# 1. Map for background images (clear, colorful, realistic, dark theme)
images = {
    'index.html': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=2000&q=80',
    'marketplace.html': 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=2000&q=80',
    'operations.html': 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=2000&q=80',
    'services.html': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=2000&q=80',
    'about.html': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=2000&q=80',
}

def clean_html(html, filename):
    # Global Nav: Use logo.png instead of text "Alosanar"
    html = re.sub(r'<a href="/" class="text-2xl font-black[^>]*>\s*Alosanar\s*</a>', 
                  '<a href="/"><img src="logo.png" alt="Alosanar" class="h-8 object-contain hidden md:block"></a>', html)
    # Remove Client Login button
    html = re.sub(r'<button class="hidden lg:block[^>]*>Client Login</button>', '', html)
    
    # Insert Energy link into nav
    energy_str = '<a class="font-[\'Space_Grotesk\'] uppercase tracking-widest text-xs text-slate-400 hover:text-blue-100 transition-colors" href="/energy.html">Energy</a>'
    
    # Target the end of the navigation div list
    if "href=\"/about.html\">About</a>\n</div>" in html:
        html = html.replace('href="/about.html">About</a>\n</div>', f'href="/about.html">About</a>\n{energy_str}\n</div>')
    elif "href=\"/about.html\">About</a></div>" in html:
        html = html.replace('href="/about.html">About</a></div>', f'href="/about.html">About</a>\n{energy_str}</div>')
    else: 
        html = html.replace('href="/about.html">About</a>', f'href="/about.html">About</a>\n{energy_str}')

    # Replace the very first <img ...> which is the background, with the Unsplash specific one for this file
    if filename in images:
        html = re.sub(r'<img class="w-full h-full object-cover[^>]*src="[^"]*"', 
                      f'<img class="w-full h-full object-cover opacity-60 mix-blend-luminosity" src="{images[filename]}"', html, count=1)
                      
    # Scrub specific AI Filler Text the user mentioned and others commonly injected
    scrub_list = [
        "Infrastructural Monolith",
        "Infrastructure Excellence",
        "Consulting",
        "Latency 0.04ms",
        "Edge Latency: &lt; 1ms",
        "Active Nodes: 242",
        "Response Efficiency +38% PUE Opt.",
        "4.2GW speed",
        "Tier III+ Standard",
        "Liquid Cooled",
        "100Gbps Backbone",
        "Compact, ultra-efficient modular units designed for immediate deployment at the edge of the network.",
        "High-density compute clusters optimized for Large Language Models and real-time visual analytics.",
        "Strategic backbone locations providing low-latency interconnects between local edge and core clouds.",
        "40% Annual Growth Rate",
        "&lt;5ms Target Latency",
        "Accelerating Edge Growth &amp; Infrastructure with precision-engineered capacity for the next generation of global compute."
    ]
    for phrase in scrub_list:
        html = html.replace(phrase, "")
        
    return html

for file in files:
    filepath = os.path.join(dir_path, file)
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = clean_html(content, file)
    
    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"Processed {file}")

