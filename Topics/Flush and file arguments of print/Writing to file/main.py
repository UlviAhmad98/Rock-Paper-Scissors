f_name = open("test.txt", "w")
my_string = "A string to be written to a file!"

# what to do with the file and the string
print(my_string, file=f_name)
f_name.close()
