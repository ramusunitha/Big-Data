def generate_mail(fname,lname):
    return fname+'-'+lname+'@dummy.com'

def generate_mail1(ls_tuple_name):
    for t in ls_tuple_name:
        print(t[0]+'.'+t[1]+'@dummy.com')

def generate_mail2(fname,lname,domain="@dummy.com"):
    return fname+'-'+lname+domain

def generate_mail3(fname='sunitha',lname='ramu',domain="@dummy.com"):
    return fname+'_'+lname+domain

print("\nStarting the Program related to Functions")
print("Function Call 1 - Positional Argument Function")
empnames=[('md','irfan'),('suresh','mohan')]
for i in empnames:
    print(generate_mail(i[0],i[1]))
empnames=[('ayub', 'khan'), ('karthick', 'sekaran')]
for i in empnames:
    print(generate_mail(i[0],i[1]))

print("\nFunction Call 2 - Positional Argument Function")
empnames=[('md','irfan'),('suresh','mohan')]
generate_mail1(empnames)
empnames=[('ayub', 'khan'), ('karthick', 'sekaran')]
generate_mail1(empnames)

print("\nFunction Call 3 - Default Argument Function")
print(generate_mail2('md','irfan'))
print(generate_mail2('md','irfan','@newdummy.com'))
print("Incorrect Position will be printed below")
print(generate_mail2('@newdummy.com','md','irfan')) # Positional, so this will be incorrect

print("\nFunction Call 4 - Keyword Argument Function")
print(generate_mail3('md','irfan'))
print(generate_mail3('md','irfan','@newdummy.com'))
print(generate_mail3())