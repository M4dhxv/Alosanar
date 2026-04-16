import re
import os

dir_path = "/Users/madhavsharma/.gemini/antigravity/scratch/alosanar_website"
files = ['index.html', 'marketplace.html', 'operations.html', 'services.html', 'about.html']

def get_nav_html():
    return """<nav class="fixed top-0 w-full z-50 bg-slate-950/60 backdrop-blur-lg shadow-[0_20px_40px_rgba(0,0,0,0.4),0_0_20px_rgba(173,198,255,0.05)]">
<div class="flex justify-between items-center w-full px-8 h-20 max-w-[1440px] mx-auto">
<a href="/" class="text-2xl font-black tracking-tighter text-blue-200 font-['Space_Grotesk']">
                Alosanar
            </a>
<div class="hidden md:flex items-center gap-10">
<a class="font-['Space_Grotesk'] uppercase tracking-widest text-xs text-slate-400 hover:text-blue-100 transition-colors" href="/">Home</a>
<a class="font-['Space_Grotesk'] uppercase tracking-widest text-xs text-slate-400 hover:text-blue-100 transition-colors" href="/marketplace.html">Marketplace</a>
<a class="font-['Space_Grotesk'] uppercase tracking-widest text-xs text-slate-400 hover:text-blue-100 transition-colors" href="/operations.html">Operations</a>
<a class="font-['Space_Grotesk'] uppercase tracking-widest text-xs text-slate-400 hover:text-blue-100 transition-colors" href="/services.html">Services</a>
<a class="font-['Space_Grotesk'] uppercase tracking-widest text-xs text-slate-400 hover:text-blue-100 transition-colors" href="/about.html">About</a>
</div>
<div class="flex items-center gap-6">
<button class="hidden lg:block font-['Space_Grotesk'] uppercase tracking-widest text-xs text-slate-400 hover:text-blue-100 transition-colors active:scale-95 transition-transform">Client Login</button>
<button class="monolith-gradient px-6 py-3 rounded text-on-primary font-['Space_Grotesk'] uppercase tracking-widest text-xs font-bold active:scale-95 transition-transform">Contact Sales</button>
</div>
</div>
</nav>"""

nav_html = get_nav_html()

for file in files:
    filepath = os.path.join(dir_path, file)
    with open(filepath, 'r') as f:
        content = f.read()

    # The AI generates navigation usually enclosed in <nav> or <header>
    # In index.html it is <nav ...> ... </nav>
    # In services.html it is <header ...> <nav ...> ... </nav> </header>
    
    # Let's replace the first occurrence of <header>...</header> or <nav>...</nav> using regex
    # We will search for <header>...</header> first. If it exists, replace it entirely. 
    # If not, replace <nav>...</nav>.
    
    header_match = re.search(r'<header[^>]*>([\s\S]*?)</header>', content)
    nav_match = re.search(r'<nav[^>]*>([\s\S]*?)</nav>', content)
    
    # Be careful not to replace the main <header> hero section if the page uses <header> for the hero!
    # In index.html, the hero is <header class="relative ...">
    # The nav is just <nav>. So replacing <header> in index.html would nuke the hero!
    
    # Better approach: We know the nav is always right after <body...> or inside a top container.
    # In all files, the nav contains "ALOSANAR" or "Alosanar" text links.
    # Let's explicitly replace <nav>...</nav> for the FIRST <nav> tag.
    
    if nav_match:
        # replace the first nav tag
        pre, match, post = content.partition(nav_match.group(0))
        
        # If it's wrapped in a <header> right above it, remove the <header> and </header> tags
        if '<header' in pre[-200:] and '</header>' in post[:200]:
            # This is risky string math. Let's just swap the <nav> element.
            pass
            
        content = pre + nav_html + post
        
        # To handle active states
        if file == 'index.html':
            content = content.replace('href="/">Home</a>', 'href="/" class="font-[\'Space_Grotesk\'] uppercase tracking-widest text-xs text-blue-200 font-bold border-b-2 border-blue-200 pb-1">Home</a>')
        elif file == 'marketplace.html':
             content = content.replace('href="/marketplace.html">Marketplace</a>', 'href="/marketplace.html" class="font-[\'Space_Grotesk\'] uppercase tracking-widest text-xs text-blue-200 font-bold border-b-2 border-blue-200 pb-1">Marketplace</a>')
        elif file == 'operations.html':
             content = content.replace('href="/operations.html">Operations</a>', 'href="/operations.html" class="font-[\'Space_Grotesk\'] uppercase tracking-widest text-xs text-blue-200 font-bold border-b-2 border-blue-200 pb-1">Operations</a>')
        elif file == 'services.html':
             content = content.replace('href="/services.html">Services</a>', 'href="/services.html" class="font-[\'Space_Grotesk\'] uppercase tracking-widest text-xs text-blue-200 font-bold border-b-2 border-blue-200 pb-1">Services</a>')
        elif file == 'about.html':
             content = content.replace('href="/about.html">About</a>', 'href="/about.html" class="font-[\'Space_Grotesk\'] uppercase tracking-widest text-xs text-blue-200 font-bold border-b-2 border-blue-200 pb-1">About</a>')
            
        with open(filepath, 'w') as f:
            f.write(content)
            print(f"Fixed {file}")

