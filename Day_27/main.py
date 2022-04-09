import tkinter

from pandas import wide_to_long

# window
window = tkinter.Tk()
window.title("My first GUI project")
window.minsize(width=500, height=300)

#Label
label = tkinter.Label(text="I am a label", font=("arial", 14, "bold"))
label.grid(column=0, row=0)
# label.pack()
#add space around the widges
label.config(padx=20, pady=20)

#Button
def click_button():
    label["text"] = input.get()
    # label.config(text="I got clicked")
    #print("I got clicked")

button = tkinter.Button(text="Click me", command= click_button)
button.grid(column=1, row=1)
# button.pack()

newbutton = tkinter.Button(text="Click me too", command= click_button)
newbutton.grid(column=3, row=0)
# newbutton.pack()

input = tkinter.Entry()
print(input.get())
input.grid(column=4, row=3)
# input.pack()



window.mainloop()

## *ARG: multiple arguments
## **KWARG : dictionary arguments
# def add(*arg):
#     list = []
#     for n in arg:
#         list.append(n)
#         total = sum(list)
#     print(total)

# add(1,2,3,4,5)

# def cal(**kwargs):
#     print(kwargs["add"])


# cal(add=5,multiply = 7)