import re

def prueba(str):
    print(re.fullmatch('^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$', str))

prueba('2022-12-1 00:00:00')