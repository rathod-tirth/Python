import pymysql

mydb= pymysql.connect(host="localhost", user="root", passwd="")

mycursor= mydb.cursor()

mycursor.execute("create database if not exists topspython")

mydb= pymysql.connect(host="localhost", user="root", passwd="", database="topspython")

mycursor= mydb.cursor()

mycursor.execute("create table if not exist student (id int primary key auto_increment, name varchar(20), subject varchar(20) )")

mydb.commit()