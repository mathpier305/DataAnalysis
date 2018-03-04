import psycopg2

def create_table():
    conn =psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn =psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    #ur.execute("INSERT INTO  store VALUES ('%s','%s','%s')" % (item,quantity, price))
    cur.execute("INSERT INTO  store VALUES (%s,%s,%s)", (item,quantity, price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    curr=conn.cursor()
    curr.execute("SELECT * FROM store")
    rows=curr.fetchall()
    conn.close
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    curr=conn.cursor()
    curr.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close

def update(quatity, price, item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    curr=conn.cursor()
    #curr.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quatity, price, item))
    curr.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quatity, price, item))
    conn.commit()
    conn.close

create_table()
#insert("Orange", 12, 25)
#delete("Wine Glass")
update(20, 15.0, 'Apple')
print(view())
#update(11, 6, "Water Glass ")
#delete("Coffe Cup ")
#print(view())
#insert("Coffe Cup ", 6, 2)
