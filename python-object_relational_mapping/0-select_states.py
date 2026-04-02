  #!/usr/bin/python3
import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connections
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
