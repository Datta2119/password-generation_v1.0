from numpy import number


import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = "!@#$&*?|/"

user_for = lower_case + upper_case + numbers + symbols
length_for_password = 8

generated_password = ''.join(random.sample(user_for, length_for_password))

print(f'Your generated password: {generated_password}')