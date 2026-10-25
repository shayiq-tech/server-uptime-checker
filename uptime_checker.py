import subprocess
from datetime import datetime

servers = ["google.com", "8.8.8.8", "thisisafakeaddress12345.com"]

up_count = 0
down_count = 0

log_file = open("uptime_log.txt", "a")

for server in servers:
	result = subprocess.run(["ping", "-c", "1", server], capture_output=True)
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	if result.returncode == 0:
		line = f"[{timestamp}] UP: {server}"
		up_count = up_count + 1
	else:
		line = f"[{timestamp}] DOWN: {server}"
		down_count = down_count + 1
	print(line)
	log_file.write(line + "\n")

summary = (f"\nSummary: {up_count} up, {down_count} down, {len(servers)} total")
print(summary)
log_file.write(summary + "\n")

log_file.close()
