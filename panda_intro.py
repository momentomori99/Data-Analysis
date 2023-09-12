import pandas as pd
import numpy as np

g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523]) #in millions
g7_pop.name = "G7 population in millions"

"""
some usefule commands
g7_pop.dtype
g7_pop.values
g7_pop.index
g7_pop.mean
g7_pop.std

additionally, you can get elements just as in a list by writing
g7_pop[i]
"""

#We can change the index!
g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
#We basically named/labeled the indexes


#You can of course do operations as well

#print(g7_pop*100000)

#we also can do boolean arrays
print(g7_pop > 70)
print(g7_pop[g7_pop > 70])


#We of course can modify Series
g7_pop["Canada"] = 40.5
