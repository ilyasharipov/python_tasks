#**Дано:**  текст, как строка (str).
 
#**Задание:**  Наши Роботы никогда не упускают возможности, чтобы улучшить свои навыки в лингвистике. Сейчас они изучают английский алфавит и что с этим делать.

#Алфавит разделен на гласные и согласные буквы (да, мы разделили буквы, а не звуки).

vowels = 'A E I O U Y'.split()

consonants = 'B C D F G H J K L M N P Q R S T V W X Z'.split()

#Дан текст с разными словами и/или числами, которые разделены пробелами и знаками пунктуации. Числа не считаются за слова (также как и смесь букв и цифр). Необходимо подсчитать слова, в которых гласные буквы чередуются с согласными (полосатые слова), то есть в таких словах нет двух гласных или двух согласных букв подряд. Слова состоящие из одной буквы - не "полосатые" (не считайте их). Регистр букв не имеет значения.

     
 #**Пример:**
 
text1 = "My name is ..." # результат: 3
text2 = "Hello world" # результат: 0
text3 = "A quantity of striped words." # результат: 1
text4 = "Dog,cat,mouse,bird.Human." # результат: 3

def check_for_banding(text):
  text_coll = text.replace(',', ' ').replace('.', ' ').upper().split()
  min_word_len = 2
  counter = 0

  for word in text_coll:
    prev = ''

    if len(word) < min_word_len:
        continue # делаем пропуск итерации если длина слова меньше нужной длины. он не учитывается
    for i in word:
      cur = '' #чередуем с локальными переменными. та что выше запоминает с итерации ниже инф
      if i in vowels:
        cur = 'vowel'
      elif i in consonants:
        cur = 'consonant'
      if cur == prev:
        break
      prev = cur
    else:
      counter += 1
  print(counter)
  return



check_for_banding(text1)
check_for_banding(text2)
check_for_banding(text3)
check_for_banding(text4)