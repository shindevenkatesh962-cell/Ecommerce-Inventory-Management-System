import database
from coustmer import coustmer
from Products import Products
from sales import sales

def main_menu():
    while True:
        print("1. Coustmer Management")
        print("2. Products Management")
        print("3. Sales Management")
        print("0. Exit")
        choice = input("Enter your selection: ")
        if choice == '1':
            coustmer.coustmer_menu()
        elif choice == '2':
            Products.Products_menu()
        elif choice == '3':
            sales.sales_menu()
        elif choice == '0':
            print("Exiting Application......")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()
    
