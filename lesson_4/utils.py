import requests
import xml.etree.ElementTree as ET
from datetime import date

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_source = ET.fromstring(requests.get(url).text)


def currency_rates(*code):
    info = ''
    error = ''

    date_extract = currency_source.attrib['Date'].split('.')
    curs_date = f'Сегодня {date(*reversed([*map(int, date_extract)]))}:\n'

    code_list = [code_l.text for code_l in currency_source.findall('./Valute/CharCode')]

    for request_code in code:

        if request_code.upper() not in code_list:
            error += f'Валюта {request_code} не найдена\n'

        for element in currency_source.findall('./Valute'):
            if request_code.upper() == element.find('./CharCode').text:
                code_value = float((element.find('./Value').text).replace(',', '.'))
                info += f'Курс {request_code} составляет {code_value} руб \n'

    result = curs_date + info + error
    print(result)


# print(currency('eur', 'usd', 'yu'))
# print(currency(*code))







