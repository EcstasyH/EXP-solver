from z3 import *
import random

primes = [331,821,233,673,967,227,953,251,397,521,263,541,181,709,811,839,109,383,797,317,571,389,509,373,379,1949,6791,3089,8929,3877,9661,6827,1033,4201,5623,8821,8779,2239,3343,3181,7213,7349,7681,9901,3691,6011,9209,9091,8287,5623,84523,93383,44623,94399,53951,11597,49391,39251,49639,76157,80329,72727,54443,50147,61409,47389,75707,43591,68909,33329,71347,57131,93893,28669,96553,706661,419609,940853,210169,624517,825007,543539,419623,330229,438721,606959,379541,367163,258329,488981,676993,980219,226549,575053,948349,974137,620957,477571,819701,440989]

has_head = 1
head = 12345
has_tail = 0
tail = 6789

totaltests = 100

g = open("all/head/paras","w+")
g.write("%d\n" %totaltests)

for testno in range(1,totaltests+1):
    m1 = primes[testno-1]
    m2 = random.randint(1,m1-1)
    
    g.write("{%d,%d,%d,%d,%d,%d}\n"
     %(has_head,has_tail,head,tail,m1,m2))

        
    f = open('all/head/test'+str(testno),mode='w+')
    f.write("(set-logic QF_SLIA)\n")
    f.write("(set-option :produce-models true)\n")
    f.write("(declare-fun x () String)\n")

    if has_head == 1 and has_tail==1:
        f.write("(assert (str.in_re x (re.++ (str.to_re \"%d\") (re.* (re.range \"0\" \"9\"))(str.to_re \"%d\"))))\n" %(head,tail))
    if has_head == 0 and has_tail==1:
        f.write("(assert (str.in_re x (re.++ (re.* (re.range \"0\" \"9\"))(str.to_re \"%d\")) ))\n" %tail)
    if has_head == 1 and has_tail==0:
        f.write("(assert (str.in_re x (re.++ (str.to_re \"%d\") (re.* (re.range \"0\" \"9\")) )))\n" %head)
    
    f.write("(assert (= (mod (mod (str.to_int x) %d) %d) 0))\n" %(m1,m2))
    f.write("(assert (< (str.len x) 100))\n")
    f.write("(check-sat)\n")
    f.write("(get-model)\n")
    f.close()

    f = open('all/head/trautest'+str(testno),mode='w+')
    f.write("(set-option :produce-models true)\n")
    f.write("(declare-fun x () String)\n")

    if has_head == 1 and has_tail==1:
        f.write("(assert (str.in.re x (re.++ (str.to.re \"%d\") (re.* (re.range \"0\" \"9\"))(str.to.re \"%d\"))))\n" %(head,tail))
    if has_head == 0 and has_tail==1:
        f.write("(assert (str.in.re x (re.++ (re.* (re.range \"0\" \"9\"))(str.to.re \"%d\"))))\n" %tail)
    if has_head == 1 and has_tail==0:
        f.write("(assert (str.in.re x (re.++ (str.to.re \"%d\")(re.* (re.range \"0\" \"9\")))))\n" %head)
    
    f.write("(assert (= (mod (mod (str.to.int x) %d) %d) 0))\n" %(m1,m2))
    f.write("(assert (< (str.len x) 100))\n")
    f.write("(check-sat)\n")
    f.write("(get-model)\n")
    f.close()

g.close()