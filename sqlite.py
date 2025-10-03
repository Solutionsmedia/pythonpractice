import sqlite3
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               id INTEGER KEY AUTOINCREAMENT,
               name TEXT,
               email TEXT
               );
               ''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products(
               id INTEGER KEY AUTOINCREAMENT,
               name TEXT,
               stock INTEGER
               );
               ''')
conn.close
print("Database created successfully")


def populatedb():
    users = [
        ("Saviour Daniels", "daniels@gmail.com"),
        ("Akanbi Nausru", "nausuru@gmail.com"),
        ("Jonh Doe", "john@gmail.com")
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO users(name, email) VALUES (?, ?)", users)

    print("Database populated successfully")


def cheap_product():
    cursor.execute()


print("populating DB")
populatedb()
