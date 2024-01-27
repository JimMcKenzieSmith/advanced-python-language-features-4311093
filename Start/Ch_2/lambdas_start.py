# Example file for Advanced Python: Language Features by Joe Marini
# Use lambdas as in-place functions


def celsisus_to_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_to_celsisus(temp):
    return (temp-32) * 5/9


ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]

# Use regular functions to convert temps
ctof = list(map(celsisus_to_fahrenheit, ctemps))
print(ctof)

# Use lambdas to accomplish the same thing
ctof = list(map(lambda x:(x * 9/5) + 32, ctemps))
print(ctof)

# Use list comprehension to accomplish the same thing
ctof = [(x * 9/5) + 32 for x in ctemps]
print(ctof)