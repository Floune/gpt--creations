#!/bin/bash

# Set the spinner character
spinner="/-\|"

# Set the number of times the spinner should spin
spin_count=50

# Set the delay between spins (in seconds)
spin_delay=0.1

# Spin the spinner
for ((i=1; i<=spin_count; i++))
do
    printf "\r${spinner:i%${#spinner}:1}"
    sleep $spin_delay
done

# Finish the spinner with a newline
printf "\n"
