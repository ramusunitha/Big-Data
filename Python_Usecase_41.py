#Scenarios 38,39 and 40 are all WIP

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

counter=36
counter+=1
print("\nScenario - {}".format(counter))
print("Enter the number 1")
num1=input()
print("Enter the number 2")
num2=input()
print("Enter 'add,subtract,multiply,divide,all'")
operation=input()
try:
    if isinstace(num1,'str') and isinstance(num2,'str'):
        print("Num1 {} and Num2 {} are strings".format(num1,num2))
except Exception as exvalue:
    if operation != '':
        result = calculator(int(num1), int(num2), operation)
        print("The result for {} with the numbers {} & {} is: {} ".format(operation, num1, num2, result))
    else:
        result = calculator(int(num1), int(num2))
        print("The result for add with the numbers {} & {} is: {} ".format(num1, num2, result))