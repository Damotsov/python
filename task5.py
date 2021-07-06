try:
    with open('task5.txt', 'w+', encoding='utf-8') as file_obj:
        line = input('введите цифры через запятую ...\n')
        file_obj.writelines(line)
        numb = line.split()
        print(sum(map(int,numb)))
except IOError:
    print('ошибка в файле')
except ValueError:
    print('неправильно набран номер.Ошибка')