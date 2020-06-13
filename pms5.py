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
root.title("Vendor")

#implementing buttons
bu7=ttk.Button(root,text="New Pizza Order")
bu7.grid(row=17,column=3,padx=20,pady=20)
bu8=ttk.Button(root,text='Cancelled Order')
bu8.grid(row=17,column=4,padx=20,pady=20)
bu9=ttk.Button(root,text='Served Order')
bu9.grid(row=18,column=3,padx=20,pady=20)
bu10=ttk.Button(root,text='Pending Order')
bu10.grid(row=18,column=4,padx=20,pady=20)

root.mainloop()