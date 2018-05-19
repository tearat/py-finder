print("___________________________________________________________________")
print()

import os

##

target = input('File name: ')
folder = os.getcwd()

print()

def finder(target, folder):
    for element in os.scandir(folder):
        if element.is_file(): # file
            if (element.name.find(target) != -1):
                print("> file: "+folder+"\\"+element.name)
        else: # folder
            if (element.name.find(target) != -1):
                print("> folder: "+folder+"\\"+element.name)
            finder(target, element.path)
finder(target, folder)

print()