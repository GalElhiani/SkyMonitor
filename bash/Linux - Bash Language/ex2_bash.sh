#!/bin/bash
read -p "please enter minimum number" min
read -p "please enter maximum number" max
random_int_within() {
	if [ $min -ge $max ]; then
		echo "error! minimum number has to be lower than maximum number"

	else
		local result=$(shuf -i $min-$max -n 1)
	fi
	echo $result
}

random_int_within

