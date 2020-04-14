# COVID-19 Visualization

This script - modified from Nik Piepenbreier - plots COVID-19 cases from several countries. Presently, Canada, China, France, Germany, Iceland, Italy,
Morocco, the United Kingdom, and the USA are included.

To execute the script, simply run

    % python plot_covid.py 

to display two figures in succession - a plot of the absolute number of cases per country (which includes current cases,
recoveries, and deaths) and a plot of per capita cases in each country. 

The user has the option to modify the start date of the displayed data, and can easily add or remove countries. 

To add a country, the user should ensure the naming convention is the same as in the data spreadsheet (linked at the bottom) 
and choose a hex color code. Then, the user should first update the ***list*** of countries, then add the country and color code
to the ***colors*** dictionary, and finally add the ***population*** of the new country. 

That's it for now!
