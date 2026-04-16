import os
dir_path = "/Users/madhavsharma/.gemini/antigravity/scratch/alosanar_website"
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
for f in files:
    filepath = os.path.join(dir_path, f)
    with open(filepath, 'r') as file:
        content = file.read()
    # Replace the old image class with a white background pill so the black text is visible against the dark website
    content = content.replace('class="h-10 object-contain hidden md:block"', 'class="h-10 object-contain hidden md:block bg-white/95 px-3 py-1.5 rounded-md shadow-sm"')
    with open(filepath, 'w') as file:
        file.write(content)
