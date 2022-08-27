def calculator(num1,num2,operation='add'):
    if operation=='add':
        return num1+num2
    if operation=='subtract':
        return num1-num2
    if operation=='multiply':
        return num1*num2
    if operation=='divide':
        return num1/num2
    if operation=='all':
        return (num1+num2,num1-num2,num1*num2,num1/num2)

counter=34
counter+=1
print("\nScenario - {}".format(counter))
print("Enter the number 1")
num1=int(input())
print("Enter the number 2")
num2=int(input())
print("Enter 'add,subtract,multiply,divide,all'")
operation=input()
if operation!='':
    result=calculator(num1,num2,operation)
    print("The result for {} with the numbers {} & {} is: {} ".format(operation, num1, num2, result))
else:
    counter += 1
    print("\nScenario - {}".format(counter))
    result=calculator(num1,num2)
    print("The result for add with the numbers {} & {} is: {} ".format(num1,num2,result))