import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model

'''
Afghanistan	Gross domestic product per capita, current prices	U.S. dollars	Units	See notes for:  Gross domestic product, current prices (National currency) Population (Persons).	599.994	2013
Albania	Gross domestic product per capita, current prices	U.S. dollars	Units	See notes for:  Gross domestic product, current prices (National currency) Population (Persons).	3,995.383	2010
'''

def load_gdp():
    gdp_data = pd.read_csv('gdp_per_capita.csv', delimiter = '\t', thousands = ',', na_values = 'n/a')
    # print(gdp_data['Country'], gdp_data['2015'])
    gdp_data.rename(columns={'2015': 'GDP per capita'}, inplace=True)
    gdp_data.set_index('Country', inplace=True)
    # print(gdp_data['Country', 'GDP per capita'] )
    return gdp_data
    
'''
"LOCATION","Country","INDICATOR","Indicator","MEASURE","Measure","INEQUALITY","Inequality","Unit Code","Unit","PowerCode Code","PowerCode","Reference Period Code","Reference Period","Value","Flag Codes","Flags"
"AUS","Australia","HO_BASE","Dwellings without basic facilities","L","Value","TOT","Total","PC","Percentage","0","units",,,1.1,"E","Estimated value"
"AUT","Austria","HO_BASE","Dwellings without basic facilities","L","Value","TOT","Total","PC","Percentage","0","units",,,1,,
"BEL","Belgium","HO_BASE","Dwellings without basic facilities","L","Value","TOT","Total","PC","Percentage","0","units",,,2,,
"CAN","Canada","HO_BASE","Dwellings without basic facilities","L","Value","TOT","Total","PC","Percentage","0","units",,,0.2,,
'''
def load_oecd():
    oecd_data = pd.read_csv('oecd_bli_2015.csv', thousands = ',')
    oecd_data = oecd_data[oecd_data['INEQUALITY'] == 'TOT']
    oecd_data = oecd_data.pivot(index='Country', columns = 'Indicator', values = 'Value')
    return oecd_data

oecd_data = load_oecd()
gdp_data = load_gdp()

country_stats = pd.merge(left=oecd_data, right=gdp_data, 
                         left_index = True, right_index = True)
                         
print(country_stats)                         

x = np.c_[country_stats[['GDP per capita']]]
y = np.c_[country_stats[['Life satisfaction']]]

country_stats.plot(kind='scatter', x = 'GDP per capita', y = 'Life satisfaction')
plt.show()

model = sklearn.linear_model.LinearRegression()
model.fit(x,y)

