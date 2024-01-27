# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use set comprehensions


# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# TODO: build a set of unique Fahrenheit temperatures
ftemps1 = [(t * 9/5) + 32 for t in ctemps]
f_unique = set(ftemps1)
print(ftemps1)
print(f_unique)

ftemps2 = {(t * 9/5) + 32 for t in ctemps}
print(ftemps2)

# TODO: build a set from an input source
s_temp = "The quick brown fox jumped over the lazy dog"
str_set = {s.upper() for s in s_temp if not s.isspace()}
print(s_temp)
print(str_set)