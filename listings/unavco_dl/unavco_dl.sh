#!/bin/bash

#we want to use the station identifier from the command line

id=$1
file=${1}.pbo.nam14.csv

if [[ -e $file ]]; then
	echo "removing $file"
	rm $file
fi

wget ftp://data-out.unavco.org/pub/products/position/${id}/$file

