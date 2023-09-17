import tkinter as tkr
import random
import string

def passwored():
    length = int(length_entry.get())
    include_numbers = numbers_var.get()
    include_characters = characters_var.get()
    namein = name_entry.get()

    if include_numbers and include_characters:
        charset = string.ascii_letters + string.digits
    elif include_numbers:
        charset = string.digits
    elif include_characters:
        charset = string.ascii_letters
    else:
        charset = ""

    password = ""

    if namein:
        before = ''.join(random.choice(charset) for _ in range(length - len(namein)))
        after = ''.join(random.choice(charset) for _ in range(length - len(namein)))
        password = before + namein + after
    else:
        password = ''.join(random.choice(charset) for _ in range(length))

    result_label.config(text="Generated Password: " + password)

window = tkr.Tk()
window.title("Random Password Generator")
window.geometry("400x300")
window.configure(bg="white")
length_label = tkr.Label(window, text="Password Length:")
length_label.pack()
length_entry = tkr.Entry(window)
length_entry.pack()
numbers_var = tkr.IntVar()
numbers_checkbox = tkr.Checkbutton(window, text="Include Numbers", variable=numbers_var)
numbers_checkbox.pack()
characters_var = tkr.IntVar()
characters_checkbox = tkr.Checkbutton(window, text="Include Characters", variable=characters_var)
characters_checkbox.pack()
name_label = tkr.Label(window, text="Name to Include:")
name_label.pack()
name_entry = tkr.Entry(window)
name_entry.pack()
generate_button = tkr.Button(window, text="Generate Password", command= passwored)
generate_button.pack()
result_label = tkr.Label(window, text="")
result_label.pack()
window.mainloop()