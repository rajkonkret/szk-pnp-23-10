# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza została podłączona")

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

except sqlite3.Error as e:
    print("błąd podczas podłączania bazy danych", e)
finally:  # wykonuje się zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
# Baza została podłączona
# Baza została zamknieta
