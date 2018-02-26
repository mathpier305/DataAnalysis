from tkinter import *

window= Tk()

def kg_to_measurements():
    g = float(e1_value.get()) * 1000
    t2.insert(END, g)
    p = float(e1_value.get()) * 2.20462
    t3.insert(END, p)
    o = float(e1_value.get()) * 35.274
    t4.insert(END,o )



t1=Label(window, text="Kg")
t1.grid(row=0, column=0)
t2=Text(window, height=1,width=20)
t2.grid(row=1, column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0, column=1)
t3=Text(window, height=1, width=20)
t3.grid(row=1, column=1)

b1=Button(window, text="Convert", command=kg_to_measurements)
b1.grid(row=0, column=2)
t4=Text(window, height=1, width=20)
t4.grid(row=1, column=2)


window.mainloop()
