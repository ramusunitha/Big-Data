def sal_hike(sal,hike):
    salhike=sal+hike
    def incentives(incentive):
        return salhike+incentive
    return incentives

print("\nReturn of the function object indicated below - 1")
print(sal_hike(10000,3000))

print("\nReturn the value from the nested function Incentives - 2")
incent=sal_hike(10000,1000)
print(incent(4000))
