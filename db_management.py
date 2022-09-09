import sqlite3 as lite
from datetime import datetime

# Connection to the database.
con = lite.connect('home_inventory.db')

# Insert data.
def insert_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Inventory (name, local, description, brand, purchase_date, purchase_price, serie_id) VALUES (?,?,?,?,?,?,?)"
        cur.execute(query, i)

# Delete data.
def delete_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Inventory WHERE id=?"
        cur.execute(query, i)

# Update data.
def update_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventory SET name=?, local=?, description=?, brand=?, purchase_date=?, purchase_price=?, serie_id=? WHERE id=?"
        cur.execute(query, i)

# See data.
def see_form():
    items_list = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventory")
        rows = cur.fetchall()
        for row in rows:
            items_list.append(row)
    return items_list