#Recursive Function - Simple Example - Factorial

def func1(a):
    if a==1:
        return a
    else:
        return a*func1(a-1)

print(func1(4))