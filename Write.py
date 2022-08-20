# read the file and store all the lines in list
# reverse the list
# write the list back to the file

# we won't to user file.close() so we use this instead
# r > representation for read
with open('text.txt', 'r') as reader:
    content = reader.readlines() #Read all lines
    reversed(content) #reverse text
    print(content) #['abc\n', 'de\n', 'fe']
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line) #create new test.txt
