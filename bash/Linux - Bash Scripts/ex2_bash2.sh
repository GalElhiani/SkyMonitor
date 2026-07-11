#!/bin/bash

read -e -p "please enter a path to a directory: " path
count=0

if cd "$path"; then

for file in *; do
	if [ -f "$file" ]; then
		count=$((count+1))
	fi
done
echo "$count"
else
echo "Invalid Path"
fi

