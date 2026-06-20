#!/bin/bash
read -p "Please enter a directory name: " DIR
echo "$DIR"

target=$(find ~ -type d -iname "$DIR")


if [ -n "$target" ] && cd "$target"; then
	echo "Found target directory"

	for curr_file in *
	do
		file "$curr_file"

	done

else
		echo "Error: cant find the target Directory"
	fi

