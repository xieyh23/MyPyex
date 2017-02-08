<<<<<<< HEAD
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" %filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

=======
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" %filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

>>>>>>> 8af5007920d10b09036763c592bded1f5db74f0b
