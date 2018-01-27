import os
import chardet

def parsing():
   folder = os.listdir()
   print(folder)
   for file in folder:
       if file.endswith('.txt'):
            with open(file, 'rb') as f:
                words = []
                for line in f:
                    enc = chardet.detect(line)
                    line = line.decode(enc['encoding'])
                    words += line.split(' ')
                words.sort(key=lambda val: len(val) <= 6)
                new_words = [word for word in words if len(word)>=6]
                unique_words=sorted(set(new_words), key=lambda val: new_words.count(val), reverse=True)
                print('Файл {} топ 10 слов: '.format(file), unique_words[:10])
parsing()