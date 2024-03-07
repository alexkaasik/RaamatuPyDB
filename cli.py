from functions import *

### SQL ###
'''
CreateTable0 = "CREATE TABLE IF NOT EXISTS Autorid([]);"
CreateTable1 = "CREATE TABLE IF NOT EXISTS Zanrid([]);"
CreateTable2 = "CREATE TABLE IF NOT EXISTS Raamatud([]);"
'''

CreateTableAutorid="""
Create table IF NOT EXISTS Autorid (
autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
autor_nimi varchar(255),
sunnikuupaev date
);
"""

CreateTableZanrid="""
Create table IF NOT EXISTS Zanrid (
zanr_id INTEGER PRIMARY KEY AUTOINCREMENT,
zanr_nimi varchar(255)
);
"""

CreateTableRaamatud="""
Create table IF NOT EXISTS Raamatud (
raamat_id INTEGER PRIMARY KEY AUTOINCREMENT,
pealkiri varchar(255),
valjaandmise_kuupaev date,
autor_id INTEGER,
zanr_id INTEGER,
FOREIGN KEY(autor_id) REFERENCES Autorid(autor_id),
FOREIGN KEY(zanr_id) REFERENCES Zanrid(zanr_id)
);
"""

CreateDataTable = """
ALTER TABLE Autorid ADD COLUMN autor_id INTEGER PRIMARY KEY AUTOINCREMENT;
ALTER TABLE Autorid ADD COLUMN autor_nimi varchar(255);
ALTER TABLE Autorid ADD COLUMN sunnikuupaev date;  

ALTER TABLE Zanrid ADD COLUMN zanr_id INTEGER PRIMARY KEY AUTOINCREMENT;
ALTER TABLE Zanrid ADD COLUMN zanr_nimi varchar(255);

ALTER TABLE Raamatud ADD COLUMN raamat_id INTEGER PRIMARY KEY AUTOINCREMENT;
ALTER TABLE Raamatud ADD COLUMN pealkiri varchar(255);
ALTER TABLE Raamatud ADD COLUMN valjaandmise_kuupäev date;
ALTER TABLE Raamatud ADD COLUMN autor_id INTEGER;
ALTER TABLE Raamatud ADD COLUMN zanr_id INTEGER;
ALTER TABLE Raamatud ADD COLUMN FOREIGN KEY(autor_id) REFERENCES  Autorid(autor_id);
ALTER TABLE Raamatud ADD COLUMN FOREIGN KEY(zanr_id) REFERENCES  Zanrid(zanr_id);
"""

CreateDateTestAutorid = """
insert into Autorid(autor_nimi, sunnikuupaev)
values
('Aleksei Darner','09-09-1923'),
('Tester Barner','23.12-1892'),
('Phil ???','20-02-2002');
"""

CreateDateTestZanrid = """
insert into Zanrid(zanr_nimi)
values
('Fantastic'),
('Comedy'),
('Action');
"""

CreateDateTestRaamatud = """
insert into Raamatud(pealkiri, valjaandmise_kuupaev, autor_id, zanr_id)
values
('TCP/IP','09.09.2023',1,3),
('Bars & eagle','23.12-2021',2,2),
('baanna','20-02-2022',3,1);
"""

### Start up ###
conn = create_connection("./data.db")
Execute_Query(conn, CreateTableAutorid)
Execute_Query(conn, CreateTableZanrid)
Execute_Query(conn, CreateTableRaamatud)
Execute_Query(conn, CreateDateTestAutorid)
Execute_Query(conn, CreateDateTestZanrid)
Execute_Query(conn, CreateDateTestRaamatud)

