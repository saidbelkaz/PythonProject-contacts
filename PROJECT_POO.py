#Importer la bibliothèque requise
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os
import os.path
#Utiliser les expressions régulières
import re
#Bibliothèque pour changer le fond
from PIL import Image, ImageTk
import datetime as dt



# Pour créer la fenêtre de l'application

root =Tk()

# Pour régler le zoom maximum et minimum de la fenêtre d'application
root.minsize(1100, 500)
root.maxsize(1100, 500)



#Pour créer un arrière-plan photo

img =Image.open("imags & icon\zNDJjd.jpg")
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
label.place(x = 0,y = 0)

#Contrôler la taille et le titre de l'application

root.geometry("1100x500")
root.title('Project Contacts App')
root.iconbitmap("imags & icon\Tatice-Cristal-Intense-Notepad-Bloc-notes.ico")





def get_data():
    
    
    #Utilisez (les expressions régulières)
 
          
    if len(nom_input.get())==0 and len(prénom_input.get())==0 and len(email_input.get())==0 and len(numéro_input.get())==0:      
        messagebox.showerror("Message d'erreur", "Ajouter des données")
        
        #Vérification du nom
    if len(nom_input.get())==0 and len(prénom_input.get())==0 and len(email_input.get())==0 and len(numéro_input.get())==0:      
        pass
    
    elif re.search("^[A-Za-z]*$",nom_input.get()):
        get_nom_input = nom_input.get()

    else:
        messagebox.showerror("Message d'erreur", "Nom incorrect")
        
        
          #Vérification du prénom
    if len(nom_input.get())==0 and len(prénom_input.get())==0 and len(email_input.get())==0 and len(numéro_input.get())==0:      
        pass
    elif re.search("^[A-Za-z]*$",prénom_input.get()):
        get_prénom_input = prénom_input.get()
    else:
        messagebox.showerror("Message d'erreur", "Prénom invalide")


          #vérification de l'E-mail
    if len(nom_input.get())==0 and len(prénom_input.get())==0 and len(email_input.get())==0 and len(numéro_input.get())==0:      
        pass
    elif re.search("^[A-Za-z][A-Za-z0-9]*@[A-Za-z]+\.[A-Za-z]+$",email_input.get()):
        if len(email_input.get())!=0 and len(nom_input.get())==0:
            messagebox.showerror("Message d'erreur", "Donne lui un nom")
        else:
           get_email_input = email_input.get()


            
    elif len(email_input.get())==0:
        get_email_input = email_input.get()
        
        
    else:
        messagebox.showerror("Message d'erreur", "Email invalide")



          #Vérifier le numéro de téléphone

    if len(nom_input.get())==0 and len(prénom_input.get())==0 and len(email_input.get())==0 and len(numéro_input.get())==0:      
        pass
    elif re.search("[0-9]{10}$",numéro_input.get()):
        if len(numéro_input.get())!=0 and len(nom_input.get())==0 :
            messagebox.showerror("Message d'erreur", "Donne lui un nom")
        else:
            get_numéro_input = numéro_input.get()
        
        
    elif len(numéro_input.get())==0:
        get_numéro_input = numéro_input.get()
        
    else:
        messagebox.showerror("Erreur", "Numéro de téléphone invalide")

        
    #Utilisez (datetime)
        
    date=dt.datetime.now()
    get_date=date.strftime("%Y-%m-%d         %H:%M")
    
    
    data =[get_nom_input, get_prénom_input, get_email_input,get_numéro_input,get_date]
    
    #utiliser le fichier csv
    
    with open('contacts.csv','a+',newline='') as c:
        writer = csv.writer(c)
        writer.writerow(data)


    contactBox.insert('','end',values = data)
    
    nom_input.delete(0, 'end')
    prénom_input.delete(0, 'end')
    email_input.delete(0, 'end')
    numéro_input.delete(0, 'end')




#Utilisez la fonction def Quitter pour le bouton de sortie

def Quitter ():
    
    file_exists = os.path.isfile('contacts.csv')
    if file_exists:
        reponse = messagebox.askyesno("Question", "Voulez-vous enregistrer ?")
        if reponse==True:
            root.destroy()
        else:
            os.remove("contacts.csv")
            root.destroy()
    else:
         root.destroy()

    

#Utilisez la fonction def Supprimer_tout pour le bouton de Supprimer tout


def Supprimer_tout():

    file_exists = os.path.isfile('contacts.csv')
    if file_exists:
        reponse = messagebox.askyesno("Question", "Voulez-vous Tout Supprimer ?")
        if reponse==True:
            os.remove("contacts.csv")
            



#Utilisez la fonction def Supprimer_tout pour le bouton de Supprimer 

def supprimer():
    file_exists = os.path.isfile('contacts.csv')
    if file_exists :
        
        #Utilisez ( administrer les exceptions )
        
        try:
            selected_item = contactBox.selection()[0] ## get selected item
            contactBox.delete(selected_item)

        except:
            
            messagebox.showerror("Erreur ", "Sélectionnez l'élément à supprimer")
    else:
        messagebox.showerror("Erreur ", "Il n'y a rien dans la boîte de contact")
        

#Utilisez la fonction def search pour le bouton de search 

