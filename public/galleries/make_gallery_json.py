import os
import json

def get_content(gallry_dir):
    content = {"name":gallry_dir[:-1]}
    # photos
    _files = os.listdir(gallry_dir)
    photos = []
    for one in _files:
        if one[-4:].lower() == '.jpg':
            photos.append(one)
    content["cover"] = gallry_dir+photos[0]
    content["description"] = ""
    content["photos"] = photos
    return content

if __name__ == '__main__':
    dirs = []
    for one in os.listdir('.'):
        if os.path.isdir(one) and one!='.idea':
            dirs.append(one+'/')
    _list = [get_content(dir) for dir in dirs]
    with open("galleries.json", 'w') as fw:
        json.dump(_list, fw, indent=4, ensure_ascii=False)

