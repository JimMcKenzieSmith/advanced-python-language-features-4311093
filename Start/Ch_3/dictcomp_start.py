# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use dictionary comprehensions


# define a list of temperature values
ctemps = [0, 12, 34, 100]
# ftemps = [1,2,3]
# ctemps += ftemps
# print(ctemps)

# TODO: Use a comprehension to build a dictionary
temp_dict = {t:(t*9/5) + 32 for t in ctemps if t < 100}
# print(temp_dict)
# print(temp_dict[12])

# TODO: Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}
# print((team1, team2))
merged = {k: v for team in (team1, team2) for k,v in team.items()}
print(merged)
merged_b = team1
for k,v in team2.items():
    merged_b[k] = v
print(merged_b)