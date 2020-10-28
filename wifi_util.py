def mortage_interest_maturity_after_years(
        interest_rate_percent,                             
        amount,
        years = 10,
        ):
    
    if years < 0:
        return (None, None)
    interest = amount * (interest_rate_percent/100 + 1) ** years   
    return (interest, years)


if __name__ == '__main__':

    '''
    amount: 0, years: 0, interest_rate_percent: 0 , result: 0 
    amount: 10000, years: 10, interest_rate_percent: 2, result: 12189.94
    amount: 10000, years: -10, interest_rate_percent: 2, result: None    
    '''
    
    tests = [
        {'amount': 0,     'years':  0,  'interest_rate_percent': 0, 'result': 0},
        {'amount': 10000, 'years': 10,  'interest_rate_percent': 2, 'result': 12190},
        {'amount': 10000, 'years': -10, 'interest_rate_percent': 2, 'result': None},
    ]
    
    for test in tests:    
        interest, years = mortage_interest_maturity_after_years(
            interest_rate_percent = test['interest_rate_percent'],
            amount                = test['amount'],
            years                 = test['years']
            )
        
        if interest is None and test['result'] is None:
            print('OK')
        elif round(interest) == round(test['result']):
            print('OK')
        else:
            print('not OK')
        # if interest is not None:        
        #    interest = "Interest rate: {0:.2f}".format(interest)
        # print(interest)
        