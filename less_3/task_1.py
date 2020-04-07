#Дано: имя и фамилия.
name = 'Ilya'
last_name = 'Sharipov'

#Задание: написать программу, которая будет приветствовать нового человека в мире Python. Текст приветсвия: Hello NAME SURNAME! You just delved into Python. Great start!
#Пример: Hello Ibrahim Petrov! You just delved into Python. Great start!

text = 'Hello {} {}! You just delved into Python. Great start!'

print(text.format(name, last_name))