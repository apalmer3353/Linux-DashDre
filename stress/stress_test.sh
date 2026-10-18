#!/bin/bash

# this script is used to put different loads on the server
# so i can see how the dashboard reacts

# script starting
systemd-notify --ready

# send notification, im still running 
(
    while true; do
        systemd-notify WATCHDOG=1
        sleep 30
    done
) &

while true; do

    # first im testing how the cpu handles a higher load
    echo "Starting CPU test"
    stress-ng --cpu 2 --timeout 30s

    # now testing memory usage with 512MB
    echo "Starting memory test"
    stress-ng --vm 1 --vm-bytes 512M --timeout 30s

    # testing how the disk handles writing data
    echo "Starting disk test"
    stress-ng --hdd 1 --hdd-bytes 256M --timeout 30s

    
    echo "Starting filesystem test"
    stress-ng --dir 1 --timeout 30s

    # testing how the system handles switching between tasks
    echo "Starting scheduling test"
    stress-ng --switch 1 --timeout 30s

    # delayyying uhmm probably 30 is good
    echo "Waiting 30 seconds"
    sleep 30
done
