class malade:
    def __init__(self,nom,prenom,cas,age):
        self.nom=nom
        self.prenom=prenom
        self.cas=cas
        self.age=age

    def remarque(self):
        if(self.age>60):
            self.remarque='agee'
        elif(self.age<15):
            self.remarque='enfant' 
        else:
            self.remarque='normale'    
    
