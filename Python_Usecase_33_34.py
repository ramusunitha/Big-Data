def fnd_greatest(lst):
    outlst = []
    for i in enumerate(lst):
        try:
            if lst[i[0]] > lst[i[0] + 1]:
                print(lst[i[1]])
                outlst.append(lst[i[0]])
        except IndexError as indx:
            if len(outlst) >= 0:
                if lst[i[0]] > lst[i[0] - 1]:
                    outlst.append(lst[i[0]])
                    print("\nGreatest number is {}".format(max(outlst)))
    if len(outlst) == 0:
        print("\nNo greatest number among the three")

def even_neg(n):
    if (n < 0) and (n % 2) == 0:
        print("Number {} is even and negative".format(n))
    elif (n % 2) == 0:
        print("Number {} is even and not negative".format(n))
    elif (n < 0) and (n % 2) != 0:
        print("Number {} is negative and not even".format(n))
    else:
        print("Number {} is not negative and not even".format(n))
def course_fee(course_lst,datascience,course_dict,choice1):
    if choice1 == 'datascience':
        print("\nChoose one of the courses or both from datascience: \n{}".format(datascience))
        print("\nmachinelearning - enter 1 \ndeeplearning - enter 2 \nBoth - enter 0")
        n = int(input())
        if n == 1:
            print("\nCourse fees of Datascience - {} is: {}".format(datascience[0], course_dict[datascience[0]]))
        if n == 2:
            print("\nCourse fees of Datascience - {} is: {}".format(datascience[1], course_dict[datascience[1]]))
        if n == 0:
            res1 = course_dict[datascience[0]]
            res2 = course_dict[datascience[1]]
            result = res1 + res2
            print("\nCourse fees of ML + DL in Datascience is: {}".format(result))
    else:
        if choice1 == 'bigdata':
            print("\nCourse fees of BigData is: {}".format(course_dict['bigdata']))
        if choice1 == 'spark':
            print("\nCourse fees of Spark is: {}".format(course_dict['spark']))

def palindrome(str_input):
    if str_input[::-1] == str_input:
        print("YAY!!! String {} is a 'Palindrome'".format(str_input))
    else:
        print("No, Sorry! This string {} is not a 'Palindrome'".format(str_input))

def datatype(x):
    print(type(x))
    if (isinstance(x, int)):
        print("X is an Integer")
    else:
        print("X is of datatype {}".format(type(x)))
        if (isinstance(x, str)):
            print("Case of {} is changed to {}".format(x, x.upper()))
    y = 100
    if (isinstance(y, int)):
        print("Y is an Integer")
    else:
        print("Y is of datatype {}".format(type(x)))

def even_odd_lst(numlst):
    oddlst = []
    evenlst = []
    for nums in numlst:
        if (nums % 2) == 0:
            evenlst.append(nums)
        else:
            oddlst.append(nums)
    print("\nInput number list is:", numlst)
    print("Even number list is:", evenlst)
    print("Odd number list is:", oddlst)

def three_list():
    threelst = []
    rng = 0
    while rng in range(0, 21):
        if (rng % 3) == 0 and (rng != 0):
            threelst.append(rng)
        rng += 3
    print("\nList of three multiples is: {}".format(threelst))

def cube(res,fournum):
    for loop in range(1, 4):
        res = res * fournum
    print("\nCube of {} is: {}".format(fournum, res))

def bonussalary(sal_lst,bonus):
    sal_bonus_lst = []
    greatsal = []
    for salitem in sal_lst:
        salbonus = salitem + bonus
        sal_bonus_lst.append(salbonus)
        if salbonus > 11000:
            greatsal.append(salbonus)
    print("\nSal_lst is: {}".format(sal_lst))
    print("Salary Bonus list is: {}".format(sal_bonus_lst))
    print("List of Sal+Bonus > 11000 is: {}".format(greatsal))

def do_while(loopnum):
    l = 1
    print("\n")
    while True:
        print("Inceptez Technologies")
        l += 1
        if (l > loopnum):
            break

def nested_list(nstlst):
    result_sum = 0
    new_whole_list = []
    for net in nstlst:
        for n in net:
            result_sum += n
            new_whole_list.append(n)
    print("\nNested List is: {}".format(nstlst))
    print("Sum of all the numbers in nstlst is: {}".format(result_sum))
    print("Minimum value of nstlst is: {}".format(min(new_whole_list)))
    print("Maximum value of nstlst is: {}".format(max(new_whole_list)))

def multiplication_tables(tablenum):
    print("\n")
    for cont in range(1, 11):
        print("{} x {} = {}".format(cont, tablenum, cont * tablenum))

#Scenario Counter
counter=32
counter += 1
print("\nScenario - {}".format(counter))

#11
lst = [324,43523,123]
fnd_greatest(lst)

#12
print("\nEnter the number:")
n = int(input())
even_neg(n)

#13
course_lst = ['bigdata', 'spark', 'datascience']
datascience = ('machinelearning', 'deeplearning')
course_dict = {'bigdata': 25000, 'spark': 15000, 'machinelearning': 25000, 'deeplearning': 45000}
print("\nChoose from the list of courses - {}".format(course_lst))
choice1 = str(input())
course_fee(course_lst,datascience,course_dict,choice1)

#14
print("\nHi! Enter the string of your choice:")
str_input = str(input())
palindrome(str_input)
# Palindrome String - iTopiNonAvevAnoNipoTi
# Non Palindrome String - iGattiNonAvevanoCugini

#15
print("\nEnter the input of your choice")
x = input()
datatype(x)

#26
numlst=list(range(5,21))
even_odd_lst(numlst)

#27
three_list()

#28
fournum=4
res=1
cube(res,fournum)

#29
sal_lst=[10000,20000,30000,10000,15000]
bonus=1000
bonussalary(sal_lst,bonus)

#30
print("\nScenario - {}".format(counter))
print("Enter the number of times you want the loop to execute")
print("Note: Even if you specify 0, the loop will execute once and stop")
loopnum=int(input())
do_while(loopnum)

#31
nstlst=[[10,20],[30,40,50],[60,70,80]]
nested_list(nstlst)

#32
tablenum=3
multiplication_tables(tablenum)

#34
fnd_greatest(lst=[5,10,15])