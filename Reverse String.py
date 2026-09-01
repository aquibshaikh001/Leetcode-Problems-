#--------------------------First solution

my_string = "hello"
reversed_string = my_string[::-1]

print(reversed_string)


#---------------------------Second solution

my_string = "hello"
reversed_string = ""
for char in my_string:
    reversed_string = char + reversed_string