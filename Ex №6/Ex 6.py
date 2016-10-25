import string
A=dict()

# Открыть файл на чтение в кодировке UTF-8
file_in = open('en-ru1.txt', 'r', encoding="UTF-8")


i=1
print("-----Чтение из файла------")
# Считать файл построчно
for stroka in file_in.readlines():
 stroka_spisok=[]
# Отделить английское слово от перевода
 stroka_spisok=stroka.split('\t-\t')

#  убрать символы перевода строк
 string=stroka_spisok[1]
 if string[-1]=='\n':
   stroka_spisok[1]=string[:-1]



#------------ Формирование словаря---------------
 key=stroka_spisok[1] # очередное русское слово
 if key in A: # есть такое слово, добавляем новый перевод в список
         A[key].append(stroka_spisok[0])
 else: # создаём новый список перевода пока неизвестного русского слова
         A[key] =[]
         A[key].append(stroka_spisok[0])


file_in.close() # считан весь исходный файл



print("-----Сортировка------")
# Словарь отсортировать нельзя, но можно сортировать ключи
keys_sort = A.keys() # получаем ключи для сортировки
keys_sort = list(keys_sort) # превращаем ключи в обычный список
keys_sort.sort() # сортируем список ключей

print("-----Вывод в файл------")
# Открыть файл на запись в кодировке UTF-8
file_out = open('ru_en.txt', 'w', encoding="UTF-8")
for key in keys_sort: # вывод элементов словаря (ключ - значение) по алфавиту
    string=str(key)+"-"+', '.join(A[key])
    print(string, file=file_out)

file_out.close()
