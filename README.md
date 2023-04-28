# Competitive_Pros

## WEIRD NUMS SOLUTION:

### This is a Python program that takes input from the user and classifies the number based on certain conditions. Let's break down the code:

> 1. `n = input().split()` - This line of code takes the input from the user as a string and splits it into a list of strings using the default separator which is a space.

> 2. `try: ... except:` - Here, we use a try-except block to handle any exceptions that may arise. We loop through each element in the list and convert it into an integer using the `int()` function. If any negative number is found, an exception is raised.

> 3. `o = [] ...` - Here, we create an empty list called "o" to store the output for each input number. We loop through each number in the input list and check if it is even or odd using the modulo operator (`%`). If it is even, we apply certain conditions to classify the number as either "Not Weird", "Weird", or "-1" if it doesn't satisfy any condition. Similarly, for odd numbers, we apply certain conditions to classify them as either "Not Weird", "Weird", or "-2" if it is equal to 5.

> 4. `print(o)` - Finally, we print the list of outputs.




## ROOM INFINITY SOLUTION:

### Taking input of number of elements and the list of integers
> k, arr = int(input()), list(map(int, input().split()))

### Creating a set from the list to find the unique integers
> myset = set(arr)

### Calculating the sum of the unique integers
> unique_sum = sum(myset)

### Calculating the sum of all integers in the original list
> total_sum = sum(arr)

### Calculating the missing number using the formula
> missing_num = ((unique_sum * k) - total_sum) // (k-1)

### Printing the missing number
> print(missing_num)
