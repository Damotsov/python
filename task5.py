def foo():
    result = 0
    flag = True
    while flag:

        num = input('enter number or`q` for exit').split()
        for key in num:
            try:
                number = int(key)
                result += number

            except:
                if key == 'q':
                    print(f'сумма равна : {result}')
                    flag = False
                else:
                    print(f'результат {result},далее возникла ошибка ввода')
                    flag = False
        print(f'конечный результат: {result}')


foo()
