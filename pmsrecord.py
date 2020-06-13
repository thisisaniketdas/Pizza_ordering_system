#implementing database for pizza management system
import sqlite3

#implementing class
class PMS1:
    def __init__(self):
        self._db=sqlite3.connect("pms1.db")
        self._db.row_factory=sqlite3.Row
        self._db.execute("create table if not exists user_record(ID integer primary key autoincrement,Full_Name text,Address text,Pizza_Type text,Mobile_No integer,Email text)")
        self._db.commit()

    # function for adding data
    def Add(self, ID,Full_Name,Address,Pizza_Type,Mobile_No,Email):
        self._db.row_factory = sqlite3.Row
        self._db.execute("insert into user_record(ID,Full_Name,Address,Pizza_Type,Mobile_No,Email) values(?,?,?,?,?,?)", (ID,Full_Name, Address,Pizza_Type,Mobile_No,Email))
        self._db.commit()
        return ("Order added successfully!!")

    # function for listing all data
    def listdata(self):
        display = self._db.execute("select * from user_record")
        return display

    # function for deleting data
    def deletedata(self, ID):
        self._db.row_factory = sqlite3.Row
        self._db.execute("delete from user_record where ID={}".format(ID))
        self._db.commit()
        return ("Order deleted successfully!!")
    #function for tracking order event
    def trackorder(self,ID):
        display=self._db.execute("select * from user_record where ID={}".format(ID))
        for row in display:
            print("ID= {}, Full_Name= {}, Address= {},Pizza_Type= {},Mobile_No= {},Email= {}".format(row["ID"], row["Full_Name"],row["Address"],row["Pizza_Type"],row["Mobile_No"],row["Email"]))
        return display

    def showorder1(self):
        display=self._db.execute("select * from user_record")
        return display
