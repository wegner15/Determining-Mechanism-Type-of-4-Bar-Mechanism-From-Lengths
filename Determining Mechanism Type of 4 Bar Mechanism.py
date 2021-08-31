# -*- coding: utf-8 -*-
from tabulate import tabulate
from tkinter import *
from tkinter import ttk
fixedLink=0 
inputLink=0 
couplerLink=0
outputLink=0
window = Tk()
link_data_frame=Frame(window, bg="white")
display_frame=LabelFrame(window, text="Mechanism Type", relief=FLAT)
a1 = Text(link_data_frame, height=1, width=10)
b1 = Text(link_data_frame, height=1, width=10)
c1 = Text(link_data_frame, height=1, width=10)
d1 = Text(link_data_frame, height=1, width=10)
output = Text(display_frame, height = 8, width = 70, bg = "light cyan")


"""
fixedLink=input("Enter the length of the fixed link in (Meters):")
inputLink=input("Enter the lenght of the input link in (Meters):")
couplerLink=input("Enter the lenght of teh coupler link in (Meters):")
outputLink=input("Enter the lenght of the output Link in (Meters):")
"""
def get_link_information():
   fixedLink = a1.get("1.0", "end-1c")
   inputLink=b1.get("1.0", "end-1c")
   couplerLink=c1.get("1.0", "end-1c")
   outputLink=d1.get("1.0", "end-1c")
   print("{:<10} {:<10} {:<10} {:<10}".format(fixedLink,inputLink,couplerLink,outputLink))
   output.delete('1.0', END)
   output.insert(END,Evaluate4BarInversion(fixedLink, inputLink, couplerLink, outputLink))
   
def GUI():
    
    
    window.title("Four Bar Inversion Evaluator")
    window.geometry('700x300')
    window.configure(background = "white");
    link_data_frame.place(x=0,y=10)

    a = Label(link_data_frame ,text = "Fixed Link").grid(row = 0,column = 0,sticky=E+W+N+S)
    b = Label(link_data_frame ,text = "Input Link").grid(row = 0,column = 3,sticky=E+W+N+S)
    c = Label(link_data_frame,text = "Coupler Link").grid(row = 0,column = 5,sticky=E+W+N+S)
    d = Label(link_data_frame ,text = "Output Link").grid(row = 0,column = 7,sticky=E+W+N+S)
    a1.grid(row = 0,column = 2,sticky=E+W+N+S)
    b1.grid(row = 0,column = 4,sticky=E+W+N+S)
    c1.grid(row = 0,column = 6,sticky=E+W+N+S)
    d1.grid(row = 0,column = 8,sticky=E+W+N+S)
    
    
    
    display_frame.place(relx=0,rely=0.2)
    
    output.pack(side=TOP, expand=0)
        
    btn = Button(window ,text="EVALUATE MECHANISM",width=100,height=2,bg="dark blue",
                 activebackground="green", activeforeground="green", fg="yellow",
                     command = lambda:get_link_information()).pack(side=BOTTOM)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    
    link_data_frame.rowconfigure(0, weight=1)
    display_frame.columnconfigure(0, weight=1)
    
    window.mainloop()
    
inputs=[["Fixed Link",fixedLink],["Input Link",inputLink],["Coupler Link",couplerLink],
        ["Output Link",outputLink]]

def Evaluate4BarInversion(fixedLink, inputLink, couplerLink, outputLink):
    Type="Not Found"
    if (fixedLink<inputLink and fixedLink<couplerLink and fixedLink<outputLink):
        if (inputLink==outputLink):
            Type="Parallel double crank mechanism"
        else:
            Type="Drag Link Double crank mechanism"
    elif(inputLink<fixedLink and inputLink<couplerLink and inputLink<outputLink):
        Type="Crank Rocker Mechanism"
    elif(couplerLink<fixedLink and couplerLink<inputLink and couplerLink<outputLink):
        Type="Double Rocker Mechanism"
    elif(outputLink<fixedLink and outputLink<inputLink and outputLink<couplerLink):
        Type="Double Rocker Mechanism"
    print("The Mechanism Type is :"+Type)
    return Type

GUI()
'''print("Fixed Link: {:<8} Input Link: {:<15} Coupler Link: {:<10} Output Link: {:<10}".format(fixedLink, 
                                                                                     inputLink, 
                                                                                     couplerLink,
                                                                                     outputLink))'''

"""
for v in inputs:
    fixedLink,inputLink,couplerLink,outputLink=v
    print("{:<8} {:<15} {:<10} {:<10}".format(fixedLink, inputLink,couplerLink,outputLink))"""
