#!/bin/tcsh

set grade = $1


if   ($grade > 90) then
	echo "A"
else if ($grade > 80) then
	echo "B"
else if ($grade > 70) then
	echo "C"
else if ($grade > 60) then
	echo "D"
else
	echo "F"
endif
