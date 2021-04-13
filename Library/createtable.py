import sqlite3
con = sqlite3.connect('library.db')
c = con.cursor()
# upbook = "update AddBook set BookName='Java' where BookName='java edition5'"
# c.execute(upbook)
c.execute("select * from AddBook")
a = c.fetchall()
print(a)
con.commit()

con.close()