import os,sys
from time import sleep
from random import seed,randint
seed()
def __init__(run=False):
    if run:
        if os.name=="nt" and os.path.normcase(os.path.basename(sys.executable))=="pythonw.exe":
            print("========================= RESTART: Starting Winux =========================")
            for i in range(randint(100000,10000000)):
                sleep(0)
            chance=input("} Running program complete, code 24\n> You shouldn't running Winux in 'pythonw.exe'. Are you want to continue?\n> (Y/N)or(True/False)\n< ")
            if chance=="Y" or chance=="y" or chance=="True" or chance=="true":
                print("> The Winux be restart will spend some times... Please wait it.\n> ERROR: Cannot found file 'User32.dll'.\n> ERROR: Cannot kept the p▯▯▯▯▯\n> ▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯▯")
            elif chance=="N" or chance=="n" or chance=="False" or chance=="false":
                sys.exit(1)
    else:
        print("========================= RESTART: Starting Winux =========================")
        for i in range(randint(100000,10000000)):
            sleep(0)
        print("} Running program complete, exit code 0x1000")
        quit(1)
# ctypes.windll.user32.MessageBoxW(None,"message","title",0x1000)
# r"resuorce\shell\image\python.gif"
