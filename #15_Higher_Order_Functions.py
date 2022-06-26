#Higher Order Functions
print("\nStarting the Program")

counter=0
counter+=1
print("HDF Example - {}".format(counter))
bonus = lambda sal,bonus:sal+bonus
deduction=lambda sal,deduct:sal-deduct

def calc_sal(sal,bonmon,dedbon,functname):
    bonus_sal=sal+bonmon
    dedbonval=functname(bonus_sal,dedbon)
    print('Bonus or deduction applied salary is {}'.format(dedbonval))
    return dedbonval

calc_sal(10000,1000,1000,bonus)
calc_sal(10000,1000,3000,deduction)

counter+=1
print("\nHDF Example with MAP function - {}".format(counter))
lst_purchase=[10000,20000,25000,30000]
add_surcharge=lambda purchase:purchase+(purchase*.01)
give_rebate=lambda purchase:purchase-(purchase-(purchase*.02))
lst_surcharge=[]
lst_surcharge=list(map(add_surcharge,lst_purchase))
lst_offeramt=[]
lst_offeramt=list(map(give_rebate,lst_purchase))
print("List Surcharge: {}".format(lst_surcharge))
print("List Offeramt: {}".format(lst_offeramt))
