import os
dir_path = "/Users/madhavsharma/.gemini/antigravity/scratch/alosanar_website"
files = [f for f in os.listdir(dir_path) if f.endswith('.html')]
for f in files:
    filepath = os.path.join(dir_path, f)
    with open(filepath, 'r') as file:
        content = file.read()
    content = content.replace("logo.png", "logo.jpg")
    with open(filepath, 'w') as file:
        file.write(content)
