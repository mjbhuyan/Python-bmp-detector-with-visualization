import subprocess
from time import sleep

y=(0.1)
subprocess.Popen(["python", 'visualization.py'])
sleep(y)
subprocess.Popen(["python", 'beatDetector.py'])
