import sqlite3


def main():

    conn = sqlite3.connect('..//test.db')
    print("Opened database successfully")
    print()
    
    cursor = conn.execute("SELECT id, name, address, salary  FROM COMPANY")
    for row in cursor:
        print("ID = %d" % row[0])
        print("NAME = %s" % row[1])
        print("ADDRESS = %s" % row[2])
        print("SALARY = %f" % row[3])
        print()

    cursor = conn.execute("SELECT * FROM COMPANY WHERE AGE = 25")
    for row in cursor:
        print("ID = %d" % row[0])
        print("NAME = %s" % row[1])
        print("Age = %d" % row[2])
        print("ADDRESS = %s" % row[3])
        print("SALARY = %f" % row[4])
        print()

    print("Operation done successfully")

    conn.close()

if __name__ == "__main__":
    main()
