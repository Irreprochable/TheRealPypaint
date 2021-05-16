from tkinter import *
from tkinter import ttk, messagebox
from turtle import *
import random

#Paramétrage de la fenêtre
window = Tk()
window.title('Pypaint')
window.geometry('992x700')
window.minsize(992,700)
window.maxsize(992,700)
window.iconbitmap('pinceau.ico')
bg = '#B8CBD0'
bg_titre = '#344D59'
bg_boutton = '#344D59'
bg_oeuvre = '#7A90A4'
window.config(bg=bg)
boucle = True

frame1 = Frame(window, bg=bg)
frame2 = Frame(window, bg=bg)

canvas = Canvas(window,width=680,height=454,bd=0,highlightthickness =0)
canvas.place(x=272,y=20)


colors = ["red","blue","lightblue","green","lightgreen","purple","yellow",
          "orange","pink","brown","grey","lightgrey","black","white"]
cbox= ttk.Combobox(frame2, values=colors)
cbox.config(font=('Helvetica',10),width=15)
cbox.set('Choisis ta couleur')
cbox.grid(row=1,column=0,pady=15)
cbox['state']= 'readonly'

tbox= ttk.Combobox(frame2, values=colors)
tbox.config(font=('Helvetica',10),width=15)
tbox.set('Choisis ta couleur')
tbox.grid(row=1,column=1,pady=15)
tbox['state']= 'readonly'

rbox= ttk.Combobox(frame2, values=colors)
rbox.config(font=('Helvetica',10),width=15)
rbox.set('Choisis ta couleur')
rbox.grid(row=1,column=2,pady=15)
rbox['state']= 'readonly'



def lecarre():
    carre = RawTurtle(canvas)
    carre.shape("square")
    carre.color(cbox.get())
    w = random.randint(2, 60)
    carre.width(w)
    carre.speed(0)
    carre.penup()
    x = random.randint(-360,360)
    y = random.randint(-247,247)
    z = random.randint(50,500)
    carre.setpos(x,y)
    carre.pendown()
    for i in range(4):
        carre.forward(z)
        carre.left(90)
    carre.penup()
    carre.setpos(700, 500)

def letriangle():
    triangle = RawTurtle(canvas)
    triangle.shape("triangle")
    triangle.color(tbox.get())
    w = random.randint(2, 60)
    triangle.width(w)
    triangle.speed(0)
    triangle.penup()
    x = random.randint(-360,360)
    y = random.randint(-247,247)
    z = random.randint(50, 500)
    triangle.setpos(x,y)
    triangle.pendown()
    for i in range(3):
        triangle.forward(z)
        triangle.left(120)
    triangle.penup()
    triangle.setpos(700, 500)

def lerond():
    rond = RawTurtle(canvas)
    rond.shape("circle")
    rond.color(rbox.get())
    w = random.randint(2,60)
    rond.width(w)
    rond.speed(0)
    rond.penup()
    x = random.randint(-360,360)
    y = random.randint(-247,247)
    z = random.randint(25,250)
    rond.setpos(x,y)
    rond.pendown()
    rond.circle(z)
    rond.penup()
    rond.setpos(700, 500)

def illustration_carre():
    carre = RawTurtle(canvas)
    carre.shape("square")
    carre.speed(8)
    carre.penup()
    carre.setpos(-200, -50)
    carre.fillcolor(cbox.get())
    carre.begin_fill()
    carre.pendown()
    for i in range(4):
        carre.forward(40)
        carre.left(90)
    carre.end_fill()
    carre.penup()
    carre.setpos(700, 500)

def illustration_triangle():
    triangle = RawTurtle(canvas)
    triangle.shape("triangle")
    triangle.speed(8)
    triangle.penup()
    triangle.setpos(0, -50)
    triangle.fillcolor(tbox.get())
    triangle.begin_fill()
    triangle.pendown()
    for i in range(3):
        triangle.forward(40)
        triangle.left(120)
    triangle.end_fill()
    triangle.penup()
    triangle.setpos(700, 500)

def illustration_rond():
    rond = RawTurtle(canvas)
    rond.shape("circle")
    rond.speed(8)
    rond.penup()
    rond.setpos(200, -50)
    rond.fillcolor(rbox.get())
    rond.begin_fill()
    rond.pendown()
    rond.circle(20)
    rond.end_fill()
    rond.penup()
    rond.setpos(700, 500)

