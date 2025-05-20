# Request user input
# Save user input
# Determine numerical length of user input
# Replace final letter of user input with "@" along with every other occurrence of the letter
# Print last 3 characters from user input backwards
# create five-letter word from first three and last two letters of input

sentence = input ("Tell me a fact: ")
str_manip = sentence
print(f"Length of sentence: {len(str_manip)}")

last_cha = str_manip [-1]
new_str = str_manip.replace(last_cha, "@")
print(f"New sentence: {new_str}")

last_three = str_manip[-3:][::-1]
print (f"The last three letter backwards are: {last_three}")

first_three = str_manip[:3]
last_two = str_manip[-2:]
secret_word = first_three + last_two
print(f"The secret five-letter word would be: {secret_word}")