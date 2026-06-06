#!/bin/bash
# Usage: ./ex2_bash2_adv.sh

# 1. Grab raw clipboard text
CLIPBOARD_TEXT=$(wl-paste -n 2>/dev/null)

# 2. Halt if the clipboard is completely empty
if [ -z "$CLIPBOARD_TEXT" ]; then
    echo "Error: Clipboard is empty!"
    exit 1
fi

# 3. Detect language explicitly to force Google to behavior correctly
# This matches the Unicode block range for Hebrew characters (U+0590 to U+05FF)
if [[ "$CLIPBOARD_TEXT" =~ [א-ת] ]]; then
    SL="he"
    TL="en"
else
    SL="auto"
    TL="he"
fi

# 4. Use 'od' to convert characters to hex cleanly (safeguards Hebrew bytes)
ENCODED_TEXT=$(printf '%s' "$CLIPBOARD_TEXT" | od -An -t x1 | tr -d '\n ' | sed 's/\(..\)/%\1/g')

# 5. Launch Google Translate with explicit source and target parameters
xdg-open "https://translate.google.com/?sl=${SL}&tl=${TL}&text=${ENCODED_TEXT}&op=translate" >/dev/null 2>&1 &
