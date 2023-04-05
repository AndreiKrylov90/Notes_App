# Даны два слова и словарь. Требуется построить цепочку слов от первого слова до второго, 
# в котором каждые два соседних слова принадлежат словарю и отличаются только в одной букве.

import requests
import re

response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

text = response.content.decode('cp1251')

with open('russian.txt', 'wb') as ru:
    ru.write(text.encode('utf-8'))

wordA = list(input("Введите первое слово: "))
wordB = list(input("Введите второе слово из такого же количества букв: "))

alphabet = 'ёйцукенгшщзхъэждлорпавыфячсмитьбю'
alphabet = list(alphabet)

if str("".join(wordA)) not in text:
    print("Вы ввели неправильно слово")
if str("".join(wordB)) not in text:
    print("Вы ввели неправильно слово")

def chain_of_words(wordA, wordB):
    temp = [0] * len(wordA)
    for i in range(len(wordA)):
        temp[i] = wordA[i]
        
    i = 0
        
    if str("".join(wordA)) == str("".join(wordB)):
        print("".join(wordA), "".join(wordB))
        return
    else:
        while i < len(wordA):
            j = 0
            while j < len(alphabet):
                temp[i] = alphabet[j]
                if str("".join(temp)) in text:
                    print("".join(wordA))
                    wordA[i] = temp[i]
                    if str("".join(wordA)) == str("".join(wordB)):
                        print("".join(wordB))
                        return
                    else:
                        break
                else:
                    j +=1
            i +=1
        chain_of_words(wordA, wordB)
chain_of_words(wordA, wordB)