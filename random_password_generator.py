#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      milo
#
# Created:     16/01/2020
# Copyright:   (c) milo 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def generate_password(password_lenght, number_of_letters, number_of_numbers):
    import random
    import string

    password = []
    numbers = 0
    letters = 0
    letters_and_numbers = string.ascii_letters + string.digits

    for i in range(password_lenght):

        if letters >= number_of_letters:
            char = random.choice(string.digits)
        elif numbers >= number_of_numbers:
            char = random.choice(string.ascii_letters)
            print(numbers)
        else:
            char = random.choice(letters_and_numbers)
            if str.isdigit(char) == True:
                numbers += 1
            else:
                letters += 1
        password.append(char)
        print(type(char))


    password = ''.join(map(str, password))
    return password



def main():
    while True:
        password_lenght = int(input("Enter passworld lenght"))
        number_of_letters = int(input("Enter number of letters"))
        number_of_numbers = int(input("Enter number of numbers"))

        if number_of_letters + number_of_numbers == password_lenght:
            password = generate_password(password_lenght, number_of_letters, number_of_numbers)
            print("Password : ",password)
            break
        else:
            print("Input error!")



if __name__ == '__main__':
    main()
