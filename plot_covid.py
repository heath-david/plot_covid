# Learn to plot

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
# matplotlib inline #if you're working in a Jupyter notebook

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
countries = ['Canada', 'China', 'France', 'Germany', 'Morocco', 'United Kingdom', 'US']
df = df[df['Country'].isin(countries)]

df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

df = df.pivot(index='Date', columns='Country', values='Cases')
countries = list(df.columns)
covid = df.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries

populations = {'Canada':37664517, 'China':1438027228, 'France': 65239883, 'Germany': 83721496, 'Morocco':35740000, 'United Kingdom': 67802690 , 'US': 330548815}
percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country]/populations[country]*100000

colors = {'Canada':'#045275', 'China':'#089099', 'France':'#7CCBA2', 'Germany':'#FCDE9C', 'Morocco':'#FF7F50', 'United Kingdom':'#7C1D6F', 'US':'#DC3977'}
plt.style.use('fivethirtyeight')

plot = covid.plot(figsize=(14,8), color=list(colors.values()), linewidth=4, legend=False)
plot.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('# of Cases')

for country in list(colors.keys()):
    plot.text(x = covid.index[-1], y = covid[country].max(), c = colors[country], s = country, weight = 'bold')

plot.text(x = covid.index[1], y = int(covid.max().max())+45000, s = "COVID-19 Cases by Country", fontsize = 15, weight = 'bold', alpha = .75)
plot.text(x = covid.index[1], y = int(covid.max().max())+15000, s = "For the USA, China, Germany, France, United Kingdom, Canada, and Morocco\nIncludes Current Cases, Recoveries, and Deaths", fontsize = 10, alpha = .75)
plot.text(x = percapita.index[1], y = -100000,s = 'Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv', fontsize = 6)

plt.tight_layout()
plt.show()

percapitaplot = percapita.plot(figsize=(14,8), color=list(colors.values()), linewidth=4, legend=False)
percapitaplot.grid(color='#d4d4d4')
percapitaplot.set_xlabel('Date')
percapitaplot.set_ylabel('# of Cases per 100,000 People')
for country in list(colors.keys()):
    percapitaplot.text(x = percapita.index[-1], y = percapita[country].max(), c = colors[country], s = country, weight = 'bold')
percapitaplot.text(x = percapita.index[1], y = percapita.max().max()+25, s = "Per Capita COVID-19 Cases by Country", fontsize = 15, weight = 'bold', alpha = .75)
percapitaplot.text(x = percapita.index[1], y = percapita.max().max()+10, s = "For the USA, China, Germany, France, United Kingdom, Canada, and Morocco\nIncludes Current Cases, Recoveries, and Deaths", fontsize = 10, alpha = .75)
percapitaplot.text(x = percapita.index[1], y = -55,s = 'datagy.io                      Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv', fontsize = 6)

plt.tight_layout()
plt.show()

