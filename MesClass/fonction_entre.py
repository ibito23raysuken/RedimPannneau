"""programme principale"""
liste_objet=[]
fin_liste=True
while fin_liste==True:
    print("choisiser le type de materiel que vous aviez")
    materiel_domestique=Materiel()
    print("Entree nom du materiel")
    materiel_domestique.nom=input()
    print("Entree nombre de {}".format(materiel_domestique.nom))
    materiel_domestique.nombre=input()
    print("Entree puissance de {}".format(materiel_domestique.nom))
    materiel_domestique.puissance=input()
    print("Entree nombre de heure de fonctionnement de {}".format(materiel_domestique.nom))
    materiel_domestique.nombredejour=input()
    liste_objet.append(materiel_domestique)
    variable=input()
    if(variable.lower()=='f'):
        fin_liste=False
Energie_necessaire=0
for i,element in enumerate(liste_objet):
    Energie_necessaire+=int(element.nombredejour)*int(element.nombre)*int(element.puissance)
print("choisir le majoration[%]")
majoration=input()
Energie__p=Energie_necessaire*(1+(int(majoration)/100))
print(Energie_necessaire,"=>",Energie__p)