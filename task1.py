from sys import argv

name, working, rate, prize = argv

print('имя скрипта: ', name)
print('выработка в час : ', working)
print('ставка в час: ', rate)
print('премия : ', prize)
score = (int(working) * int(rate)) + int(prize)
print('заработная плата сотрудника составила: ', score)
