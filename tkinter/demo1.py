from cgitb import text
from tkinter import *
from turtle import left
from PIL import Image, ImageTk
from webview import WebViewException, start 
import webview



root = Tk()
root.geometry("650x650")

# *************************************Img*********************************
p1 = Image.open("icons/MicrosoftTeams-image_5.png")
image1 = p1.resize((20,20), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)

p2 = Image.open("icons/search.png")
image2 = p2.resize((20,20), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)

p3 = Image.open("icons/MicrosoftTeams-image_4.png")
image3 = p3.resize((20,20), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)

p4 = Image.open("icons/MicrosoftTeams-image_2.png")
image4 = p4.resize((20,20), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image4)

p5 = Image.open("icons/MicrosoftTeams-image_3.png")
image5 = p5.resize((20,20), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image5)

p6 = Image.open("icons/MicrosoftTeams-image_1.png")
image6 = p6.resize((20,20), Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(image6)
# *************************************topframe*********************************
topframe = Frame(root,bg="#454545", borderwidth=14)
topframe.pack(side=TOP,fill=X)

w = Label(topframe, text ='Education 3D', font = "30",bg="#454545",foreground="white" )
w.pack( padx=30,side= LEFT, anchor="w" )

inputtxt = Text(topframe,height =1,width=20,bg="#262626",foreground="white")
inputtxt.pack( side= LEFT, anchor="w")

button = Button(topframe, image=photo2,bg="white")
button.pack(side= LEFT, anchor="w")

# button = Button(topframe,height =1 ,width=5,text='Setting')
# button.pack(side= RIGHT, anchor="w")

button1 = Button(topframe, image=photo1,compound=LEFT,bg="white")
button1.pack(side= RIGHT, anchor="w")

button = Button(topframe,height =1 ,width=15,text='Import Models',bg="white")
button.pack(side= RIGHT, anchor="w",padx=30)

# ==================================================================


# ====================================================================================




# *************************************leftframe*********************************
leftframe = Frame(root,bg="#454545")
leftframe.pack(side=LEFT,fill=Y)

button1 = Button(leftframe,text='Home', image=photo4,padx=20,compound=LEFT ,foreground="black",bg="white")
button1.pack(side= TOP, anchor="w",pady=5)

button1 = Button(leftframe,text='Video', image=photo3,padx=21,compound=LEFT,foreground="black",bg="white")
button1.pack(side= TOP, anchor="w",pady=5)

button1 = Button(leftframe,text='Video', image=photo5,padx=21,compound=LEFT,foreground="black",bg="white")
button1.pack(side= TOP, anchor="w",pady=5)

button1 = Button(leftframe,text='Video', image=photo6,padx=21,compound=LEFT,foreground="black",bg="white")
button1.pack(side= TOP, anchor="w",pady=5)
# button1 = Button(leftframe,height =1 ,width=5,text='Models')
# button1.pack(side= TOP, anchor="w")




root.mainloop()
















