#!/bin/tcsh
# foreach variable ( <list> ) <block>
#
# Example: counting, adding

set cnt = 0

foreach x (`ls ./`)
  if ($x == foreach_break_example.csh) then
      echo "That's me: $x"
      continue # <-- omit everything below
  endif

  echo $x

  if ($cnt >= 10) then
      echo "I've got $cnt files, I am done."
      break #<-- exit the foreach NOW
  endif

  @ cnt += 1
end
