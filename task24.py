'''
Напишите функцию которая будет определять полигдром ли введенная строка. Если да 2
то печатать “True”, если нет “False”.
'''

def polidrom_word(word):
    if word == word[::-1]:
        print("True")
    else:
        print('False')

polidrom_word('мадам')

polidrom_word('слово')