import os 

# ---------- CREATES NEW FILE ----------
def create_file(filename):
    try:
        with open(filename , 'x') as file:
            print(f"{filename} is created successfully !...")
    except FileExistsError:
        print(f"{filename} is already Exits")

    except Exception as e:
        print("Some Error occured in creating file")



# ---------- SHOWS ALL FILES ----------
def view_all_files():
    files = os.listdir()
    if not files:
        print("No File Found!...")
    else:
        print("Files in  directory...")
        for file in files:
            print(file) 



# ---------- DELETE FIEL ----------
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Some error occured in deleting file")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}:\n {content}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist !...")
    
    except Exception as e:
        print("Some Error occured in reading files")



# ---------- EDIT CONTENT OF FILE ----------
def edit_file(filename):
    try:
        with open(filename , 'a') as file:
            content = input("Enter some data to add: ")
            file.write(content +"\n")
            print(f"Content added to {filename} successfully !")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print("Some error occured to editing file")



# ---------- MAIN FUNCTION ----------
def main():
    while True:
        print("\nFILE MANAGEMENT APP\n\n")
        print("1.Create New File\n2.view new file\n3.delet file\n4.read file\n5.edit file\n6.exit\n")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            filename = input("Enter the File name to create: ")            
            create_file(filename)
        elif choice == 2:
            view_all_files()
        elif choice == 3:
            filename = input("Enter the name of file you want to delet: ")
            delete_file(filename)
        elif choice == 4:
            filename = input("Enter file name of file you want to read: ")
            read_file(filename)
        elif choice == 5:
            filename = input("Enter file name of file you want to edit: ")
            edit_file(filename)            
        elif choice == 6:
            print("closing the file")
            break
        else:
            print("Wrong choice")


# ---------- RUNS MAIN FUNCTION ----------
if __name__ == "__main__":
    main()
