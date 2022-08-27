#Higher Order Functions
print("\nStarting the Program")

counter=0
counter+=1
print("HDF Example - {}".format(counter))

lam=lambda amount,offer_percent:amount-(amount*offer_percent)

def promo(amount,offer_percent,offer_cap_limit,functname):
    if amount*offer_percent < offer_cap_limit:
        return functname(amount,offer_percent)
    else:
        return amount-offer_cap_limit

print(promo(1000,.10,200,lam))