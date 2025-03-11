import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()

PASSKEY = os.getenv('PASSKEY')



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= PASSKEY,
    database="entreprise"
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"Connected to MySQL version {db_info}")
    
    cursor = mydb.cursor()
    cursor.execute("use entreprise;")
    # cursor.execute("CREATE TABLE employe (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom varchar(255), prenom varchar(25), salaire DECIMAL(10,2), id_service INT);")

    # cursor.execute("INSERT INTO employe (nom,prenom,salaire,id_service) VALUES('Alvarez','Pedro', 1200.00, 3),('Cameron', 'James',7500.01, 1),('Roberts','Julia',2500.50, 2);")
    # mydb.commit()
    
    
    # cursor.execute("SELECT * from employe WHERE salaire > 3000;")
    # results= cursor.fetchall()
    # result = cursor.fetchone()
    # print(results)
    # print("--------------------")
    # print(result)
    
    # cursor.execute("CREATE TABLE service (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, nom varchar(255));")
    # cursor.execute("INSERT INTO service (nom) VALUES('Administration'),('Direction'),('Management');")
    # mydb.commit()
    
    cursor.execute("SELECT * from service;")
    results= cursor.fetchall()
    print(results)
    
    
    cursor.close()
    mydb.close()
 