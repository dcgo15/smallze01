from tkinter import *
from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfile
import clipboard

app = Tk()
app.title("BockNext")
app.geometry("700x400")
app.configure(bg="#f7c886")
app.resizable(height=0, width=0)

#Abrir

def file():

    filetypes = (
        ("text files", "*.txt"),
        ('All files', '*.*')
    )
    f = fd.askopenfile(filetypes=filetypes)

    Titulo2.insert("1.0", f.readlines())

#Final do abrir

def Salvar():
    files = (
        ("text files", "*.txt"),
        ("All files", "*.*")
    )
    file = asksaveasfile(filetypes = files, defaultextension = files)

#Final do Salvar


meuMenu = Menu(app)
#ARQUIVOS
fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label="Abrir         CTRL+O", command= file)
fileMenu.add_command(label="Salvar       CTRL+S", command = Salvar)
meuMenu.add_cascade(label="Arquivos", menu= fileMenu)



#EDITAR
fileEdit = Menu(meuMenu, tearoff=0)
fileEdit.add_command(label="Copiar         CTRL+C")
fileEdit.add_command(label="Colar         CTRL+V")
fileEdit.add_command(label="Selecionar tudo     CTRL+A")
meuMenu.add_cascade(label="Editar", menu = fileEdit)


Titulo = Label(app, text="**Aqui fica o titulo de sua anotação depois de salvo", font="Arial 16 bold",
               fg="white", bg="#f7c886").place(x=0, y=0)

Titulo2 = Text(app, width= 100,height=47,font="Arial 9 bold", bg="white")
Titulo2.place(x= 0, y=50)

app.config(menu=meuMenu)

app.mainloop()
