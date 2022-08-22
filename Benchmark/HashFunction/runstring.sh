#!/bin/bash
echo "begin test..."

cd all
    cd tail
    ./runz3str.sh > z3str-result 
    cd ..
cd ..

cd flatten
    cd head-tail
    ./runz3str.sh > z3str-result 
    cd ..
    cd tail
    ./runz3str.sh > z3str-result 
    cd ..
cd ..