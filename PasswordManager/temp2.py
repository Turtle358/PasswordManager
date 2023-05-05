import sqlite3
conn = sqlite3.connect("Logins.db")
c = conn.cursor()
c.execute("SELECT *,oid FROM LoginPassword")
records = c.fetchall()
c.close()
print_records = ""
for record in records:
    print_records += "Website: " + str(record[0]) + "\nUsername:" + str(record[1])
    print(print_records)
