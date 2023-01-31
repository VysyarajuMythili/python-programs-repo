import os
import shutil
def folderCreation(parent_path):
        folder_name = input("Enter the folder name= ")
        path = os.path.join(parent_path,folder_name)
        os.mkdir(path)
        print("folder created=",folder_name)
        return folder_name

def destination_path(choice,des):
    if ch.casefold() == "yes":
        dest_inp=des+ ":" 
        folder = folderCreation(dest_inp)
        dest_dir = os.path.join(dest_inp,folder)
    else:
        dest_dir = destination+":"
    return dest_dir

try:
    source = os.getcwd()
    print(f"source directory = {source}")
    files = os.listdir(source)
    print("-----------------------------------")
    print(f"List of files in the source directory= {files}")
    file_name = input("Enter the file name to copy in the current directory= ")
    source_path=os.path.join(source,file_name)
    present = False
    try:
        isFile = os.path.isfile(source_path)
        if isFile:
                print("---------------------------------------------------")
                destination  = input("Enter the drive for which you want to copy the file ?[D/E] =")
                if destination == 'D' or destination == 'd':
                    print("---------Copying to D drive--------")
                    if destination.islower():
                        destination = destination.upper()
                    ch = input("Do u want to make a folder to copy the file to the specified drive[yes/no] =")
                    dest = destination_path(ch,destination)
                    destination_path = shutil.copy(source_path,dest)
                    print(f"File copied to the destination path ={destination_path}")
                elif destination == 'E' or destination == 'e':
                    print("---------Copying to E drive--------")
                    if destination.islower():
                        destination = destination.upper()
                    ch = input("Do u want to make a folder to copy the file to the specified drive[yes/no] =")
                    dest = destination_path(ch,destination)
                    destination_path = shutil.copy(source_path,dest)
                    print(f"File copied to the destination path ={destination_path}")
        else:
            raise FileNotFoundError("File Not Found")
    except FileNotFoundError as ex:
        print(f"Exception occurred = {ex}")

except Exception as ex:
    print(f"Exception raised = {ex}")