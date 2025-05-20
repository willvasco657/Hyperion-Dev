# create string "the!quick!brown!fox!jumps!over!the!lazy!dog."
# format the sentence to replace "!" with " "
# format the sentence to uppercase
# format the sentence to print in reverse
# print the sentence

# I used the "string_example1" as a reference point for my lines of code
# as well as the examples from the "String and Numericak Data" PDF
manip_string = "the!quick!brown!fox!jumps!over!the!lazy!dog."
manip_string = manip_string.replace("!", " ")
manip_string = manip_string.upper()
print(f"{manip_string}"[::-1])