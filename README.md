# Linux Infrastructure Monitoring Dashboard

## Project Overview
This project is a Linux monitoring dashboard I built for
my linux projet. 

It monitors a Google Cloud Ubuntu server and displays
system performance in a web dashboard.

## Features
- Live CPU usage
- Live memory usage
- Disk usage monitoring
- Network sent and received
- Historical performance graphs
- Adjustable performance alerts
- Automatic service recovery
- Stress testing with stress-ng

## How It Works
- I used Python to check the server's CPU, memory, disk, and network usage.

- The Python script sends that information through a Linux named pipe.

- Another script reads the information from the pipe and saves it.

- Flask takes the saved information and makes it available to my dashboard.

- The dashboard displays the current usage, past activity in graphs, and alerts when usage gets too high.

- I used systemd to run and restart the services, and cron to check them every five minutes.

## Technologies Used
- Ubuntu
- Google Cloud
- Bash
- Python
- Flask
- psutil
- systemd
- cron
- Git and GitHub
- Google search for much  help with python coding

## Author
Aeondre Palmer
