i = 0
numbers = []
"""
#while-loop
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)


    i = i + 1
    print "Number now:", numbers
    print "At the bottom i is %d \n" % i
"""
"""
#for-loop
for i in range(0,6):
    print "At the top i is %d" % i
    numbers.append(i)
    print "Number now:", numbers
    print "At the bottom i is %d \n" % i
"""


print "The numbers:"

for num in numbers:
    print num
