from tkinter import *
from functions import *
from sql import *

### Start up ###
conn = create_connection("./data.db")

Execute_Query(conn, CreateTableAutorid)
Execute_Query(conn, CreateTableZanrid)
Execute_Query(conn, CreateTableRaamatud)

date = Execute_Query_Read(conn,'select * from Autorid;')    
if (not date):
    Execute_Query(conn, CreateDateTestAutorid)
    Execute_Query(conn, CreateDateTestZanrid)
    Execute_Query(conn, CreateDateTestRaamatud)


MaxW1 = 7
MaxH1 = 1

MaxW2 = 20
MaxH = 9

gui = Tk()


Menu = Button(gui,text = 'Menu',bg="white",font="Arial 24",width=MaxW1, height=MaxH1, borderwidth=4, relief="solid")
Menu.grid(row=0,column=0)
Add = Button(gui,text = 'Add',bg="white",font="Arial 24",width=MaxW1,height=MaxH1,borderwidth=4, relief="solid")
Add.grid(row=1,column=0)
Change = Button(gui,text = 'Change',bg="white",font="Arial 24",width=MaxW1,height=MaxH1, borderwidth=4, relief="solid")
Change.grid(row=2,column=0)
Delete = Button(gui,text = 'Delete',bg="white",font="Arial 24",width=MaxW1,height=MaxH1, borderwidth=4, relief="solid")
Delete.grid(row=3,column=0)
Leave = Button(gui,text = 'Exit',bg="white",font="Arial 24",width=MaxW1,height=MaxH1, borderwidth=4, relief="solid",command=lambda: gui.quit())
Leave.grid(row=4,column=0)


Label1 = Label(gui, bg="white",font="Arial 24",width=MaxW2, height=MaxH, borderwidth=4, relief="solid") 
Label1.grid(row=0, column=1, rowspan=5)
gui.mainloop()
