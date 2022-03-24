import os
path = os.getcwd()

def file_read_write():
    #________________________________________________
    filelist =[]                                            #Создаем список из трех файлов
    for root, dirs, files in os.walk(path):
        for file in files:
            if (file.endswith(".txt")):
                filelist.append(os.path.join(file))
    #________________________________________________
    file_text = {}                                          #Сортируем файлы
    file_len = {}
    for name_file in filelist:
        with open(name_file, encoding='UTF-8') as f:
            l = 0
            for line in f:
                l += 1
                file_len[name_file] = l
    for name_file in filelist:
        with open(name_file, encoding='UTF-8') as f:
            file_text[name_file] = f.read()
    file_len_sort = dict(sorted(file_len.items(), key=lambda item: item[1]))
    #________________________________________________
    with open('dz_fail.txt', 'a', encoding='utf-8') as w:    #Записываем в созданный файл
        for file in file_len_sort:
            w.write(file + '\n')
            w.write(str(file_len[file]) + '\n')
            w.write(file_text[file] + '\n')

file_read_write()




