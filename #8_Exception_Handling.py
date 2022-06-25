print("Input Numerator:")
n=int(input())
print("Input Denominator")
d=int(input())

try:
    res=n/d
    print("Success. Quotient is: {}".format(res))
except Exception as expvalue:
    print("Exception occured. Exception is: {}".format(expvalue))
else:
    print("No Exception - the division is successful")
finally:
    print("End of Program. Thank you!")