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

SelectAutorid="""
    SELECT * FROM Autorid
"""

SelectZanrid="""
    SELECT * FROM Zanrid;
"""

SelectRaamatud="""
    SELECT Raamatud.raamat_id, Raamatud.pealkiri, Raamatud.valjaandmise_kuupaev, Autorid.autor_nimi, Zanrid.zanr_nimi
    FROM Raamatud
    INNER JOIN Autorid ON Raamatud.autor_id=Autorid.autor_id
    INNER JOIN Zanrid ON Raamatud.zanr_id=Zanrid.zanr_id;
"""
