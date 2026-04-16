import os
dir_path = "/Users/madhavsharma/.gemini/antigravity/scratch/alosanar_website"
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
for f in files:
    filepath = os.path.join(dir_path, f)
    with open(filepath, 'r') as file:
        content = file.read()
    content = content.replace("logo.jpg", "logo.png")
    # Increase height slightly so the landscape text logo is legible
    content = content.replace('class="h-8 object-contain hidden md:block"', 'class="h-10 object-contain hidden md:block"')
    with open(filepath, 'w') as file:
        file.write(content)
