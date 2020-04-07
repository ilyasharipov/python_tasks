#Давайте научим наших роботов отличать слова от чисел.

#Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв.

#Дано: Строка со словами (str).

#Задание: напишите программу, которая проверяет есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.

#Примеры:

def is_three_words_in_a_row(text):
  words = text.split()
  counter = 0

  for word in words:
    counter += 1 if word.isalpha() else counter
  print(counter == 3)
  return counter == 3

text1 = "Hello World hello" #результат: True
text2 = "He is 123 man" #результат: False
text3 = "1 2 3 4" #результат: False

is_three_words_in_a_row(text1)
is_three_words_in_a_row(text2)
is_three_words_in_a_row(text3)
