from tkinter import *
from tkinter import messagebox
def exi(w1):
	w1.destroy()
	quit()


def show(w1,w2):
	w1.update()
	w1.deiconify()
	w2.destroy()
	
def dis(e1,n):
	print(n)
	''''n=str(n)
	print(n)
	z=open(e1,"w")
	z.write(n)
	z.close()
	print(n)'''
	

def pro(e1):
	try:
		a=e1.get("1.0","end-1c")
		e1.delete('1.0', END)
		f=open(a,"r")
		s=f.read()
		s=s.split('\n')
		for x in s:
			x=str(x)
			x=x.split(',')
			n.append(x)
		f.close()
		messagebox.showinfo("MSG","YOO,YOU DID SUCESSFULLY")
	except:
		e1.delete('1.0', END)
		messagebox.showinfo("ERROR", "FILE NOT FOUND OR PATH NAME ERROR")	
	
	
def main(w1):

	w2=Tk()
	w2.configure(background="#7E847F")
	w2.title("CSV TO JASON CONVERTER")
	w2.geometry("700x350+160+70")

	l1=Label(w2,text="ENTER THE FULL PATH OF THE CSV FILE",height=1,width=50,fg="#3510EF",bg="#27E253")
	l1.pack()
	l1.place(x=200,y=20)


	e1=Text(w2,height=1,width=45,font=("ubuntu",15))
	e1.pack()
	e1.place(x=130,y=75)

	
	
	b2=Button(w2,text="CONVERT",height=3,width=20,bg="#4DEBCB",command=lambda: pro(e1))
	b2.pack()
	b2.place(x=430,y=150)

	z=""
	b3=Button(w2,text="SHOW",height=3,width=20,bg="#4DEBCB",command=lambda : dis(e1,n))
	b3.pack()
	b3.place(x=150,y=150)
	
	b4=Button(w2,text="BACK",height=1,width=20,bg="#4DEBCB",command=lambda:show(w1,w2))
	b4.pack()
	b4.place(x=10,y=10)
	
	b4=Button(w2,text="QUIT",height=3,width=20,bg="#4DEBCB",command=lambda:exi(w1))
	b4.pack()
	b4.place(x=290,y=250)
	
	
	
	w2.mainloop()
n=[]

def kane(w1):
	w1.withdraw()
	main(w1)