#!/bin/bash

# Trap Ctrl-C (SIGINT) to handle interruption
trap 'echo -e "\nInterrupted. Exiting..."; exit 1' INT

total_wait=120  # 2 minutes in seconds
echo "Waiting for 2 minutes..."

# Progress loop
for ((i=0; i<total_wait; i++)); do
    echo -n "."  # Print dot without newline
    sleep 1
done

echo -e "\nDone waiting. 2 minutes have elapsed."
exit 0