
# lambda
a=lambda x :x+5
print(a(2))

b=lambda x,y:x+y
print(b(2,3))

c=lambda x,y :x if (x>y) else y
print(c(2,4))

d=lambda x:x*x
print(d(4))

# map
lst=[1,2,3,4,5,6]
l=list(map(lambda x:x+5,lst))
print(l)

#filter 
lst=[1,2,3,4,5,6,7,8]
l=list(filter(lambda x:x%2,lst))
print(l)

#reduce
lst=[1,2,3,4,5,6,7,8]
from functools import reduce
y=reduce(lambda x,y :x+y,lst)
print(y)
