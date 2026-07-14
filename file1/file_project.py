from pathlib import Path
import shutil
def create_folder():
    try:
        name=input("Please tell Your Folder name:")
        p=Path(name)
        p.mkdir()
        print("Folder Created Successfully.")
    except Exception as err:
        print(f"Sorry an error Occured as {err}")

def read_file_folder():
    p=Path("")
    items=list(p.rglob('*'))
    for i ,v in enumerate(items):
        print(f"{i+1} : {v}")


def update_floder():
    try:
        read_file_folder()
        old_name=input("please tell which folder name  do you want to update:\n ")
        p=Path(old_name)
        if p.exists() and p.is_dir():
            new_name=input("Enter the New name of yiur Folder:\n")
            new_p=Path(new_name)
            p.rename(new_p)
            print("your Folder is Renamed successfully :\n")
        else:
            print("No Such Folder Exist\n")
    except Exception as err:
        print(f"Sorry an Error Ocurred as {err}")


def delete_floder():
    try:
        read_file_folder()
        name=input("Enter the Name of the Folder which would you want to delete\n")
        p=Path(name)
        if p.exists() and p.is_dir():
            shutil.rmtree(p)
            print(f"Folder {name} is Deleted Sucessfully!\n")
        else:
            print("No Such Folder Exist\n")
    except Exception as err:
        print(f"Sorry an Error Ocurred as {err}")


def create_file():
    try:
        read_file_folder()
        name=input("Enter the name of the File Do you want to create:\n")
        p=Path(name)
        if not p.exists():
            with open(name,"w") as fs:
                data=input("Enter the Data you want to add i  your file\n")
                fs.write(data)
            print("File Created Successfully\n")
        else:
            print("File  already Exsits!!..\n")
    except Exception as err:
         print(f"Sorry an Error Ocurred as {err}")
         
def read_file():
    try:
        read_file_folder()
        name=input("Enter the Name of the File Do you wamt to read\n")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(name,'r') as fs:
                content=fs.read()
                print("Your File Content is :\n")
                print(content)
        else:
            print("File Doesn't exsits\n")
    except Exception as err:
         print(f"Sorry an Error Ocurred as {err}")


def update_file():
    try:
        read_file_folder()
        name=input("Enter the Name of the File do you want To editt\n")
        p=Path(name)
        if p.exists() and p.is_file():
            print("options")
            print("1-Renaming the File Name\n2-For appending some data to the file\n3-For Ovwer write the File Content\n")
            choice=int(input("Tell your Choice:\n"))
            if choice ==1:
                new_name=input("Enter the New name for your File\n")
                new_p=Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("your file name is changed succeassfully\n")
                else:
                    print("Sorry This name File is already exsists \n")
            if choice==2:
                with open(name,'a') as fs:
                    data=input("Enter the data you want append in your file\n")
                    fs.write(" "+ data)
                print("Data is Append successfully\n")
            if choice==3:
                with open(name,'w') as fs:
                    data=input("Enter the data you want Over write in your file\n")
                    fs.write(" "+ data)
                print("Data is changed  successfully\n")
    except Exception as err:
         print(f"Sorry an Error Ocurred as {err}")
         

def delete_file():
    try:
        read_file_folder()
        name=input("Enter the Name of the File do you want To Delete\n")
        p=Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File is deletes Successfully\n")
        else:
            print("No Such File exsists\n")
    except Exception as err:
        print(f"Sorry an Error Ocurred as {err}")

    
        

                
                
                     
while True:
    print("\toptions\t")
    print("1-Create a file\n2-Read files and folders\n3-Update the Folder\n4-Delete the Folder\n5-Create a File\n6-Read Files\n7-update Files\n8-Delete Files\n0-Exit")

    op = int(input("Enter your Option please: "))

    if op == 1:
        create_folder()

    elif op == 2:
        read_file_folder()

    elif op == 3:
        update_floder()

    elif op == 4:
        delete_floder()

    elif op == 5:
        create_file()

    elif op == 6:
        read_file()
    elif op==7:
        update_file()
    elif op==8:
        delete_file()
    elif op==0:
        break
    
