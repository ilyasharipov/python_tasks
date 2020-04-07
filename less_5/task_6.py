#На протяжении веков, левши страдали от дискриминации в мире, созданном для правшей." Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.

#"Большинство людей (70-95%) правши, меньшинство (5-30 %) левши, и неопределеное число людей вероятно лучше всего охарактеризовать, как "симметричные"." Scientific American. www.scientificamerican.com

#Один робот был занят простой задачей: объединить последовательность строк в одно выражение для создания инструкции по обходу корабля. Но робот был левша и зачастую шутил и запутывал своих друзей правшей.

#Дано: последовательность строк.

#Задание: вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми. В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре.

#Примеры:

a = ["left", "right", "left", "stop"] # результат: "left,left,left,stop"
b = ["bright aright", "ok"] #результат: "bleft aleft,ok"
c = ["enough", "jokes"] #результат: "enough,jokes"

def get_things_for_left_handed(text_block):
  #print(text_block)
  text_for_left_handed = ''

  for word in text_block:
    #print(word)
    if word == 'right':
      text_for_left_handed += 'left,' 
    else:
      text_for_left_handed += word + ','

  result = text_for_left_handed[:-1] + ''

  print(result)
  return

get_things_for_left_handed(a)
get_things_for_left_handed(b)
get_things_for_left_handed(c)