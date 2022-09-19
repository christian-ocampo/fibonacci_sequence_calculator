import sys


# Generators and Yield
#
# Generators act as a more memory-efficient form of creating sequences.
# In simple terms, generators can be thought of as empty sequences
# being continuously appended using 'yield'. In order for them to be
# memory-efficient, they can only be used once.

# The fibonacci series is a sequence of integers where each integer
# is the sum of the previous two, except for the first two integers
# in the sequence.
#
# This function demonstrates the fibonacci series for the first
# 'n' integers without the usage of a generator.
def fib(n):
    nums = []
    a, b = 0, 1

    while len(nums) < n:
        nums.append(a)
        # It is crucial to re-assign both variables at the same time
        # because each is dependent on the other's previous value.
        a, b = b, a + b

    return nums


print('Fibonacci series without using a generator.')
print(fib(10))  # The result is [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# The size of this file 8856 bytes!
print(f'File Size: {sys.getsizeof(fib(1000))}')
print()


# This file size is greatly reduced using generators.
def fib_gen(n):
    a, b = 0, 1

    for index in range(n):
        yield a
        # It is crucial to re-assign both variables at the same time
        # because each is dependent on the other's previous value.
        a, b = b, a + b


print('Fibonacci series using a generator.')
for i in fib_gen(10):
    print(i)

print(f'File Size: {sys.getsizeof(fib_gen(1000))}.')  # Only 104 bytes!
print()


# Alternatively. recursions may be used to display the fibonacci series
# for the first 'n' integers.
def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


print('Fibonacci series using recursion:')
for number in range(1, 11):
    print(fib_rec(number))

# Fibonacci Series explanation:
# F(n) = F(n - 1) + F(n - 2)
# Where F(0) = 0 and F(1) = 1
#
# Example:
# F(5) = F(4) + F(3)
#      = [F(3) + F(2)] + [F(2) + F(1)]
#      = [[F(2) + F(1)] + [F(1) + F(0)]] + [[F(1) + F(0)] + 1
#      = [[F(1) + F(0)] + 1] + [1 + 0] + [1 + 0] + 1
#      = [[1 + 0] + 1] + 1 + 1 + 1
#      = [1 + 1] + 1 + 1 + 1
#      = 2 + 1 + 1 + 1
#      = 5
print(f'The fifth integer in the fibonacci series is: {fib_rec(5)},',
      'assuming we exclude zero.')
