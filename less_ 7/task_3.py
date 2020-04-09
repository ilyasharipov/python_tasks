#Дано: словарь банк - курс доллара (dict).

#Задание: определить банк и курс покупки валюты с наиболее привлекательным предложением.

#Пример:

rates = {'Sberbank': 55.8, 'VTB24': 53.91} # результат: VTB24 -> 53.91 

def lazy_convertor(data):
  bank = ''
  best_rate = list(rates.values())[0]

  for key, value in data.items():
    if (value <= best_rate):
      bank = key
      best_rate = value

  print('{} -> {}'.format(bank, best_rate))
  return

lazy_convertor(rates)