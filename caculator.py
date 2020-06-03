def add(a, b):
    print (a, " + ", b,  " = ", (a+b))
    return a+b

def minus(a, b):
    print (a, " - ", b,  " = ", (a-b))
    return a-b

def multiply(a, b):
    print (a, " * ", b,  " = ", (a*b))
    return a*b

def divide(a, b):
    print (a, " / ", b,  " = ", (a/b))
    return a/b


print (divide (multiply (minus ( add(1,2), 4), 100), 20) )