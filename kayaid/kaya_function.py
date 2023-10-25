def kaya_eq(pop, gdp, enInt, carbInt):
    """
    Calculate C02 emissions with the kaya identity.

    Args:
        pop (float): Population size (in millions).
        gdp (float): GDP per capita (in 1000$/person).
        enInt (float): Energy intensity (in Gigajoule/1000$GDP).
        carbInt (float): Carbon intensity (in tonnes CO2/Gigajoule).

    Returns:
        float: CO2 emissions in million tonnes.
    """
    return pop * gdp * enInt * carbInt 
    

germany_co2 = kaya_eq(pop=82.4, gdp=44, enInt=5, carbInt=0.05)
print(germany_co2)