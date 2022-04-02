from tkinter import*
import pygame.mixer
from tkinter.messagebox import askokcancel 
from tkinter import filedialog as fd



app = Tk()
app.title("Orquestra - Reprodutor musical")
app.geometry("500x500")
app.resizable(False ,False)
app.config(bg = "black")

title = Label(app, text= "Orquestra", font = "Arial 17 bold", bg="black", fg="#f29305").pack()

mixer = pygame.mixer
mixer.init()



filetypes = (("Music Files", ".mp3"),)
f = fd.askopenfile(filetypes = filetypes)
sound_e = f
track = mixer.Sound(sound_e)
track.play(loops = -1)

def abrir():
	global  track
	global filetypes
	global sound_e
	
	




#sound_ e="AUD-20220211-WA0038.mp3"


#Label(app, height= 5, bg = "black").pack()
#abrir = Button(app, text = "Escolher Music", font = "Arial 9 bold", bg = "#f29305", fg = "black", height=1, width= 14, command = abrir)
#abrir.pack()

Label(app, height= 1, bg = "black").pack()


play = Button(app, text = " Play ▶️", bg = "#f29305", fg="black", height=1, width= 14, font= "Arial 9 bold", command = abrir)
play.pack()

def parar():
	global abrir
	track.stop()

def shutdown():
	if askokcancel(title= "Tem certeza?", message = "Você realmente quer sair?"):
		app.destroy()

parar = Button(app, text = "Pause ⏸ ", bg = "#f29305", fg="black", height=1, width= 14, font= "Arial 9 bold", command= parar).pack()

app.protocol("WM_DELETE_WINDOW", shutdown)


Label(app, height= 3, bg = "black").pack()

def change_volume(v):
	track.set_volume(volume.get())

volume = DoubleVar()
volume_scale = Scale(app, variable = volume, from_ = 0.0 , to = 1.0 , resolution = 0.1, label= "Volume", orient = HORIZONTAL, command = change_volume, background = "#f29305" , fg = "black", font= "Arial 7 bold")
volume_scale.pack()

Label(app, text="Desenvolvido por Daniel Gomes 2021", bg="black", font = "Arial 5", fg= "#f29305", height=51).pack()

app.mainloop()