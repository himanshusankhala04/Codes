from tkinter import filedialog
from tkinter import messagebox 
from tkinter import *
import tkinter as tk
import img2pdf 
from PIL import Image 
import os 

def convert(path):      
    file_name, file_extension = os.path.splitext(path)
    img_file = Image.open(path) 

    pdf_path = file_name + "_converted" + ".pdf"

    byte_file = img2pdf.convert(img_file.filename) 

    pdf_file = open(pdf_path, "wb") 
    pdf_file.write(byte_file) 

    img_file.close() 
    pdf_file.close() 

    messagebox.showinfo("showinfo", "Successfully converted") 


def sfile():
    global path
    path = filedialog.askopenfilename(initialdir='c:\desktop',title = "Select file", filetypes=(("jpeg files", "*.jpg"),("image files", "*.png *.gif *.bmp"),("all files","*.*")))
    global b1, b1
    if path != "":
        b1.configure(state=DISABLED)
        b2.configure(state=NORMAL)
    else:
        sfile()

def convertor():
    b2.configure(state=DISABLED)
    convert(path)
    b1.configure(state=NORMAL)

def close_window ():
    root.destroy()

root = tk.Tk()
path = ""

root.title("Img to PDF Convertor")
root.geometry("300x100")
b1 = tk.Button(root,text="Select file",command=sfile)
b1.pack()

b2 = tk.Button(root,text="Convert",command=convertor)
b2.configure(state=DISABLED)
b2.pack()
tk.Button (root, text = "Exit", command =close_window).pack()
root.mainloop()