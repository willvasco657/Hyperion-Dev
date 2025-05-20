meme_string = input("Please enter your least favourite food and why: ") # Ask user for the input string
n_meme_string = " " 

for i in range(len(meme_string)): # Create a for loop to determine which character is capitalised
    if i % 2 == 1: # If command to determine the interval at which the characters are capitalised
        n_meme_string += meme_string[i].upper() 
    else:
        n_meme_string += meme_string[i].lower()
print(n_meme_string) # Print the string with alternative characters capitalised

new_meme = meme_string.split() # Create a new variable so the program can use the same user input whilst splitting the string
for i in range(len(new_meme)): # Index the user input so the program can determine which words to capitalise
    if i % 2 == 1:
        new_meme[i] = new_meme[i].upper()
    else:
        new_meme[i] = new_meme[i].lower()

cap_sentence = " ".join(new_meme) # Join the string back together once the correct words have been capitalised
print(cap_sentence) # Print the same input but with alternative words capitalised instead
