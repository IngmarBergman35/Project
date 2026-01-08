import tkinter
from fonction import *

'''parametrage app'''
app=tkinter.Tk() 
app.resizable(False,False) #empecher l'app d'etre redimentionner en L et l
app.config(bg="#002366") 
frame1=tkinter.Frame(app,width=700,height=250) 
frame1.grid(row=0,column=0,padx=10,pady=10) #pas oublier bordure pad
frame1.config(bg='#002366')

'''zone de texte'''
lab1=tkinter.Label(frame1,text='Moteur de recherche',font=('Cambria',20),bg='#FFC1CC',fg='black')
lab1.grid(row=0,column=0,padx=5,pady=5)
'''zone de saisie texte'''                                                   
entry1=tkinter.Entry(frame1,bg='#FFC1CC',width=80)
entry1.grid(row=1,column=0,padx=5,pady=5)
'''fonction associée au bouton'''


#bouton recherche

button1=tkinter.Button(frame1,text='Rechercher',bg='#FFC1CC',fg='black',command=recherche) 
button1.grid(row=2,column=0,padx=5,pady=5) 

''''boucle infini pour pas de fin''' 

app.mainloop()
    

#B5F5D1
#F4B5F5
#C4FFE0
#D6F5B5

    