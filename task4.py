translater = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_list = []
result = []
try:
    file_obj = open("task4.txt", 'r',encoding='utf-8')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word +' - '+ tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("test_4_input.txt", "w",encoding='utf-8')
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close()