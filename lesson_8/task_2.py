import requests
import re
import os

url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
log_file = requests.get(url).iter_lines(delimiter=b'\n')


def log_parse(src, dst):
    with open(dst, 'a', encoding='utf-8') as f:
        for line in src:
            line = line.decode(encoding='utf-8')
            if line:
                remote_addr = re.search(r'\w{1,4}([\.|:]\w{1,4}){3,7}', line).group()
                req_datetime = re.search(r'(\d+/\w{3}/\d{4}((:\d{2}){3})\s\+\d{4})', line).group()
                req_type = re.search(r']\s"(\w{3})', line).group(1)
                resource = re.search(r'\s(\/.+)+\b"\s', line).group(1)
                resp_code = re.search(r'"\s(\d{3})', line).group(1)
                resp_size = re.search(r'\s(\d+)\s"', line).group(1)

                result = (remote_addr, req_datetime, req_type, resource, resp_code, resp_size)
                f.write(str(result) + '\n')

# function test
if os.path.exists('log_report.txt'):
    os.remove('log_report.txt')
log_parse(log_file, 'log_report.txt')
