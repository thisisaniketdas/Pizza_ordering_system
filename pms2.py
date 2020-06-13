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
root.title("Order Pizza")

#implementing label1
ttk.Label(root,text="Full Name:").grid(row=5,column=2,padx=10,pady=10)
entry1=ttk.Entry(root,width=30,font=('Arial',10))
entry1.grid(row=5,column=3,padx=10,pady=10)

#implementing label 2
ttk.Label(root,text="Address:").grid(row=6,column=2,padx=10,pady=10)
entry2=Text(root,height=5,font=('Arial',10),padx=10,pady=10)
entry2.grid(row=6,column=3,columnspan=2)

#implementing radiobuttons
#setting gender entry
pizzat=StringVar()
pizzat.set('small')
ttk.Label(root,text="Pizza Type:").grid(row=7,column=2,padx=10,pady=10)
ttk.Radiobutton(root,text='Small (Rs.95)',variable=pizzat,value='small').grid(row=7,column=3,padx=10,pady=10)
ttk.Radiobutton(root,text='Medium (Rs.195)',variable=pizzat,value='medium').grid(row=7,column=4,padx=10,pady=10)
ttk.Radiobutton(root,text='Large (Rs.295)',variable=pizzat,value='large').grid(row=7,column=5,padx=10,pady=10)

#implementing label 3
ttk.Label(root,text="Mobile no:").grid(row=8,column=2,padx=10,pady=10)
entry3=ttk.Entry(root,width=30,font=('Arial',10))
entry3.grid(row=8,column=3,padx=10,pady=10)

#implementing label 4
ttk.Label(root,text="Email:").grid(row=9,column=2,padx=10,pady=10)
entry4=ttk.Entry(root,width=30,font=('Arial',10))
entry4.grid(row=9,column=3,padx=20,pady=20)

#implementing button
bu4=ttk.Button(root,text="Submit")
bu4.grid(row=10,column=3)

#implementing button event
def buclick2():
    print("Full Name: {}".format(entry1.get()))
    print("Pizza type: {}".format(pizzat.get()))
    print("Mobile no: {}".format(entry3.get()))
    print("Email: {}".format(entry4.get()))

    if (entry1.get() == '' and entry2.get() =='' and entry3.get() =='' and entry4.get() ==''):
        messagebox.showinfo(title="Order Status", message="Please fill all the details!!")
    else:
        messagebox.showinfo(title="Order Status", message="Order submitted successfully!!")

#accessing button
bu4.config(command=buclick2)
root.mainloop()