#import tkinter
from tkinter import *

def button_clicked():
    my_text = input.get()
    my_label.config(text=my_text)
#    my_label.config(text=my_text.get())

window = Tk()
window.title("My first GUI program")
window.minsize(600, 300)
window.config(padx=100, pady=200)

#Labels

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Buttons

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=2, row=0)

#Entry
#my_text = StringVar()
#input = Entry(width=10, textvariable=my_text)
input = Entry(width=10)
input.grid(column=3, row=3)





window.mainloop()
