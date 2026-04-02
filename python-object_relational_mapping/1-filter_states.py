
  #!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    mySQL_u = sys.argv[1]
    mySQL_p = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mySQL_u,
        passwd=mySQL_p,
        db=db_name
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
```

**Fix 2: If the script should list ALL states but the output format is wrong**, the issue might be that the expected format uses `(id, 'Name')` — which Python tuples already do, so double-check the expected output doesn't want plain text like:
```
1: California
