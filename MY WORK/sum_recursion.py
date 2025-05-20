
# Create function to sum all elements in a list
def sums(first, index):
    if index == 0: # Create the base case
        return first[0] # Return the first element in the list
    return first[index] + sums(first, index - 1) # Return the sum of digits including base case

print(sums([1, 2, 3, 4, 6, 18, 64, 22, 48], 4)) # Call function and print result