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
   

    cursor.execute("SELECT * from etudiant_main;")
    results= cursor.fetchall()
    # result = cursor.fetchone()
    print(results)
    # print("--------------------")
    # print(result)

    # Job 03
    # cursor.execute("INSERT INTO etage (nom,numero, superficie) VALUES('RDC',0,500);")
    # mydb.commit()
    # cursor.execute("INSERT INTO etage (id,nom,numero, superficie) VALUES(2,'R+1',1,500);")
    # mydb.commit()
    
    # cursor.execute("SELECT * from etage;")
    # results = cursor.fetchall()
    # print("--------------------")
    # print(results)
    
    # cursor.execute("INSERT INTO salle (nom,id_etage, capacite) VALUES('Lounge',1,100),('Studio Son',1,5),('Broadcasting',2,50),('Bocal Peda',2,4),('Coworking',2,80),('Studio Video', 2,5) ;")
    # mydb.commit()
    # cursor.execute("SELECT * from salle;")
    # results = cursor.fetchall()
    # print("--------------------")
    # print(results)
    
    ## Job 04
    cursor.execute("SELECT nom, capacite from salle;")
    results = cursor.fetchall()
    print("--------------------")
    print(results)
    
    cursor.close()
    mydb.close()