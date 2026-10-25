# Server Uptime Checker

## Problem
At my job, alerts on the service board flag when a server or service becomes 
unreachable. This script is a simplified version of that detection process — 
checking whether a list of servers is responding, and reporting a clear status for 
each.

## Solution
A Python script that:
- Pings a list of servers
- Reports a timestamped UP/DOWN status for each one
- Prints a summary count at the end
- Logs all results to a persistent file (uptime_log.txt), which grows with each run

## How to run it
python3 uptime_checker.py

## What I learned
- Running system commands from Python using the subprocess module
- Working with timestamps using datetime
- Reading/writing files in Python
- Using .gitignore to keep generated log files out of version control
