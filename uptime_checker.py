import subprocess
from datetime import datetime

servers = ["google.com", "8.8.8.8", "thisisafakeaddress12345.com"]

for server in servers:
	result = subprocess.run(["ping", "-c", "1", server], capture_output=True)
	timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	if result.returncode == 0:
		print(f"[{timestamp}] UP: {server}")
	else:
		print(f"[{timestamp}] DOWN: {server}")

