# import schedule
# import time
#
#
# # Function to display the reminder
# def show_reminder(message):
#     print(f"Reminder: {message}")
#     # Optionally add functionalities like displaying pop-ups or using TTS
#
#
# # User enters the reminder details
# message = input("Enter your reminder: ")
# # You can add functionalities to input time and other details
#
# # Schedule the reminder (replace 10 with desired delay in seconds)
# schedule.every(10).seconds.do(show_reminder, message)
#
# # Keep the program running to check for scheduled tasks
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# Practicing MySQL to create a database and store the data into it.

# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     port="3306",
#     user="root",
#     passwd="diwakar7231236",
#     database="testdb"
# )
#
# myCursor = mydb.cursor()

# myCursor.execute("create database testdb")

# for db in myCursor:
#     print(db)

# myCursor.execute("Create table students(name varchar(50), age integer(10))")
#
# myCursor.execute("show tables")
#
# for table in myCursor:
#     print(table)

# sqlFormula = "insert into students(name, age) values(%s, %s)"
# student1 = ("Diwakar", 20)
#
# myCursor.execute(sqlFormula, student1)
#
# mydb.commit()

# sqlFormula = "insert into students(name, age) values(%s, %s)"
# students = [("Khushi", 20),
#             ("Aviral", 22),
#             ("Aditya", 23),
#             ("Rohan", 17)]
#
# myCursor.executemany(sqlFormula, students)
#
# mydb.commit()

# myCursor.execute("select * from students")
#
# myResult = myCursor.fetchall()
#
# for row in myResult:
#     print(row)

# This is more secure way to use mysql with parameters and taking the input using %s instead of directly accessing
# from the formula
# sql = "select * from students where name = %s"
#
# myCursor.execute(sql, ("Diwakar", ))
#
# myResult = myCursor.fetchall()
#
# for row in myResult:
#     print(row)


