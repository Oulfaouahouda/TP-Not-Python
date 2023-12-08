
def produce_default_dict():
    return {'root': 'password'}

def salutation(nom, age):
    if age == "1":
        return f"Bonjour '{nom}', j'ai actuellement {age} an."
    else:
        return f"Bonjour '{nom}', j'ai actuellement {age} ans."

def power_2(limit):
    i = 0
    while 2 ** i <= limit:
        print(2 ** i, end=",") if 2 ** (i + 1) <= limit else print(2 ** i)
        i += 1

def check_ip_format(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

# Exemples d'appels (à commenter si je veux importer ce script dans un autre fichier)
# print(produce_default_dict())
# print(salutation('gael', '24'))
# print(salutation('bébé', '0'))
# power_2(10)
# print(check_ip_format('10.0.0.0'))
# print(check_ip_format('192.12.'))
