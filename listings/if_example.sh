#!/bin/bash
# 
# BASH SYNTAX: 
#
# if [ <some test> ]
# then
#  	<commands>
# fi
#
# Example: What are we gonna do today?

day='Sat' #`date | awk '{print $1}'`

if [ $day == 'Thu' ]
then
   echo 'New PAG Package'
else
   if [ $day == 'Sat' ] || [ $day == 'Sun' ] 
   then
      echo 'weekend'
   else
      echo 'Deal with other stuff'
   fi
fi
