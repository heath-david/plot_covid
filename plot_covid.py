# Learn to plot

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
# matplotlib inline #if you're working in a Jupyter notebook
df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
countries = ['Canada', 'China', 'France', 'Germany', 'Iceland', 'Italy', 'Morocco', 'United Kingdom', 'US']
df = df[df['Country'].isin(countries)]

# Modify the start date to zoom in on more recent data. Earliest day of data is 1-22-2020. 
start_date='3-20-2020' # Past 3 weeks
df = df[df.Date >= start_date]

df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)

covid = df.pivot(index='Date', columns='Country', values='Cases')
countries = list(covid.columns)
covid.columns = countries

colors = {'Canada':'#045275', 'China':'#089099', 'France':'#7CCBA2', 'Germany':'#FCDE9C', 'Iceland':'#800000', 'Italy':'#FFDF00', 'Morocco':'#FF7F50', 'US':'#DC3977', 'United Kingdom':'#7C1D6F'}
# I couldn't figure out why the US and United Kingdom text colors were switched. I know that the df is supposed to
# be in alphabetical order since the .csv is alphabetical, and that the colors list above would have to match that
# order to properly plot the label. Turns out, the spreadsheet lists the US first in the 'U' countries. Even ahead
# of Uganda lol. 

plt.style.use('Solarize_Light2')

plot = covid.plot(figsize=(14,8), color=list(colors.values()), linewidth=4, legend=False)
plot.yaxis.set_major_formatter(matplotlib.ticker.StrMethodFormatter('{x:,.0f}'))
plot.grid(color='#d4d4d4')
plot.set_xlabel('Date')
plot.set_ylabel('# of Cases')

for country in list(colors.keys()):
    plot.text(x = covid.index[-1], y = covid[country].max(), c = colors[country], s = country, weight = 'bold')

plot.text(x = covid.index[1], y = int(covid.max().max())+70000, s = "COVID-19 Cases by Country", fontsize = 15, weight = 'bold', alpha = .75)
plot.text(x = covid.index[1], y = int(covid.max().max())+40000, s = "For the USA, China, Germany, Iceland, Italy, France, United Kingdom, Canada, and Morocco\nIncludes Current Cases, Recoveries, and Deaths", fontsize = 10, alpha = .75)
# Think of a way to autoscale these ^ text placements
plot.text(x = covid.index[1], y = -100000,s = 'Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv\nModified from Nik Piepenbreier', fontsize = 6)

plt.tight_layout()
plt.show()

populations = {'Canada':37664517, 'China':1438027228, 'France':65239883, 'Germany':83721496, 'Iceland':364134, 'Italy':60360000 ,'Morocco':35740000, 'United Kingdom':67802690, 'US':330548815}
percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country]/populations[country]*100000

percapitaplot = percapita.plot(figsize=(14,8), color=list(colors.values()), linewidth=4, legend=False)
percapitaplot.grid(color='#d4d4d4')
percapitaplot.set_xlabel('Date')
percapitaplot.set_ylabel('# of Cases per 100,000 People')
for country in list(colors.keys()):
    percapitaplot.text(x = percapita.index[-1], y = percapita[country].max(), c = colors[country], s = country, weight = 'bold')
percapitaplot.text(x = percapita.index[1], y = percapita.max().max()+80, s = "Per Capita COVID-19 Cases by Country", fontsize = 15, weight = 'bold', alpha = .75)
percapitaplot.text(x = percapita.index[1], y = percapita.max().max()+40, s = "For the USA, China, Germany, Iceland, France, United Kingdom, Canada, and Morocco\nIncludes Current Cases, Recoveries, and Deaths", fontsize = 10, alpha = .75)
percapitaplot.text(x = percapita.index[1], y = -65,s = 'Source: https://github.com/datasets/covid-19/blob/master/data/countries-aggregated.csv\nModified from Nik Piepenbreier', fontsize = 6)

plt.tight_layout()
plt.show()

