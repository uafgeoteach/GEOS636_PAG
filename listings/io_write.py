fname = 'io_write.txt'

#open file in write mode, add text
#needs newline if we want them
f = open(fname, "w")
f.write("First Text\n")
f.close()

#open file in write mode again, overwrite
f = open(fname, "w")
f.write("Second Text\n")
f.close()

#open file in append mode and append text
f = open(fname, "a")
f.write("Appended Text\n")
f.close()

