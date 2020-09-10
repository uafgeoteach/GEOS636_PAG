#!/bin/tcsh
# foreach variable ( <list> ) <block>
#
# Example: counting, adding

#from 2 to 10 in steps of 2
foreach x (`seq 2 2 10`)
	echo $x
end
echo 'first `for` done'

#sum of vector elements
set s = 0
foreach x (23 1 5)
   @ s += $x 
end

echo $s
