#!/bin/bash

#two paramters DIR (directory name)  and SIZE (file size)

read -e -p "Please enter a directory name: " DIR
read -p "Please enter maximum size: " X
target=$(find ~ -type d -name "$DIR")
if cd "$target"; then

	echo "Found target directory"

	for file in *
	do
		size=$(wc -c < "$file")

		if [ "$size" -ge "$X" ]; then
			rm "$file"

		else

			continue

		fi

	done
echo "Deleted files successfully"

else
	echo "Error: cant find the target Directory"
fi

