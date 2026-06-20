#!/bin/bash

count=0

if cd "$1"; then

for file in *; do
	if [ -f "$file" ]; then
		count=$((count+1))
	fi
done
echo "$count"
else
echo "Invalid Path"
fi

