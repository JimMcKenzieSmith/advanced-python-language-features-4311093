# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


# TODO: pass different arguments
print(addition(1, 2, 3, 4, 5))

# TODO: pass an existing list
my_nums = [5,6,7,8,9]
print(addition(*my_nums))