import os
import subprocess

# 1. Create a new user with a specific password
username = "haidanh"
password = "H@i03052008"

# Create the user and set the password
subprocess.run(f"sudo useradd -m -s /bin/bash {username}", shell=True)
subprocess.run(f"echo '{username}:{password}' | sudo chpasswd", shell=True)

# 2. Install and configure SSH
subprocess.run("sudo apt update", shell=True)
subprocess.run("sudo apt install -y openssh-server", shell=True)

# Ensure SSH is enabled and running
subprocess.run("sudo systemctl enable ssh", shell=True)
subprocess.run("sudo systemctl start ssh", shell=True)

# 3. Install ngrok and set up the tunnel for SSH
# Download ngrok (if not already installed)
if not os.path.exists('ngrok'):
    subprocess.run("wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz", shell=True)
    subprocess.run("unzip ngrok-v3-stable-linux-amd64.tgz", shell=True)

# Authenticate with ngrok
authtoken = "2nt6X8cpunsTkK0kqsmshNYK1s7_i5UTNmYYMf14qdXjVidg"
subprocess.run(f"./ngrok authtoken {authtoken}", shell=True)

# Expose SSH (port 22) via ngrok
subprocess.run("./ngrok tcp 22 &", shell=True)

print("User 'haidanh' created, SSH server running, and ngrok tunnel is set up.")
print("Check the ngrok dashboard or console output for the tunnel URL.")
