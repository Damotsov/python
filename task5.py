proceeds = int(input('введите значение выручки...'))
costs = int(input('введите издержки...'))
result = proceeds - costs
profitability = result / result

if proceeds > costs:
    print('выручка больше издержек')
    print(f'выручка составила: {result}')
    print(f'рентабельность составила: {profitability}')
elif proceeds < costs:
    print('отработали в минус!')
    print(f'минус составил- {result}')
else:
    print('отработали в ноль')

staff = int(input('введите колличество сотрудников...'))
for_one = result // staff
print(f'прибыль на одного сотрудники составила : {for_one}')
