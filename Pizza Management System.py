from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from listorders import listorders1
#accessing database class
from pmsrecord import PMS1
DBConnect=PMS1()

#implementing window layout
root=Tk()

# implementing background
root.configure(background="#800000")

#implementing style
st=ttk.Style()
st.theme_use('classic')

#implementing title
root.title("Customer")
root.geometry('1280x1280')
#implementing buttons
bu1=ttk.Button(root,text="Order Pizza")
bu1.grid(row=0,column=0,padx=20,pady=20)
ph1=PhotoImage(file="download.gif")
bu1.config(image=ph1,compound=RIGHT)
tmi=ph1.subsample(6,6)
bu1.config(image=ph1)
bu2=ttk.Button(root,text="Cancel Order")
bu2.grid(row=0,column=1,padx=20,pady=20)
ph2=PhotoImage(file="online_shop_ecommerce_shopping-46-512.gif")
bu2.config(image=ph2,compound=RIGHT)
tm2=ph1.subsample(3,3)
bu2.config(image=ph2)
bu3=ttk.Button(root,text="Track Order")
bu3.grid(row=0,column=2,padx=20,pady=20)
ph3=PhotoImage(file="download_001.gif")
bu3.config(image=ph3,compound=RIGHT)
tm3=ph3.subsample(3,3)
bu3.config(image=ph3)
#implementing place order operations
def orderpizzaevent():
    # implementing background
    root.configure(background="orange")
    # implementing style
    st = ttk.Style()
    st.theme_use('classic')

    # implementing title
    root.title("Order Pizza")
    #implementing label 0
    ttk.Label(root, text="Order ID:",font=('Arial',15)).grid(row=3, column=0, padx=10, pady=10)
    entry0 = ttk.Entry(root, width=30, font=('Arial', 10))
    entry0.grid(row=3, column=1, padx=10, pady=10)

    # implementing label1

    ttk.Label(root, text="Full Name:",font=('Arial',15)).grid(row=4, column=0, padx=10, pady=10)
    entry1 = ttk.Entry(root, width=30, font=('Arial', 10))
    entry1.grid(row=4, column=1, padx=10, pady=10)

    # implementing label 2
    ttk.Label(root, text="Address:",font=('Arial',15)).grid(row=5, column=0, padx=10, pady=10)
    entry2 = Text(root, height=5, font=('Arial', 10), padx=10, pady=10)
    entry2.grid(row=5, column=1, columnspan=2)

    # implementing radiobuttons
    # setting pizza-size entry
    pizzat = StringVar()
    pizzat.set('small')
    ttk.Label(root, text="Pizza Type:",font=('Arial',15)).grid(row=6, column=0, padx=10, pady=10)
    ttk.Radiobutton(root, text='Small (Rs.95)', variable=pizzat, value='small').grid(row=6, column=1, padx=10, pady=10)
    ttk.Radiobutton(root, text='Medium (Rs.195)', variable=pizzat, value='medium').grid(row=6, column=2, padx=10,
                                                                                        pady=10)
    ttk.Radiobutton(root, text='Large (Rs.295)', variable=pizzat, value='large').grid(row=6, column=3, padx=10, pady=10)

    # implementing label 3
    ttk.Label(root, text="Mobile no:",font=('Arial',15)).grid(row=7, column=0, padx=10, pady=10)
    entry3 = ttk.Entry(root, width=30, font=('Arial', 10))
    entry3.grid(row=7, column=1, padx=10, pady=10)

    # implementing label 4
    ttk.Label(root, text="Email:",font=('Arial',15)).grid(row=8, column=0, padx=10, pady=10)
    entry4 = ttk.Entry(root, width=30, font=('Arial', 10))
    entry4.grid(row=8, column=1, padx=20, pady=20)

    # implementing button
    bu4 = ttk.Button(root, text="Submit")
    bu4.grid(row=8, column=2)

    # implementing button event
    def buclick2():
        print("Order ID: {}".format(entry0.get()))
        print("Full Name: {}".format(entry1.get()))
        print("Address: {}".format(entry2.get(1.0, 'end')))
        print("Pizza Type: {}".format(pizzat.get()))
        # as this is text so it will print from beginning to the end of text
        print("Mobile No.: {}".format(entry3.get()))
        print("Email: {}".format(entry4.get()))
        # connecting adding operation
        msg = DBConnect.Add(entry0.get(),entry1.get(), entry2.get(1.0, 'end'),pizzat.get(),entry3.get(),entry4.get())
        messagebox.showinfo(title="Add Info", message=msg)

    bu4.configure(command=buclick2)
