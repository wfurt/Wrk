#!/bin/bash

ARG=-p
I=0
MAX=10

if [ "$2" != '' ]; then
    MAX=$2
fi

rm -f results.txt
while [ $I -lt $MAX ]; do
	./wrk.sh $1 $ARG 2>/dev/null | grep /sec: | tee -a results.txt
	I=$(($I+1))
done
echo $@ done
./process.py
