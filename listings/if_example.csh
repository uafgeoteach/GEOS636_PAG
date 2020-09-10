#!/bin/tcsh
# if ( <condition> ) then <statement>
# [else <statement> ]
# endif
#
# Example: What are we gonna do today?

set day = `date | awk '{print $1}'`

if ($day == 'Wed' ) then
   echo 'New PAG Package'
else
   if ($day == 'Sat' || \
       $day == 'Sun') then
      echo 'weekend'
   else
      echo 'Deal with other stuff'
   endif
endif
