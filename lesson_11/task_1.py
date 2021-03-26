class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_num(cls, date):
        numbers = date.split('-')
        result = tuple(int(num) for num in numbers)
        print(result)

    @staticmethod
    def check_date(str_date):
        numbers = {k: int(v) for k, v in zip(('d', 'm', 'y'), str_date.split('-'))}
        # print(numbers)
        if numbers['d'] > 31 or numbers['m'] > 12:
            print(f'The date {str_date} is invalid. Error')
        else:
            print(f'The date {str_date} is valid. OK')



# test section

d1 = '12-12-2019'
d2 = '78-7-1998'
Date.date_to_num(d1)
Date.check_date(d1)
Date.check_date(d2)



