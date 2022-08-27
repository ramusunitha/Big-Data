#Python Scenarios - Sunitha Ramu - WE39

counter=0
counter+=1
print("\nScenario - {}".format(counter))
x=100
y=10
z=x*y
z1=x/y
print("Multiplication Result: {}".format(z))
print("Division Result: {}".format(z1))

counter+=1
print("\nScenario - {}".format(counter))
a=2000
a=a/y
print("Division Result: {}".format(a))

counter+=1
print("\nScenario - {}".format(counter))
x:int=100
y=str(x)
print("Type of Y is {} and Type of X is {}".format(type(y),type(x)))

counter+=1
print("\nScenario - {}".format(counter))
name='Sunitha'
a1=100
print("Type of name is {} and a1 is {}. \nNote - The datatypes were assigned dynamically and so it has been inferred dynamically.".format(type(name),type(a1)))

counter+=1
print("\nScenario - {}".format(counter))
try:
    newval=name+a1
except Exception as excpvalue:
    print("Strongly Typed and hence the addition of 'str' and 'int' will error out")
    print("Exception is: {}".format(excpvalue))

counter+=1
print("\nScenario - {}".format(counter))
a=10
b=20
c=30
d=40
print("a is {}, b is {}, c is {}, d is {}".format(a,b,c,d))

counter+=1
print("\nScenario - {}".format(counter))
try:
    print("'A' is {}".format(A))
except Exception as newex:
    print("Exception {} occured".format(newex))
    print("A is not defined and a is defined and a is {}".format(a))

counter+=1
print("\nScenario - {}".format(counter))
print("This is an error for a variable starting with number. \n 1xtreme='with number will error out with SyntaxError")
#1xtreme='with number'

counter+=1
print("\nScenario - {}".format(counter))
print("Usage of Single Quotes - Sunitha's code")
print('''Usage of Single,double & triple quotes "Sunitha's Book" - \nThe statement is enclosed in triple quotes''')

counter+=1
print("\nScenario - {}".format(counter))
if a==10:
    if b>=20:
        if c<=30:
            if d==40:
                print("Inside the loop of a=10,b=20,c=30 & d=40. \nUsed all the relational operators")

counter += 1
print("\nScenario - {}".format(counter))
lst = [30, 5, 29]
outlst = []
for i in enumerate(lst):
    try:
        if lst[i[0]] > lst[i[0] + 1]:
            outlst.append(lst[i[0]])
    except IndexError as indx:
        if len(outlst) >= 0:
            if lst[i[0]] > lst[i[0] - 1]:
                outlst.append(lst[i[0]])
                print("Greatest number is {}".format(max(outlst)))
if len(outlst) == 0:
    print("No greatest number among the three")

counter += 1
print("\nScenario - {}".format(counter))
print("Enter the number:")
n = int(input())
if (n < 0) and (n % 2) == 0:
    print("Number {} is even and negative".format(n))
elif (n % 2) == 0:
    print("Number {} is even and not negative".format(n))
elif (n < 0) and (n % 2) != 0:
    print("Number {} is negative and not even".format(n))
else:
    print("Number {} is not negative and not even".format(n))

counter += 1
print("\nScenario - {}".format(counter))
course_lst = ['bigdata', 'spark', 'datascience']
datascience = ('machinelearning', 'deeplearning')
course_dict = {'bigdata': 25000, 'spark': 15000, 'machinelearning': 25000, 'deeplearning': 45000}
print("Choose from the list of courses - {}".format(course_lst))
choice1 = str(input())
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

counter += 1
print("\nScenario - {}".format(counter))
print("Hi! Enter the string of your choice:")
str_input = str(input())
if str_input[::-1] == str_input:
    print("YAY!!! String {} is a 'Palindrome'".format(str_input))
else:
    print("No, Sorry! This string {} is not a 'Palindrome'".format(str_input))

# Palindrome String - iTopiNonAvevAnoNipoTi
# Non Palindrome String - iGattiNonAvevanoCugini

counter = 14
counter += 1
print("\nScenario - {}".format(counter))
print("Enter the input of your choice")
x = input()
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

counter+=1
print("\nScenario - {}".format(counter))
lst_rng=list(range(2,12))
print("List created with range:",lst_rng)
lst_rng.insert(2,100)
print("List created after Insert:",lst_rng)

counter+=1
print("\nScenario - {}".format(counter))
tup_st_full=("Inceptez","Technologies","Pvt","Ltd")
tup_st_part=(tup_st_full[1],tup_st_full[3])
print("Full Tuple is: {}".format(tup_st_full))
print("New Tuple created with 2nd and 4th fields:",tup_st_part)
print("Proving the immutability feature of the tuple_st_full")
try:
    tup_st_full[1]='new element'
except Exception as tupval:
    print("Exception during changing tuple occured: {}".format(tupval))

counter+=1
print("\nScenario - {}".format(counter))
result={}
list_dict=[]
list_tup=[("Inceptez","Technologies"),("Apple","Incorporation")]
for (key,val) in list_tup:
    result={key:val}
    list_dict.append(result)
print("List of Tuples: {}".format(list_tup))
print("List of Dictionaries: {}".format(list_dict))
print("Using GET Function - Value of key 'Apple' is: {}".format(list_dict[1].get('Apple')))
print("Using [] - Value of key 'Apple is: {}".format(list_dict[1]['Apple']))

counter+=1
print("\nScenario - {}".format(counter))
lst_non_dup=[]
lst_tuple=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]
dupset=set(lst_tuple)
for items in dupset:
    lst_non_dup.append(items)
