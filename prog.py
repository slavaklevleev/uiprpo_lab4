import re

f = open("data.txt", "r")
Lines = f.readlines()

def phone_format(n):                                                                                                                                  
    return (format(int(n[:-1]), ",").replace(",", "-") + n[-1]).replace("-", " (", 1).replace("-", ") ", 1)

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
                phone = '+' + phone_format(elem.replace(' ', ''))
                newString.append(phone)
            if idx == 3:
                newString.append(check_email(elem))

    
        f_out.write('|'.join(newString) + '\n')
