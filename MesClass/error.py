from tkinter import messagebox
def show_error_windows(self):
    if (len(self.liste_materiel)==0):
        messagebox.showerror("ERREUR","liste vide")
    messagebox.showerror("ERREUR","une erreur est survenu")