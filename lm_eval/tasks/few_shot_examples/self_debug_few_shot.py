# Write Python function to complete the task and pass the assertion tests.

### Task Start ###
# These are the assertions for your function:
assert count_ways(2) == 3

""" Write a function to find the number of ways to fill it with 2 x 1 dominoes for the given 3 x n board. """
def count_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 3
    return count_ways(n-1) + count_ways(n-2)

Feedback: The code above is wrong. Please fix it.

def count_ways(n):
  A = [0] * (n + 1)
  B = [0] * (n + 1)
  A[0] = 1
  A[1] = 0
  B[0] = 0
  B[1] = 1
  for i in range(2, n+1):
    A[i] = A[i - 2] + 2 * B[i - 1]
    B[i] = A[i - 1] + B[i - 2]
  return A[n]

Feedback: The code above is correct.
### Task End ###

### Task Start ###
# These are the assertions for your function:
assert differ_At_One_Bit_Pos(15,8) == False

""" Write a python function to check whether the two numbers differ at one bit position only or not. """
def differ_At_One_Bit_Pos(lhs,rhs):
    if (lhs - rhs) == 0 or (lhs - rhs) == 1:
        return True
    return False

Feedback: The code above is wrong. Please fix it.

def differ_At_One_Bit_Pos(a,b):
  x = a ^ b
  return x and (not(x & (x - 1)))

Feedback: The code above is correct.

### Task End ###

### Task Start ###
# These are the assertions for your function:
assert find_char_long('Please move back to stream') == ['Please', 'move', 'back', 'stream']

""" Write a function to find all words which are at least 4 characters long in a string by using regex. """
def find_char_long(text):
  return (re.findall(r"\b\w{4,}\b", text))

Feedback: The code above is wrong. Please fix it.

import re
def find_char_long(text):
  return (re.findall(r"\b\w{4,}\b", text))

Feedback: The code above is correct.

### Task End ###

### Task Start ###
# These are the assertions for your function:
assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

""" Write a function to find squares of individual elements in a list using lambda function. """
def square_nums(nums):
  square_nums = list(map(lambda x: x ** 2, nums))
  return square_nums

Feedback: The code above is correct.

### Task End ###

### Task Start ###
# These are the assertions for your function:
assert find_Rotations("aaaa") == 1

""" Write a python function to find the minimum number of rotations required to get the same string. """
def find_Rotations(s):
    if len(s) == 1:
        return 1
    elif len(s) == 0:
        return 0
    else:
        l = len(s)
        min = len(s)
        for i, c in enumerate(s):
            if c == s[0]:
                temp = i
                if temp < min:
                    min = temp
        return min

Feedback: The code above is wrong. Please fix it.

def find_Rotations(s):
  n = len(s)
  for i in range(1, n + 1):
    if s[i:n] + s[0:i] == s:
      return i
  return n

Feedback: The code above is correct.

### Task End ###

### Task Start ###
# These are the assertions for your function:
assert small_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100],2)==[10,20]

"""  Write a function to get the n smallest items from a dataset. """
def small_nnum(lst,n):
  lst = sorted(lst)
  lst = lst[:n]
  return lst

Feedback: The code above is correct.

### Task End ###

### Task Start ###
# These are the assertions for your function:
