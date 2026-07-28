#all imports for calculator. Mandatory for pyton app programming
import math
import numpy
import pandas
#Title
print('====================================\n Advanced Scientific Calculator \n Type or exit to stop \n ===================================' )
user_result=input('Enter calculation:')
try:
    # Try to convert the input to a float number
    # If they typed math like "5 + 5", eval() handles it first
    value = eval(user_result) 
    print(f"Result: {value}")
except Exception:
    # If eval() or evaluation fails because they typed regular words/letters
    print('sorry - this is a calculator')
while True:  # 1. Start the loop
    user_result = input("Enter calculation: ")

    if user_result in ['quit', 'exit']:
        print('Bye! Have a good day!')
        break  #  SUCCESS! Breaks out of the while loop safely.
