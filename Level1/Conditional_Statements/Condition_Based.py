# Read a number from user. Display the output based on the given conditions.

# 1. If the given number is between -1 and -3 or between 10&13, print "Case 1".

# 2. If the given number between -4 and -8 or between 14 &18, print "Case 2".

# 3. If the given number is 19, print "Case 3".

# 4. otherwise, print "Case 4".

# NOTE: Both the boundaries are included in the set. For example, if -8 is the input it should display Case 2

# sample input 1: -1

# sample output: Case 1

# sample input 2: 13

# sample output 2: Case 1

# sample input 3: -5

# sample output 3: Case 2


n=int(input())
if ((n<=-1 and n>=-3) or (n>=10 and n<=13)):
    print("Case 1")
elif ((n<=-4 and n>=-8) or (n>=14 and n<=18)):
    print("Case 2")
elif n==19:
    print("Case 3")
else:
    print("Case 4")