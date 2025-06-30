import os,sys
from shared import lang_import
from shared import command_import
from shared import user_import
import shared
from time import sleep
from random import randint,choice,seed
from special import git

lang=lang_import()
user=user_import()
command=command_import()

class git:
    ubuntu=["https://github.com/Age10-Moyu/Winux/libs/install/Linux/Ubuntu",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/Ubuntu",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/resource",
        "https://github.com/Age10-Moyu/libs/install/Linux/Ubuntu",
        "https://github.com/Age10-Moyu/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/resource/install/Linux/Ubuntu",
        "https://github.com/Age10-Moyu/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/resource/install/Linux/resource",]
    arch=["https://github.com/Age10-Moyu/Winux/libs/install/Linux/Arch",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/Arch",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/resource",
        "https://github.com/Age10-Moyu/libs/install/Linux/Arch",
        "https://github.com/Age10-Moyu/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/resource/install/Linux/Arch",
        "https://github.com/Age10-Moyu/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/resource/install/Linux/resource",]
    dm=["https://github.com/Age10-Moyu/Winux/libs/install/Linux/regular/dynamic/standard",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/regular/dynamic/standard",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/resource",
        "https://github.com/Age10-Moyu/libs/install/Linux/regular/dynamic/standard",
        "https://github.com/Age10-Moyu/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/resource/install/Linux/regular/dynamic/standard",
        "https://github.com/Age10-Moyu/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/resource/install/Linux/resource",]
    lightdm=["https://github.com/Age10-Moyu/Winux/libs/install/Linux/regular/dynamic/light",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/regular/dynamic/light",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/resource",
        "https://github.com/Age10-Moyu/libs/install/Linux/regular/dynamic/light",
        "https://github.com/Age10-Moyu/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/resource/install/Linux/regular/dynamic/light",
        "https://github.com/Age10-Moyu/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/resource/install/Linux/resource",]
    notepad=["https://github.com/Age10-Moyu/Winux/libs/install/Linux/regular/application/notepad",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/regular/application/notepad",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/Winux/resource/install/Linux/resource",
        "https://github.com/Age10-Moyu/libs/install/Linux/regular/application/notepad",
        "https://github.com/Age10-Moyu/libs/install/Linux/libs",
        "https://github.com/Age10-Moyu/libs/install/Linux/resource",
        "https://github.com/Age10-Moyu/resource/install/Linux/regular/application/notepad",
        "https://github.com/Age10-Moyu/resource/install/Linux/libs",
        "https://github.com/Age10-Moyu/resource/install/Linux/resource",]
    
support=["ubuntu","arch","dm","lightdm","notepad"]


