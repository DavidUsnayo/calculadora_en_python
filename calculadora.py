from tkinter import *

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("400x400")

vent = Frame(ventana,bg="#52d6fe")
vent.pack()

def numero(num):
    entrada.insert(END,num)  
    print(num)

def resultado():
    dato = entrada.get()
    entrada.delete(0,END)
    entrada.insert(0,eval(dato))

def limpiar():
    entrada.delete(0,END)

entrada = Entry(vent, justify="right", font=("arial",15))
entrada.grid(row=0, column=0, columnspan=3, pady=10, ipady=10)

btn1 = Button(vent, text="1", font=("arial",20), command=lambda: numero(1))
btn1.grid(row=1, column=0, pady=2, padx=2, ipadx=5)

btn2 = Button(vent, text="2", font=("arial",20), command=lambda: numero(2))
btn2.grid(row=1, column=1, pady=2, padx=2, ipadx=5)

btn3 = Button(vent, text="3", font=("arial",20), command=lambda: numero(3))
btn3.grid(row=1, column=2, pady=2, padx=2, ipadx=5)


btn4 = Button(vent, text="4", font=("arial",20), command=lambda: numero(4))
btn4.grid(row=2, column=0, pady=2, padx=2, ipadx=5)

btn5 = Button(vent, text="5", font=("arial",20), command=lambda: numero(5))
btn5.grid(row=2, column=1, pady=2, padx=2, ipadx=5)

btn6 = Button(vent, text="6", font=("arial",20), command=lambda: numero(6))
btn6.grid(row=2, column=2, pady=2, padx=2, ipadx=5)


btn7 = Button(vent, text="7", font=("arial",20), command=lambda: numero(7))
btn7.grid(row=3, column=0, pady=2, padx=2, ipadx=5)

btn8 = Button(vent, text="8", font=("arial",20), command=lambda: numero(8))
btn8.grid(row=3, column=1, pady=2, padx=2, ipadx=5)

btn9 = Button(vent, text="9", font=("arial",20), command=lambda: numero(9))
btn9.grid(row=3, column=2, pady=2, padx=2, ipadx=5)


sum = Button(vent, text="+", font=("arial",20), command=lambda: numero("+"))
sum.grid(row=4, column=0, pady=2, padx=2, ipadx=5)

resta = Button(vent, text="-", font=("arial",20), command=lambda: numero("-"))
resta.grid(row=4, column=1, pady=2, padx=2, ipadx=5)

multi = Button(vent, text="*", font=("arial",20), command=lambda: numero("*"))
multi.grid(row=4, column=2, pady=2, padx=2, ipadx=5)


igual = Button(vent, text="=", font=("arial",20), width=8, command=resultado)
igual.grid(row=5, column=1, columnspan=2, pady=2, padx=2, ipadx=5)

borrar = Button(vent, text="C", font=("arial",20), command=limpiar)
borrar.grid(row=5, column=0, pady=2, padx=2, ipadx=5)
vent.mainloop()