import psycopg2, re
from psycopg2 import Error



contacts=[
    (6, 'Parida', 'Zholshybek', '87476564411'),
    (7, 'Anuar', 'Izbasar', '87674442323'),#incorect
    (8, 'Qairat', 'Nurtas', '98989898'),#incorect
    (9, 'Akulpa', 'Anuarqyzy', '87075656633')
]



pattern =r'^8777[0-9]{7}$|^8747[0-9]{7}$|^8778[0-9]{7}$|^8700[0-9]{7}$|^8707[0-9]{7}$|^8708[0-9]{7}$|^8705[0-9]{7}$|^8775[0-9]{7}$' 
pattern2=r'^(\+?7|8)(700|701|702|705|707|708|709|747|750|751|760|761|762|763|764|771|775|776|777|778|780|781|782|783|784|785|786|787|788|789|747|760|761|762|763|764|771|775|776|777|778|780|781|782|783|784|785|786|787|788|789)\d{7}$'

incorrect_numbers=[]
coorect_numbers=[]
for adam in contacts:
    if re.match(pattern, adam[3])==None:
        incorrect_numbers.append(adam)
    else:
        coorect_numbers.append(adam)


try:
    config = psycopg2.connect(
    host = 'localhost',
    database='phonebook',
    user='postgres',
    password='1123'
    )

    current = config.cursor()
    sql='''
        INSERT INTO phone_number (phone_number_id, name, surname, number_value) VALUES (%s, %s, %s, %s);
'''
    current.executemany(sql, coorect_numbers)
    config.commit()

except (Exception, Error) as error:
    print("ERROR", error)
finally:
    if config:
        current.close()
        config.close()
print(f'List of incorrect values is: {incorrect_numbers}')