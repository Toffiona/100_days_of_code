from tkinter import *

# CREATE A NEW WINDOW OBJECT FROM Tk CLASS AND CONFIGURATION
window = Tk()
window.title("Widget Example")
window.minsize(width= 500, height=300)

# CREATE LABEL from Label CLASS
label = Label(text="This is old text")
#use config function to change the text of label
label.config(text="This is new text")
label.pack()

# CREATE BUTTONS from Button CLASS and give command (function) to button after user click on it
def action():
    print("Do something")
button = Button(text="Click here", command=action)
button.pack()

# CREATE ENTRIES (single line text) from Entry Class
entry = Entry(width=30)
# add text to entry to begin with (to tell user what to do)
entry.insert(END, string="Some text to begin with")
# get/print the text from entry
print(entry.get())
entry.pack()

# TEXT: Create text box
text = Text(width=30, height=5)
# put cursor in the textbox
text.focus()
# Add some text to begin with
text.insert(END, "Examples of multi-lines text entry \nthis is, new line")
#Get's current value in textbox at line 1, character 0
print(text.get("2.2", END))
text.pack()

# Create spinbox from Spinbox Class and give command(function) when user select an option)
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command = spinbox_used)
spinbox.pack()

# Create scale from Scale Class and give command when user select a scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=10, command= scale_used)
scale.pack()

# Create Check Button from Checkbutton Class
def checkbutton_used():
    print(checked_state.get())
    # Create varaible to hold on to checked state from IntVar Class, 0 is off and 1 is on
checked_state = IntVar()
checked_state.get()

checked_button = Checkbutton(text="Is on?", variable=checked_state, command = checkbutton_used)
checked_button.pack()

# Create radio button from Radiobutton Class
def radiobutton_checked():
    print(radio_state.get())

    # create the variable to hold on to the value of radito button been checked/selected
radio_state = IntVar()

radiobutton1 = Radiobutton(text="Option 1", value=1, variable= radio_state, command=radiobutton_checked)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable= radio_state, command=radiobutton_checked)
radiobutton1.pack()
radiobutton2.pack()

# Create listbox from Listbox and give command when an item selected from list
def listbox_used(e):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()





window.mainloop()
