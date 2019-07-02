import tkinter
import tkinter.messagebox
from tkinter import * 
import cv2
import os

top = tkinter.Tk()
top.title("Image Format Convert v1.0")
top.geometry("300x180+1000+500")

L1 = Label(top, text="Origin Image Path：").grid(row=0,column=0)
origin_path = Entry(top, bd =2)
origin_path.grid(row=0,column=1,padx=0,pady=10)

L2 = Label(top, text="Output Image Path：").grid(row=1,column=0)
output_path = Entry(top, bd =2)
output_path.grid(row=1,column=1,padx=0,pady=10)

L3 = Label(top, text="Output Format    ：").grid(row=2,column=0, sticky=W)
out_format = Entry(top, bd =2)
out_format.grid(row=2,column=1,padx=0,pady=10)

def Start():
    print(origin_path.get())
    print(output_path.get())
    print(out_format.get())

    origin = origin_path.get()
    output = output_path.get()
    img_format = out_format.get()
    
    i = 0
    for f in os.listdir(origin):
        f_name = f.split('.')[0]
        im = cv2.imread(origin + '/' + f)
        cv2.imwrite(output + '/' + f_name + '.' + img_format, im)
        i += 1
    
    tkinter.messagebox.showinfo('Success', '%d Images have been converted!' % i)

bt = Button(top, text="Convert", command=Start, width=10).grid(row=3, column=1, sticky=E)

top.mainloop()
