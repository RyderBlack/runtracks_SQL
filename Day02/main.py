# import _mysql_connector
import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()

PASSKEY = os.getenv('PASSKEY')



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= PASSKEY,
    database="laplateforme"
)

if mydb.is_connected():
    db_info = mydb.get_server_info()
    print(f"Connected to MySQL version {db_info}")
    
    cursor = mydb.cursor()
    cursor.execute("use laplateforme;")
    results= cursor.fetchall()
    
    result = cursor.fetchone()
    print(results)
    print("--------------------")
    print(result)
    cursor.close()
    
    cursor = mydb.cursor()
    cursor.execute("show TABLES;")
    

    results= cursor.fetchall()
    result = cursor.fetchone()
    print(results)
    print("--------------------")
    print(result)
    cursor.close()

    cursor = mydb.cursor()
    cursor.execute("SELECT * from etudiant_main;")
    results= cursor.fetchall()
    result = cursor.fetchone()
    print(results)
    print("--------------------")
    print(result)
    cursor.close()
    
    mydb.close()