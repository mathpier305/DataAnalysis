import sqlite3

def create_table():
    conn =sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cur.execute("INSERT INTO  store VALUES ('Wine Glass', 8, 10.5)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn =sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO  store VALUES (?,?,?)", (item,quantity, price))
    conn.commit()
    conn.close()

insert("Coffe Cup ", 6, 2)

def view():
    conn=sqlite3.connect("lite.db")
    curr=conn.cursor()
    curr.execute("SELECT * FROM store")
    rows=curr.fetchall()
    conn.close
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    curr=conn.cursor()
    curr.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close

def update(quatity, price, item):
    conn=sqlite3.connect("lite.db")
    curr=conn.cursor()
    curr.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quatity, price, item))
    conn.commit()
    conn.close

update(11, 6, "Water Glass ")
delete("Coffe Cup ")
print(view())
