
# print value of pi upto n decimal place

import math
c=math.pi
n = int(input())
for i in range(1,n+1):
    c= math.pi
    d=("{:.{}f}").format(c,i)
    print(d)