#implementing cancel order operations
def cancelorderevent():
    # implementing background
    root.configure(background="grey")

    # implementing style
    st = ttk.Style()
    st.theme_use('classic')

    # implementing title
    root.title("Cancel Order")

    # implementing label6
    ttk.Label(root, text="Order ID:",font=('Arial',15)).grid(row=3, column=0, padx=10, pady=10)
    entry0 = ttk.Entry(root, width=30, font=('Arial', 20))
    entry0.grid(row=3, column=1, padx=10, pady=10)

    # implementing button
    bu5 = ttk.Button(root, text="Cancel now")
    bu5.grid(row=4, column=1)

    # implementing button event
    def buclick3():
        print("Order ID: {}".format(entry0.get()))
        msg = DBConnect.deletedata(entry0.get())
        messagebox.showinfo(title="Add Info", message=msg)

    # accessing button
    bu5.config(command=buclick3)

#implementing track-order operations
def trackorderevent():
    # implementing background
    root.configure(background="yellow")

    # implementing style
    st = ttk.Style()
    st.theme_use('classic')

    # implementing title
    root.title("Track Order")

    # implementing label 7
    ttk.Label(root, text="Order ID:",font=('Arial',15)).grid(row=3, column=0, padx=10, pady=10)
    entry0 = ttk.Entry(root, width=30, font=('Arial', 20))
    entry0.grid(row=3, column=1, padx=10, pady=10)

    # implementing buttons
    bu6 = ttk.Button(root, text="Track Now")
    bu6.grid(row=4, column=1)

    # implementing buttonevent
    def buclick4():
        print("Order ID: {}".format(entry0.get()))
        if(entry0.get()==''):
            messagebox.showinfo(title="Track Status", message="Invalid Order ID!!..")
        else:
            DBConnect.trackorder(entry0.get())
            messagebox.showinfo(title="Track Status", message="Order Tracked!!")

    # accessing button
    bu6.config(command=buclick4)




#accessing order-pizza window
bu1.configure(command=orderpizzaevent)
#accessing cancel-order window
bu2.configure(command=cancelorderevent)
#accessing track-order window
bu3.configure(command=trackorderevent)


#implementing vendor's view button
bu11=ttk.Button(root,text="Vendor Window")
bu11.grid(row=2,column=1,padx=20,pady=20)

#calling vendors window
def vendorevent():
    # implementing background
    root.configure(background="#e1d8b2")

    # implementing style
    st = ttk.Style()
    st.theme_use('classic')

    # implementing title
    root.title("Vendor")

    #implementing passeword-security
    ttk.Label(root,text="Enter Password to enter admin system:",font=('Arial',15)).grid(row=3,column=0,padx=20,pady=20)
    entryforpassword=ttk.Entry(root,width=30,show='*',font=('Arial',20))
    entryforpassword.grid(row=3,column=1,padx=10,pady=10)
    bu12=ttk.Button(root,text="Login")
    bu12.grid(row=4,column=1,padx=20,pady=20)

    #defining function to perform encryption
    def passwordaccess():
        print("Enter Password to enter admin system: {}".format(entryforpassword.get()))
        if(entryforpassword.get()=='8528'):
            messagebox.showinfo(title="Order Status", message="Access Granted!!...")
            # implementing buttons
            bu7 = ttk.Button(root,width=60,text="New Pizza Orders")
            bu7.grid(row=5, column=1, padx=20, pady=20)

            entryforshowcan=ttk.Entry(root, width=50,font=('Arial', 10))
            entryforshowcan.grid(row=6,column=1)

            def ordershow():
                entryforshowcan.insert(0,"Order-List opened!!")
                Listorders = listorders1()

            bu7.config(command=ordershow)
        else:
            messagebox.showinfo(title="Order Status", message="Access Denied!!...")
    bu12.configure(command=passwordaccess)



#accessing vendor's view
bu11.configure(command=vendorevent)




root.mainloop()                     #for execution

