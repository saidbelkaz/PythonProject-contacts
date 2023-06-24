#Importer la bibliothèque requise
import tkinter as tk

from tkinter import *
from tkinter import StringVar
from tkinter import messagebox

#Bibliothèque pour changer le fond
from PIL import Image, ImageTk

# Pour créer la fenêtre de l'application
tk = Tk()

#Contrôler la taille et le titre de l'application

tk.geometry("1100x500")
tk.title('Login page')
tk.iconbitmap("imags & icon\Icons8-Windows-8-User-Interface-Login.ico")

# Pour régler le zoom maximum et minimum de la fenêtre d'application

tk.minsize(1100, 500)
tk.maxsize(1100, 500)



#Pour créer un arrière-plan photo

img =Image.open("imags & icon\zNDJjd.jpg")
bg = ImageTk.PhotoImage(img)
label = Label(tk, image=bg)
label.place(x = 0,y = 0)


def Login():

    
    
    login=Frame(tk, width=700, height=400,bg='#F3F3F3',highlightthickness=6)
    login.config(highlightbackground = "red",highlightcolor= "red")
    login.place(x=200,y=50)

    label_title2=Label(tk,text='Se connecter',bg='#F3F3F3',fg='blue',font=("tajwal", 20, "bold")).place(x=450,y=80)

    
    def toggle_password():
        if checkbutton.var.get():
            entry_password['show'] = ""
        else:
            entry_password['show'] = "*"
    


    label_email=Label(tk,text='Username          :',bg='#F3F3F3',font=("tajwal", 20, "bold")).place(x=250,y=160)
    email_var = StringVar()
    entry_email=Entry(tk,font=("tajwal", 20, "bold"),bg='#EFEFEF', justify="center",highlightthickness=2,textvariable=email_var)
    entry_email.config(highlightcolor= "#456EFF")
    entry_email.place(x=500,y=160)

    password_label=Label(tk,text='Password          :',bg='#F3F3F3',font=("tajwal", 20, "bold")).place(x=250,y=260)
    password_var = StringVar()
    entry_password = Entry(tk, font=("tajwal", 20, "bold"),show='*',bg='#EFEFEF', justify="center", highlightthickness=2,textvariable=password_var)
    entry_password.config( highlightcolor= "#456EFF")
    entry_password.place(x=500,y=260)
    
    checkbutton =Checkbutton(tk,text="Afficher le mot de passe",onvalue=True,offvalue=False,command=toggle_password)
    checkbutton.var = BooleanVar(value=False)
    checkbutton['variable'] = checkbutton.var
    checkbutton.place(x=500,y=310)
    

#Utilisez la fonction def buton pour le bouton de Button_login 

    def buton():
        email=email_var.get()
        password=password_var.get()
        
        if len(email_var.get())!=0 and len(password_var.get())!=0:
            if email=='user22' and password=='root':
                tk.destroy()
        
                #Utilisez (MANIPULER LES MODULES ET LES BIBLIOTHEQUES)
                import PROJECT_POO

                
            else:
                messagebox.showerror('Error', 'Mot de passe ou user incorrect')
        else:
                messagebox.showerror('Error', "Entrez un mot de passe et un user")


#Utilisez la fonction def butq pour le bouton de Button_quiter 

    def butinfo():
        messagebox.showinfo("Pour essayer l'application", "Username :   user22                            \
                                              Password :   root")
        
    # Utilisez les boutons
    '''
    img1=Image.open(r"imags & icon/login.jpg")
    img1=img1.resize((200,45), Image. ANTIALIAS)
    photoimage1=ImageTk.PhotoImage(img1)
    b1=Button(tk, image=photoimage1, borderwidth=0,cursor="hand2", fg="white",command=buton)
    b1.place(x=500,y=350, width=300)
    '''
    Button_login=Button(tk,text='Login',font=("tajwal", 18, "bold" ),fg='white', bg='blue',activebackground='SlateGray4'\
                      ,relief= GROOVE, cursor="hand2",width=20,command=buton).place(x=500,y=350)

    
    Button_info= Button(tk, bitmap="question",relief= GROOVE, cursor="hand2",width=40,bg='red',activebackground='SlateGray4'\
                     ,command=butinfo)
    Button_info.place(x=220,y=400)
Login()

# Pour afficher la fenêtre de l'application

tk.mainloop()
