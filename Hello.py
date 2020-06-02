a = 1
print (a)
b = 1
print (b)
for i in range(10000):
    c = a + b
    print (c)
    a = b
    b = c
