import oriented1 as o
import mysql.connector 

mydb = mysql.connector.connect( 
host="localhost", 
user="root",
passwd="",
database="sante" 
)
mycursor = mydb.cursor()

def create_malade(health_inst,id):

    pression=str(health_inst.max)+'.'+str(health_inst.min)
    pression=float(pression)

    sql = 'INSERT INTO `sante`( `poid`, `taille`, `pression`, `glycemie`, `id_malade` )VALUES (%s,%s,%s,%s,%s)' 
    val = (health_inst.poid,health_inst.taille,health_inst.pression,health_inst.glycemie,id) 
    mycursor.execute(sql, val) 
    mydb.commit() 
    print(mycursor.rowcount, "record inserted.")

x=o.health
cas1=x(60,1.59,1.02,8,14)
create_malade(cas1,1)

