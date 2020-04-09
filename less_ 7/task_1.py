#Дано: текст (str).

#Задание: необходимо получить 2 словаря (популярности слов и популярности символов, букв).

#Пример:

text = "hello, word of word" # результат: 
     #chars_popularity = {'h': 1, 'e': 1, 'l': 2, ..};
     #words_popularity = {'hello': 1, 'word': 2, 'of': 1}

def text_analysis_for_popularity(text):
  words = text.replace(',', ' ').split()
  #print(words)
  chars_popularity = {}
  words_popularity = {}

  for word in words:
    words_popularity[word] = 1 if word not in words_popularity else words_popularity[word] + 1
    for char in word:
      chars_popularity[char] = 1 if char not in chars_popularity else chars_popularity[char] + 1
      
  print(words_popularity)
  print(chars_popularity)
  return


text_analysis_for_popularity(text)