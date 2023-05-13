import random

a =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_len = int(input('Введите длину пароля:'))
password = ''
if password_len <= 0:
    print("Ошибка: 404 (необходимо написать положительное число, которое больше 0)")

for i in range(password_len):
    password += random.choice(a)

print(password)

