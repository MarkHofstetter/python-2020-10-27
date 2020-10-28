import pytest
from wifi_util import mortage_interest_maturity_after_years

def test_mortage_interest_maturity_after_years():
    tests = [
        {'amount': 0,     'years':  0,  'interest_rate_percent': 0, 'result': 0},
        {'amount': 10000, 'years': 10,  'interest_rate_percent': 2, 'result': 12189.944199947573},
        {'amount': 10000, 'years': -10, 'interest_rate_percent': 2, 'result': None},
    ]
    
    for test in tests:    
        interest, years = mortage_interest_maturity_after_years(
            interest_rate_percent = test['interest_rate_percent'],
            amount                = test['amount'],
            years                 = test['years']
            )
        
        assert interest == test['result']
        