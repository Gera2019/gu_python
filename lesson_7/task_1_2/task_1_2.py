import os
from template_parse import yaml_parse

with open('template.yaml', 'r') as f:
   template = f.readlines()

result = yaml_parse(template)

for dir, files in result.items():
   try:
      os.makedirs(dir)
   except Exception as e:
         print(f'The directory {dir} already exists')
         ask = input(f'Overwrite the existing folder {dir}? Type y(yes), n(no): ')
         if ask == 'y':
               os.makedirs(dir, exist_ok=True)
         elif ask == 'n':
            print(e)
         else:
            print('Please enter y (for yes) or n (for no)')
            ask = input(f'Overwrite the existing folder {dir}? Type y or n: ')
   else:
        for fi in files:
            node = os.path.join(dir, fi)
            print(node)
            if not os.path.exists(node):
                with open(node, 'w'): pass
            elif input(f'Overwrite the existing file {node}? Type y or n: ') == 'y':
              with open(node, 'w'): pass
