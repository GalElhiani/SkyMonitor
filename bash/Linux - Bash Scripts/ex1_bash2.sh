#!/bin/bash

var=$(date +%F)

for file in *; do
	if [ -f "$file" ] && [ "$file" != "$0" ]; then
		mv "$file" "${var} - $file"
	fi

done
