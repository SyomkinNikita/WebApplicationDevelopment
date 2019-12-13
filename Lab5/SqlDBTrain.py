import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="12345",
    db="first_db"
)

c = db.cursor()

# c.execute("INSERT INTO books (name, description) VALUES (%s, %s);", ('Книга', 'Описание книги'))


# db.commit()

c.execute("SELECT * FROM books;")

entries = c.fetchall()

for e in entries:
    print(e)

c.close()
db.close()
