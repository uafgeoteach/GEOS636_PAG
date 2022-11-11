#!/bin/bash

obs="1294501"

wget "https://pds-geosciences.wustl.edu/mro/mro-m-sharad-5-radargram-v2/mrosh_2101/data/geom/s_0${obs:0:4}xx/s_0${obs}_geom.tab"
