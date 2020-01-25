# Рекурсивный проход по всем каталогам в заданной директории,
# удалить все файлы из директории, созданные или измененные сегодня,
# в названии которых встречается del, вывести список удаленных файлов

import os
import datetime

print('Введите путь к папке, в которой нужно удалить файлы, в названии которых встречается del: ')
directory_path = input()
file_name = "del"
delete_list = []


# дата и время создания файла
def modification_date(path):
    unix_time = os.path.getmtime(path)  # время последнего изменения файла в сек
    time = datetime.datetime.fromtimestamp(unix_time)

    return time.date()  # функция возвращает


if os.path.exists(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for name in files:
            if name.find(file_name) != -1:  # поиск файлов, в имени которых встречается del
                '''Метод join позволяет совместить несколько путей при помощи присвоенного разделителя'''
                print('Путь к файлу с именем del:')
                print(os.path.join(root, name))  # вывод пути файла, где в названии встречается del
                print(files)  # вывод набора файлов, находящихся в папке
                file_date = modification_date(os.path.join(root, name))
                print('Дата создания/изменения файла:', file_date)
                now = datetime.datetime.now()
                print('Сегодня:', now.date())

                if file_date == now.date():
                    delete_list.append(files)
                    # os.remove(os.path.join(root, name))  # удаление файлов с именем del
                else:
                    print('Файлов созданных или измененных сегодня нет!')
else:
    print('Такого пути нет!')

print('Удаленные файлы:', delete_list)
file = open("out.txt", "w")
for item in delete_list:
    file.write("%s\n" % item)
file.close()

# dirs это список директорий в текущей директории
# files - список файлов в текущей директории
# root - путь до файла(или каталога) в текущей точке итерации