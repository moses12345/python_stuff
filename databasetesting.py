# import sqlite3

# connection=sqlite3.connect("mydatabase.db")
# print("db created successfully")
# # crsr=sqlite3.Cursor()

# sql_command="""CREATE TABLE emp(
#     staff_number INTEGER PRIMARY KEY,
#     fname VARCHAR(30),
#     lname VARCHAR(30),
#     gender CHAR(1),
#     joining DATE
# );
# """
# connection.execute(sql_command)

# sql_command="""INSERT INTO emp VALUES(1,"AAAAA","QQQ","M","2001-03-01"); """
# connection.execute(sql_command)

# # sql_command="""INSERT INTO emp VALUES(2,"qwe","rrr","M","2001-03-10"); """
# # crsr.execute(sql_command)
# connection.execute("SELECT * FROM emp")
# ans=connection.fetchall()

# connection.commit()

# connection.close()

