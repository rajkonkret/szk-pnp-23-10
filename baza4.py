# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza została podłączona")

    insert = '''
        INSERT INTO software (id, name, price) VALUES (1, 'Python', 100);
        '''
    # cursor.execute(insert) insert wykonujemy raz
    # sql_connection.commit()

    select = '''
    SELECT * FROM software WHERE id=1;'''

    update = '''
    UPDATE software SET price = 2000 WHERE id=1;
    '''
    # cursor.execute(update) # komentuje bo nie potrzebujemy drugi raz robic update
    # sql_connection.commit()

    delete = '''
    DELETE FROM software WHERE id=1;
    '''
    cursor.execute(delete)
    sql_connection.commit()

    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 100.0)


except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych", e)
finally:  # wykonuje się zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
# Baza została podłączona
# Baza została zamknieta