while True:
    option:str = input("mode:")
    if option == "":
        option="9"
    match option.lower()[0]:
        case 'q':
            exit()
        case 'p': # Printing tables data
            select_table_name=PickTable()
            select_table=f"SELECT * FROM {select_table_name};"
            print(select_table)
            date = Execute_Query_Read(conn,select_table)
            print(select_table_name.center(20))
            for user in date:
                print(user)

        case 'a': # Adding date to tables
            insert_table_name=PickTable()

            match insert_table_name:
                case "Autorid":
                    TableColumns = "autor_nimi, sunnikuupaev"
                    autor_nimi:str = input("Enter autor nimi: ")
                    sunnikuupaev:str = input("Enter autor sunnikuupaev: ")
                    RowValues = f"{autor_nimi},{sunnikuupaev}"

                case "Zanrid":
                    TableColumns = "zanr_nimi"
                    zanr_nimi:str = input("Enter zanr nimi: ")
                    RowValues = f"{zanr_nimi}"

                case "Raamatud":
                    TableColumns = "pealkiri, valjaandmise_kuupaev, autor_id, zanr_id"
                    pealkiri:str = input("Enter autor nimi: ")
                    valjaandmise_kuupaev:str = input("Enter autor sunnikuupaev: ")
                    
                    while True:
                        autor_id:str = input("Enter autorINT: ")
                        if autor_id.isdigit() and int(autor_id) <= int(len(Execute_Query_Read(conn,"select * from Autorid"))):
                            break
                    while True:
                        zanr_id:int = input("Enter zanrINT: ")
                        if zanr_id.isdigit() and int(zanr_id) <= len(Execute_Query_Read(conn,"select * from Zanrid")):
                            break
                    RowValues:str = f"'{pealkiri}','{valjaandmise_kuupaev}',{autor_id},{zanr_id}"

                    insert_table = f"insert into {insert_table_name} ({TableColumns}) values ({RowValues}) "
                    Execute_Query(conn,insert_table)
        case 'c':
            Alter_table_name=PickTable()

            date = Execute_Query_Read(conn,f"SELECT * FROM {Alter_table_name}")
            for user in date:
                print(user)

            condPick:str = input("index 0\nname 1\n: ")
            if condPick == "0":
                Index:int = input("input: ")
                if int(Index) <= len(f"SELECT * FROM {Alter_table_name}"):
                    Cond = f" {Alter_table_name[:-2]}_id = {Index} "
            elif condPick == "1":
                name:str = input("input name: ")
                Cond = f"{Alter_table_name[:-2]}_id = {name}"

            match Alter_table_name:
                case "Autorid":
                    valuePick:str = input("0=autor_nimi\n1=sunnikuupaev\n: ")
                    if valuePick == "0":
                        Var = "autor_nimi"
                    elif valuePick == "1":
                        Var = "sunnikuupaev"

                case "Zanrid":
                    Var = "zanr_nimi"

                case "Raamatud":
                    valuePick:str = input("0=pealkiri\n1=valjaandmise_kuupaev\n2=autor_id\n3=zanr_id\n: ")
                    if valuePick == "0":
                        Var = "pealkiri"
                    elif valuePick == "1":
                        Var = "valjaandmise_kuupaev"
                    elif valuePick == "2":
                        Var = "autor_id"
                    elif valuePick == "3":
                        Var = "zanr_id"

            Value:str = input("Change to")
            AlterTable = f"update {Alter_table_name} set {Var} = '{Value}' where {Cond};"
            Execute_Query(conn, AlterTable)

        case 'd':
            DelWha:str=input("1 a, 2 z 3 both:")
            Cond:str = ""
            if DelWha == '1' or DelWha == '3':
                date = Execute_Query_Read(conn,"SELECT * FROM Autorid")
                print("Autorid".center(20))
                for user in date:
                    print(user)
                    AutorIndex = input("input A Index: ")
                    Cond += f"autor_id = {AutorIndex}"

            if DelWha == '3':
                Cond += " and "
                
            if DelWha == '2' or DelWha == '3':
                print("Zanrid".center(20))
                date = Execute_Query_Read(conn,"SELECT * FROM Autorid")
                for user in date:
                    print(user)
                ZanrIndex = input("input Z Index: ")
                Cond += f"zanr_id = {ZanrIndex}"

            deleteQ:str = f"DELETE FROM Raamatud where {Cond};"
            Execute_Query_Delete(conn,deleteQ)
