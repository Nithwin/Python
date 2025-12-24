# PYTHON PROGRAMMING NOTES

## Table of Contents
1. [Lambda Functions](#lambda-functions)
2. [Conditional Expressions](#conditional-expressions)
3. [Higher-Order Functions](#higher-order-functions)
   - [Map](#map-function)
   - [Filter](#filter-function)
   - [Reduce](#reduce-function)
4. [Function Arguments](#function-arguments)
5. [Default Parameters](#default-parameters)
6. [Higher-Order Functions (Callbacks)](#callbacks)
7. [Dictionaries](#dictionaries)
8. [Sorting with Lambda](#sorting-with-lambda)
9. [Built-in Functions](#built-in-functions)

---

## Lambda Functions

Lambda functions are anonymous functions defined using the `lambda` keyword.

**Syntax:** `lambda arguments: expression`

### Examples

```python
# Regular function
def sq(x):
    return x*x

# Lambda equivalent
sq2 = lambda x: x**2

# Regular sum function
def sum(x,y):
    return x+y

# Lambda equivalent
sum2 = lambda x,y: x+y
```

### Usage
```python
print(sq(5))      # Output: 25
print(sq2(6))     # Output: 36
print(sum(3,4))   # Output: 7
print(sum2(3,4))  # Output: 7
```

---

## Conditional Expressions

Also known as **Ternary Operator** - a one-line if-else statement.

**Syntax:** `value_if_true if condition else value_if_false`

### Examples

```python
age = 18

# Traditional if-else
if age < 18:
    print('Not Eligible')
else:
    print('Eligible')

# Ternary operator (one-liner)
var = 'Not Eligible' if age < 18 else 'Eligible'
print('Not Eligible' if age < 18 else 'Eligible')
```

---

## Higher-Order Functions

### Map Function

Applies a function to all items in a list.

#### Custom Implementation
```python
def map2(func, ls):
    for i in range(0, len(ls)):
        ls[i] = func(ls[i])
    return ls
```

#### Built-in Map Examples
```python
l = [8,4,6,8,2,1]

# Square all elements
new_l = list(map(lambda x: x**2, l))

# Traditional loop approach
for i in range(0, len(l)):
    l[i] *= l[i]
```

---

### Filter Function

Filters items based on a condition.

#### Custom Implementation
```python
def filter2(func, ls):
    res = []
    for i in ls:
        if func(i):
            res.append(i)
    return res
```

#### Examples
```python
def cmp(x):
    return x%2 == 0

l = [8,4,6,8,2,1]

# Get odd numbers
odd_numbers = list(filter2(lambda x: x%2 != 0, l))
```

---

### Reduce Function

Reduces a list to a single value by applying a function cumulatively.

**Note:** Import required: `from functools import reduce`

#### Custom Implementation
```python
def reduce2(func, ls):
    prev = 1
    for i in ls:
        prev = func(prev, i)
    return prev
```

#### Example
```python
def mul(x,y):
    return x*y

l = [8,4,6,8,2,1]

# Multiply all elements
res = reduce2(lambda x,y: x*y, l)
```

---

## Function Arguments

- **`*args`**: Variable number of positional arguments (tuple)
- **`**kwargs`**: Variable number of keyword arguments (dictionary)

### Examples

```python
def Fun(x, *args, **kwargs):
    print(x)                    # First positional argument
    print(args)                 # Tuple of additional positional arguments
    print(kwargs.values())      # Dictionary values of keyword arguments

Fun(5, 6, 7, 8, name='python', year=2025, age=45)
```

**Output:**
```
5
(6, 7, 8)
dict_values(['python', 2025, 45])
```

### Variable Arguments Example
```python
def add(*args):
    return sum(args)

print(add(5,6,7,7,8,9))  # Sum of all arguments
```

---

## Default Parameters

Functions can have default parameter values.

```python
def Welcome(name, message="Hello"):
    print(message + " " + name)

Welcome("Python", "Hi")  # Output: Hi Python
Welcome("Python")        # Output: Hello Python (uses default)
```

---

## Higher-Order Functions (Callbacks)

Functions that accept other functions as arguments.

### Examples

```python
def mul(x,y):
    return x*y

def Operations(fun, x, y):
    return fun(x, y)

print(Operations(mul, 3, 2))  # Output: 6
```

### List Multiplication Example
```python
def mul(ls):
    res = 1
    for i in ls:
        res *= i
    return res

print(mul([1,2,3,4]))  # Output: 24
```

---

## Dictionaries

### Creation and Basic Operations

```python
dist = {
    "Name": "Python",
    "Number": 25,
    34: 1,  # Keys can be different types
}

dist2 = {
    "Reg_no": "8575"
}
```

### Dictionary Methods

| Method | Description |
|--------|-------------|
| `dist.update(dist2)` | Merge dictionaries |
| `dist.get('Name')` | Safe key access (returns None if not found) |
| `dist['Name']` | Direct access (raises KeyError if not found) |
| `dist.pop('Name')` | Remove and return value |
| `dist.popitem()` | Remove and return last key-value pair |
| `dist.clear()` | Remove all items |
| `dist.copy()` | Create a shallow copy |

### Adding/Updating Values

```python
dist2 = {}
dist2['Name'] = 'Hello'
dist2['Name'] = 'Python'    # Overwrites previous value
dist2['5'] = 'Python'
```

### Iterating Through Dictionary

```python
for key, value in dist2.items():
    print(key + " " + value)
```

### Checking Keys

```python
if "Name" in dist2:
    print(dist2["Name"])
```

### Useful Functions

- `len(dist2)` - Number of key-value pairs
- `dir(dist)` - List all methods available

---

## Sorting with Lambda

```python
l = [(1,3,4), (5,2,6), (9,1,3)]

# Sort by second element of each tuple
l.sort(key=lambda x: x[1])
```

---

## Built-in Functions

| Function | Description |
|----------|-------------|
| `all()` | Returns True if all elements are True |
| `help()` | Get documentation for a function/object |
| `dir()` | List attributes and methods of an object |
| `len()` | Return the length of an object |
| `sum()` | Sum of all elements in an iterable |

### Example
```python
age = 18
if all([age == 18, age == 18, age == 18]):
    print('Success')
```
