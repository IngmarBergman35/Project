import tkinter
from customtkinter import *
from PIL import Image
#ajouter image

app=tkinter.Tk()
app.geometry("500x400")


set_appearance_mode("dark")

img=Image.open("message_icon.png")
#ajouter image

btn=CTkButtons(master=app, text="Pick Me", corner_radius=32, fg_color="#00FF0D",
               hover_color="#FF00C3",border_color="FFFFFF",
               border_width=1,)
#image pour ajouter sur le bouton

btn.place(relx=0.5,anchor="center")

app.mainloop()

#################################################################################################

from Customtkinter import*

app=CTk()
app.geometry("500x400")

label=CTklabel(master=app, text="...", font=("Yu Gothic",20),text_color="#")

label.place(relx=0.5, rely=0.5, anchor="center")


app.mainloop()

#################################################################################################

from Customtkinter import*

app=CTk()
app.geometry("500x400")

combobox=CTkComboBox(master=app, values=["option1","option2","option3","option4"], fg_color="#34828C",
                     border_color="#439177", dropdown_fg_color="#439177")

combobox.place(relx=0.5,rely=0.5, anchor="center")
               
               
app.mainloop()
             