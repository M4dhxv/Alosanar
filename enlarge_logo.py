import os
dir_path = "/Users/madhavsharma/.gemini/antigravity/scratch/alosanar_website"
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
for f in files:
    filepath = os.path.join(dir_path, f)
    with open(filepath, 'r') as file:
        content = file.read()
    # Increase logo size significantly and ensure it shows on mobile
    content = content.replace('class="h-10 object-contain hidden md:block"', 'class="h-12 md:h-16 object-contain max-w-[200px] md:max-w-none mt-1"')
    with open(filepath, 'w') as file:
        file.write(content)
