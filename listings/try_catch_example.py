# try:
#   STATEMENT
# except [ErrorCode]:
#   STATEMENT
# [except [ErrorCode]:
#   STATEMENT]
# [finally:
#   STATEMENT]
# 
# EXAMPLE: iterating and dividing
#

values = [1, 'x', 3]

for x in values:
  try: 
    r = 1/x
    print("reciprocal of %d is %f" % (x, r))
  except Exception as e:
    print(e)

  

   
