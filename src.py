import os
userInput = ''


def menuDisplay():
    print("TO-DO")
    print("Press 1: Create a ToDo File")
    print("Press 2: Read a ToDo File")
    print("Press 3: Update a ToDo File")
    print("Press 4: Delete a ToDo File")
    print("Press 5: View the List of Files")
    print("Press 6: Add Something to the ToDo File")
    print("Press 7: Change the Name of the ToDo File")
    print("Press 8: Exit")
    userInput = input("Enter Your Choice")
    return userInput

def menuFunctionCall(userInput):
    match userInput:
        case '1':
            userInput = '1'
            create_file()
            return 0
        case '2':
            userInput = '2'
            read_file()
            return 0
            
        case '3':
            userInput = '3'
            write_file()
            return 0
            
        case '4':
            userInput = '4'
            delete_file()
            return 0
            
        case '5':
            userInput = '5'
            view_fileList()
            return 0
            
        case '6':
            userInput = '6'
            append_file()
            return 0
         
        case '7':
            userInput = '7'
            rename_file()
            return 0
        
        case '8':
            userInput = '8'
            return 0

def create_file():
    try:
        filename = input("Enter Name of the File ")
        contents = input("Enter the contents for the file")
        with open(filename, 'w') as f:
            f.write(contents)
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)

def read_file():
    try:
        filename = input("Enter Name of the File ")
        with open(filename, 'r') as f:
            contents = f.read()
            print("Contents of the File is " +contents)
    except IOError:
        print("Error: could not read file " + filename)

def write_file():
    try:
        filename =  input("Enter the Name of the file you want ot change")
        text = input("Enter the contents of the File ")
        with open(filename, 'w') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)

def delete_file():
    filename = input("Enter the file name to be deleted")
    os.remove(filename)
    print("File " + filename + " deleted successfully.")

def view_fileList():
     total_list = os.listdir('.')
     for i in total_list:
         if '.txt' in total_list[i]:
             print(total_list[i])

def append_file():
    try:
        filename =  input("Enter the Name of the file you want ot change")
        text = input("Enter the contents of the File ")
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)

def rename_file():
    filename = input("Enter Current File Name")
    new_filename = input("Enter New File Name")
    os.rename(filename, new_filename)
    print("File "+filename+" renamed to " + new_filename + " successfully.")

if __name__ == '__main__':
	while not userInput == '8':
          userInput=menuDisplay()
          menuFunctionCall(userInput)