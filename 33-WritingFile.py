text = "Are you good?"

# with open('test.txt', 'w') as file:
with open('test.txt', 'a') as file:
    file.write(text)

# the text can be overwritten by default
# or can be append with 'a'