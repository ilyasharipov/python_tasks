#Дано: список (list) целых чисел (int).

#Задание: нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива.

#Пример:

elements1 = [0, 1, 2, 3, 4, 5] # результат: 30
elements2 = [1, 3, 5] # результат: 30
elements3 = [] # результат: 0

def get_sum_even_elements(elements):
  if not elements:
    print(0)
    return

  result = 0;
  last_index = elements[-1]

  for i, el in enumerate(elements1):
      result += el if (i % 2 == 0) else 0
  
  print(result * last_index)
  return

get_sum_even_elements(elements1)
get_sum_even_elements(elements2)
get_sum_even_elements(elements3)