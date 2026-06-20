#!/bin/bash
# Usage: source ~/Desktop/git/bash/"Linux - Bash Scripts"/advanced/ex3_bash2_adv.sh

# Checks to see if the user used source
(return 0 2>/dev/null) || {                                                    
    echo "ERROR: This script must use source, not bash."
    echo "Correct usage: source ~/Desktop/git/bash/\"Linux - Bash Scripts\"/advanced/ex3_bash2_adv.sh"
    exit 1
}

BASE_PATH="/home/$USER/Desktop/git/bash/Linux - Bash Scripts/advanced"

# Bind F11 to your Google Search script
bind -x '"\e[23~":"bash \"'"$BASE_PATH"'/ex1_bash2_adv.sh\""'

# Bind F12 to your Google Translate script
bind -x '"\e[24~":"bash \"'"$BASE_PATH"'/ex2_bash2_adv.sh\""'

echo "Hotkeys configured successfully:"
echo "bound F11 to ex1_bash2_adv.sh"
echo "bound F12 to ex2_bash2_adv.sh"
