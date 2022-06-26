#Higher Order Functions
print("\nStarting the Program")

bonus = lambda sal,bonus:sal+bonus
deduction=lambda sal,deduct:sal-deduct

def calc_sal(sal,bonmon,dedbon,functname):
    bonus_sal=sal+bonmon
    dedbonval=functname(bonus_sal,dedbon)
    print('Bonus or deduction applied salary is {}'.format(dedbonval))
    return dedbonval

calc_sal(10000,1000,1000,bonus)
calc_sal(10000,1000,3000,deduction)