# Creat function that finds largest integer in a list
def largest(first, num):
     if num == 1: # Create base case
          return first[0] # Return the first element in the list
     return max(first[num - 1], largest(first, num - 1)) # Find the largest number in the list


numbers = [15, 23, 1, 28, 45, 16, 89, 49] #  EXAMPLE
print(largest(numbers, len(numbers)))