import sys
sys.stdout.flush()
def return_collatz(a):
    if a%2 == 0:
        a = a/2
    else:
        a = 3*a + 1
    return a

def collatz_count(a):
    count = 1
    while a != 1:
        count = count + 1
        a = return_collatz(a)
        #print count
    return count

seq = [0]*1000000

for i in range(1000000):
    #print i
    seq[i] = collatz_count(i+1)
    if i % 1000 == 0 or i == 1000000:
        print "At ", i, " the sequence is ", seq[i]

print max(seq)
print seq.index(max(seq)) + 1



