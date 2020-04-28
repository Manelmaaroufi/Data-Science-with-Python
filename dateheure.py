import time 
#appel au biblio time qui existe par defaut


from datetime import date 
#adate= biblio #appel au date et heure d'aujourd hui

print(time.strftime('%H:%M:%S'))
 #2 importation + transformation de time (tps) en type str

today= date.today() #la var today recoit d.t

print('today s current date is -',today)
