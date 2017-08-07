import sqlite3
import os


def main():

    try:
        os.remove('..//test.db')
    except OSError:
        pass

    conn = sqlite3.connect('..//test.db')
    print("Opened database successfully")

    cursor = conn.cursor()

    cursor.execute(" CREATE TABLE COMPANY \
                   (ID INT PRIMARY KEY     NOT NULL, \
                    NAME           TEXT    NOT NULL, \
                    AGE            INT     NOT NULL, \
                    ADDRESS        CHAR(50), \
                    SALARY         REAL); ")

    print("Table created successfully")

    cursor.close()

    conn.close()

if __name__ == "__main__":
    main()
