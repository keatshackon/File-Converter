from tkinter import *
from tkinter import messagebox
def qui(w1):
	w1.destroy()
	quit()
	
def c(e1,e2):
	try:
		a=e1.get("1.0","end-1c")
		b=e2.get("1.0","end-1c")
		e1.delete('1.0', END)
		e2.delete('1.0', END)
		f=open(a,"w")
		f.write(b)
	
		f.close()
		messagebox.showinfo("MSG", "yoo,you did sucessfully")
	except:
		messagebox.showinfo("ERROR", "FILE NOT FOUND OR PATH NAME ERROR OR EMPTY CSV FILE")

def show(w1,w3):
	w1.update()
	w1.deiconify()
	w3.destroy()

def main(w1):

	w3=Tk()
	w3.configure(background="#7E847F")
	w3.title("CSV TO JASON CONVERTER")
	w3.geometry("700x400+300+70")

	l1=Label(w3,text="ENTER THE FULL PATH OF THE CSV FILE,WHERE U WANT TO CREATE",height=1,width=60,fg="#3510EF",bg="#27E253")
	l1.pack()
	l1.place(x=230,y=40)


	e1=Text(w3,height=1,width=45,font=("ubuntu",15))
	e1.pack()
	e1.place(x=190,y=70)
	
	b4=Button(w3,text="BACK",height=2,width=15,bg="#4DEBCB",command=lambda:show(w1,w3))
	b4.pack()
	b4.place(x=5,y=5)
	
	b5=Button(w3,text="QUIT",height=2,width=20,bg="#4DEBCB",command=lambda:qui(w1))
	b5.pack()
	b5.place(x=290,y=250)

	
	b5=Button(w3,text="CREATE",height=2,width=20,bg="#4DEBCB",command=lambda:c(e1,e2))
	b5.pack()
	b5.place(x=495,y=250)
	
	
	
	e2=Text(w3,height=10,width=20,font=("ubuntu",15))
	e2.pack()
	e2.place(x=10,y=150)
	
	
	
	l2=Label(w3,text="WRITE CSV FILE HERE",height=1,width=20,fg="#3510EF",bg="#27E253")
	l2.pack()
	l2.place(x=40,y=125)
	
	w3.mainloop()

	
def sane(w1):
	w1.withdraw()
	main(w1) 