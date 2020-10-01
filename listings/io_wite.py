fname = "io_print.txt"

#1) open this file in read mode
print("Example 1")
print("--------------------Start")
my_file = open(fname, "r")
#print the entire thing
print(my_file.read()) 
#close the file
my_file.close()
print("--------------------End")

#2) print a two lines of the file
print("Example 2")
print("--------------------Start")
my_file = open(fname, "r")
#read and print a line, twice
print(my_file.readline()) 
print(my_file.readline()) 
#close the file
my_file.close()
print("--------------------End")

#3) print each line in a loop
print("Example 3")
print("--------------------Start")
with open(fname, 'r') as my_file:
   for l in my_file:
      print(l, end='') 
print("--------------------End")

