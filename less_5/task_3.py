#Дано: Число N = [1-9].

#Задание: нужно написать программу, которая выведет последовательность 123..N

#Пример:

 #N = 3, результат: 123
 #N = 9, результат: 123456789     
 #x = 1, результат: 1

def get_sequence(num):
  i = 0
  sequence = ''

  while num > 0:
    i += 1
    sequence += str(i)
    num -= 1
  
  print(sequence)
  return

get_sequence(3)
get_sequence(9)
get_sequence(1)