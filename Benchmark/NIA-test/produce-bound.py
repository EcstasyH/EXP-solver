from z3 import *
import random

expnum = 1
linearnum = 2
expfml = 2
linearfml = 3
totaltests = 100

x=[0]*(expnum+linearnum+2)

g = open("NIA-bound/1-2-2-3/paras","w+")
g.write("%d\n" %totaltests)
g.write("{%d,%d,%d,%d}\n" %(expnum,linearnum,expfml,linearfml))

for testno in range(1,totaltests+1):
    for i in range(1,expnum+linearnum+1):
        x[i] = Int('x'+str(i))
    pow = Function('pow',IntSort(),IntSort())

    s = Solver()

    for i in range (1,expnum+linearnum+1):
        s.add(x[i] >= 0)

    for i in range (1,expfml+1):
        g.write("{")
        expr = 0
        for j in range (1,expnum+1):
            coef = random.randint(-10,10)
            expr = expr + coef * pow(x[j])
            g.write("%d," %coef)
        # bound cases
        for j in range (1,expnum+linearnum+1):
            coef = random.randint(-10**5,10**5)
            expr = expr + coef * x[j]
            g.write("%d," %coef)
        
        num = random.randint(-10**5,10**5)
        s.add(expr <= num)
        g.write("%d}\n" % num)
    
    for i in range (1,linearfml+1):
        expr = 0
        g.write("{")
        for j in range (1,expnum+linearnum+1):
            coef = random.randint(-10**2,10**2)
            expr = expr + coef * x[j]
            g.write("%d," %coef)
        num = random.randint(-10**5,10**5)
        s.add(expr <= num)
        g.write("%d}\n" % num)
            
    f = open('NIA-bound/1-2-2-3/test'+str(testno),mode='w+')
    f.write("(set-logic ALL)\n")
    f.write("(define-fun-rec pow ((x Int)) Int (ite (= x 0) 1 (* 10 (pow (- x 1)) ) ) )\n")
    f.write(s.sexpr())
    f.write("(check-sat)\n")
    f.write("(get-model)\n")
    f.seek(0)
    d = f.readlines()
    f.seek(0)
    for i in d:
        if i != "(declare-fun pow (Int) Int)\n":
            f.write(i)
    f.truncate()    
    f.close()

g.close()