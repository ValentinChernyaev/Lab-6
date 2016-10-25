import string

def Translate_word(word):
 str_add=""
 punct=""
 rus_word=""

 if word.istitle():
  # Слово было заглавным
   was_title=True
 else:
   was_title=False
 # Последний символ знак пунктуации
 if word[len(word)-1] in string.punctuation:
    str_add=word[len(word)-1:len(word)]
    # str_add="."
    punct=True #слово было со знаком
 if punct==True:
    word_trans=word[0:len(word)-1].lower() # режем
 else: # резать не надо
    word_trans=word.lower()

 if word_trans in A:
    if was_title:
      rus_word=A[word_trans].title()+str_add
    else:
      rus_word=A[word_trans]+str_add
 else:
      rus_word=word
 return rus_word


stroka_rus_spisok=[]
A=dict()
# Считать словарь
file_dict = open('c:\en-ru.txt', 'r', encoding="UTF-8")


i=1
#------------Ввод словаря--------------
for stroka in file_dict.readlines():
    stroka_spisok=stroka.split()
    key=stroka_spisok[0] # ключ английское слово
    A[key]=stroka_spisok[2] # значение перевод
    # print(i, key, A[key])
    i+=1
file_dict.close() # считан весь файл словаря

file_in = open('c:\input.txt', 'r')
file_out= open('c:\output.txt', "w",encoding="UTF-8")

print("---------------------------------------------")
for stroka in file_in.readlines(): # перебрать все строки
    stroka_rus_spisok=[] # очистить список для перевода строки
    stroka_spisok=stroka.split()

    for eng_word in stroka_spisok: # перебрать строку по словам
       rus_word=Translate_word(eng_word) # перевести слово функцией
       stroka_rus_spisok.append(rus_word) # добавить перевод слова
       # в список строки

    print(' '.join(stroka_rus_spisok)) # вывод на экран
    print (' '.join(stroka_rus_spisok), file=file_out)  # через print в файл



print("---------------------------------------------")

file_in.close()
file_out.close()



