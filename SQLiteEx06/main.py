import sqlite3
import os


def main():

    try:
        os.remove('..//StudentInfo.db')
    except OSError:
        pass

    conn = sqlite3.connect('..//StudentInfo.db')
    print("Opened database successfully")

    cursor = conn.cursor()

    cursor.execute(" CREATE TABLE StudentInfo \
                   (ID INT PRIMARY KEY     NOT NULL, \
                    NAME           TEXT    NOT NULL, \
                    AGE            INT     NOT NULL, \
                    Score          INT     NOT NULL ); ")

    print("Table created successfully")

    studentLst1 = [1, 'Wolf',   16, 82]
    studentLst2 = [2, 'Phoebe', 16, 80]
    studentLst3 = [3, 'Aries',  17, 100]
    studentLst4 = [4, 'Ken',    16, 75]

    studentInfoLst = [studentLst1, studentLst2, studentLst3, studentLst4]

    for studentLst in studentInfoLst:
        # This is the qmark style:
        cursor.execute("insert into StudentInfo values (?, ?, ?, ?)", (studentLst[0], studentLst[1], studentLst[2], studentLst[3]))

    conn.commit()

    for studentLst in studentInfoLst:
        # And this is the named style:
        cursor.execute("SELECT * FROM StudentInfo WHERE NAME=:who", {"who": studentLst[1]})
        print(cursor.fetchone())

    cursor.close()

    conn.close()

if __name__ == "__main__":
    main()
