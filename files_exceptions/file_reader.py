"""Reading from a file and stripping whitespace around string."""

# with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#    print(contents.rstrip())

# File paths
# with open('text_files/countries.txt') as file_object:
#    contents = file_object.read()
#    print(contents)

filename = 'pi_digits.txt'

# Reading a line by line
# with open(filename) as file_object:
#    for line in file_object:
#        print(line.rstrip())


# Make a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


# Working with a file's contents
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
