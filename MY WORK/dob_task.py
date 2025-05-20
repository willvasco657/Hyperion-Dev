with open('DOB.txt', 'r+') as f: # Open the DOB.txt file to read
    lines = f.readlines()

# Create a list to store the names and DOB's   
names = []
dobs = []

for line in lines: # Get the program to read each line
    info_split = line.strip().split() # This splits the lines into single words
    name = " ".join(info_split[:-3]) # Selects the first 2 words in the line
    dob = " ".join(info_split[-3:]) # Selects the last 3 words in the line
    names.append(name) # Add the first 2 words to the names list
    dobs.append(dob) # Add the last 3 words to the dobs list

print ("Names: " + "\n") # Print the list of names
for name in names: # Print what has been defined as name
    print(name)

print ("\n" "Date of birth: ") # Print the date of birth
for dob in dobs: # Find what has been defined as dob
    print(dob)
    