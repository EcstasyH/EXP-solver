#!/bin/bash
echo "begin test..."

cd new-test
    cd 2-3-3-4
    #./runz3.sh > z3-result2 
    ./runcvc4.sh > cvc4-result
    cd ..
    cd 3-4-4-5
    #./runz3.sh > z3-result2 
    ./runcvc4.sh > cvc4-result
    cd ..
    cd 4-5-5-6
    #./runz3.sh > z3-result2
    ./runcvc4.sh > cvc4-result
    cd ..
cd ..