#Дано: кортеж или список чисел.

#Задание: Медиана - это числовое значение, которое делит сортированый массив чисел на большую и меньшую половины. В сортированом массиве с нечетным числом элементов медиана - это число в середине массива. Для массива с четным числом элементов, где нет одного элемента точно посередине, медиана - это среднее значение двух чисел, находящихся в середине массива. В этой задаче дан непустой массив натуральных чисел. Вам необходимо найти медиану данного массива.

#Пример:

elements1 = [1, 2, 3, 4, 5] # результат: 3
elements2 = [3, 1, 2, 5, 3] # результат: 3
elements3 = [1, 300, 2, 200, 1] # результат: 2
elements4 = [3, 6, 20, 99, 10, 15] # результат: 12.5

def get_median_value(coll):
  sorted_coll = sorted(coll)
  if len(sorted_coll) % 2 != 0:
    index = round(len(sorted_coll) / 2)
    print(sorted_coll[index])
    return
  elif len(sorted_coll) % 2 == 0:
    index = round(len(sorted_coll) / 2)
    print(sorted_coll[index])
    average = (sorted_coll[index] + sorted_coll[index - 1]) / 2
    print(average)
    return
  return

get_median_value(elements1)
get_median_value(elements2)
get_median_value(elements3)
get_median_value(elements4)