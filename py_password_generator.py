import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','#','/','&','(',')','*','+']

print("------ Welcome to PyPassword generator ------")
nr_letters = int(input("enter the number of letters you want :\n"))
nr_numbers = int(input("enter the number of digits you want :\n"))
nr_symbols = int(input("enter the number of symbols you want :\n"))

password_list = []
for char in range(0,nr_letters):
    password_list.append(rd.choice(letters))
for char in range(0,nr_numbers):
    password_list.append(rd.choice(numbers))
for char in range(0,nr_symbols):
    password_list.append(rd.choice(symbols))
password = ""        
rd.shuffle(password_list)
for char in password_list:
    password += char
print(f"Your password is: {password}")     
