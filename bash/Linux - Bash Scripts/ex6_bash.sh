#!/bin/bash

#mapping hebrew and keyboard layouts to strings
english_map="qwertyuiop[]asdfghjkl;'\`zxcvbnm,./"
hebrew_map="/'קראטוןםפ][שדגכעיחלךף,\;זסבהנמצתץ."

#read input string
read -p "Please enter input in english/hebrew: " inputString

#convert string to lowercase
inputString="${inputString,,}"
outputString=""
#check if the input is in english
if echo "$inputString" | grep -q '[a-z]'; then
echo "if1"
Source="$english_map"
Dest="$hebrew_map"

#check if the input is in hebrew
elif echo "$inputString" | grep -q '[א-ת]'; then
echo "if2"
Source="$hebrew_map"
Dest="$english_map"

fi

echo "DEBUG SOURCE LENGTH IS  ${#Source}"
echo "DEBUG DEST LENGTH IS ${#Dest}"

#iterate through the inputString char by char
for (( i=0; i<"${#inputString}"; i++ )); do
char="${inputString:$i:1}"
found=false
#iterate through the source map
for (( j=0; j<"${#Source}"; j++ )); do
source_char="${Source:$j:1}"


if [[ "$source_char" == "$char" ]]; then
translated_char="${Dest:$j:1}"
outputString+="$translated_char"
found=true
break

fi

done

#we handle special cases like space or number to keep it as is
if [ "$found" = false ]; then
outputString+="$char"
fi

done


echo "Converted: $outputString"
