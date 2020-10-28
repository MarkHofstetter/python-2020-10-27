def mortage_interest_maturity_after_years(
        interest_rate_percent,                             
        amount,
        years = 10,
        ):
    interest = amount * (interest_rate_percent/100 + 1) ** years    
    return interest

print("Context ", __name__)

if __name__ == '__main__':

    interest = mortage_interest_maturity_after_years(
        interest_rate_percent = 2,
        amount = 10000)    
    
    interest = "Interest rate: {0:.2f}".format(interest)
    print(interest)