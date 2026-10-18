#!/bin/bash

# check my dashboard services and restart them if needed
for service in dashboard-api dashboard-reader dashboard-monitor
do
    if ! systemctl is-active --quiet "$service"; then
        systemctl restart "$service"
        echo "$(date): Restarted $service" >> /var/log/dashboard-health.log
    fi
done
