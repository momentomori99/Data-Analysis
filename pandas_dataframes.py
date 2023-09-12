import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
        'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

"""
The datafram is just a combination of pandas series.
Every column is just a series.
"""

df.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]

"""
Some usefule commands:
df.columns
df.index
df.size
df.shape
df.dtypes
df.dtypes.value_counts()
"""

print(df.info()) #Gives info about the structure of the dataframe.
print(df.describe()) #Gives you statistics of the dataframe

"""
Indexing, selection and slicing
"""
df.loc["Canada"] #select rows by index
df.iloc[-1] #select rows by seq. position
df["Population"] #Gives you the column

df.loc["France" : "Italy"]
df.loc['France': 'Italy', 'Population']
df.loc['France': 'Italy', ['Population', 'GDP']]
