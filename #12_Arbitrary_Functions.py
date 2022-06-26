def arb_func(*args):
    print(args)
    print(type(args))
    final_result=args[0]+'.'+args[1]+args[2]
    return final_result

def func1(**a):
    print('Any type of arguments will be placed in a dictionary')
    print(a)
    print(type(a))
    print(a['x']+a['y'])

def func2(*a):
    print('Any arguments will be in a tuple')
    print(a)
    print(type(a))
    if len(a)==3:
        print("Salary+Bonus-Deduction:"+str(a[0]+a[1]-a[2]))
        res=a[0]+a[1]-a[2]
        print("On Hand Salary is {}".format(res))
    else:
        print(a)

print("\n1. Arbitrary Function - With Tuple *args")
print(arb_func('md','irfan','@inceptez.com'))

print("\n2. Arbitrary Functions - With Dictionary **args")
func1(y=200,x=100)

print("\n3. Arbitary Functions - With Tuple *a logic")
func2(1000,2000)
func2(1000,2000,500)

print("\n4. Arbitrary Functions - With Dictionary arguments **a - Mismatched Key names")
try:
    func1(a=1000,b=4000)
except KeyError as excpvalue:
    print("Exception of {} occurred".format(excpvalue))

print("\n5. Arbitrary Functions - With Dictionary arguments **a - Without Keys")
try:
    func1(1000,4000)
except Exception as newval:
    print("Exception Occurred - {}".format(newval))
