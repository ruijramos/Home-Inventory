import sqlite3

dbfile = '/home/niklas/Desktop/Stuff/StockData-IBM.db'
con = sqlite3.connect('home_inventory.db')
cur = con.cursor()

table_list = [a for a in cur.execute("SELECT * FROM Inventory")]
print(table_list)

con.close()