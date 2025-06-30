import subprocess

def connect(show=True):
        ret = subprocess.run("ping 110.242.68.66 -n 1", shell=show, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True if ret.returncode == 200 else False
