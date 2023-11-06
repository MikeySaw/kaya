def kaya_eq(pop, gdp, enInt, carbInt, output_type="CO2"):
    """
    Calculate C02 emissions with the kaya identity.
    Here is a link explaining the function https://en.wikipedia.org/wiki/Kaya_identity

    Args:
        pop (float): Population size (in millions).
        gdp (float): GDP per capita (in 1000$/person).
        enInt (float): Energy intensity (in Gigajoule/1000$GDP).
        carbInt (float): Carbon intensity (in tonnes CO2/Gigajoule).
        output_type (str): Output type (either CO2 or C for Carbon).

    Returns:
        float: CO2 emissions in million tonnes (default).
        float: C emission in million tones (if output_type = C)
    Raises:
        ValueError: If any of the input values is negative
    """
    if pop < 0 or gdp < 0 or enInt < 0 or carbInt < 0:
            raise ValueError("Input values must be non-negative!")
    
    if output_type == "CO2":
        return pop * gdp * enInt * carbInt 
    elif output_type == "C":
        return (pop * gdp * enInt * carbInt) / 3.67
    else:
         raise ValueError("Invalid output_type. Use either 'CO2' or 'C'!")
    

# test for germany
germany_co2 = kaya_eq(pop=82.4, gdp=44, enInt=5, carbInt=0.05) 
print(germany_co2)

# test with negative values
negative_co2 = kaya_eq(pop=-50, gdp=30, carbInt=-2, enInt=-3)
print(negative_co2)