import os
from tkinter import *
from tkinter import messagebox

##

root = Tk()
root.geometry('800x500')
root.title('py finder')

label_1 = Label(root, text="target:")
input_target = Entry()
button = Button( root, text="find", command=lambda: click(1) )

label_results = Label(root, text="results:")
label_test = Label(root, text="test")

label_1.pack()
input_target.pack()
button.pack()
label_results.pack()

##

results = []
black_list = [".git"]

def click(event):
    global results
    results = []
    
    finder( input_target.get().lower(), os.getcwd() )
    label_test.grid_remove()
    results_str = ""
    for line in results:
        results_str += line + "\n"
    if not results:
        results_str = "nothing"
    label_test.configure(text=str(results_str))
    label_test.pack()

def finder(target, folder):
    if (target.strip() != ""):
        for element in os.scandir(folder):
            if element.is_file(): # file
                if (element.name.lower().find(target) != -1):
                    results.append("> file: "+folder+"\\"+element.name)
            else: # folder
                if (element.name.lower().find(target) != -1):
                    results.append("> folder: "+folder+"\\"+element.name)
                if (element.name not in black_list):
                    finder(target, element.path)
    else:
        results.append("empty target")

root.bind('<Return>', click)
input_target.focus_set()
root.mainloop()