from tkinter import *
from functions import *
from sql import *

li=[["autor_id","autor_nimi","sunnikuupaev"],["zanr_id","zanr"],["raamat_id","pealkiri","valjaandmise_kuupaev","autor_id","zanr_id"]]

gui = Tk()

def clearFrame():
    # destroy all widgets from frame
    for widget in GuiScreen.winfo_children():
        widget.destroy()
    #GuiScreen.grid_forget():

#def wo():
#    Label1.config(state=NORMAL)
#    Label1.delete("1.0",END)  
#    s = PickTable()
#    s = f"select * from {s};"
#    SqlQuery=Execute_Query_Read(conn,s)
#
#    for text in SqlQuery:
#        Label1.insert(END,f"{text}\n")
#
#    Label1.config(state= DISABLED)

cells = {}
def Print_List_Of_Data(table,mode):
    clearFrame()
    cells = {}
    CBG = {}
    boola = {}
    s = f"select * from {table.get()};"
    SqlQeury=Execute_Query_Read(conn,s)
    ColumnTableHeader(table)
    r = (len(SqlQeury))
    w = (len(SqlQeury[0]))
    for x in range(r):
        for y in range(w):
            test:str = SqlQeury[x][y]
            if (mode == "dele"):
                boola[(x,0)]=IntVar()
                CB = Checkbutton(GuiScreen,onvalue=1, offvalue=0,variable=boola[(x,0)] ).grid(row=x+1,column=0)
                CBG[(x,0)] = CB

            b = Label( GuiScreen, text=test, width=15 ,height=2,bd=1,bg="#aaaaaa",relief="solid")
            b.configure(state=DISABLED)
            b.grid(row=x+1, column=y+1)
            cells[(x,y)] = b
    if (mode == "dele"):
        Button(GuiScreen, text="go", command=lambda boola=boola, CBG=CBG, table=table,cells=cells:What_To_Delete(CBG,boola,table,cells)).grid(row=r+1,column=1)
    
def What_To_Delete(CBG,boola,table,cells):
    for ga in CBG:
        #print(cells[ga]['text'])
        #print( f"{CBG[ga]} - {ga[0]+1} - {boola[ga].get()}" )
        if (boola[ga].get()==1):
            Qe = f"delete from {table.get()} where {table.get()[:-2].lower()}_id = {cells[ga]['text']}"
            #print(Qe)
            Execute_Query_Delete(conn,Qe)
    Print_List_Of_Data(table,"dele")
        
def What_table_to_use_RB(mode:str):
    clearFrame()
    Rg = StringVar() 
    R1 = Radiobutton(GuiScreen,text="Autoridi",variable=Rg,value="Autorid")
    R2 = Radiobutton(GuiScreen,text="Zanrid",variable=Rg,value="Zanrid")
    R3 = Radiobutton(GuiScreen,text="Raamatud",variable=Rg,value="Raamatud")
    if ( mode == "print" ):
        B1 = Button(GuiScreen,text="Print",command=lambda Rg=Rg:Print_List_Of_Data(Rg,"print"))
    elif (mode == "dele"):
        B1 = Button(GuiScreen,text="Print",command=lambda Rg=Rg:Print_List_Of_Data(Rg,"dele"))

    R1.grid(row=0,column=0)
    R2.grid(row=0,column=1)
    R3.grid(row=0,column=2)
    B1.grid(row=1,column=0)

def ColumnTableHeader(table): 
    la={}
    i:int
    
    if (table.get()=="Autorid"):
        i = 0
    elif ( table.get() == "Zanrid" ):
        i = 1
    elif ( table.get() == "Raamatud"):
        i = 2

    for x in range(len(li[i])):
        lable1 = Label(GuiScreen,text=(li[i][x]),width=15, height=2, bd=1,bg="#aaaaaa",relief="solid").grid(row=0,column=x+1)
        la[x] = lable1


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

MaxW2 = 24
MaxH2 = 9

Menu = Button(gui,text = 'Menu',bg="white",font="Arial 24",width=MaxW1, height=MaxH1, borderwidth=4, relief="solid",command=lambda: What_table_to_use_RB("print"))
Menu.grid(row=0,column=0)
Add = Button(gui,text = 'Add',bg="white",font="Arial 24",width=MaxW1,height=MaxH1,borderwidth=4, relief="solid",command=lambda:What_table_to_use_RB("add"))
Add.grid(row=1,column=0)
Change = Button(gui,text = 'Change',bg="white",font="Arial 24",width=MaxW1,height=MaxH1, borderwidth=4, relief="solid")
Change.grid(row=2,column=0)
Delete = Button(gui,text = 'Delete',bg="white",font="Arial 24",width=MaxW1,height=MaxH1, borderwidth=4, relief="solid",command=lambda:What_table_to_use_RB("dele"))
Delete.grid(row=3,column=0)
Leave = Button(gui,text = 'Exit',bg="white",font="Arial 24",width=MaxW1,height=MaxH1, borderwidth=4, relief="solid",command=lambda: gui.quit())
Leave.grid(row=4,column=0)
GuiScreen = Frame(gui,width=600,height=MaxH2)
GuiScreen.grid(row=0, column=1,rowspan=5)

#Label1 = Text(GuiScreen, bg="white",font="Arial 24",width=MaxW2, height=MaxH, borderwidth=4, relief="solid",state= DISABLED)
#Label1.grid(row=0, column=0)
#
#scrool = Scrollbar(GuiScreen,orient="vertical",command=Label1.yview)
#scrool.grid(row=0, column=1,sticky=N+S+W)
#
#Label1.configure(yscrollcommand=scrool.set)

gui.mainloop()
