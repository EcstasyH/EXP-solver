from z3 import *
import random

primes = [929,839,739,761,389,701,283,887,569,359,881,163,683,719,907,607,653,857,431,331,239,127,563,607,311,8831,6967,2417,4099,7001,8117,8677,3253,9419,3449,1171,9103,1307,4919,5821,8101,5147,9337,9067,1009,6679,6011,5471,7723,2027,94433,15149,13901,17183,68791,50263,54559,67181,38561,10691,90263,41887,83891,36929,55213,72139,25601,31159,52709,98939,83077,74363,21937,97547,47017,904697,911893,640891,124133,341821,946753,660599,856733,937067,999329,444557,297719,203449,357263,145399,192347,892597,420731,210143,475957,371251,843067,498461,265861,917803]
has_head = 1
head = 12345
has_tail = 1
tail = 6789

totaltests = 100

g = open("flatten/head-tail/paras","w+")
g.write("%d\n" %totaltests)

for testno in range(1,totaltests+1):
    m1 = primes[testno-1]
    m2 = random.randint(1,m1-1)
    a = random.randint(1,99)
    b = random.randint(1,99)
    
    g.write("{%d,%d,%d,{%d,%d},%d,%d,%d}\n"
     %(has_head,has_tail,head,a,b,tail,m1,m2))

        
    f = open('flatten/head-tail/test'+str(testno),mode='w+')
    f.write("(set-logic QF_SLIA)\n")
    f.write("(set-option :produce-models true)\n")
    f.write("(declare-fun x () String)\n")

    if has_head == 1 and has_tail==1:
        f.write("(assert (str.in_re x (re.++ (str.to_re \"%d\") (re.+ (str.to_re \"%d\")) (re.+ (str.to_re \"%d\"))(str.to_re \"%d\"))))\n" %(head,a,b,tail))
    if has_head == 0 and has_tail==1:
        f.write("(assert (str.in_re x (re.++ (re.+ (str.to_re \"%d\")) (re.+ (str.to_re \"%d\"))(str.to_re \"%d\")) ))\n" %(a,b,tail))
    if has_head == 1 and has_tail==0:
        f.write("(assert (str.in_re x (re.++ (str.to_re \"%d\") (re.+ (str.to_re \"%d\")) (re.+ (str.to_re \"%d\")) )))\n" %(head,a,b))
    
    f.write("(assert (= (mod (mod (str.to_int x) %d) %d) 0))\n" %(m1,m2))
    f.write("(assert (< (str.len x) 100))\n")
    f.write("(check-sat)\n")
    f.write("(get-model)\n")
    f.close()

    f = open('flatten/head-tail/trautest'+str(testno),mode='w+')
    f.write("(set-option :produce-models true)\n")
    f.write("(declare-fun x () String)\n")

    if has_head == 1 and has_tail==1:
        f.write("(assert (str.in.re x (re.++ (str.to.re \"%d\") (re.+ (str.to.re \"%d\")) (re.+ (str.to.re \"%d\"))(str.to.re \"%d\"))))\n" %(head,a,b,tail))
    if has_head == 0 and has_tail==1:
        f.write("(assert (str.in.re x (re.++ (re.+ (str.to.re \"%d\")) (re.+ (str.to.re \"%d\"))(str.to.re \"%d\"))))\n" %(a,b,tail))
    if has_head == 1 and has_tail==0:
        f.write("(assert (str.in.re x (re.++ (str.to.re \"%d\") (re.+ (str.to.re \"%d\")) (re.+ (str.to.re \"%d\")))))\n" %(head,a,b))
    
    f.write("(assert (= (mod (mod (str.to.int x) %d) %d) 0))\n" %(m1,m2))
    f.write("(assert (< (str.len x) 100))\n")
    f.write("(check-sat)\n")
    f.write("(get-model)\n")
    f.close()

g.close()