import MySQLdb

# Connect to the mysql database, run query, and print all rows.
db = MySQLdb.connect('localhost', 'root', '1234asdf', 'animalia');
cursor = db.cursor()
cursor.execute("SELECT * from animalia")
data = cursor.fetchall()

for row in data:
    print row

db.close()
