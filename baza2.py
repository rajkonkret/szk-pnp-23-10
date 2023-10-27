# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    query = '''
    CREATE TABLE IF NOT EXISTS developers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    insert = '''
    INSERT INTO developers (id, name, email, salary) VALUES (1, 'Radek', 'raj@wp.pl', 5000);
    '''

    cursor = sql_connection.cursor()
    print("Baza została podłączona")

    sql_connection.execute(query)

    sql_connection.execute(insert)

    sql_connection.commit()
    sql_connection.close()

except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych", e)
finally:  # wykonuje się zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
# Baza została podłączona
# Baza została zamknieta
