#!/bin/bash
# for variable in <list> 
# do 
# 	<block>
# done
#
#
# Example: counting, adding

#from 2 to 10 in steps of 2
for x in `seq 2 2 10`
do
	echo $x
done

echo 'first `for` done'

#sum of vector elements
s=0 
for x in 23 1 5
do
   s=$((s + $x))
done

echo $s
