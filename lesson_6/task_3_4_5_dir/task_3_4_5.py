import sys

"""
Help: users_hobby.py <path to the users list> <path to the hobby list> <pass to the joined list>
"""
file_path = sys.argv[1:]


def users_hobby(*file_path):
    user_path = r'{}'.format(file_path[0]) # используем приобразование в "сырой" формат, в случае если путь будет содержать символы /\ и т.д.
    hobby_path = r'{}'.format(file_path[1])
    result_path = r'{}'.format(file_path[2])

    with open(user_path, 'r', encoding='utf-8') as f_users:
        with open(hobby_path, 'r', encoding='utf-8') as f_hobby:
            with open(result_path, 'w+', encoding='utf-8') as f_result:
                for user in f_users:
                    result = '{0}: {1}'.format(user.rstrip('\n'), str(next(f_hobby, None)).rstrip('\n'))
                    f_result.writelines(result + '\n')
            print('Write files is finished')

users_hobby(*file_path)