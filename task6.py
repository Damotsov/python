start = float(input('введите результат первого дня....'))
finish = float(input('ввдеите результат второго дня....'))
day = 0
while start < finish:
    start = start + start * 0.1
    day += 1
    print(f'{day}-й день: {start:.1f}')
