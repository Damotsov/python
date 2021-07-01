from itertools import count
from itertools import cycle
for i in count(1):
    if i == 50:
        break
    else:
        print(i)
##########################################################
c=0
for i in cycle('rep'):
    if c > 10:
        break
    print(i)
    c += 1