def search():

    file_exists = os.path.isfile('contacts.csv')
    if file_exists :        
            t = True
            recherche=search_var.get()
            if len (recherche)!=0:
                file = open('contacts.csv', 'r+')
                contacts = []
                for n in file:
                     n = n.split(',')
                     if recherche in n:   
                         contactBox.delete(*contactBox.get_children())
                         contacts.append((n[0], n[1], n[2], n[3],n[4]))
                         for contact in contacts:
                             contactBox.insert('', END, values=contact)
                             t=False
                    
                if t==True:
                    messagebox.showerror(f'Python Error', f"Error: '{recherche}' n'est pas dans la liste de contacts")

    else:
        messagebox.showerror("Erreur ", "Il n'y a rien dans la boîte de contact")


 
def refresh():
    
    file_exists = os.path.isfile('contacts.csv')
    if file_exists :        
        entry_search.delete(0,END)
        contactBox.delete(*contactBox.get_children())
        with open('contacts.csv', 'r') as c:
            read = csv.reader(c)
            for i in read:
                contactBox.insert('', 'end', values = i)



#Utilisez la fonction def info pour le bouton de  info

def info():
    messagebox.showinfo("À propos de l'application", "Cette application de contacts est enregistrée en tant que fichier csv \
et cette application a été créée par le stagiaire    Said Belkaz du groupe TDD113")


#Utiliser label and input

nomlbl=Label(root, text="Nom                : ", font = ('Helvetica bold', 12),bg='blue')
nom_input=Entry(root, width= 30,highlightthickness=2, justify="center")
nomlbl.place(x=50,y=30)
nom_input.config(highlightcolor= "#FF0000")
nom_input.place(x=160,y=30)

prénomlbl = Label(root, text="Prénom          : " ,font = ('Helvetica bold', 12),bg='blue')
prénom_input = Entry(root, width =30, highlightthickness=2,justify="center")
prénomlbl.place(x=50,y=60)
prénom_input.config(highlightcolor= "#FF0000")
prénom_input.place(x=160,y=60)



emaillbl = Label(root, text="Email              : ", font = ('Helvetica bold', 12),bg='blue')
email_input = Entry(root, width = 30, highlightthickness=2,justify="center")
emaillbl.place (x=50, y=90)
email_input.config(highlightcolor= "#FF0000")
email_input.place (x= 160,y =90)

numérolbl = Label(root, text="Numéro          : ", font = ('Helvetica bold', 12),bg='blue')
numéro_input = Entry(root, width = 30, highlightthickness=2,justify="center")
numérolbl.place (x=50, y=120)
numéro_input.config(highlightcolor= "#FF0000")
numéro_input.place (x=160, y=120)


# Utilisez les boutons

infob=Button(root,text='info',width=50,relief= GROOVE, cursor="hand2",bg='red',fg='black'\
             ,activebackground='SlateGray4', bitmap="info", command=info).place(x=1000 , y=5)




supprimertout_button=Button(root, text ="Supprimer Tout",bg='red' ,activebackground='SlateGray4'\
                             ,relief= GROOVE, cursor="hand2",command=Supprimer_tout) .place (x=170 , y=450)

supprimer_button=Button (root, text="Supprimer",bg='red',activebackground='slateGray4'\
                         , relief= GROOVE,width=12 , cursor="hand2", command=supprimer) .place(x=50 , y=450)



Ajouter_button=Button(root, text="Ajouter",fg='white', bg='blue',activebackground='SlateGray4'\
                      ,relief= GROOVE, cursor="hand2",width=25 , command=get_data)
Ajouter_button.place(x=160, y=150)

Quitter_button=Button(root, text='Quitter', bg='tomato',activebackground='white'\
                      ,relief= GROOVE, cursor="hand2", width=15,command =Quitter)
Quitter_button.place(x=940 , y=450)

search_var = StringVar()
entry_search=Entry(root,font=("Helvetica bold", 12),bg='#EFEFEF', justify="center",highlightthickness=2,textvariable=search_var)
entry_search.config(highlightcolor= "#FF0000")
entry_search.place(x=600,y=150)

Button_search=Button(root,text='Search',fg='white', bg='blue',activebackground='SlateGray4'\
                      ,relief= GROOVE, cursor="hand2",width=10,command=search).place(x=800,y=150)

Button_refrech=Button(root,text='Refresh ',fg='white', bg='blue',activebackground='SlateGray4'\
                      ,relief= GROOVE, cursor="hand2",width=10,command=refresh).place(x=970,y=150)



#Créer une boîte de connexion pour afficher les résultats

header =('Nom', 'Prénom', 'Email','Numéro de telephone','Date modified')

contactBox =ttk.Treeview(root, column = header, cursor="hand2",show='headings')
contactBox.column("# 1",anchor=CENTER)
contactBox.column("# 2",anchor=CENTER)
contactBox.column("# 3",anchor=CENTER)
contactBox.column("# 4",anchor=CENTER)
contactBox.column("# 5",anchor=CENTER)
contactBox.grid(row=4, column = 0, columnspan=10 , pady=200, padx=50 )

#créer "scrollbar" Pour une navigation facile à l'intérieur de la boîte de contacts

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=contactBox.yview)
contactBox.configure(yscroll=scrollbar.set)
scrollbar.grid(row=4, column = 9, columnspan=10 , pady=200, padx=10 , sticky='ns')

# Cette boucle consiste à montrer chaque entrée à l'intérieur de ce qu'elle correspond à header
for i in header:
    contactBox.heading(i, text=i)

    
# Lire tout à l'intérieur du fichier csv

file_exists = os.path.isfile('contacts.csv') #true/false
if file_exists: #true
   with open('contacts.csv', 'r') as c:
       read = csv.reader(c)
       for i in read:
           contactBox.insert('', 'end', values = i)



# Pour afficher la fenêtre de l'application
root.mainloop()
























                   
                          
             
