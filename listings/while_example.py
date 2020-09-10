# while CONDITION:
#   STATEMENT
#   [if CONDITION:
#       break]
# 
# EXAMPLE: Run until a new minute starts

import time, datetime

#infinite loop, unless there's a break
#somewhere
while True:
    #use datetime module to get second
    sec = datetime.datetime.now().second
    
    print(sec)
    time.sleep(1)

    #not every while needs a break
    if sec == 59:
        break
    
	
