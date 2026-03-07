# import os

# os.chdir("E:\my python projects\clear and cluter.py")
# a = []
# for index,files in enumerate(os.listdir()):
#     a.append(files)

# def rename_file():
#     jpg_count = 0
#     py_count = 0
#     png_count = 0
    
    
#     for index, files  in enumerate(a):
#         if files.endswith(".jpg") :
#             jpg_count+=1
#             os.rename(f"E:/practice/{files}",f"{jpg_count}.jpg")
#             print(f"Renamed: {files}  >> {jpg_count}.jpg")
#         if files.endswith(".py"):
#             py_count+=1
#             os.rename(f"E:/practice/{files}",f"{py_count}.py")
#             print(f"Renamed: {files}  >> {py_count}.py")
#         if files.endswith(".png"):
#             png_count+=1
#             os.rename(f"E:/practice/{files}",f"{png_count}.png") 
#             print(f"Renamed:{files}  >> {png_count}.png")   
        


# rename_file()
import os

os.chdir(r"\\my python projects\\clear and cluter.py")
a = os.listdir()

def file(type_file):
    i = 0
    found = False  # check karne ke liye
    for index, files in enumerate(a):
        if files.endswith(type_file):
            i += 1
            new_name = f"{i}{type_file}"   # user ke diye gaye extension ka use
            os.rename(f"E:/practice/{files}", f"E:/practice/{new_name}")
            print(f"Renamed: {files} -> {new_name}")
            found = True

    if not found:
        print(f"This folder does not contain any '{type_file}' file")    

type_file = input("Enter the type of file (e.g. .jpg , .png , .py): ")
file(type_file)        