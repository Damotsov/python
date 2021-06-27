num_one = int(input('enter ....'))
num_two = int(input('enter...'))


def foo(a, b):
    if a & b != 0:
        result = a // b
        print(result)
    else:
        print('не корректные данные')


foo(num_one, num_two)
