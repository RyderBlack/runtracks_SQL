   
    
import os
import mysql.connector
from dotenv import load_dotenv

class Employe:
    def __init__(self):
        load_dotenv()
        PASSKEY = os.getenv('PASSKEY')
        
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=PASSKEY,
            database="entreprise"
        )
        self.cursor = self.connection.cursor()
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    # CREATE operations
    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)" # %s as placeholders to prevent sql injection attacks!
        values = (nom, prenom, salaire, id_service)
        
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error creating employee: {err}")
            return None
    
    # SHOW operations
    def get_all_employes(self):
        query = "SELECT * FROM employe"
        
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error retrieving employees: {err}")
            return []
    
    def get_employe_by_id(self, employe_id):
        query = "SELECT * FROM employe WHERE id = %s"
        
        try:
            self.cursor.execute(query, (employe_id,))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error retrieving employee: {err}")
            return None
    
    def get_employes_by_service(self, id_service):
        query = "SELECT * FROM employe WHERE id_service = %s"
        
        try:
            self.cursor.execute(query, (id_service,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error retrieving employees by service: {err}")
            return []
    
    def get_employes_by_salary_range(self, min_salary, max_salary):
        query = "SELECT * FROM employe WHERE salaire BETWEEN %s AND %s"
        
        try:
            self.cursor.execute(query, (min_salary, max_salary))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error retrieving employees by salary range: {err}")
            return []
    
    # UPDATE operations
    def update_employe(self, employe_id, nom=None, prenom=None, salaire=None, id_service=None):
    
        update_parts = []
        values = []
        
        if nom is not None:
            update_parts.append("nom = %s")
            values.append(nom)
        
        if prenom is not None:
            update_parts.append("prenom = %s")
            values.append(prenom)
        
        if salaire is not None:
            update_parts.append("salaire = %s")
            values.append(salaire)
        
        if id_service is not None:
            update_parts.append("id_service = %s")
            values.append(id_service)
        
        if not update_parts:
            return False 
        
        query = f"UPDATE employe SET {', '.join(update_parts)} WHERE id = %s"
        values.append(employe_id)
        
        try:
            self.cursor.execute(query, tuple(values))
            self.connection.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"Error updating employee: {err}")
            return False
    
    # DELETE operations
    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        
        try:
            self.cursor.execute(query, (employe_id,))
            self.connection.commit()
            return self.cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"Error deleting employee: {err}")
            return False


if __name__ == "__main__":
    employe_manager = Employe()
    
    # CREATE EMPLOYEE
    print("Creating a new employee...")
    new_id = employe_manager.create_employe("Smith", "John", 3500.75, 2)
    print(f"New employee created with ID: {new_id}")
    
    # SHOW ALL EMPLOYEES
    print("\nGetting all employees:")
    all_employes = employe_manager.get_all_employes()
    for emp in all_employes:
        print(emp)
    
    print("\nGetting employee by ID:")
    emp = employe_manager.get_employe_by_id(new_id)
    print(emp)
    
    print("\nGetting employees with salary > 3000:")
    high_salary_emps = employe_manager.get_employes_by_salary_range(3000, 10000)
    for emp in high_salary_emps:
        print(emp)
    
    # UPDATE DATA
    print("\nUpdating employee...")
    success = employe_manager.update_employe(new_id, salaire=4000.00)
    print(f"Update successful: {success}")
    
    # SHOW UPDATED DATA
    updated_emp = employe_manager.get_employe_by_id(new_id)
    print(f"Updated employee: {updated_emp}")
    
    # DELETE QUERY
    print("\nDeleting employee...")
    success = employe_manager.delete_employe(new_id)
    print(f"Delete successful: {success}")
    


    employe_manager.close()