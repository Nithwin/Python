"""
================================================================================
                            PYTHON NOTES & EXAMPLES
================================================================================
"""

# ============================================================================
# 1. DATA TYPES & TYPE CHECKING
# ============================================================================
#
# Common Data Types:
#   str    : Text/String
#   int    : Integer
#   float  : Decimal number
#   bool   : Boolean (True/False)
#   list   : Mutable sequence
#   tuple  : Immutable sequence
#   dict   : Key-value pairs
#   set    : Unordered unique elements
#
# Example:
#   a = 'Hello'
#   num = 34547645637.56
#   flag = False
#   print(type(num))   # <class 'float'>
#   print(type(a))     # <class 'str'>
#
# User Input:
#   a = input('Enter your name: ')  # Read input as string


# ============================================================================
# 2. LOGICAL & BITWISE OPERATORS
# ============================================================================
#
# Logical Operators (with Boolean values):
#   and : Logical AND
#   or  : Logical OR
#   not : Logical NOT
#
# Example:
#   b1 = True
#   b2 = False
#   print(b1 and b2)   # False
#   print(b1 or b2)    # True
#   print(not b2)      # True
#
# Bitwise Operators:
#   &   : Bitwise AND
#   |   : Bitwise OR
#
# Example:
#   b1 = True
#   b2 = False
#   print(b1 & b2)     # False
#   print(b1 | b2)     # True


# ============================================================================
# 3. ARITHMETIC OPERATORS
# ============================================================================
#
#   +   : Addition
#   -   : Subtraction
#   *   : Multiplication
#   **  : Exponentiation (power)
#   /   : Division (float result)
#   //  : Floor division (integer result)
#   %   : Modulus (remainder)
#
# Example:
#   a = 4
#   b = 5
#   print(a + b)       # 9
#   print(a - b)       # -1
#   print(a * b)       # 20
#   print(a ** b)      # 1024 (4^5)
#   print(a / b)       # 0.8
#   print(a // b)      # 0
#
# Compound Assignment:
#   a *= b             # Same as: a = a * b


# ============================================================================
# 4. CONTROL STATEMENTS & CONDITIONS
# ============================================================================
#
# If-Elif-Else:
#   num1 = 1
#   num2 = 2
#   if num1 == num2:
#       print(num1 + num2)
#   elif num1 == 1 and num2 == 2:
#       print(num1 * num2)        # Executes: 1 * 2 = 2
#   else:
#       print(num2 - num1)


# ============================================================================
# 5. LOOPS
# ============================================================================
#
# For Loop - Backward with break:
#   for i in range(11, 0, -1):
#       if i%2 == 0:
#           break                  # Exit loop when i is even
#       else:
#           print(i, end=' ')
#
# While Loop:
#   i = 0
#   while i <= 10:
#       print(i, end=' ')
#       i += 1


# ============================================================================
# 6. STRING METHODS
# ============================================================================
#
# Case Methods:
#   - upper()          : Convert to uppercase
#   - lower()          : Convert to lowercase
#   - title()          : Capitalize first letter of each word
#   - capitalize()     : Capitalize first letter only
#   - swapcase()       : Swap case of all letters
#
# Testing Methods:
#   - isupper()        : Check if all letters are uppercase
#   - islower()        : Check if all letters are lowercase
#   - isalpha()        : Check if all characters are alphabetic
#   - isdigit()        : Check if all characters are digits
#
# Search Methods:
#   - find(substr)     : Find index of substring (-1 if not found)
#   - count(substr)    : Count occurrences of substring
#   - startswith(str)  : Check if starts with substring
#   - endswith(str)    : Check if ends with substring
#
# Modification Methods:
#   - replace(old, new) : Replace all occurrences
#   - strip()          : Remove leading/trailing whitespace
#   - lstrip()         : Remove leading whitespace
#   - rstrip()         : Remove trailing whitespace
#   - split(sep)       : Split into list
#   - join(list)       : Join list elements
#
# Formatting:
#   - format()         : Format string with placeholders
#   - f-strings        : f"{variable} text"
#
# Example:
#   s = "Python is an programming language"
#   print(s.upper())               # PYTHON IS AN PROGRAMMING LANGUAGE
#   print(s.lower())               # python is an programming language
#   print(s.title())               # Python Is An Programming Language
#   print(s.find('is'))            # 7
#   print(s.count('l'))            # 3
#   print(s.startswith('Python'))  # True
#   print(s.replace('Python', 'C++'))  # C++ is an programming language
#   
#   ls = s.split(' ')              # Split by space
#   print(" ".join(ls))            # Join back
#   print("{} {} Good".format('College','is'))
#   name = "Laptop"
#   print(f"{name} is Good")       # Laptop is Good


