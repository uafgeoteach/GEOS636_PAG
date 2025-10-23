#!/bin/bash
FILES="./*.csv"
for f in $FILES
do
	python speedPlot.py $f
done
