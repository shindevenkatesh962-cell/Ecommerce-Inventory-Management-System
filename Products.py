from database import conn

# Product class

class Products:
    def __init__(self):
        # self.name = name
        # self.contact= contact
        pass
        
#CREATE TABLE
    @staticmethod
    def create_table():
        cur=conn.cursor()
        cur.execute(
            
            '''CREATE TABLE IF NOT EXISTS Products(
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                quantity INT NOT NULL
            )'''
        )
        conn.commit()
        cur.close() 

#INSERT into Products        
    @staticmethod
    def insert_product(name,description, price, quantity):
        cur=conn.cursor()
        cur.execute(
            '''INSERT INTO Products(name,description, price, quantity) VALUES(%s,%s,%s,%s)''',
            (name,description, price, quantity),
        )
        conn.commit()
        cur.close()
        
#UPDATE Products
    @staticmethod
    def update_product(product_id, name=None,description=None, price=None, quantity=None):
        cur=conn.cursor()
        cur.execute("SELECT * FROM Products WHERE id = %s", (product_id,))
        product=cur.fetchone() 
        if not product:
            print("Product not Found!")
            cur.close()
            return 
        update_filed=[]
        if name:
            update_filed.append(f"name='{name}'")
        if description:
            update_filed.append(f"description='{description}'")
        if price:
            update_filed.append(f"price={price}")
        if quantity:
            update_filed.append(f"quantity={quantity}")
        update_query=f"UPDATE Products SET {','.join(update_filed)} WHERE id=%s"
        cur.execute(update_query,(product_id,))
        conn.commit()
        cur.close()
   
   # DELETE From Products
   
    @staticmethod
    def delete_product(product_id):
        cur=conn.cursor()
        cur.execute("DELETE FROM Products WHERE id=%s",(product_id,))
        conn.commit()
        cur.close()
        
   # fetch all products
    @staticmethod
    def get_all_products():
        cur=conn.cursor()
        cur.execute("SELECT * FROM Products")
        products=cur.fetchall()
        cur.close()
        return products
    
    #fetch single product
    @staticmethod
    def get_product_by_id(product_id):
        cur=conn.cursor()
        cur.execute("SELECT * FROM Products WHERE id=%s",(product_id,))
        product=cur.fetchone()
        cur.close()
        return product
    

    # Product Menu
    @staticmethod
    def Products_menu():
        while True:
            print("\nProduct Menu:")
            print("1. Create Product Table")
            print("2. Insert Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. View All Products")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                Products.create_table()
                print("Product table created successfully.")
            elif choice == '2':
                name = input("Enter product name: ")
                description = input("Enter product description: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                Products.insert_product(name,description, price, quantity)
                print("Product inserted successfully.")
            elif choice == '3':
                product_id = int(input("Enter product ID to update: "))
                description = input("Enter new description (leave blank to keep unchanged): ")
                price = input("Enter new price (leave blank to keep unchanged): ")
                quantity = input("Enter new quantity (leave blank to keep unchanged): ")
                Products.update_product(product_id, description if description else None, float(price) if price else None, int(quantity) if quantity else None)
                print("Product updated successfully.")
            elif choice == '4':
                product_id = int(input("Enter product ID to delete: "))
                Products.delete_product(product_id)
                print("Product deleted successfully.")
            elif choice == '5':
                products = Products.get_all_products()
                for p in products:
                    print(f"ID: {p[0]}, Description: {p[1]}, Price: {p[2]}, Quantity: {p[3]}")
            elif choice == '6':
                print("Exiting Product Menu.")
                break
            else:
                print("Invalid choice. Please try again.")
      
        
# Products().product_menu()
    