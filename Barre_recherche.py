import tkinter
from fonction import *

'''parametrage app'''
app=tkinter.Tk() 
app.resizable(False,False) #empecher l'app d'etre redimentionner en L et l
app.config(bg="green") 
frame1=tkinter.Frame(app,width=700,height=250) 
frame1.grid(row=0,column=0,padx=10,pady=10) #pas oublier bordure pad
frame1.config(bg='green')

'''zone de texte'''
lab1=tkinter.Label(frame1,text='Moteur de recherche',font=('Cambria',20),bg='pink',fg='white')
lab1.grid(row=0,column=0,padx=5,pady=5)
'''zone de saisie texte'''
entry1=tkinter.Entry(frame1,bg='green',width=80)
entry1.grid(row=1,column=0,padx=5,pady=5)
'''fonction associée au bouton''


#bouton recherche
button1=tkinter.Button(frame1,text='Rechercher',bg='purple',fg='white',command=recherche) 
button1.grid(row=2,column=0,padx=5,pady=5) 

''''boucle infini pour pas de fin''' 

app.mainloop()
    
    