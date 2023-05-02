# Install MySQL on your computer
# hhtps://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Dilane10'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create adatabase
cursorObject.execute("CREATE DATABASE clients")

print("Database created!")