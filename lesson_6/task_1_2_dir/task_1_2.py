import requests

log_src = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').iter_lines()

log_format = []
count = {}

for line in log_src:
    log_line = line.decode(encoding='utf-8').split(' ')

    log_format.append(f'{log_line[0], log_line[5][1:], log_line[6]}\n')

    if log_line[0] not in count:
        count.update({log_line[0]: 1})
    else:
        count[log_line[0]] += 1

suspicious_addr = ((ip_addr, count[ip_addr]) for ip_addr in count.keys() if count[ip_addr] == max(count.values()))

with open('log_file.txt', 'w', encoding='utf-8') as f:
    f.writelines(log_format)

with open('report.txt', 'w', encoding='utf-8') as f:
    f.write(f'{tuple(*suspicious_addr)}')

