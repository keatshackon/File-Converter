from tkinter import *
from  converte import kane
from cre import sane


w1=Tk()
w1.configure(background="#7E847F")
w1.title("CSV TO JASON CONVERTER")
w1.geometry("500x300+400+70")


l1=Label(w1,text="WELCOME TO KEATS'S WORLD",height=2,width=40,fg="#150401",bg="#9AD2C7")
l1.pack()
l1.place(x=120,y=20)


b2=Button(w1,text="CREATE CSV FILE",height=4,width=20,bg="#4DEBCB",command=lambda:sane(w1))
b2.pack()
b2.place(x=90,y=110)

b2=Button(w1,text="CONVERT CSV FILE",height=4,width=20,bg="#4DEBCB",command=lambda:kane(w1))
b2.pack()
b2.place(x=300,y=110)



w1.mainloop()