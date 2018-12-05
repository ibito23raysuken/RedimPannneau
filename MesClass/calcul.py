from MesClass.error import show_error_windows
from math import ceil
def calcul(self):
    try:
        Energie_necessaire=0
        for i,element in enumerate(self.liste_materiel):
            Energie_necessaire+=int(element.nombredejour)*int(element.nombre)*int(element.puissance)
        Puissance_utile=0
        for i,element in enumerate(self.liste_materiel):
            Puissance_utile+=int(element.nombre)*int(element.puissance)
        majoration=self.maj
        print(majoration)
        Energie__p=Energie_necessaire*(1+(int(majoration)/100))
        puissance_utile=Energie__p/int(self.irradiation.get())
        nbr_panneau=puissance_utile/int(self.Puissance_cellule.get())
        nbr_panneau=ceil(nbr_panneau)
        print(self.jour.get())
        print(self.tension_batterie.get())
        """calcule de intensiter du batterie"""
        Energie_stocker=Energie_necessaire*int(self.jour.get())
        print(Energie_necessaire,"=>",Energie_stocker)
        EFS=float(Energie_stocker)*(1+int(self.maj_regulation)/100)
        intensite=EFS/int(self.tension_batterie.get())
        I_regulateur_entree=float(self.Puissance_cellule.get())*(nbr_panneau)/float(self.tension_batterie.get())
        I_regulateur_sortie=Puissance_utile/int(self.tension_batterie.get())
        self.reponse_P["text"] =ceil(Energie_necessaire) 
        self.reponse_Nbre["text"] =ceil(nbr_panneau)
        self.Intensite["text"] =ceil(intensite)
        self.reponse_I_E["text"] =ceil(I_regulateur_entree)
        self.reponse_I_s["text"] =ceil(I_regulateur_sortie)
    except ValueError:
        show_error_windows(self)
    except ZeroDivisionError:
        print("non divisible")