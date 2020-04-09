#Дано: словарь ФИО - номер телефона(dict).

#Задание: получить новый словарь, инвертировав исходный, т.е. пары ключ - значение поменять местами (значение - ключ).

#Пример:

book = {'Petr': '546810', 'Katya': '241815'} # результат: {'546810': 'Petr', '241815': 'Katya'}

def data_reverse(data):
  keys = data.keys()
  values = data.values()

  print(dict(zip(values, keys)))

data_reverse(book)