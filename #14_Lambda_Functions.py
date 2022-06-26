#Lambda Function Secnarios
'''
Normal function calling scenarios - Positional,named,default arguments,*args,**kwargs
All the above can be done in Lambda functions as well
Can we have more than one line in Lambda function? - NO
Can we apply lambda function in regular function? - YES
'''

def generate_func(fname,lname,domain):
    lam_func=lambda x:x.lower()
    dom=lam_func(domain)
    return fname+lname+dom

def new_gen_fun(fname,lname,domain,lam_func_arg):
    dom=lam_func_arg(domain)
    return fname+lname+dom

print("\nStarting the Program")
counter=0

#Positional
counter+=1
print("Scenario {} - #Positional".format(counter))
generate_mail=lambda fname,lname,domain:fname+lname+domain
print(generate_mail('sunitha','ramu','@positional.com'))

#Keyword
counter+=1
print("\nScenario {} - #Keyword".format(counter))
print(generate_mail(fname='sunitha',lname='ramu',domain='@keyword.com'))

#default argument
counter+=1
print("\nScenario {} - #default argument".format(counter))
generate_mail=lambda fname,lname,domain='@defaultarg.com':fname+lname+domain
lst=[('md','irfan'),('sunitha','ramu')]
for i in lst:
    print(generate_mail(i[0],i[1]))

#Arbitrary Arguments
counter+=1
print("\nScenario {} - #Arbitrary Arguments".format(counter))
generate_mail=lambda *args:args[0]+'_'+args[1]+args[2]
print(generate_mail('sunitha','ramu','@arb.com'))

#Keyword Arbitrary Arguments
counter+=1
print("\nScenario {} - #Keyword Arbitrary Arguments".format(counter))
generate_mail=lambda **kwargs:kwargs['fname']+'.'+kwargs['lname']+kwargs['domain']
print(generate_mail(fname='sunitha',lname='ramu',domain='@keywordarb.com'))

#Lambda inside regular function
counter+=1
print("\nScenario {} - #Lambda inside regular function".format(counter))
print(generate_func('md','irfan','@INSIDELAMBDA.com'))

#Lambda outside regular function
counter+=1
print("\nScenario {} - #Lambda outside regular function".format(counter))
lam_func1=lambda x:x.lower()
lam_func2=lambda x:x.upper()
print(new_gen_fun('md','irfan','@outsidelambda.com',lam_func1))
print(new_gen_fun('md','irfan','@outsidelambda.com',lam_func2))

#Lambda function returning collection types
counter+=1
print("\nScenario {} - #Lambda function returning collection types".format(counter))
gen_m=lambda fname,lname,domain:{fname+lname:fname+lname+domain}
print(gen_m('Sunitha','Ramu','@colltype.com'))

counter+=1
print("\nScenario {} - #Lambda function returning collection types".format(counter))
lst_surcharge=[]
lst_purchase=[10000,20000,25000,30000]
add_surcharge=lambda purchase:purchase+(purchase*.01)
for i in lst_purchase:
    lst_surcharge.append(add_surcharge(i))
print(lst_surcharge)

