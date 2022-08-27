def promo(*args):
    if (args[0]*args[1])<args[2]:
        return args[0]-(args[0]*args[1])
    else:
        return args[0]-args[1]

def key_promo(**args):
    if (args['x']*args['y'])<args['z']:
        return args['x']-(args['x']*args['y'])
    else:
        return args['x']-args['y']

def normal_promo(a,b,c=200):
    try:
        assert b>0
        if (a * b) < c:
            return a - (a * b)
        else:
            return a - b
    except AssertionError:
        print("Offer percent is Negative")

print("\nA. Normal Function")
print(normal_promo(1000,.10,200))
print("\nB. Default Parameter Function")
print(normal_promo(1000,.10))
print("\nC. Arbitrary Function - With Tuple *args")
print(promo(1000,.10,200))
print("\nD. Arbitrary Function - With keyword **args")
print(key_promo(x=1000,y=.10,z=200))
print("\n40. Exception handling - for usecase 38")
print(normal_promo(1000,-.10,200))