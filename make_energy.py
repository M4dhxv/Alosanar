import re
import os

dir_path = "/Users/madhavsharma/.gemini/antigravity/scratch/alosanar_website"
with open(os.path.join(dir_path, 'index.html'), 'r') as f:
    html = f.read()

# Replace title
html = html.replace('<title>Alosanar | The Architectural Monolith</title>', '<title>Alosanar | Energy Integration</title>')

# Active state for nav
html = html.replace('href="/">Home</a>', 'href="/" class="font-[\'Space_Grotesk\'] uppercase tracking-widest text-xs text-slate-400 hover:text-blue-100 transition-colors">Home</a>')
html = html.replace('href="/energy.html">Energy</a>', 'href="/energy.html" class="font-[\'Space_Grotesk\'] uppercase tracking-widest text-xs text-blue-200 font-bold border-b-2 border-blue-200 pb-1">Energy</a>')

# Background Image
html = html.replace(
    'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=2000&q=80',
    'https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=2000&q=80'
)

# Hero Replacement
html = re.sub(
    r'<h1 class="font-headline[^>]*>.*?</h1>',
    r'<h1 class="font-headline text-[3.5rem] md:text-[5rem] leading-[1.1] mb-8 -ml-1 tracking-tighter text-on-surface">Data Center <span class="text-primary italic">Energy Integration</span></h1>',
    html, flags=re.DOTALL
)

html = re.sub(
    r'<p class="max-w-xl font-body text-lg text-on-surface-variant leading-relaxed">\s*Development and operations at an unprecedented scale, architected for the future of global compute demands.\s*</p>',
    r'<p class="max-w-xl font-body text-lg text-on-surface-variant leading-relaxed">The well publicized energy concerns stemming from data center demands leave out a very big mitigating factor.</p>',
    html
)

# Now we find the <section> elements after the hero <header> and before the footer
# And replace them with exactly one section containing the rest of the text
start_idx = html.find('</header>') + len('</header>')
end_idx = html.find('<footer')

mid_section = """
<section class="py-32 bg-surface">
    <div class="max-w-5xl mx-auto px-8">
        <h2 class="font-headline text-3xl mb-8 text-on-surface">Gigawatts of Available Power</h2>
        <div class="space-y-6">
            <p class="font-body text-xl text-on-surface-variant leading-relaxed">
                While there are energy constraints for some greenfield projects and projects with very specific location requirements, the reality is there are gigawatts worth of available power scattered about in disparate buildings and properties throughout the US and the world. 
            </p>
            <p class="font-body text-xl text-on-surface-variant leading-relaxed">
                This includes both immediate connectivity and available grid capacity that is untapped.
            </p>
            <p class="font-body text-xl text-on-surface-variant leading-relaxed border-l-2 border-primary pl-6">
                We have assembled a large and growing portfolio of properties through site rights, referrals, lease or purchase that provide access to this capacity.
            </p>
        </div>
    </div>
</section>
"""

new_html = html[:start_idx] + mid_section + html[end_idx:]

with open(os.path.join(dir_path, 'energy.html'), 'w') as f:
    f.write(new_html)

