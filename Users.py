import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os


def openFolder(): 
    initial_directory = "C:/"
    filePath = filedialog.askdirectory(initialdir=initial_directory)
    textbox.insert('end', filePath)
def scanFiles():
     files = os.listdir(textbox.get("1.0",'end-1c') )
     fileCounter = 1
     for file in files:
        data=(file,fileCounter,"")
        tree.insert(parent='',index=0,values= data,)     
        fileCounter= fileCounter + 1
root = tk.Tk()

root.title("New Window")
root.geometry("800x500")

label = tk.Label(root,text="Folder Path:",font=('Arial',16),)
label.pack()
label.place(x=10,y=100)

textbox = tk.Text(root, height=1,width=20, font=('Arial',16))
textbox.pack()
textbox.place(x=130,y=100)


button = tk.Button(root, height=1, width=12, text="Browse Folder", command=openFolder, font=('Arial',12))
button.pack()
button.place(x=380,y=100)

button = tk.Button(root, height=1, width=12, text="Scan Directory", command=scanFiles, font=('Arial',12))
button.pack()
button.place(x=600,y=100)


tree = ttk.Treeview(root)
tree['columns'] = ("Excel File Name", "File Name","Keyword")
tree.column('#0',width=50,minwidth=25)
tree.column('Excel File Name',anchor='w',width=250)
tree.column('File Name',anchor='w',width=250)
tree.column('Keyword',anchor='w',width=200)

tree.heading('#0', text='No.',anchor='w')
tree.heading('Excel File Name', text='Excel File Name',anchor='w')
tree.heading('File Name', text='File Name',anchor='w')
tree.heading('Keyword', text='Keyword',anchor='w')
tree.pack()
tree.place(x=20,y=150)
# My Changes
root.mainloop()
