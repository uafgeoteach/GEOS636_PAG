# if CONDITION: 
#    STATEMENT
# [elif CONDITION: 
#    STATEMENT ]
# [elif...]
# [else:
#    STATEMENT ]
#
import datetime

#Get day of the week as an integer, 
#Monday is 0, Sunday is 6.
day = datetime.datetime.today().weekday()

if day == 2:
   print('New PAG Package')
elif day == 5 or day == 6:
   print('weekend')
else:
   print('Deal with other stuff.') 

