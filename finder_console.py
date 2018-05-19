print("___________________________________________________________________")
print()

import os

##

black_list = [".git"]

while 1:
    target = input('File name: ')
    folder = os.getcwd()

    print()

    def finder(target, folder):
        for element in os.scandir(folder):
            if element.is_file(): # file
                if (element.name.lower().find(target) != -1):
                    print("> file: "+folder+"\\"+element.name)
            else: # folder
                if (element.name.lower().find(target) != -1):
                    print("> folder: "+folder+"\\"+element.name)
                if (element.name not in black_list):
                    finder(target, element.path)
    finder(target, folder)

    print()