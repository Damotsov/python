message = input('enter string.....').split()
for n, i in enumerate(message, 1):
    print(n, i) if len(i) <= 10 else print(n, i[:10])
