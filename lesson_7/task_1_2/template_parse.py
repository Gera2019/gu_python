def yaml_parse(template):
   root = template[0].rstrip('\n')
   path = ''
   file_list = []
   structure = {}
   indent = [0, 0]

   for line in template[1:]:
      indent[1] = line.count('  |')
      # print(indent)
      line = line.rstrip('\n').lstrip('  |')
      if indent[1] > indent[0]:
         structure[root + '/' + path] = file_list[:]
         file_list.clear()
         if line.startswith('--'):
            line = line.lstrip('--')
            if path == '':
               path = line
            else:
               path = path + '/' + line
         else:
            file_list.append(line)

      if indent[0] == indent[1]:
         if line.startswith('--'):
            line = line.lstrip('--')
            structure[root + '/' + path] = file_list[:]
            file_list.clear()
            path = path + '/' + line
         else:
            file_list.append(line)
            structure[root + '/' + path] = file_list[:]

      if indent[1] < indent[0]:
         structure[root + '/' + path] = file_list[:]
         file_list.clear()
         if line.startswith('--'):
            line = line.lstrip('--')
            path = line
      indent[0] = indent[1]

   return structure
#
# with open('template.yaml', 'r') as f:
#    template = f.readlines()
# res = yaml_parse(template)
# for i in res:
#    print(i, res[i])
# print(res)