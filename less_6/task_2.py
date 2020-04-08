#Дано: массив чисел (float или/и int).

#Задание: нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом. Если список пуст, то результат равен 0 (ноль).

#Числа с плавающей точкой представлены в компьютерах как двоичная дробь. Результат проверяется с точностью до третьего знака, как ±0.001

#Пример:

elements1 = [1, 2, 3] # результат: 2
elements2 = [5, -5] # результат: 10
elements3 = [10.2, -2.2, 0, 1.1, 0.5] # результат: 12.4
elements4 = [] # результат: 0

def get_diff_between_max_min_el(elements):
  if not elements:
    print(0)
    return

  max_el = max(elements)
  min_el = min(elements)

  diff = max_el - min_el
  print('{0:.3f}'.format(diff))
  return


get_diff_between_max_min_el(elements1)
get_diff_between_max_min_el(elements2)
get_diff_between_max_min_el(elements3)
get_diff_between_max_min_el(elements4)

#print(abs(5 - 5))