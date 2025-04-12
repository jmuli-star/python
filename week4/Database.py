import _sqlite3
#connecting to a database

students =_sqlite3.connect("students.db")
print(students)

#cursor object => gives access. excute python commands, Bridge btweeen sql. 
cursor = students.cursor()

#create a table
# cursor.execute("""
# create table school (
#      name TEXT,
#      gender TEXT,
#      age INTEGER )              
# """)

# #PRINT OUT

# cursor.execute(""" 
#                insert into school (name,gender,age)
#                values ("Ali", "male",17)
# """)

students.commit()
print(cursor.execute("select * from school"))

# rows = cursor.fetchall()
# print(rows)

users = [("chausiku", "female", 19),
         ("Osama", "Male", 20)
         ]

cursor.executemany("""
insert into students (name,gender,age)
                   values(?,?,?)""", users)
cursor.execute("select * from wanafunzi")
rows = cursor.fetchall()
print(rows)
