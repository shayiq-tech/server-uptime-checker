import subprocess
servers = ["google.com", "8.8.8.8", 
"thisisafakeaddress12345.com"]
for server in servers:
	result = subprocess.run(["ping", "-c", "1", 
server], capture_output=True)
	if result.returncode == 0:
		print(f"✅ {server} is UP")
	else:
		print(f"❌ {server} is DOWN")


