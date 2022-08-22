#!/bin/bash
echo "begin test using Z3 ..."

count=1
while(( $count<= 100 ))
do
    START=$(date +%s)
    # do something
    # start your script work here
    echo $count
    z3 -smt2 test$count -T:60
    let "count++"
    # your logic ends here
    END=$(date +%s)
    DIFF=$(( $END - $START ))
    echo "It took $DIFF seconds"
done