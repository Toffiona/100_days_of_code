from decimal import ROUND_UP
from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=10, pady=10)

# initiate grid column 0 and row 0
label1 = Label(text="Converter")
label1.grid(column=0, row=0)

entry = Entry(width=10)
entry.grid(column=3, row=3)

equal_label=Label(text="is equal to")
equal_label.grid(column=2, row=4)

miles_label = Label(text="Miles")
miles_label.grid(column=4, row=3)

result_label = Label(text=0)
result_label.grid(column=3, row=4)

km_label= Label(text="Km")
km_label.grid(column=4, row=4)

def calculate():
    result = entry.get()
    km_result = round(int(result) * 1.609344)
    result_label["text"]= km_result

button = Button(text="Calculate", command= calculate)
button.grid(column=3, row=5)




window.mainloop()



