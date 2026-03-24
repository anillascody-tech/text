#交换a,b的值
a,b = 10,20
print(a,b)
a,b = b,a
print(a,b)
c = a
a = b
b = c
print(a,b)

#练习2,a=1,b=2,c=3,将abc赋值给cab
a,b,c = 1,2,3
d = a#abca
a = c#cbca
c = b#cbba
b = d#caba
print(a,b,c)

