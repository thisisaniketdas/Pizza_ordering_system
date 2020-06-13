from tkinter import *
from tkinter import ttk
#
#also you have to right click the file left side and got to mark directory as source root
from pmsdatabasecontrol import PMS #here DBC is the class name in DBConnectMain_Control Python file
#implementing class
class ListTickets:
    def __init__(self):
        self._DBConnect=DBC()  #creating instance of class to invoke the functions in DBConnectMain_Control Python file
        self._root=Tk()
        tv=ttk.Treeview(self._root)
        tv.pack()
#giving heading in first column '#0'
        tv.heading('#0',text="ID")
#creating column in treeview
        tv.configure(column=('Name','Gender','Comments'))
#giving heading on further treeview columns
        tv.heading('Name', text="Name")
        tv.heading('Gender', text="Gender")
        tv.heading('Comments', text="Comments")
        display=self._DBConnect.listdata()
        for row in display:
            tv.insert('','end','#{}'.format(row["ID"]),text=row["ID"])
            tv.set('#{}'.format(row["ID"],'Name',row["Name"]))
            tv.set('#{}'.format(row["ID"],'Gender',row["Gender"]))
            tv.set('#{}'.format(row["ID"],'Comments',row["Comments"]))
            #print("ID: {}, Name: {}, Gender: {}, Comments: {}".format(row["ID"], row["Name"], row["Gender"], row["Comments"]))
#showing as it is listing all the data of the databases
        self._root.mainloop()