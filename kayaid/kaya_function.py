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

    Raises:
        ValueError: If any of the input values is negative
    """
    if pop < 0 or gdp < 0 or enInt < 0 or carbInt < 0:
            raise ValueError("Input values must be non-negative!")
    return pop * gdp * enInt * carbInt 
    

# test for germany
germany_co2 = kaya_eq(pop=82.4, gdp=44, enInt=5, carbInt=0.05) 
print(germany_co2)

# test with negative values
negative_co2 = kaya_eq(pop=-50, gdp=30, carbInt=-2, enInt=-3)
print(negative_co2)