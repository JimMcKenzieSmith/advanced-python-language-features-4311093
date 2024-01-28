# Example file for Advanced Python: Language Features by Joe Marini
# Sequence pattern matching example - matches against value sequences

import math


# Set up some test data with different math operations
operations = [
    ["Add", 1, 2, 3, 4, 5],
    ["Mul", 5, 6],
    ["Add", 10, 20],
    ["Sqrt", 9],
]

result = 0

# TODO: process each operation along with the set of given numbers
for op in operations:
    match op:
        case "Mul", num1, num2:
            result = num1 * num2
        case "Sqrt", num:
            result = math.sqrt(num)
        case "Add", num1, *args:
            result = num1 + sum(args)
        case _:
            continue

    print(f"{op}: {result}")
