#!/bin/bash

# Get user input for the service
read -p "Type service name: " service_name

# Display the initial status
echo "Service $service_name is:" 
systemctl status "$service_name" | grep "Active:"

# Set menu prompt
PS3="Select an action: "
options=("Start" "Stop" "Leave at current state")

# Open select loop
select opt in "${options[@]}"
do
  case "$opt" in
    "Start")
      sudo systemctl start "$service_name"
      break
      ;;
    "Stop")
      sudo systemctl stop "$service_name"
      break
      ;;
    "Leave at current state")
      echo "No changes made."
      break
      ;;
    *)
      echo "Invalid option. Please choose 1, 2, or 3."
      ;;
  esac
done

# Display the final status
echo "Service $service_name is now:" 
systemctl status "$service_name" | grep "Active:"

