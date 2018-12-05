#! /usr/bin/python3.6
# -*-coding:utf-8 -*
class Materiel:
    def __init__(self):
        self._nom="vide"
        self._puissance=0
        self._nombre=0
        self._nombredejour=0
    def __str__(self):
        return 'nom :{0} -nombre:{1}-puissance:{2}'.format(self._nom,self._nombre,self._puissance)
    def _set_nom(self,nom):
        self._nom=nom
    def _get_nom(self):
        return self._nom   
    def _set_nombre(self,nombre):
        self._nombre=nombre
    def _get_nombre(self):
        return self._nombre
    def _set_puissance(self,puissance):
        self._puissance=puissance
    def _get_puissance(self):
        return self._puissance 
    def _set_nombredejour(self,nombredejour):
        self._nombredejour=nombredejour
    def _get_nombredejour(self):
        return self._nombredejour 
    nom=property(_get_nom,_set_nom)
    nombre=property(_get_nombre,_set_nombre)
    puissance=property(_get_puissance,_set_puissance)
    nombredejour=property(_get_nombredejour,_set_nombredejour)

