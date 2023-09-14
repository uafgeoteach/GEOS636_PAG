#!/bin/bash
# while [ <condition> ] 
# do
# 	<block> 
# done
#
# Example: Run until a new minute starts

#infinite loop unless there's a 
#break somewhere
while [ 1 ]
do
   #use unix date command 
   #to get a the current second
   sec=`date +"%S"` 

   echo $sec
   sleep 1

   if [ $sec == 59 ] 
   then 
        echo "done."
	break
   fi
done

