import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "qwertyui",
    "database": "wipro_nga"
}
conn = None
cursor = None

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee WHERE salary > 50000")
    print("High Earners:", cursor.fetchall())

    new_emp_sql = """
            INSERT INTO employee (`Employee no`, `Employee name`, `salary`) 
            VALUES (%s, %s, %s)
        """
    cursor.execute(new_emp_sql, (5, "Alice Smith", 55000))

    update_sql = "UPDATE employee SET salary = salary * 1.10 WHERE `Employee no` = %s"
    cursor.execute(update_sql, (5,))

    conn.commit()
    print(f"Success! Rows affected: {cursor.rowcount}")

except mysql.connector.Error as err:
    print(f"Database Error: {err}")
except Exception as e:
    print(f"Other Error: {e}")
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
