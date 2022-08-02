"""Opening sites"""

import os

while True:
    sayt = input('введите название сайта \n')
    if sayt == 'конец':
        break

    if "https://" in sayt:
        os.system('start ' + sayt)

    elif "www." in sayt:
        sayt = 'https://' + sayt
        os.system('start ' + sayt)
    else:
        sayt = 'https://www.' + sayt
        os.system('start ' + sayt)