BACKGROUND_COLOR = "#B1DDC6"

from cgitb import text
from tkinter import *
import pandas
import random
import time
#------------------------------CREATE FLASH CARD----------------------#
data = pandas.read_csv("./Day_31_Flash Card/data/french_words.csv")
df_dict = data.to_dict('records')
# print(df_dict)

def new_word():
    random_pair = random.choice(df_dict)
    for key in random_pair:
        french_word = random_pair["French"]
        english_word = random_pair["English"]
    canvas.itemconfig(card, image = f_image)
    canvas.itemconfig(title, text = "French", fill= "black")
    canvas.itemconfig(word, text = french_word, fill= "black")
    
    def translate():
        canvas.itemconfig(card, image= e_image)
        canvas.itemconfig(title, text = "English", fill="white")
        canvas.itemconfig(word, text=english_word, fill="white")

    window.after(3000, translate)
    


#-------------------------------UI------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
f_image=PhotoImage(file=".\Day_31_Flash Card\images\card_front.png")
e_image = PhotoImage(file=".\Day_31_Flash Card\images\card_back.png")        
card = canvas.create_image(400, 270, image=f_image)
title = canvas.create_text(400, 150, text = "title", fill="black", font= ("ariel",40, "italic"), tags = "ttl")
word = canvas.create_text(400, 263, text = "text", fill="black", font= ("ariel",60, "bold "), tags= "txt")

canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = PhotoImage(file=".\Day_31_Flash Card\images\wrong.png")
wrong_button = Button(image=wrong_button_image, bg=BACKGROUND_COLOR, highlightthickness= 0, command=new_word)
wrong_button.grid(row=1, column=0)

correct_button_image = PhotoImage(file=".\Day_31_Flash Card\images\correct.png")
correct_button = Button(image=correct_button_image, bg=BACKGROUND_COLOR, highlightthickness=0, command = new_word)
correct_button.grid(row=1, column=1)

new_word()

window.mainloop()
