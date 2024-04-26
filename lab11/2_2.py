import psycopg2 
from psycopg2 import Error 
 
def create_func(query): 
    try: 
        connection = psycopg2.connect( 
            host = 'localhost',
            database='phonebook',
            user='postgres',
            password='1123'
            )
        cursor = connection.cursor() 
        cursor.execute(query) 
        connection.commit() 
 
    except (Exception, Error) as error: 
        print("Error with PostgreSQL", error) 
    finally: 
        if connection: 
            cursor.close() 
            connection.close() 
            print('Procedure is created') 
 
postgresql_proc = """ 
CREATE OR REPLACE PROCEDURE add_user(n_id integer, n_name varchar,n_surname varchar, n_number varchar) 
AS $$  
BEGIN 
    IF EXISTS (select * from phonebook where name = n_name) THEN 
        UPDATE phonebook SET number = n_number where name = n_name;
    ELSE
        INSERT INTO phonebook Values (n_id, n_name, n_number);
END IF;
END; 
$$ 
LANGUAGE plpgsql 
""" 
create_func(postgresql_proc)