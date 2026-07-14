from database import conn

# Coustmer class

class coustmer:
    def __init__(self):
        # self.name = name
        # self.contact= contact
        pass
        
#CREATE TABLE
    @staticmethod
    def create_table():
        cur=conn.cursor()
        cur.execute(
            
            '''CREATE TABLE IF NOT EXISTS coustmer(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                contact VARCHAR(15) NOT NULL
            )'''
        )
        conn.commit()
        cur.close() 

#INSERT into coustmer        
    @staticmethod
    def insert_coustmer(name,contact):
        cur=conn.cursor()
        cur.execute(
            '''INSERT INTO coustmer(name,contact) VALUES(%s,%s)''',
            (name,contact),
        )
        conn.commit()
        cur.close()
        
#UPDATE Coustmer
    @staticmethod
    def update_coustmer(coustmer_id,name=None,contact=None ):   
        cur=conn.cursor()
        cur.execute( "Select * FROM coustmer WHERE id =%s",(coustmer_id,) )
        coustmer=cur.fetchone() 
        if not coustmer:
            print("Coustmer not Found!")
            cur.close()
            return 
        update_filed=[]
        if name:
            update_filed.append(f"name='{name}'")
        if contact:
            update_filed.append(f"contact='{contact}'")
        update_query=f"UPDATE coustmer SET {','.join(update_filed)} WHERE id=%s"
        cur.execute(update_query,(coustmer_id,))
        conn.commit()
        cur.close()
   
   # DELETE From Coustmer
   
    @staticmethod
    def delete_coustmer(coustmer_id):
        cur=conn.cursor()
        cur.execute("DELETE FROM coustmer WHERE id=%s",(coustmer_id,))
        conn.commit()
        cur.close()
        
   # fetch all coustmers1
    @staticmethod
    def get_all_coustmer():
        cur=conn.cursor()
        cur.execute("SELECT * FROM coustmer")
        coustmers=cur.fetchall()
        cur.close()
        return coustmers
  
    # get coustmer by id
    @staticmethod
    def get_coustmer_by_id(coustmer_id):
        cur=conn.cursor()
        cur.execute("SELECT * FROM coustmer WHERE id=%s",(coustmer_id,))
        coustmer=cur.fetchone()
        cur.close()
        return coustmer
    
    # Coustmer Menu
    @staticmethod
    def coustmer_menu():
        while True:
            print("\nCoustmer Menu:")
            print("1. Create Coustmer Table")
            print("2. Insert Coustmer")
            print("3. Update Coustmer")
            print("4. Delete Coustmer")
            print("5. View All Coustmers")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                coustmer.create_table()
                print("Coustmer table created successfully.")
            elif choice == '2':
                name = input("Enter coustmer name: ")
                contact = input("Enter coustmer contact: ")
                coustmer.insert_coustmer(name, contact)
                print("Coustmer inserted successfully.")
            elif choice == '3':
                coustmer_id = (input("Enter coustmer ID to update: "))
                name = input("Enter new name (leave blank to keep unchanged): ")
                contact = input("Enter new contact (leave blank to keep unchanged): ")
                coustmer.update_coustmer(coustmer_id, name if name else None, contact if contact else None)
                print("Coustmer updated successfully.")
            elif choice == '4':
                coustmer_id = int(input("Enter coustmer ID to delete: "))
                coustmer.delete_coustmer(coustmer_id)
                print("Coustmer deleted successfully.")
            elif choice == '5':
                coustmers = coustmer.get_all_coustmer()
                for c in coustmers:
                    print(f"ID: {c[0]}, Name: {c[1]}, Contact: {c[2]}")
            elif choice == '6':
                print("Exiting Coustmer Menu.")
                break
            else:
                print("Invalid choice. Please try again.")
      
        
# coustmer().coustmer_menu()
    