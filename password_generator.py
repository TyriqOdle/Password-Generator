import random

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


# User selects the platform name for the password

platform = input("Enter the plarform for this password: ")

# User selects the username name for the password

username = input("Enter the username: ")

# User selects length

user_length = int(input("1. Short (10 Characters)" \
"2. Medium (15 characters)" \
"3 Long (24 Characters)" \
"Select a length: "))

# Determaining the length based on the input

if user_length == 1:
    length = 10
elif user_length == 2:
    length = 15
else:
    length = 24



for i in range(length):
    password += random.choice(random.choice(letters + numbers + special_chars))


file.write(platform + "\t" + username + "\t" + password + "\n")
file.close()

print("Password Has been successfully saved to the file.")

