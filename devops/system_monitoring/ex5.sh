#!/bin/bash

num=$(( (RANDOM % 10) + 1 ))

if  "$num" -gt 5 ]; then

	echo "success!"
	echo "$num"
else
	echo "failure!"
	echo "$num"
fi
