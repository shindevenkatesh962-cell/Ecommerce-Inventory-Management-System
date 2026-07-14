import psycopg2
def connection():
    con=psycopg2.connect(
        host="localhost",
        database="ecommerce",
         user="postgres",  
         password="Venkatesh@2005",
         port="5432"
        
    )
    if con:
        print("Database connected successfully")
    else:
        print("Database connection failed")
    return con
conn=connection()