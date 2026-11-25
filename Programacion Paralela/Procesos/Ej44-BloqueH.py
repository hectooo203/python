import subprocess
import time

procesoContinuo = subprocess.Popen(["ping", "-t" ,"8.8.8.8"])

procesoContinuo.terminate()

try:
    procesoContinuo.wait(timeout=3)
except subprocess.TimeoutExpired:
    procesoContinuo.kill()