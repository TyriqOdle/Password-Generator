import random
from tkinter import *


def generate():

    # Opens the password file in append mode.
    file = open("passwords.txt", "a")

    password = ""
    # Letters
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

    # Numbers
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Special characters
    special_chars = [
        '!', '@', '#', '$', '%', '^', '&', '*',
    ]
    platform = platform_input.get()
    username = userName_input.get()
    length = length_slider.get()

    # Creating the password based ont he length

    for i in range(length):
        password += random.choice(random.choice(letters + numbers + special_chars))

    # Adding the new password, username and password to the file

    file.write(platform + "\t" + username + "\t" + password + "\n")
    file.close()

    # Displayes a message when the password is added to the file.

    successText = Label(window,text="Password Has been successfully saved to the file.", fg="green")
    successText.pack()

    # Resets the inputs

    platform_input.delete(0,END)
    userName_input.delete(0,END)
    

    print("Password Has been successfully saved to the file.")


window = Tk() # Creates the window


window.title("Password Generator")

window.geometry("400x400")

label = Label(window, text="Welcome to Password Generator")

label.pack()

# Platform Input Ui
platform_label = Label(window,text="Platform/Website")
platform_input = Entry(window)
platform_label.pack()
platform_input.pack()

# Username Input Ui
userName_label = Label(window, text="Username")
userName_input = Entry(window)
userName_label.pack()
userName_input.pack()


# Length Input Ui scale

length_label = Label(window,text="Password Length")
length_label.pack()

length_slider = Scale(window, from_=10, to=100,orient=HORIZONTAL)
length_slider.pack()


# Submit button

submit = Button(window, text="Submit", command=generate)
submit.pack()




window.mainloop()