print("List of tuples without duplicates is: {}".format(lst_non_dup))

counter+=1
print("\nScenario - {}".format(counter))
lst_non_dup.append(("Intel","Corp"))
print("List after appending ('intel','corp') is: {}".format(lst_non_dup))

counter+=1
print("\nScenario - {}".format(counter))
res_list=[]
for d_items in list_dict:
    res_list.append(*d_items)
print("List of Keys in the List Dict {} is: {}".format(list_dict,res_list))

counter+=1
print("\nScenario - {}".format(counter))
lst_num=[10,20,40,30,20]
bkplst=lst_num
print("Original lst_num is: {}".format(lst_num))
lst_num.sort()
print("Sorted lst_num in Ascending order is: {}".format(lst_num))
lst_num.sort(reverse=True)
print("Sorted lst_num in Descending order is: {}".format(lst_num))
print("Minimum value in lst_num is: {}".format(min(lst_num)))
print("Maximum value in lst_num is: {}".format(max(lst_num)))
print("Sum of lst_num is: {}".format(sum(lst_num)))
wo_dup=set(lst_num)
lst_wo_dup=[]
for si in wo_dup:
    lst_wo_dup.append(si)
idx1=lst_wo_dup.index(30)
idx2=lst_wo_dup.index(20)
lst_wo_dup.pop(idx1)
lst_wo_dup.pop(idx2)
print("List without numbers 30 & 20 are:",lst_wo_dup)

counter+=1
print("\nScenario - {}".format(counter))
tup=(10,20,40,30,20)
bkptup=tup
restup=tuple(sorted(tup))
print("Original Tuple is: {}".format(tup))
print("Sorted Tuple in Ascending order is: {}".format(restup))
resdestup=tuple(sorted(tup,reverse=True))
print("Sorted Tuple in Descending order is: {}".format(resdestup))
print("Minimum value in tuple is: {}".format(min(tup)))
print("Maximum value in tuple is: {}".format(max(tup)))
print("Sum of tuple is: {}".format(sum(tup)))
list_tup_dup=tuple(set(tup))
newlst=[]
for tval in list_tup_dup:
    if (tval==30) or (tval==20):
        some=0
    else:
        newlst.append(tval)
print("Tuple without the numbers 20 & 30 is: {}".format(tuple(newlst)))

counter+=1
print("\nScenario - {}".format(counter))
str1="Inceptez Technologies Pvt Ltd"
lst_str1=str1.split()
print("String '{}' converted to List {}".format(str1,lst_str1))

counter+=1
print("\nScenario - {}".format(counter))
reslst=[]
emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]
element_1=tuple(emplstlst[0])
print("Element 1 of the emplstlst is: {}".format(element_1))
print("Element 2 - Reverse of the name tuple is: {}".format(emplstlst[1][1][::-1]))
for l in emplstlst:
    reslst.append(tuple(l))
print("Tuple of emplstlst is: {}".format(tuple(reslst)))
sal_sum=int(emplstlst[0][2])+int(emplstlst[1][2])
print("Sum of salary from emplstlst is: {}".format(sal_sum))

counter+=1
print("\nScenario - {}".format(counter))
numlst=list(range(5,21))
oddlst=[]
evenlst=[]
for nums in numlst:
    if (nums%2)==0:
        evenlst.append(nums)
    else:
        oddlst.append(nums)
print("Input number list is:",numlst)
print("Even number list is:",evenlst)
print("Odd number list is:",oddlst)

counter+=1
print("\nScenario - {}".format(counter))
threelst=[]
rng=0
while rng in range(0,21):
    if (rng%3)==0 and (rng!=0):
        threelst.append(rng)
    rng+=3
print("List of three multiples is: {}".format(threelst))

counter+=1
print("\nScenario - {}".format(counter))
fournum=4
res=1
for loop in range(1,4):
    res=res*fournum
print("Cube of {} is: {}".format(fournum,res))

counter+=1
print("\nScenario - {}".format(counter))
sal_lst=[10000,20000,30000,10000,15000]
bonus=1000
sal_bonus_lst=[]
greatsal=[]
for salitem in sal_lst:
    salbonus=salitem+bonus
    sal_bonus_lst.append(salbonus)
    if salbonus > 11000:
        greatsal.append(salbonus)
print("Sal_lst is: {}".format(sal_lst))
print("Salary Bonus list is: {}".format(sal_bonus_lst))
print("List of Sal+Bonus > 11000 is: {}".format(greatsal))

counter+=1
print("\nScenario - {}".format(counter))
print("Enter the number of times you want the loop to execute")
print("Note: Even if you specify 0, the loop will execute once and stop")
loopnum=int(input())
l=1
while True:
    print("Inceptez Technologies")
    l+=1
    if(l > loopnum):
        break

counter+=1
print("\nScenario - {}".format(counter))
nstlst=[[10,20],[30,40,50],[60,70,80]]
result_sum=0
new_whole_list=[]
for net in nstlst:
    for n in net:
        result_sum+=n
        new_whole_list.append(n)
print("Nested List is: {}".format(nstlst))
print("Sum of all the numbers in nstlst is: {}".format(result_sum))
print("Minimum value of nstlst is: {}".format(min(new_whole_list)))
print("Maximum value of nstlst is: {}".format(max(new_whole_list)))

counter+=1
print("\nScenario - {}".format(counter))
tablenum=3
for cont in range(1,11):
    print("{} x {} = {}".format(cont,tablenum,cont*tablenum))