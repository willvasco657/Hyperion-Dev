# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key]) #  Change function to 'key' not 'k'

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", #  Change inverted commas to speech marks
                         "maggie": "(Pacifier Suck)"
                         }

#  Place square bracket for keys in dictionary
print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

