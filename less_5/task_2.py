#Дано: Число x.

#Задание: нужно написать программу, которая дает оценку заданному значению, используя следующие правила.

#если x нечетное, то это "Плохо"
#если x = [2, 5] и четное, то это "Неплохо"
#если x = [6, 20] и четное, то это "Так себе"
#если x > 20 и четное, то это "Отлично"
#Пример:

 #x = 15, результат: "Плохо"
 #x = 4, результат: "Неплохо"     
 #x = 8, результат: "Так себе"   
 #x = 24, результат: "Отлично"

def get_rating_value(num):
  if num % 2 != 0:
    print('Плохо')
    return
  elif num > 20 and num % 2 == 0:
    print('Отлично')
    return
  elif num >= 6 <= 20 and num % 2 == 0:
    print('Так себе')
    return
  elif num % 2 == 0 and num >= 2 <= 5:
      print('Неплохо')
      return

#Плохо
get_rating_value(3)
get_rating_value(7)
#Неплохо
get_rating_value(2)
get_rating_value(4)
#Так себе
get_rating_value(6)
get_rating_value(20)
#Отлично
get_rating_value(24)
get_rating_value(26)
#Примеры
get_rating_value(15) # 'Так себе'
get_rating_value(5) # 'Плохо
get_rating_value(8) # 'Так себе'