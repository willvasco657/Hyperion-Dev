# Determine number of lines to output
# Create only 5 initial lines
# Create an additional 4 lines that will reverse the statement
# Create a 'for loop' with variable '*'
# Range should have the total lines determined
# If statement creates the first 5 lines
# Else statement creates the bottom 4 lines in reverse

top_lines = 5
bot_lines = top_lines * 2-1

for i in range(1, bot_lines + 1):
    if i <= top_lines:
        print("*" * i)
    else:
        print("*" * (bot_lines - i + 1))