def efface_carre():
    carre = RawTurtle(canvas)
    carre.shape("square")
    carre.speed(8)
    carre.penup()
    carre.setpos(-200, -50)
    carre.color('white')
    carre.fillcolor('white')
    carre.begin_fill()
    carre.pendown()
    for i in range(4):
        carre.forward(40)
        carre.left(90)
    carre.end_fill()
    carre.penup()
    carre.setpos(700, 500)

def efface_triangle():
    triangle = RawTurtle(canvas)
    triangle.shape("triangle")
    triangle.speed(8)
    triangle.penup()
    triangle.setpos(0, -50)
    triangle.color('white')
    triangle.fillcolor('white')
    triangle.begin_fill()
    triangle.pendown()
    for i in range(3):
        triangle.forward(40)
        triangle.left(120)
    triangle.end_fill()
    triangle.penup()
    triangle.setpos(700, 500)

def efface_rond():
    rond = RawTurtle(canvas)
    rond.shape("circle")
    rond.speed(8)
    rond.penup()
    rond.setpos(200, -50)
    rond.color('white')
    rond.fillcolor('white')
    rond.begin_fill()
    rond.pendown()
    rond.circle(20)
    rond.end_fill()
    rond.penup()
    rond.setpos(700, 500)


def execution():
    efface_carre()
    efface_triangle()
    efface_rond()
    while boucle:
        lecarre()
        letriangle()
        lerond()

def titre_oeuvre():
    global boucle
    boucle = False
    canvas_title = Canvas(window, width=680, height=50, bg=bg_oeuvre, bd=5, highlightthickness=0, relief=RAISED)
    canvas_title.place(x=267, y=474)
    plume = RawTurtle(canvas_title)
    plume.color('white')
    plume.hideturtle()
    plume.penup()
    plume.setpos(0,-15)
    global box_title
    box_title = Toplevel(window)
    box_title.title("Pypaint")
    box_title.geometry("320x150")
    box_title.iconbitmap('pinceau.ico')
    box_title.minsize(320, 150)
    box_title.maxsize(320, 150)
    box_title.config(bg=bg)
    mini_frame = Frame(box_title,bg=bg)
    ordre = Label(mini_frame, text='Mettez donc un titre à votre chef-d\'œuvre !', font =('Montserrat', 10),bg=bg,fg=bg_titre)
    ordre.grid(row=0,column=0,pady=10)
    a = StringVar()
    le_nom = Entry(mini_frame, width=30, textvariable=a,)
    le_nom.grid(row=1, column=0, pady=10)
    a.set("Le nom, la date")
    def titre():
        plume.pendown()
        plume.write(a.get(),move=False,align='center',font=('Helvetica',20,"bold"))
        canvas_title.configure(bg=bg_oeuvre)
        box_title.destroy()
    entrer = Button(mini_frame, text='Entrer',font=('Montserrat', 10),bg=bg_boutton,fg='white',command=titre)
    entrer.grid(row=2,column=0,pady=10)
    mini_frame.pack()

def exit():
    sortir = messagebox.askyesno('Exit','Voulez-vous quitter le logiciel ?')
    if sortir == True:
        window.destroy()
    else:
        pass

Title = Label(window, text='Pypaint', font =('Montserrat', 40), bg =bg,fg=bg_titre)
Title.place(x=15,y=590)

#Boutons start et stop
start_button = Button(frame1, text='Start',font=('Montserrat',20),bg =bg_boutton,fg='white',command=execution)
start_button.grid(row=0,column=0,padx=1,pady=10,ipadx=10)
stop_button = Button(frame1, text='Stop',font=('Montserrat',20),bg =bg_boutton,fg='white',command=titre_oeuvre)
stop_button.grid(row=1,column=0,padx=1,pady=10,ipadx=11)
exit_button = Button(window, text='Exit',font=('Montserrat',20),bg='white',fg=bg_boutton,command=exit)
exit_button.place(x=90,y=360,width=67)

###

#Boutons carré,triangle et rond
carre_button = Button(frame2, text='C',font=('Montserrat',20),bg =bg_boutton,fg='white',command=illustration_carre)
carre_button.grid(row=0,column=0,ipadx=8)
triangle_button = Button(frame2, text='T',font=('Montserrat',20),bg =bg_boutton,fg='white',command=illustration_triangle)
triangle_button.grid(row=0,column=1,ipadx=9,padx=100)
rond_button = Button(frame2, text='R',font=('Montserrat',20),bg =bg_boutton,fg='white',command=illustration_rond)
rond_button.grid(row=0,column=2,ipadx=8)
###

frame1.place(x=65,y=100)
frame2.place(x=362,y=560)


window.mainloop()

