from tkinter import*
from pytube import YouTube
from pytube.cli import on_progress

app = Tk()
app.title("YouTobe- TESTE V1.1")
app.geometry("400x600")
app.config(bg = "white")
app.resizable(width=False, height=False)

lb1 = Label(app, text = "YouTobe", font= "Arial 25 bold", fg = "red",
            bg = "white").pack()


#Area do link

def copia():
    print(link.get())
    lb["text"] = link.get()

    yt = YouTube(link.get(), on_progress_callback = on_progress)

    Ttitulo2["text"] = yts.get()

    ys = yt.streams.get_highest_resolution()

    ys.download()


lb2 = Label(app, text = "Digite o Link: ", font = "Arial 14 bold", fg="Black",
            bg = "white", height=5).pack()
link = Entry(app, width=28, font="Arial", bg="white")
link.place(x=80, y=120)

bt = Button(app, width = 29, text="Salvar", command=copia).place(x=80, y=150)
#teste lb dps apagar

Ttitulo = Label(app, text = "Titulo: ", font="Arial 16 bold", fg="red", bg="white").place(x=80, y=220)
Ttitulo2 = Label(app, text = "***O titulo ira aparecer aqui ", font="Arial 12 bold", fg="red", bg="white").place(x=80, y=250)

lb = Label(app, text="***Link do video aparece aqui depois de salvar",font="Arial 9 bold", bg="white")
lb.place(x=80, y=300)

#Fim da Area do Link

Creditos = Label(app, text = "Desenvolvido por Daniel Gomes 2022", bg="white", fg="red").place(x=80, y=580)

app.mainloop()
