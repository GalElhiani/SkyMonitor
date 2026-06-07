#!/bin/bash
# Usage: source ~/Desktop/git/bash/"Linux - Bash Scripts"/ex9_bash2.sh

# Checks to see if the user used source
(return 0 2>/dev/null) || {                                                    
    echo "ERROR: This script must use source, not bash."
    echo "Correct usage: source ~/Desktop/git/bash/\"Linux - Bash Scripts\"/ex9_bash2.sh"
    exit 1
}

# Bind F10 using path
bind -x '"\e[21~":"bash \"/home/'"$USER"'/Desktop/git/bash/Linux - Bash Scripts/ex8_bash2.sh\""'

echo "F10 is now bound to ex8_bash2.sh"
