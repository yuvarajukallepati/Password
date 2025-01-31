# This code will give you a strong password of your desired length.


import random
length=int(input("enter the length of password: "))
if(length>3):
    n_letters=int(input("enter the no of letters: "))
    n_numbers=(int(input("enter the no of numbers:")))

    letters=['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pwd=[]
    for i in range(n_letters):
        char=random.choice(letters)
        pwd += char
    for i in range(n_numbers):
        num=random.choice(numbers)
        pwd += num
    print(pwd)
    random.shuffle(pwd)
    print(pwd)

    password=""
    for char in pwd:
        password+=char
    print(password)

else:
    print("password length must be greater than 3 digits")
    