from tkinter import*

def somar():
	somar = int(N1.get()) + int(N2.get())
	return var.set(somar)
	
def subtrair():
	subtrair = int(N1.get()) - int(N2.get())
	return var.set(subtrair)
	
def mult():
	mult = int(N1.get()) * int(N2.get())
	return var.set(mult)
	
def div():
	div = int(N1.get()) / int(N2.get())
	return var.set(div)

app = Tk()
app.title("Calcudan")
app.geometry("600x600")
app.config(bg = "white")
app.resizable(False , False)

var = StringVar()

lb1 = Label(app, text = "CalcuDan", font="Arial 21 bold", bg="white", fg="blue")
lb1.pack()

Label(app, bg="white", height=4).pack()

lb2 = Label(app, text = "Numero 1:", font= "Arial 9", bg = "white", fg="black")
lb2.pack()

N1 = Entry(app)
N1.pack()

#button somar
bt1 = Button(app, text="+", font = "Arial 16 bold", bg="blue", fg="white", command= somar)
bt1.place(x=220, y =430)
#Fim button somae

#Button sub
bt2 = Button(app, text="-", font="arial 16 bold", bg="blue", fg="white" , command = subtrair).place(x=400, y = 430)
#Fim botao sub

#Button mult
bt3 = Button(app, text="×", font="arial 16 bold", bg="blue", fg="white", command = mult).place(x = 220, y = 560)
#Fim botao mult

#Button div
bt4 = Button(app, text=":", font="arial 16 bold", bg="blue", fg="white", command = div).place(x = 400, y = 560)
#Fim botao div

nada = Label(app, bg="white", height=8).pack()

lb3 = Label(app, text ="Numero 2:", font = "Arial 9", bg = "white", fg="black").pack()

N2 = Entry(app)
N2.pack()

Label(app, bg = "white" , height = 4).pack()

Resultado = Label(app, text = "**Seu resultado aparecerá aqui" , font= "Arial 7", textvariable = var, bg = "white", fg="blue")
Resultado.pack()

app.mainloop()