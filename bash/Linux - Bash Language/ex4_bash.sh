#!/bin/bash
declare -A mentors
mentors=(["Naftali"]="Naftali" ["Tal"]="Tal" ["ilya"]="Ilya" ["Exit"]="Exit")
mentors_emails=("naftali@infinitylabs.co.il" "tal@infinitylabs.co.il" "ilya@infinitylabs.co.il")
PS3="Please enter your choice: "
select name in "${mentors[@]}";
do
case $name in
	"Naftali")
		echo "naftali@infinitylabs.co.il"
	;;

	"Tal")
		echo "tal@infinitylabs.co.il"
	;;

	"Ilya")
		echo "ilya@infinitylabs.co.il"
	;;

	"Exit")
		exit
	;;

	*)
		echo "invalid choice"
	;;
esac
done
