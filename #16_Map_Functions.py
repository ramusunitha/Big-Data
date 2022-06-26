#Map Function in Python

def mul(i):
    return(i*i)

print("\nStarting the Program")
x=list(map(mul,(3,5,7,9,11,13)))
print("\nOutput from the map function is: {}".format(x))
print("\nEnding the Program")
