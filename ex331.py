i = 0
j = 0
k = 0
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
def func1(i,j,k):
    #print"please input i:  >>>"
    i=int(raw_input("please input i:  >>>"))
    #print"please input j  >>>"
    j=int(raw_input("please input j:  >>>"))
    #print"please input k  >>>"
    k=int(raw_input("please input k:  >>>"))
    print"i: %d, j:%d" % (i, j)
    while i < j:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + k
        print "Number now:", numbers
        print "At the bottom i is %d \n" % i
 
func1(i,j,k)

print "The numbers:"

for num in numbers:
    print num
