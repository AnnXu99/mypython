import math

A = input("first input : ")
B = input("second input : ")

math_op = input("math type : ")

if('+' in math_op): #For addtion of two variables
    print(float(A) + float(B))
elif('-' in math_op): #subtranction, the elif stands for else if
    print(float(A) - float(B))
elif('*' in math_op):
    print(float(A) * float(B))
elif('/' in math_op):
    print(float(A) / float(B))


