import malade1 as m
import mysql.connector 
mydb = mysql.connector.connect( 
host="localhost", 
user="root",
passwd="",
database="sante" 
)
mycursor = mydb.cursor()

def create_malade(inst_malade):
    sql = 'INSERT INTO `malade`(nom`, `prenom`, `age`, `cas`, `remarque`) VALUES (%s, %s,%s,%s,%s)' 
    val = (inst_malade.nom,inst_malade.prenom,inst_malade.age,inst_malade.cas,inst_malade.remarque) 
    mycursor.execute(sql, val) 
    mydb.commit() 
    print(mycursor.rowcount, "record inserted.")

inst=m.malade('test','test','hypertendu',62)
inst.remarque()
create_malade(inst)