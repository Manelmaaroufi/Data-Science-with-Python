import time
import mysql.connector 
mydb = mysql.connector.connect( 
host="localhost", 
user="root",
passwd="",
database="sante" 
)
mycursor = mydb.cursor()

def create_malade(inst_bilan):
    sql = 'INSERT INTO `sante`(`poid`, `taille`, `pression`, `glycemie`, `id_malade`) VALUES (%s, %s,%s,%s,%s)' 
    val = (inst_bilan.poid,inst_bilan.taille,inst_bilan.glycemie,inst_bilan.id_malade) 
    mycursor.execute(sql, val) 
    mydb.commit() 
    print(mycursor.rowcount, "record inserted.")

#??????
