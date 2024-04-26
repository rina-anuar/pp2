import psycopg2
from psycopg2 import Error 
def ch():
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
            SELECT EXISTS(SELECT 1 FROM phone_number WHERE name=%s OR  surname=%s OR  number_value=%s)
        '''
        current.execute(sql1, (pattern, pattern, pattern))
        find = current.fetchone()#может вернут None i tek list qaitarady 
        #find = current.fetchall()# tuple of list qaitarady 
        #f = find[0][0]

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
            print('Data not found')

    except (Exception, Error) as error: 
        print("Ошибка с PostgreSQL:", error) 
        
    finally: 
        if config: 
            current.close() 
            config.close()
ch()