import os
import shutil


def templates(root):
    template_path = os.path.join(root, 'templates')
    project = [item[0] for item in os.walk(root)]

    if not os.path.exists(template_path):
        os.mkdir(template_path)

    for item in project:
        tail = os.path.split(item)[1]
        if 'templates' in tail and item != template_path:
            try:
                for node in os.scandir(item):
                    shutil.move(node.path, template_path)
                os.rmdir(item)
            except Exception as e:
                print(f'The template in {item} already exists in {template_path}')

templates('my_project')