def install(package=None,use_uac=True):
    if os.name=="nt" and os.path.normcase(os.path.basename(sys.executable))=="pythonw.exe":
        if lang=="zh_cn":
            print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
        else:
            print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
        print("> ERROR: Cannot install any packages in pythonw.exe.\n> Try to running in python.exe?")
    else:
        if "--rootin" in command or "--system" in command or not use_uac:
            if package=="ubuntu":
                if lang=="zh_cn":
                    input("> 请求的操作需要提升。\n")
                    uac=input("> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
                else:
                    input("> The requested operation requires elevation.\n")
                    uac=input("> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
                if uac=="zyz20120418":
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> 开始安装：Ubuntu")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.\n> Starting to install: Ubuntu")
                    seed()
                    print("> [Mirror] Check the mirrors:")
                    sleep(randint(5,20))
                    print("> [Main] https://github.com... done")
                    sleep(randint(5,20))
                    print("> [Mirror] https://www.github-zh.com... bad")
                    print("> All mirrors are in there.\n> Start to install Ubuntu:")
                    sleep(1)
                    for i in range(randint(25,3000)):
                        print("> Get "+str(i+1)+r": [Mirror] "+choice(git.ubuntu)+": done"+"\n> Ign "+str(i+1)+r": [Mirror] "+choice(git.ubuntu)+": done\n> Pst "+str(i+1)+r": [Mirror] "+choice(git.ubuntu)+": done")
                        sleep(0)
                    linux=True
                    if lang=="zh_cn":
                        print("> Ubuntu 已经成功地安装到了您的计算机上。")
                    else:
                        print("> Ubuntu is install in your PC successfully.")
            elif package=="arch":
                if lang=="zh_cn":
                    input("")
                    uac=input("> 请求的操作需要提升。\n")
                    uac=input("> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
                else:
                    input("> The requested operation requires elevation.\n")
                    uac=input("> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
                if uac=="zyz20120418":
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> 开始安装：Arch Linux")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.\n> Starting to install: Arch Linux")
                    seed()
                    print("> [Mirror] Check the mirrors:")
                    sleep(randint(5,20))
                    print("> [Main] https://github.com... done")
                    sleep(randint(5,20))
                    print("> [Mirror] https://www.github-zh.com... bad")
                    print("bad\n> All mirrors are in there.\n> Start to install Arch Linux:")
                    sleep(1)
                    for i in range(randint(25,3000)):
                        print("> Get "+str(i+1)+r": [Mirror] "+choice(git.arch)+": done"+"\n> Ign "+str(i+1)+r": [Mirror] "+choice(git.arch)+": done\n> Pst "+str(i+1)+r": [Mirror] "+choice(git.arch)+": done")
                        sleep(0)
                    linux=True
                    if lang=="zh_cn":
                        print("> Arch Linux 已经成功地安装到了您的计算机上。")
                    else:
                        print("> Arch Linux is install in your PC successfully.")
                else:
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：密码不正确：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
                    else:
                        print("} Running command "+command+": Password is incorrect: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
            elif package=="dynamic" or package=="dm":
                if lang=="zh_cn":
                    input("")
                    uac=input("> 请求的操作需要提升。\n")
                    uac=input("> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
                else:
                    input("> The requested operation requires elevation.\n")
                    uac=input("> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
                if uac=="zyz20120418":
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> 开始安装：标准渲染器")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.\n> Starting to install: Standard dynamic")
                    seed()
                    print("> [Mirror] Check the mirrors:")
                    sleep(randint(5,20))
                    print("> [Main] https://github.com... done")
                    sleep(randint(5,20))
                    print("> [Mirror] https://www.github-zh.com... bad")
                    print("bad\n> All mirrors are in there.\n> Start to install dynamic:")
                    sleep(1)
                    for i in range(randint(25,3000)):
                        print("> Get "+str(i+1)+r": [Mirror] "+choice(git.dm)+": done"+"\n> Ign "+str(i+1)+r": [Mirror] "+choice(git.dm)+": done\n> Pst "+str(i+1)+r": [Mirror] "+choice(git.dm)+": done")
                        sleep(0)
                    shared.dynamic_in=True
                    shared.dm_in=True
                    if lang=="zh_cn":
                        print("> 标准渲染器 已经成功地安装到了您的计算机上。")
                    else:
                        print("> Standard dynamic is install in your PC successfully.")
                else:
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：密码不正确：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
                    else:
                        print("} Running command "+command+": Password is incorrect: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
            elif package=="lightdm":
                if lang=="zh_cn":
                    input("")
                    uac=input("> 请求的操作需要提升。\n")
                    uac=input("> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
                else:
                    input("> The requested operation requires elevation.\n")
                    uac=input("> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
                if uac=="zyz20120418":
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> 开始安装：Light渲染器")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.\n> Starting to install: Lightdm")
                    seed()
                    print("> [Mirror] Check the mirrors:")
                    sleep(randint(5,20))
                    print("> [Main] https://github.com... done")
                    sleep(randint(5,20))
                    print("> [Mirror] https://www.github-zh.com... bad")
                    print("bad\n> All mirrors are in there.\n> Start to install lightdm:")
                    sleep(1)
                    for i in range(randint(25,3000)):
                        print("> Get "+str(i+1)+r": [Mirror] "+choice(git.dm)+": done"+"\n> Ign "+str(i+1)+r": [Mirror] "+choice(git.dm)+": done\n> Pst "+str(i+1)+r": [Mirror] "+choice(git.dm)+": done")
                        sleep(0)
                    shared.dynamic_in=True
                    shared.dm_in=True
                    if lang=="zh_cn":
                        print("> Light渲染器 已经成功地安装到了您的计算机上。")
                    else:
                        print("> Lightdm is install in your PC successfully.")
                else:
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：密码不正确：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
                    else:
                        print("} Running command "+command+": Password is incorrect: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
            elif package=="notepad":
                if lang=="zh_cn":
                    input("")
                    uac=input("> 请求的操作需要提升。\n")
                    uac=input("> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
                else:
                    input("> The requested operation requires elevation.\n")
                    uac=input("> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
                if uac=="zyz20120418":
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> 开始安装：记事本")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.\n> Starting to install: Notepad")
                    seed()
                    print("> [Mirror] Check the mirrors:")
                    sleep(randint(5,20))
                    print("> [Main] https://github.com... done")
                    sleep(randint(5,20))
                    print("> [Mirror] https://www.github-zh.com... bad")
                    print("bad\n> All mirrors are in there.\n> Start to install notepad:")
                    sleep(1)
                    for i in range(randint(25,3000)):
                        print("> Get "+str(i+1)+r": [Mirror] "+choice(git.notepad)+": done"+"\n> Ign "+str(i+1)+r": [Mirror] "+choice(git.notepad)+": done\n> Pst "+str(i+1)+r": [Mirror] "+choice(git.notepad)+": done")
                        sleep(0)
                    shared.notepad_in=True
                    if lang=="zh_cn":
                        print("> 记事本 已经成功地安装到了您的计算机上。")
                    else:
                        print("> Notepad is install in your PC successfully.")
                else:
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：密码不正确：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
                    else:
                        print("} Running command "+command+": Password is incorrect: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
            elif package==git.empty("install"):
                if lang=="zh_cn":
                    print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> ERROR: need compact 'value' but there have not.")
                else:
                    print("} Running command "+command+": From "+user+".\n> Command running complete: command running complete.\n> ERROR: need compact 'value' but there have not.")
            else:
                if lang=="zh_cn":
                    print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> Cannot find the selected Standard Package.")
                else:
                    print("} Running command "+command+": From "+user+".\n> Command running complete: command running complete.\n> Cannot find the selected Standard Package.")
        else:
            if lang=="zh_cn":
                print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：权限不足。")
            else:
                print("} Running command "+command+": From "+user+".\n> Command running complete: InsufficientPermissionsError.")
            print("> ERROR: Cannot running install command, Are you root?")

if __name__=="__main__":
    if len(sys.argv)>=3 and sys.argv[1]=="-m" and sys.argv[2]=="install":
        package_name=sys.argv[3] if len(sys.argv) > 3 else None
        if package_name in support:
            print("} Using external output.\n> This program or script has no output symbol configured, will replace by default profile.\n")
            install(package_name,False)
        else:
            print("} Using external output.\n> This program or script has no output symbol configured, will replace by default profile.\n")
            print(f"> ERROR: '{package_name}' is not a valid package name.")
            print(f"> Available packages: {', '.join(support)}")
    else:
        print("} Using external output.\n> This program or script has no output symbol configured, will replace by default profile.\n")
        print("> Usage: python git.py -m install [package_name]")
        print(f"> Available packages: {', '.join(support)}")