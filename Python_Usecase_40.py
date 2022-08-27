lam = lambda amount,offer_percent,offer_cap_limit:amount-(amount*offer_percent) if (amount*offer_percent)<offer_cap_limit else (amount-offer_percent)

print("\n40. Lambda Function with IF_ELSE")
print(lam(1000,.10,200))
