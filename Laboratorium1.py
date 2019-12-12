# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:53:23 2019

@author: Asaldor
"""

#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests


# Dane wejściowe.
curr1 = 'GBP'
curr2 = 'EUR'
date_from = '2019-10-01'
date_to = '2019-10-30'

def fetch_currency(currency,beg,end):
    url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + currency + "/" + date_from + "/" + date_to + "/"
    currency_req = requests.get(url)
    currency_data = currency_req.json()
    return currency_data['rates']
# Funkcja wczytujaca walute
rate1 = fetch_currency(curr1,date_from,date_to)
rate2 = fetch_currency(curr2,date_from,date_to)

# Ograniczenie wpisow do 6.
rate_dataframe1 = pd.DataFrame.from_dict(rate1).head(6)
rate_dataframe2 = pd.DataFrame.from_dict(rate2).head(6)

#Indeksy ustawione na datę.
plot_data1 = rate_dataframe1.set_index(['effectiveDate'])['mid']
plot_data2 = rate_dataframe2.set_index(['effectiveDate'])['mid']

# Funkcja obliczająca korelację dwóch kursów.
correlation = np.corrcoef (plot_data1, plot_data2)[0][1]

# Rysowanie wykresu pokazującego wyliczoną korelację oraz wartość obydwu kursów w porównaniu do PLN.
plt.plot(plot_data1, 'r--', plot_data2,'b--')
plt.ylim(ymin=0,ymax=7)
plt.title('Korelacja {} do {} = {}'.format(curr1, curr2, correlation))
plt.ylabel('Wartość w PLN')
plt.xlabel('Data')
plt.legend([curr1, curr2], loc='lower right')
plt.show()

