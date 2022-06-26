#Anonymous Function / Lambda Function / Function Literal

print("\nStarting the Program")
print("Example 1")
a = lambda x:x+10
print(a(100))

print("\nExample 2")
generate_mail=lambda fname,lname,domain:fname+lname+domain

lst=[('md','irfan','@dummy.com'),('sunitha','ramu','@newdummy.com')]
for i in lst:
    print(generate_mail(i[0],i[1],i[2]))

day2lst=[('seetha','ramu','@dummy.com'),('ss','ramu','@newdummy.com')]
for i in day2lst:
    print(generate_mail(i[0],i[1],i[2]))

print("\nExample 3 - With default values in lambda function")
generate_mail=lambda fname,lname,domain='@newmail.com':fname+lname+domain

lst=[('md','irfan'),('sunitha','ramu')]
for i in lst:
    print(generate_mail(i[0],i[1]))