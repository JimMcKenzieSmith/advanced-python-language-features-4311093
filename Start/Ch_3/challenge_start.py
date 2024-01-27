# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

digits = [d for d in test_str if d.isdigit()]
punc = [d for d in test_str 
        if not d.isdigit() and not d.isalpha() and not d.isspace()]
unique_letters = {s for s in test_str if s.isalpha()}

# print the data
str_data = {
    "Length": len(test_str),
    "Digits": len(digits),
    "Punctuation": len(punc),
    "Unique Letters": "".join(unique_letters),
    "Unique Count": len(unique_letters)
}
pprint.pp(str_data)
