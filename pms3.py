from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()   #implementing window layout

#implementing background
root.configure(background="#e1d8b2")

#implementing style
st=ttk.Style()
st.theme_use('classic')

#implementing title
root.title("Cancel Order")

#implementing label5
ttk.Label(root,text="Name:").grid(row=11,column=2,padx=10,pady=10)
entry5=ttk.Entry(root,width=30,font=('Arial',10))
entry5.grid(row=11,column=3,padx=10,pady=10)

#implementing label6
ttk.Label(root,text="Order ID:").grid(row=12,column=2,padx=10,pady=10)
entry6=ttk.Entry(root,width=30,font=('Arial',10))
entry6.grid(row=12,column=3,padx=10,pady=10)

#implementing button
bu5=ttk.Button(root,text="Cancel now")
bu5.grid(row=13,column=3)

#implementing button event
def buclick3():
    if (entry5.get() == '' and entry6.get() ==''):
        messagebox.showinfo(title="Order Status", message="Please fill all the details!!")
    else:
        messagebox.showinfo(title="Order Status", message="Order Cancelled successfully!!")

#accessing button
bu5.config(command=buclick3)

root.mainloop()