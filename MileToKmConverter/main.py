from tkinter import *

def convert():
    km = float(miles_input.get()) * 1.609
    km = round(km, 2)
    result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)
km_label = Label(text="km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)
result_label= Label(text="0")
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

window.mainloop()