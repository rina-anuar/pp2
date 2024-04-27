import psycopg2
from psycopg2 import Error
try:
    config = psycopg2.connect(
        host = 'localhost',
        database='phonebook',
        user='postgres',
        password='1123'
        )

    current = config.cursor()

    by = input('By what do u wanna change?: ')
    by = by.lower().strip()

    if by not in ['name', 'surname', 'number_value']:
        print('There are no row like this :( Try: name, surname, namber_value')
        exit()
    pattern = input('Which data do wanna change?: ')
    sql1='''
        SELECT EXISTS(SELECT 1 FROM phone_number WHERE name=%s OR  surname=%s OR  number_value=%s )
    '''
    current.execute(sql1, (pattern, pattern, pattern))
    find = current.fetchone()[0]#может вернут None, лист қайтарады 
    #find = current.fetchall()#тюпл оф лист қайтарады
    #f = find[0][0]
    #print(find)

    sql=''
    if find:
        print('Okey, we have this data')
        change = input('How change this?: ')
        if by=='number_value':
        
            sql='''
                UPDATE phone_number SET number_value = %s WHERE number_value = %s
        '''
        elif by=='name':
            sql='''
                UPDATE phone_number SET name = %s  WHERE name = %s
        '''
        elif by == 'surname':
            sql='''
                UPDATE phone_number SET surname = %s  WHERE surname = %s
        '''

        current.execute(sql, (change, pattern))
        print('Updated succssesfully!!!!')
        config.commit()
    else:
        print('Data not found! But you can insert new information')
        name = input('name: ')
        surname = input('surname: ')
        number_value = input('namber_value: ')
        current.execute("SELECT MAX(phone_number_id) FROM phone_number")
        max_id=current.fetchall()[0][0]
        cur_id=max_id+1


        sql1='''
            INSERT INTO phone_number (phone_number_id, name, surname, number_value) VALUES (%s,%s, %s, %s);
        '''
        current.execute(sql1, (cur_id, name, surname, number_value))
        print('Added succssesfully!!!!')
        config.commit()
except (Exception, Error) as error: 
        print("ERROR PostgreSQL:", error) 
        
finally: 
        if config: 
            current.close() 
            config.close()