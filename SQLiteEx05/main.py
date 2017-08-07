import sqlite3


def main():

    conn = sqlite3.connect('..//test.db')
    print("Opened database successfully")

    conn.execute("DELETE from COMPANY where ID=2;")
    conn.commit()
    print("Total number of rows deleted : %d", conn.total_changes)

    cursor = conn.execute("SELECT id, name, address, salary  FROM COMPANY")
    for row in cursor:
        print("ID = %d" % row[0])
        print("NAME = %s" % row[1])
        print("ADDRESS = %s" % row[2])
        print("SALARY = %f" % row[3])
        print()

    print("Operation done successfully")
    conn.close()

if __name__ == "__main__":
    main()
