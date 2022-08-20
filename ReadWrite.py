file = open("text.txt")
# read all the contents of file
# Read n number of characters by passing parameters
# print(file.read(5)) #output abc d

# read one single line at a time readLine()
# print(file.readline(2)) #Output line line 2 > ab


# print line by line using readline method
# line = file.readline()
# # using for loop
# while line != "":
#     print(line)
#     line = file.readline() #to stop loo[ing

for line in file.readlines():
    print(line)

file.close()