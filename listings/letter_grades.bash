#!/bin/bash
function letter_grade(){
  if   [ $1 -gt 90 ]; then
	echo "A"
  elif [ $1 -gt 80 ]; then
	echo "B"
  elif [ $1 -gt 70 ]; then
	echo "C"
  elif [ $1 -gt 60 ]; then
	echo "D"
  else
	echo "F"
  fi
}

letter_grade 85
