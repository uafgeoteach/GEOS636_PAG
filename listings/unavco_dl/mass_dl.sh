#!/usr/bin/bash

for s in AV21 AV36 AV37 AC10 AV09 P127; do
	./unavco_dl.sh $s
done

