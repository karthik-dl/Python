from tkinter import*
calcy = Tk()
calcy.geometry("410x405")
calcy.title("Simple Calculator")
calcy.configure(bg="black")

equation=""

def show(value):
    global equation
    equation+=value
    entry.delete(0,END)
    entry.insert(END,equation)

def clear():
    global equation
    equation =" "
    entry.delete(0,END)
    
def claculate():
    global equation
    # result=" "
    if equation != "":
        try:
            result = eval(equation)
            entry.delete(0, END)  # Clear the entry box
            entry.insert(END, str(result))  # Display the result
            equation = str(result)
        except:
            entry.delete(0, END)
            entry.insert(END, "Error")  # Display error
            equation = ""
            
entry=Entry(calcy,font=("arial",30),bd=10,justify="right")
entry.pack(fill=BOTH,ipadx=8,padx=10,pady=10)

btn1=Button(calcy,text="C",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="green",command=lambda: clear())
btn1.place(x=10,y=100)

btn1=Button(calcy,text="/",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("/"))
btn1.place(x=110,y=100)

btn1=Button(calcy,text="%",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("%"))
btn1.place(x=210,y=100)

btn1=Button(calcy,text="*",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda: show("*"))
btn1.place(x=310,y=100)

btn1=Button(calcy,text="7",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("7"))
btn1.place(x=10,y=160)

btn1=Button(calcy,text="8",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("8"))
btn1.place(x=110,y=160)

btn1=Button(calcy,text="9",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("9"))
btn1.place(x=210,y=160)

btn1=Button(calcy,text="-",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("-"))
btn1.place(x=310,y=160)

btn1=Button(calcy,text="4",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("4"))
btn1.place(x=10,y=220)

btn1=Button(calcy,text="5",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("5"))
btn1.place(x=110,y=220)

btn1=Button(calcy,text="6",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("6"))
btn1.place(x=210,y=220)

btn1=Button(calcy,text=".",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("."))
btn1.place(x=310,y=220)

btn1=Button(calcy,text="1",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("1"))
btn1.place(x=10,y=280)

btn1=Button(calcy,text="2",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("2"))
btn1.place(x=110,y=280)

btn1=Button(calcy,text="3",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("3"))
btn1.place(x=210,y=280)

btn1=Button(calcy,text="+",width=5,height=3,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("+"))
btn1.place(x=310,y=280)


btn1=Button(calcy,text="0",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:show("0"))
btn1.place(x=210,y=340)

btn1=Button(calcy,text="=",width=11,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="blue",command=lambda:claculate())
btn1.place(x=10,y=340)
calcy.mainloop()
