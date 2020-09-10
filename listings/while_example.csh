#!/bin/tcsh
# while ( <condition> ) <block> end
#
# Example: Run until a new minute starts

#infinite loop unless there's a 
#break somewhere
while ( 1 )
   #use unix date command 
   #to get a the current second
   set sec = `date +"%S"` 

   echo $sec
   sleep 1

   if($sec == 59) then 
        echo "done."
	break
   endif
end

