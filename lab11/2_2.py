import psycopg2
from psycopg2 import Error

try:
    config = psycopg2.connect(
        host='localhost',
        database='phonebook',
        user='postgres',
        password='1123'
    )

    current = config.cursor()

    name = input('Name: ')
    surname = input('Surname: ')
    number_value = input('Number: ')

    current.execute("CALL insert_user(%s, %s, %s)", (name, surname, number_value))
    print('Added successfully!')
    config.commit()

except (Exception, Error) as error:
    print("ERROR PostgreSQL:", error)

finally:
    if config:
        current.close()
        config.close()