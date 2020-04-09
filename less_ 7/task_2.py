#Дано: целое число (int).

#Задание: Римские цифры пришли к нам из древней римской системы счета. Они основаны на особых буквах алфавита, которые в различных сочетаниях, путем суммирования (а иногда и разницы) описывают различные числа. Первые 10 римских чисел это:

ten = {
  1: 'I',
  4: 'IV',
  9: 'IX',
  10: 'X',
  50: 'L',
  100: 'C',
  500: 'D',
  1000: 'M'
}

#Римская система счета имеет десятичное основание, но она непозиционная и не включает в себя 0 (ноль). Римские числа образуются путем комбинации следующих семи символов:

#Символ Значение I 1 (unus) V 5 (quinque) X 10 (decem) L 50 (quinquaginta) C 100 (centum) D 500 (quingenti) M 1,000 (mille) Узнать больше о римских цифрах вы можете в статье на Википедии.

#В этой задаче, вам необходимо преобразовать данное целое число (от 1 до 3999) в римскую систему счета.

#Пример:

x1 = 6 # результат: 'VI'
x2 = 76 # результат: 'LXXVI'
x3 = 13 # результат: 'XIII'
x4 = 44 # результат: 'XLIV'
x5 = 3999 # результат: 'MMMCMXCIX'

def roman_translator(x): #перевод в римские
    roman = ''
    if x > 3999:
      print ("is`t possble.")
    else:
      for arabic, keys in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1), 'M CM D CD C XC L XL X IX V IV I'.split()):
          roman += x // arabic * keys
          x %= arabic
    print(roman)
    return

roman_translator(x1)
roman_translator(x2)
roman_translator(x3)
roman_translator(x4)
roman_translator(x5)