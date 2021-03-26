import re

def email_parse(address):
    if '@' in address:
        addr = address.split('@')
        username = addr[0]
        domain = addr[1]
        if not username or not domain:
            return False
        else:
            valid_username = re.findall(r'(^[^\.]\S+[^\s][^\.]$)', username)
            valid_domain = re.findall(r'^\w+\.+\w+[^\s][^,]$', domain)
            if valid_username and valid_domain:
                return 'OK'
            else: return False
    else: return False


# function test
address_list = ('hj kh@yiu.yu', 'Jr#a.zy.cello@gma il.com', 'Htyut&&i7@gmail.com', 'gghj@..o', 'rrrr!r@tyu.ghj.g', '@mail.ru', 'gagaga')

for address in address_list:
    try:
        if email_parse(address):
            print(address, email_parse(address))
        else: raise ValueError
    except ValueError:
        print(f'{address} is not valid email address')
