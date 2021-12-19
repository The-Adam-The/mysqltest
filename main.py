import mysql.connector


#Connect to DB
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="testdatabase"
)
#create cursor object
my_cursor = db.cursor()

#Create the database
# my_cursor.execute("CREATE DATABASE testdatabase")

#create table
my_cursor.execute("CREATE TABLE PERSON (name VARCHAR(20), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")


#Describe created database
# my_cursor.execute("DESCRIBE Person")
# for x in my_cursor:
#     print(x)

#insert data in into DB
# my_cursor.execute("INSERT INTO Person (name, age) VALUES(%s,%s)", ("Joe", 22))
# db.commit()


#View data in DB
my_cursor.execute("SELECT * FROM Person")

for x in my_cursor:
    print(x)