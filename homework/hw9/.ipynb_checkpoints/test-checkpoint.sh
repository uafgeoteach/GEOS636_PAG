#!/bin/bash
#changing directories. NOTE: This script will break if files are moved to a different directory
for file in ./*.csv; do python speedPlot.py $file; done
#iterating over csv files in directory
