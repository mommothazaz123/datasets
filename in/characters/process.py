import json
import re
import shutil

import requests

with open('characters.json') as f:
    characters = json.load(f)

num_characters_with_image = 0
for i, character in enumerate(characters):
    image = character['stats']['image']
    if re.match(r"(https?://)([/.\w\s-]*)\.(?:jpg|gif|png)", image):
        print(f"Getting {image}...")
        img = requests.get(image, stream=True)
        print(img.status_code)
        if img.status_code == 200:
            num_characters_with_image += 1
            img.raw.decode_content = True
            with open(f'{num_characters_with_image}.png', 'wb') as out_file:
                shutil.copyfileobj(img.raw, out_file)
