#! /usr/bin/python3.6
# -*-coding:utf-8 -*
from tkinter import *
from tkinter import ttk
from MesClass.Materiel  import Materiel
from MesClass.calcul import calcul
class Interface(Frame):
    def __init__(self,fenetre,**kwargs):
        Frame.__init__(self,fenetre,width=408,height=576,**kwargs)
        self.pack(fill=BOTH)
        fenetre.title('Dimensionnement Panneau Solaire')
        frame1=LabelFrame(self,width=200, height=200, text="information")
        frame2=LabelFrame(self,width=200, height=200, text="liste des equipement")    
        frame3=LabelFrame(self,width=200, height=50, text="variation meteo") 
        frame4=LabelFrame(self,width=200, height=50, text="Reponse") 
        frame5=LabelFrame(self,width=200, height=50, text="propriete de batterie")
        frame1.pack(side=LEFT,fill=Y,padx=20,pady=20)
        frame2.pack(side=RIGHT, fill=X,padx=20,pady=20)
        frame3.pack(padx=20,pady=20)
        frame5.pack(padx=20,pady=20)
        frame4.pack(padx=20,pady=20)
        
        """entree les differente 
        parametre que l'application a besoin"""
        self.Nom=Label(frame1, text="Nom materiel:")
        Nom_materiel_entree=StringVar()
        self.Nom_materiel=Entry(frame1,textvariable=Nom_materiel_entree,width=10)
        self.Nombre=Label(frame1, text="Nombre materiel:")
        nombre_materiel_entree=IntVar()
        self.nombre_materiel=Entry(frame1,textvariable=nombre_materiel_entree,width=10)
        self.Puissance=Label(frame1, text="Puissance:")
        puissance_materiel_entree=IntVar()
        self.puissance_materiel=Entry(frame1,textvariable=puissance_materiel_entree,width=10)
        self.Duree=Label(frame1, text="Duree:")
        duree_materiel_entree=IntVar()
        self.duree_materiel=Entry(frame1,textvariable=duree_materiel_entree,width=10)
        self.liste=Listbox(frame2)
        self.liste_materiel=[]   
        self.bouton_clic=Button(frame1,text="add",command=self.clic)
        self.bouton_calcul=Button(frame2,text="calculer",command=self.calcul)
        """panneau solaire"""
        self.irrad=Label(frame3, text="irradiation:")
        irradiation_entree=StringVar()
        self.irradiation=Entry(frame3,textvariable=irradiation_entree,width=10)
        self.Puissan_cellul=Label(frame3, text="puissance cellul:")
        Puissan_cellul_entree=StringVar()
        self.Puissance_cellule=Entry(frame3,textvariable=Puissan_cellul_entree,width=10)
        """dimmensionnent de regulateur"""
        self.majoration_reg=Label(frame5, text="Majoration:")
        self.cb_reg = ttk.Combobox(frame5, values=("0%","25%", "50%", "75%", "100%"))
        self.cb_reg.set("50%")
        self.cb_reg.bind('<<ComboboxSelected>>', self.on_select)
        self.label_jour=Label(frame5, text="jour:")
        jour_entree=StringVar()
        self.jour=Entry(frame5,textvariable=jour_entree,width=10)
        self.label_tension=Label(frame5, text="tension Batterie:")
        tension_entree=StringVar()
        self.tension_batterie=Entry(frame5,textvariable=tension_entree,width=10)
        """"""
        self.majoration=Label(frame2, text="Majoration:")
        self.cb = ttk.Combobox(frame2, values=("0%","25%", "50%", "75%", "100%"))
        self.cb.set("50%")
        self.cb.bind('<<ComboboxSelected>>', self.on_select)
        self.maj=int()
        self.maj_regulation=int()
        """assemblage de chaque partie 
        de l'application"""   
        self.Nom.grid(row=0,column=0, sticky=W)
        self.Nom_materiel.grid(row=0,column=1, sticky=W)
        self.Nombre.grid(row=1,column=0, sticky=W)
        self.nombre_materiel.grid(row=1,column=1, sticky=W)
        self.Puissance.grid(row=2,column=0, sticky=W)
        self.puissance_materiel.grid(row=2,column=1, sticky=W)
        self.Duree.grid(row=3,column=0, sticky=W)
        self.duree_materiel.grid(row=3,column=1, sticky=W)
        self.bouton_clic.grid(row=4, sticky=W)

        self.irrad.grid(row=0,column=0, sticky=W)
        self.irradiation.grid(row=0,column=1, sticky=W)
        self.Puissan_cellul.grid(row=1,column=0, sticky=W)
        self.Puissance_cellule.grid(row=1,column=1, sticky=W)
        self.liste.pack()
        self.majoration.pack()
        self.cb.pack()
        self.bouton_calcul.pack()
        self.label_jour.pack()
        self.jour.pack()
        self.label_tension.pack()
        self.tension_batterie.pack()
        self.majoration_reg.pack()
        self.cb_reg.pack()

        """reponse de calcule"""
        self.label_P=Label(frame4, text="Puissance necessaire:")
        self.reponse_P=Label(frame4, text="*")
        self.label_Nbre=Label(frame4, text="Nbre de panneau:")
        self.reponse_Nbre=Label(frame4, text="*")
        self.label_Intensite=Label(frame4, text="Intensite Batterie:")
        self.Intensite=Label(frame4, text="*")  
        self.label_I_E=Label(frame4, text="Intensite regulateur entree:")
        self.reponse_I_E=Label(frame4, text="*")
        self.label_I_S=Label(frame4, text="Intensite regulateur sortie:")
        self.reponse_I_s=Label(frame4, text="*")      
        self.label_P.grid(row=0,column=0, sticky=W)
        self.reponse_P.grid(row=0,column=1, sticky=W)
        self.label_Nbre.grid(row=1,column=0, sticky=W)
        self.reponse_Nbre.grid(row=1,column=1, sticky=W)
        self.label_Intensite.grid(row=2,column=0, sticky=W)
        self.Intensite.grid(row=2,column=1, sticky=W)
        self.label_I_E.grid(row=3,column=0, sticky=W)
        self.reponse_I_E.grid(row=3,column=1, sticky=W)
        self.label_I_S.grid(row=4,column=0, sticky=W)
        self.reponse_I_s.grid(row=4,column=1, sticky=W)
        

    def clic(self):
        #fonction appeller lors de clic 
        materiel_domestique=Materiel()
        materiel_domestique.nom=self.Nom_materiel.get()
        materiel_domestique.nombre=self.nombre_materiel.get()
        materiel_domestique.puissance=self.puissance_materiel.get()
        materiel_domestique.nombredejour=self.duree_materiel.get()
        self.liste_materiel.append(materiel_domestique)
        self.liste.insert(END,self.liste_materiel[-1].nom)
    def calcul(self):
        calcul(self)
    def on_select(self,event=None):
        if event: # <-- this works only with bind because `command=` doesn't send event
            self.maj=re.sub(r"%", r"", self.cb.get())
            print(self.maj)
            self.maj_regulation=re.sub(r"%", r"", self.cb_reg.get())
            print(self.maj_regulation)

""" appelle du programme il faut le diviser pour tavaille dans une classe"""
if __name__ == '__main__':
    fenetre=Tk()
    interface=Interface(fenetre)
    interface.mainloop()  
    interface.destroy()