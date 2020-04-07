#Дано: Число, как целочисленное (int).

#Задание:

#"Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

#Вы должны написать программу, которая принимает положительное целое число и возвращает сл. значения.

#"Fizz Buzz", если число делится на 3 и 5;
#"Fizz", если число делится на 3;
#"Buzz", если число делится на 5;
#Число, как строку для остальных случаев.

#Пример:

 #x = 15, результат: "Fizz Buzz"
 #x = 6, результат: "Fizz"     
 #x = 5, результат: "Buzz"   
 #x = 7, результат: "7"

def fizz_buzz(num):
  if num % 3 == 0 and num % 5 == 0:
    print('Fizz Buzz')
    return
  elif num % 3 == 0:
    print('Fizz')
    return
  elif num % 5 == 0:
    print('Buzz')
    return
  print(num)
  return

fizz_buzz(15)
fizz_buzz(6)
fizz_buzz(5)
fizz_buzz(7)