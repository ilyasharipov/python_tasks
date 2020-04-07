#Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
#Для примера: Дано число 123405. Результат будет: 12345=120 (не забудьте исключить нули).

#Дано: положительное целое число.
#Задание: необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.

#Примеры:
#Дано число 123405. Результат будет: 12345=120 (не забудьте исключить нули).

def get_value_smart_multiplication(num):
  if (num <= 0):
    print(0)
    return

  string = str(num)
  i = 0
  result = 1

  while i < len(string) - 1:
    result += int(string[i]) if int(string[i]) == 0 else result * int(string[i])
    i += 1
  print(result)

  return


get_value_smart_multiplication(123405)
get_value_smart_multiplication(100000002345)
get_value_smart_multiplication(-5)
get_value_smart_multiplication(0)