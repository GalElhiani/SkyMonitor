#!/bin/bash

#this script generates a random number from 1-10 and succeeds if the number is greater than 5
#Tested by: Amir malul
#Authored by: Gal Elhiani

num=$(( (RANDOM % 10) + 1 ))

if [ "$num" -gt 5 ]; then

	echo "success!"
	echo "$num"
	logger "Code ran successfully"
else
	echo "failure!"
	echo "$num"
fi
