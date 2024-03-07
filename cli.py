from functions import *

### SQL ###

#CreateTable0 = "CREATE TABLE IF NOT EXITS Raamatud([]);"
#CreateTable1 = "CREATE TABLE IF NOT EXITS Raamatud([]);"
#CreateTable2 = "CREATE TABLE IF NOT EXITS Raamatud([]);"

CreateTable0="""
    Create table IF NOT EXISTS Raamatud (
        autor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        autor_nimi varchar(255),
        sunnikuupaev date
    );
"""

CreateTable1="""
    Create table IF NOT EXISTS Zanrid (
        zanr_id INTEGER PRIMARY KEY AUTOINCREMENT,
        zanri_nimi varchar(255)
    );
"""
CreateTable2="""
    Create table IF NOT EXISTS Raamatud (
        raamat_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pealkiri varchar(255),
        valjaandmise_kuupäev date,
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
	ALTER TABLE Zanrid ADD COLUMN zanri_nimi varchar(255);

	ALTER TABLE Raamatud ADD COLUMN raamat_id INTEGER PRIMARY KEY AUTOINCREMENT;
	ALTER TABLE Raamatud ADD COLUMN pealkiri varchar(255);
	ALTER TABLE Raamatud ADD COLUMN valjaandmise_kuupäev date;
	ALTER TABLE Raamatud ADD COLUMN autor_id INTEGER;
	ALTER TABLE Raamatud ADD COLUMN zanr_id INTEGER;
	ALTER TABLE Raamatud ADD COLUMN FOREIGN KEY(autor_id) REFERENCES  Autorid(autor_id);
	ALTER TABLE Raamatud ADD COLUMN FOREIGN KEY(zanr_id) REFERENCES  Zanrid(zanr_id);
"""

CreateDateTest = """
	insert into Autorid(autor_nimi,sünnikuupäev)
	values
	('Aleksei Darner','09-09-1923'),
	('Tester Barner','23.12-1892'),
	('Phil ???','20-02-2002');

	insert into Zanrid(zanri_nimi)
	values
	('Fantastic'),
	('Comedy'),
	('Action');

	insert into Raamatud(pealkiri, väljaandmise_kuupäev, autor_id, zanr_id)
	values
	('TCP/IP','09-09-2023',1,3),
	('Bars & eagle','23.12-2021',2,2),
	('baanna','20-02-2022',3,1);

	select * from Autorid;
	select * from Zanrid;
	select * from Raamatud;
"""

select_table = """
    select * from Raamatud;
"""

del_user_data="""
    delete from users where student = true;
"""

del_user_tb="drop table users;"


### user ###
print("0")
conn = create_connection("./data.db")
print("1")
Execute_Query(conn, CreateTable0)
Execute_Query(conn, CreateTable1)
Execute_Query(conn, CreateTable2)
print("2")
Execute_Query(conn, CreateDateTest)


while True:
    option:str = input("input:")
    match option.lower()[0]:
        case 'q':
            exit()
        case 'p':
            date = Execute_Query_Read(conn,select_table)
            print("user")
            for user in date:
                print(user)
