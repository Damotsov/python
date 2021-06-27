active = True
other = []
while active:
    message = input('введите элемент который необходимо добавить в список....')
    if message == 'q':
        active = False
    else:
        other.append(message)
    for i in range(1, len(other), 2):
        other[i - 1], other[i] = other[i], other[i - 1]
print(other)