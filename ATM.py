from tkinter import*
ATM=Tk()
ATM.title("ATM Project")
ATM.geometry("430x500")
ATM.config(bg="Skyblue")
  
balance=1000    
deposited_amount=0  

def submit():
    enterd_pin=pin_entry.get()
    pin_entry.delete(0,END)
    # pin_entry.insert(END)
   
    try:
        if enterd_pin == "1234":
            top=Toplevel(ATM)
            top.geometry("600x600")
            top.config(bg="skyblue")
             
            def deposit():
                """Function to handle deposit amount entry."""
                deposit_window = Toplevel(ATM)
                deposit_window.geometry("500x400")
                deposit_window.config(bg="skyblue")

                
                def add_deposit():

                    global balance  # Use the global balance variable
                    try:
                        amount = float(deposit_entry.get())
                        if amount <= 0:
                            error_text.config(text="Enter a valid deposit amount", font=("arial", 12, "bold"), fg="red", bg="skyblue")
                        else:
                            balance += amount  # Add the amount to the balance
                            deposited_amount = amount 
                            error_text.config(text=f"₹{amount} deposited successfully!", font=("arial", 12, "bold"), fg="green", bg="skyblue")
                            deposit_entry.delete(0, END)  # Clear the deposit entry field
                            balance_label.config(text=f"Current Balance: ₹{balance}")
                            deposited_label.config(text=f"Last Deposited: ₹{deposited_amount}")
                    except ValueError:
                        error_text.config(text="Enter a valid number", font=("arial", 12, "bold"), fg="red", bg="skyblue")

                    # Label and entry for deposit
                balance_label = Label(deposit_window, text=f"Current Balance: ₹{balance}", font=("arial", 12, "bold"), fg="blue", bg="skyblue")
                balance_label.pack(pady=10)

                deposit_label = Label(deposit_window, text="Enter Deposit Amount", font=("arial", 12, "bold"), fg="green", bg="skyblue")
                deposit_label.pack(pady=20)

                deposit_entry = Entry(deposit_window, font=("arial", 14), bd=5, width=20)
                deposit_entry.pack(pady=10)
                
                deposited_label = Label(deposit_window, text="Last Deposited: ₹0", font=("arial", 12, "bold"), fg="orange", bg="skyblue")
                deposited_label.pack(pady=10)
                
                deposit_error_text = Label(deposit_window, text="", font=("arial", 12, "bold"), fg="red", bg="skyblue")
                deposit_error_text.pack(pady=10)
                
                deposit_button = Button(deposit_window, text="Deposit", font=("arial", 14, "bold"), fg="white", bg="green", width=15,height=2,command=add_deposit)
                deposit_button.pack(pady=20)
                
            lbl=Label(top,text="State Bank Of India",font=("arial",14,"bold"),fg="red",bg="skyblue",justify="center")
            lbl.pack(pady=20)
            
            btn=Button(top,text="Deposit",font=("arial",14,"bold"),fg="red",bg="yellow",width=15,command=deposit)
            btn.place (x=30,y=100)
            
            btn=Button(top,text="FastCash",font=("arial",14,"bold"),fg="red",bg="yellow",width=15)
            btn.place (x=370,y=100) 
               
            btn=Button(top,text="Transfer",font=("arial",14,"bold"),fg="red",bg="yellow",width=15)
            btn.place (x=30,y=150)
                
            btn=Button(top,text="Cash Withdraw",font=("arial",14,"bold"),fg="red",bg="yellow",width=15)
            btn.place (x=370,y=150)
                
            btn=Button(top,text="Pin Change",font=("arial",14,"bold"),fg="red",bg="yellow",width=15)
            btn.place (x=30,y=200)
            
            btn=Button(top,text="Balence Enquiry",font=("arial",14,"bold"),fg="red",bg="yellow",width=15)
            btn.place (x=370,y=200) 
               
            btn=Button(top,text="Other",font=("arial",14,"bold"),fg="red",bg="yellow",width=15)
            btn.place (x=30,y=250)
                
            btn=Button(top,text="MiniStatement",font=("arial",14,"bold"),fg="red",bg="yellow",width=15)
            btn.place (x=370,y=250)          
        else:
            error_text.config(text="you enter invalid password",font=("arial",5,"bold"),fg="red",bg="yellow")
            pin_entry.delete(0,END)
            # print("invalid password")
    except Exception as e:
        print("Error:",e)

def update_entry(value):
    current_text = pin_entry.get()
    pin_entry.delete(0, END) 
    pin_entry.insert(END, current_text + value)  
        
heading=Label(ATM,text="WELCOME\nPlease Insert your Card",font=("arial",14,"bold"),fg="green",bg="skyblue")
heading.place(x=70,y=50)

pin=Label(ATM,text="Please Enter the your Secret Pin",font=("arial",10,"bold"),fg="green",bg="skyblue")
pin.place(x=90,y=120)

pin_entry=Entry(ATM,font=("arial",20),bd=5,width=25)
pin_entry.place(x=10,y=150)


btn1=Button(ATM,text="7",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("7"))
btn1.place(x=10,y=200)

btn1=Button(ATM,text="8",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("8"))
btn1.place(x=110,y=200)

btn1=Button(ATM,text="9",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("9"))
btn1.place(x=210,y=200)

btn1=Button(ATM,text="clear",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="green", command=lambda:pin_entry.delete(0, END))
btn1.place(x=310,y=200)

btn1=Button(ATM,text="4",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("4"))
btn1.place(x=10,y=270)

btn1=Button(ATM,text="5",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("5"))
btn1.place(x=110,y=270)

btn1=Button(ATM,text="6",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("6"))
btn1.place(x=210,y=270)

btn1=Button(ATM,text="confirm",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="orange",command=submit)
btn1.place(x=310,y=270)

btn1=Button(ATM,text="1",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("1"))
btn1.place(x=10,y=340)

btn1=Button(ATM,text="2",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("2"))
btn1.place(x=110,y=340)

btn1=Button(ATM,text="3",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("3"))
btn1.place(x=210,y=340)
btn1=Button(ATM,text="cancel",width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="red",)
btn1.place(x=310,y=340)

btn1=Button(ATM,text=".",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("."))
btn1.place(x=10,y=410)

btn1=Button(ATM,text="0",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("0"))
btn1.place(x=110,y=410)

btn1=Button(ATM,text="00",width=4,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="white",command=lambda:update_entry("00"))
btn1.place(x=210,y=410)
btn=Button(ATM,text="Enter",command=submit,width=5,height=1,font=("arial",20,"bold"),bd=1,fg="black",bg="red")
btn.place(x=310,y=410)

error_text = Label(ATM, text="", font=("arial", 10, "bold"), fg="red", bg="skyblue")
error_text.place(x=90, y=200)







ATM.mainloop()