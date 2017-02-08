<<<<<<< HEAD
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#We could do these two on one line too, how?
input = open(from_file)
indata = input.read()

#indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file,'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()
#open(from_file).close()
=======
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#We could do these two on one line too, how?
input = open(from_file)
indata = input.read()

#indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

output = open(to_file,'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()
#open(from_file).close()
>>>>>>> 8af5007920d10b09036763c592bded1f5db74f0b