# ============================================================================
# 7. LISTS - Mutable sequences of elements
# ============================================================================
#
# Key Methods:
#   - append(x)      : Add element to end
#   - extend(list)   : Add multiple elements
#   - insert(i, x)   : Insert element at index
#   - remove(x)      : Remove first occurrence
#   - pop([i])       : Remove and return element at index (default: last)
#   - clear()        : Remove all elements
#   - index(x)       : Find index of first occurrence
#   - count(x)       : Count occurrences
#   - sort()         : Sort in-place
#   - reverse()      : Reverse in-place
#   - copy()         : Shallow copy
#
# Example - List Comprehension:
#   ls = [1,2,3,4]
#   ls = [i**2 for i in range(0, len(ls)) if i%2 == 0]
#   print(ls)                    # Output: [0, 4]
#
# Example - Methods:
#   ls = [1,2,3,4]
#   ls.append(5)
#   ls.extend([86,4,3])
#   ls.insert(1, 1000)
#   ls.remove(1000)
#   ls.pop()                     # Remove last element
#   
#   print(ls.count(3))           # Count occurrences
#   print(ls.index(3))           # Find index
#   
#   ls.sort()                    # Sort ascending
#   ls.reverse()                 # Reverse order
#   
#   ls2 = ls.copy()              # Create independent copy
#   ls2[0] = 100000              # Modify copy, not original
#
# Useful Functions:
#   len(ls), max(ls), min(ls), sum(ls)


# ============================================================================
# 8. TUPLES - Immutable sequences of elements
# ============================================================================
#
# Key Characteristics:
#   - Immutable (cannot be modified after creation)
#   - Ordered and indexed
#   - Can contain duplicate elements
#
# Key Methods:
#   - index(x)   : Return index of first occurrence
#   - count(x)   : Count occurrences of element
#   - len()      : Length
#   - max()      : Maximum value
#   - min()      : Minimum value
#   - sum()      : Sum of all elements
#   - Unpacking  : x, y, z = tuple_with_3_elements
#
# Example:
#   tp = (1,2,3,4)
#   tp2 = (9,8,7)
#   
#   print(tp.index(4))           # Output: 3
#   print(len(tp))               # Output: 4
#   print(max(tp))               # Output: 4
#   print(min(tp))               # Output: 1
#   print(sum(tp))               # Output: 10
#   print(tp * 3)                # Repetition: (1,2,3,4,1,2,3,4,1,2,3,4)
#   
#   x, y, z = tp2                # Unpacking
#   print(x, y, z)               # Output: 9 8 7


# ============================================================================
# 9. SETS - Unordered collections of unique elements
# ============================================================================
# 
# Key Methods:
#   - add(x)           : Add single element
#   - update(list)     : Add multiple elements
#   - remove(x)        : Remove element (raises error if not found)
#   - discard(x)       : Remove element (no error if not found)
#   - pop()            : Remove and return arbitrary element
#   - clear()          : Remove all elements
#   - difference(set)  : Elements in first set but not in second
#   - issubset(set)    : Check if all elements are in another set
#
# Example:
#   s = {1,2,3,4}
#   s = {i**2 for i in s}                    # Set comprehension
#   print(s)                                 # Output: {1, 4, 9, 16}
#
#   s2 = set()
#   s2.add(5)
#   s2.add(4)
#   s2.add(3)
#   s2.update([9,4,19,34])
#   s2 = s2.difference({9,4})
#   
#   subset = {7,6,5,4,3,2}
#   print({99,6}.issubset(subset))          # Check if subset
#   print(s2)