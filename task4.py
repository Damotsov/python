number = int(input('enter number>>>'))
maximum = number % 10#получаем последнюю цифру
while number > 1:
    number = number // 10
    if number % 10 > maximum:#получаем вторую и сравниваем с первой
        maximum = number % 10
    if number > 9:# а тут в случае если вторая цифра оказалась большой сокращаем ее возвращая в начало цикла
        continue
    else:
        print('максимальное число- ', maximum)
        break
