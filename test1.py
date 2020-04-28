import oriented1
import malade1 as m

humain=oriented1.health
#personne1=humain(61,1.59,1.02,8,12) essai1
#entrant des parametres essai 2
#faire ceci en boucle

try:
    taille=float(input('donner la taille'))
    poid=float(input('donner le poid'))
    gl=float(input('donner la val de glycemie'))
    mini=int(input('donner le min de sa presion '))
    maxi=int(input('donner le max de sa presion '))
except:
    print('toutes les val doivent etre numeriques')    
personne1=humain(poid,taille,gl,mini,maxi)


cas1=m.malade('asma','ben ali','hypotension',66)
cas1.remarque()



print('la personne x son Imc est %s , sa presion est %s ' %(personne1.imc(),personne1.pression()))