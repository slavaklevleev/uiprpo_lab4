import re

f = open("data.txt", "r")
Lines = f.readlines()

def check_phone(phone):
    # убираем все символы, кроме цифр
    phone = re.sub(r'\D', '', phone)
    country_code = phone[0:len(phone) - 10]
    # проверяем длину номера
    if (len(phone) - len(country_code)) != 10:
        return '-'
    # форматируем номер телефона
    return '+' + country_code + ' (' + phone[len(country_code):len(country_code) + 3] + ') ' + phone[len(country_code) + 3:len(country_code) + 6] + '-' + phone[len(country_code) + 6:len(country_code) + 8] + '-' + phone[len(country_code) + 8:]

def check_email(email):
    email = email.replace(' ', '').replace('..', '.')
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        email = re.sub(r'\.{2,}', '.', email)
        email = re.sub(r'@{2,}', '@', email)
        if not re.match(pattern, email):
            return ''
    username, domain = email.split('@')
    domain_parts = domain.split('.')
    if len(domain_parts) > 2:
        domain = '.'.join(domain_parts[-2:])
    return f'{username}@{domain}'

with open('output.txt', 'w') as f_out:
    for line in Lines:
        arr = line.strip().split('|')
        newString = []
        for idx, elem in enumerate(arr):
            if idx == 0:
                name = re.sub(r'(?<=[a-z])([A-Z])', r' \1', elem).strip()
                newString.append(name)
            if idx == 1:
                age = re.search(r'[0-9]+', elem)
                if age:
                    newString.append(elem)
                else:
                    newString.append('')
            if idx == 2:
                phone = check_phone(elem)
                newString.append(phone)
            if idx == 3:
                newString.append(check_email(elem))

    
        f_out.write('|'.join(newString) + '\n')
