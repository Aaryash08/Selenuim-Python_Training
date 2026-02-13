import mysql.connector
host="localhost"
user="root"
password="qwertyui"
database="wipro_nga"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("Connected to the database successfully")
# query="select * from employee"
query="insert into `employee`(`Employee no`,`Employee name`,`Salary`) values('4','yali','80000');"

cursor.execute(query)

result=cursor.fetchall()
for row in result:
    print(row)
