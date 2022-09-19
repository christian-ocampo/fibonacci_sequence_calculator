# fibonacci_sequence_calculator
Calculated Fibonacci Sequence to nth terms using three methods.

The Fibonacci Series is a sequence of integers where each integer is the sum of the previous two, except for the first two integers in the sequence. This program demonstrates this sequence using three methods: lists, generators, and recursion.

In the list method, an empty list called nums is created alongside variable a and b with values of 0 and 1, respectively. A while loop is created which ends when the length of nums is less than the number inputted by the user. The loop begins by appending the value of a to the list and re-assigning a and b to b and a + b, respectively. It is important to re-assign both variables at the same time because each is dependent on the other's previous value. Once the loop finishes, the fib function returns the completed nums list and prints the result.

In the generator method, variables a and b are assigned 0 and 1 respectively. A for loop is created to run for n times where the value of a is returned as a generator. After the variable a is printed, a and b are re-assigned to b and a + b, respectively. It is important to re-assign both variables at the same time because each is dependent on the other's previous value.

In the recursion method, the equation F(n) = F(n - 1) + F(n - 2) is used, where n > 1. When n <= 1, if else statements are used to return 0 if n is 0, or 1 if n is 1. Otherwise, the fib_rec function calls itself with the statement fib_rec(n - 1) + fib_rec(n - 2). Unlike the previous 2 methods, the recursion method only prints the value of the requested order of the sequence instead of the complete sequence for the first n numbers.
##### For example:
```
 F(5) = F(4) + F(3)
      = [F(3) + F(2)] + [F(2) + F(1)]
      = [[F(2) + F(1)] + [F(1) + F(0)]] + [[F(1) + F(0)] + 1
      = [[F(1) + F(0)] + 1] + [1 + 0] + [1 + 0] + 1
      = [[1 + 0] + 1] + 1 + 1 + 1
      = [1 + 1] + 1 + 1 + 1
      = 2 + 1 + 1 + 1
      = 5 <- This is the value that would be displayed
