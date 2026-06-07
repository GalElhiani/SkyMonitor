#!/bin/bash
# Usage: ./ex1_bash2_adv.sh

# 1. Grab the raw text from the Wayland clipboard buffer as plain text
CLIPBOARD_TEXT=$(wl-paste --type text/plain -n 2>/dev/null)

# 2. Stop if the clipboard is empty
if [ -z "$CLIPBOARD_TEXT" ]; then
    echo "Error: Clipboard is empty!"
    exit 1
fi

echo "Searching Google for: $CLIPBOARD_TEXT"

# 3. Pure Bash URL Encoding (Zero external tools, 100% reliable)
ENCODED_TEXT=""
for (( i=0; i<${#CLIPBOARD_TEXT}; i++ )); do
    char="${CLIPBOARD_TEXT:$i:1}"
    case "$char" in
        [a-zA-Z0-9.~_-]) ENCODED_TEXT+="$char" ;;
        *) printf -v hex '%%%02X' "'$char"
           ENCODED_TEXT+="$hex" ;;
    esac
done

# 4. Open the default browser to the Google search results and silence terminal logs
xdg-open "https://www.google.com/search?q=${ENCODED_TEXT}" >/dev/null 2>&1 &
