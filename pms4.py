from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#implementing window layout
root=Tk()

#implementing background
root.configure(background="#e1d8b2")

#implementing style
st=ttk.Style()
st.theme_use('classic')

#implementing title
root.title("Track Order")

#implementing label 7
ttk.Label(root,text="Order Id:").grid(row=14,column=2,padx=10,pady=10)
entry7=ttk.Entry(root,width=30,font=('Arial',10))
entry7.grid(row=14,column=3,padx=10,pady=10)

#implementing buttons
bu6=ttk.Button(root,text="Track Now")
bu6.grid(row=15,column=3)

#implementing buttonevent
def buclick4():
    if (entry7.get() == ''):
        messagebox.showinfo(title="Order Status", message="Please fill all the details!!")
    else:
        messagebox.showinfo(title="Order Status", message="Order Cancelled successfully!!")

# accessing button
bu6.config(command=buclick4)

root.mainloop()