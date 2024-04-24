import psycopg2
def find(pattern):
    config = psycopg2.connect(
        host = 'localhost',
        database='phonebook',
        user='postgres',
        password='1123'
    )

    current = config.cursor()
    sql = '''
        SELECT * FROM phone_number WHERE name LIKE %s OR surname LIKE %s OR number_value LIKE %s

    '''
    current.execute(sql, (pattern,  pattern, pattern))
    record = current.fetchall()#іздеген нәрсені тюпл ретінде қайтарады
    if record:
        for i in record:
            print(i)
    else:
        print('Data not found! :(')

pattern = input('What do you want to find?: ')
find(pattern)