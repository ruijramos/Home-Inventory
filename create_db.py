import sqlite3 as lite

# Connection to the database.
con = lite.connect('home_inventory.db')

# Table creation.
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Inventory(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, local TEXT, description TEXT, brand TEXT, purchase_date DATE, purchase_price DECIMAL, serie_id TEXT)")