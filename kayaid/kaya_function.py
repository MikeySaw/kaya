def kaya_eq(pop, gdp, enInt, carbInt):
    return pop * gdp * enInt * carbInt 
    

germany_co2 = kaya_eq(pop=82.4, gdp=44, enInt=5, carbInt=0.05)
print(germany_co2)