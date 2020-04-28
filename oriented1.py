class health:
    def __init__(self,poid,taille,glycemie,min,max):
        self.poid=poid
        self.taille=taille
        self.glycemie=glycemie
        self.min=min
        self.max=max

    def imc(self):
        return self.poid/(self.taille*self.taille)    
        
    def pression(self):
        if( (self.min< 8) or (self.max< 12) ):
            return('hypotension')
        elif( (self.max>13) or (self.min>9) ):
            return('hypertension')
        else:
            return('ideale')    

    def glycemie(self):
        if(self.glycemie>1.4):
            return('hyperglycemie')  
        elif(self.glycemie<0.8):
            return('hypoglycemie')  
        else:
            return('ideal')      