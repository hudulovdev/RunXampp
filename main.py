import subprocess

def start_xampp():
    subprocess.run("sudo /opt/lampp/lampp startapache", shell=True)

def stop_xampp():
    subprocess.run("sudo /opt/lampp/lampp stopapache", shell=True)

# Start XAMPP
start_xampp()

# Stop XAMPP
stop_xampp()
