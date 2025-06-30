import platform

def get(type):
    if type not in ["type","name","version","ver"]:
        raise TypeError(f"invalid type '{type}'")
    else:
        if type in ["type","name"]:
            return platform.system()
        elif type in ["version","ver"]:
            if type=="ver":
                if platform.system().lower()=="windows":
                    import winreg
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion") as key:
                        return str(winreg.QueryValueEx(key, "ProductName")[0].title())
                elif platform.system().lower()=="linux":
                    with open('/etc/os-release') as f:
                        return next(line.split('=')[1].strip('"\n') 
                            for line in f 
                            if line.startswith('PRETTY_NAME='))
                elif platform.system().lower()=="darwin":
                    return "Macos "+platform.mac_ver()[0]
                else:
                    return platform.platform()
            else:
                return platform.platform()