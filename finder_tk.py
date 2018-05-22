import os
from tkinter import *
from tkinter import messagebox

black_list = [".git","node_modules"]

##

root = Tk()
root.geometry('800x500')
root.title('py finder')

label_1 = Label(root, text="target:")
input_target = Entry()
button = Button( root, text="find", command=lambda: click(1) )
scrollbar = Scrollbar(root)
listbox = Listbox(root)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

label_1.pack(fill=BOTH)
input_target.pack()
button.pack()
scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(fill=BOTH, expand=1)

##

def click(event):
    global results
    results = []
    listbox.delete(0, END)
    finder( input_target.get().lower(), os.getcwd() )
    for line in results:
        listbox.insert(END, line)
    if not results:
        listbox.insert(END, "nothing")

def finder(target, folder):
    if (target.strip() != ""):
        for element in os.scandir(folder):
            if element.is_file(): # file
                if (element.name.lower().find(target) != -1):
                    results.append("> file: "+folder+"\\"+element.name)
            else: # folder
                if (element.name not in black_list):
                    if (element.name.lower().find(target) != -1):
                        results.append("> folder: "+folder+"\\"+element.name)
                    finder(target, element.path)
    else:
        results.append("empty target")

root.bind('<Return>', click)
input_target.focus_set()
root.mainloop()