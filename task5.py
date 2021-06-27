my_list = [8, 7, 6, 5, 4, 3, 2, 1]
message = int(input('enter number ......'))
i = 0
for n in my_list:
    if message <= n:
        i += 1
    else:
        break
my_list.insert(i, message)
print(my_list)
