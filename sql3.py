
import sqlite3 

ulanish = sqlite3.connect('server.db')

#cursor method

curosr = ulanish.cursor()
#1-datebase
curosr.execute("""
CREATE TABLE IF NOT EXISTS shop(
    name TEXT,
    last_name TEXT,
    age INTEGER
)                
""")

curosr.execute("""
INSERT INTO shop VALUES                
('Bekzodbek', 'Tursunboyeev', 16),
('Bekzodbek', 'Tursunboyeev', 16),
('Bekzodbek', 'Tursunboyeev', 16)
""")
curosr.execute("SELECT * FROM shop")
server1 = curosr.fetchall()
#2-datebase
cursor1 = ulanish.cursor()
cursor1.execute("""
CREATE TABLE IF NOT EXISTS car(
    name TEXT,
    last_name TEXT,
    age INTEGER
)                
""")

cursor1.execute("""
INSERT INTO car VALUES                
('Banan', '12 000som', 1600),
('Olma', '6 000 som', 692),
('shaftoli', '10000som', 2000)
""")
cursor1.execute("SELECT * FROM car")
server2 = cursor1.fetchall()
#3-datebase
cursor3 = ulanish.cursor()

cursor3.execute("""
CREATE TABLE IF NOT EXISTS garden(
    name TEXT,
    last_name TEXT,
    age INTEGER
)                
""")

cursor3.execute("""
INSERT INTO garden VALUES                
('otkan kunlar', '20000nusxa', 5000),
('ikki eshik orasi', '1000nusxa', 10006),
('alkimyogar', '200nusxa', 5200)
""")

cursor3.execute("SELECT * FROM garden")

server3 = cursor3.fetchall()

#4-datebase
cursor4 = ulanish.cursor()
cursor4.execute("""
CREATE TABLE IF NOT EXISTS bog(
    name TEXT,
    last_name TEXT,
    age INTEGER
)                
""")

cursor4.execute("""
INSERT INTO bog VALUES                
('16-maktab', '800nafar', 0),
('42-maktab', '1500nafar', 5),
('39-maktab', '200nafar', 5)
""")
cursor4.execute("SELECT * FROM bog")
server4 = cursor4.fetchall()
#5-datebase
cursor5 = ulanish.cursor()
cursor5.execute("""
CREATE TABLE IF NOT EXISTS kom(
    name TEXT,
    last_name TEXT,
    age INTEGER
)                
""")

cursor5.execute("""
INSERT INTO kom VALUES                
('samsung', 's 10', 10),
('redmi', 'note 9', 10),
('artel', 'v5', 0)
""")

cursor5.execute("SELECT * FROM kom")

server5 = cursor5.fetchall()




wh = "ha"
while wh == 'ha':
    sorov = input('Qidiring: ').lower()
    if sorov == "ismlar":
        print(server1)
    elif sorov == "mevalar":
        print(server2)
    elif sorov == "kitoblar":
        print(server3)
    elif sorov == "maktablar":
        print(server4)
    elif sorov == "telefonlar":
        print(server5)
    else:
        print(f'{sorov} boyicha hech narsa topilmadi')
    if wh == "yoq":
        print('Etiboringiz uchun rahmat tugadi')
    wh = input("Davom etishni hohlaysizmi? ").lower()
