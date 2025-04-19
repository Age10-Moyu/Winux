#Copyright
"""
------Source code------
Copyright 2025 GD Studio in China.

------Winux------
Copyright 2025 GD Studio.

------MCLDevTools------
Copyright 2025 Bedrock Technology & Gaming Team.
BTAGT，隶属于 GD Studio。
Bedrock Technology & Gaming Team, affiliated with GD Studio.

------Translation------
Copyright 2025 GD Studio in China.

------Statement------
版权GD Studio所有。在未经许可的情况下严禁外传。
Bedrock Technology & Gaming Team、IS Studio为GD Studio旗下工作室，由GD Studio in China授权使用。
无论何时GD Studio都拥有此软件源代码的所有权。
未经许可的外传、开源、转让、出租、出售、出借行为属于违反版权法之行为，我们有权对您进行诉讼。
Copyright GD Studio. All Rights Reserved. Unauthorized distribution is strictly prohibited.
Bedrock Technology & Gaming Team and IS Studio are studios under GD Studio, authorized for use by GD Studio in China.
GD Studio retains ownership of the source code of this software at all times.
Unauthorized distribution, open sourcing, transfer, rental, sale, or lending constitutes a violation of the Copyright Law of the P.R.China, and we reserve the right to take legal action against you.
"""
#Instruction
"""
本程序被GD Studio定义为测试性程序rd开发阶段，属未完成范畴，建议修改后使用，尽量不要直接运行！
本程序基于 Python 3.14.0a5 编写，语言为简体中文，翻译由 Microsoft Translator (正式) 完成
1~26行为版权声明，28~38行为事项说明，42~508行为代码部分，509~513行为脚注部分
代码中的 time.perf_counter() 模块仅在 Python 3.7 及以后版本可用，如果不可用将会替换成 time.time()，但是精度误差较大
代码里的 InsufficientPermissionsError 可以换成 PermissionsError
----< 为输入指定内容，如密码、要求输入等
----> 为提示系统消息，如启动、更改语言等
----} 为回报命令内容，如命令执行提示等
----] 为一般输入，如命令等
"""
#最后编辑于2025年4月18日，今天是我的生日！
#Last edited on April 18 2025, today is my birthday!
"================= 分界线|Demarcation Line ================="
#SourceCode
import kl
kl
from web import connect as web
from shell import __init__ as shell
from sys import version_info as ver
from time import sleep,perf_counter,time
from random import randint,seed,choice
from os import system
import sys
class gdoa:
    def ide(restart):
        print("} Running program complete, exit code 1")
        raise SyntaxError("invalid syntax")
        sys.exit(1)
def music(file):
    system("mpg123"+file)
shell(True)
if int(f"{ver.major}")>=3 and int(f"{ver.minor}")>=7:
    del ver
    ver=True
else:
    ver=False
if ver:
    start=perf_counter()
else:
    start=time()
sleep(0)
print("========================= RESTART: Starting Winux =========================")
seed()
for i in range(randint(100000,10000000)):
    sleep(0)
i=0
if ver:
    end=perf_counter()
else:
    end=time()
if not bool(system("")):
    print("} Running program complete, code",system(""))
else:
    gdoa.ide("restart")
print("} The startup takes "+str(end--start)+" second.")
del perf_counter,start,end,time
user=r"WU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUwpZT1UgU0hPVUxEIE5PVCBUWVBFIFRISVMKWU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUw=="
password=r"WU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUwpZT1UgU0hPVUxEIE5PVCBUWVBFIFRISVMKWU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUw=="
change=r"WU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUwpZT1UgU0hPVUxEIE5PVCBUWVBFIFRISVMKWU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUw=="
server=False
login=False
admin=False
try:
    user=input("> Login in your account:\n< ")
except KeyboardInterrupt:
    pass
print("> Please wait it...")
sleep(0)
sleep(0)
if user=="age10_moyu" or user=="Age10_moyu" or user=="Age10_Moyu" or user=="age10_Moyu" or user=="System" or user=="system":
    print("> Languace change to 简体中文:")
    sleep(0)
    lang="zh_cn"
    sleep(0)
    root=True
    sleep(0)
    if user=="age10_moyu" or user=="Age10_moyu" or user=="Age10_Moyu" or user=="age10_Moyu":
        user="Age10_Moyu"
    elif user=="System" or user=="system":
        user="System"
    sleep(0)
    try:
        password=input("> 输入密码登录：\n< ")
    except KeyboardInterrupt:
        pass
    if password=="zyz20120418":
        print("> 账户登录：登录到 "+user+"：登录在 PC 上")
    elif password==r"WU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUwpZT1UgU0hPVUxEIE5PVCBUWVBFIFRISVMKWU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUw==":
        print("> 账户登录：登录到 TypeError: password is incorrect：登录在 KeyboardInterrupt 上")
        sys.exit(1)
    else:
        print("> 账户登录：登录到 TypeError: password is incorrect：登录在 SyntaxError: invalid syntax 上")
        sys.exit(1)
else:
    if user=="" or user==" " or "  " in user or user==r"WU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUwpZT1UgU0hPVUxEIE5PVCBUWVBFIFRISVMKWU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUw==":
        user="Default User"
        print("> Log in default account (Default User).")
    lang="en_us"
    sleep(0)
    root=False
    sleep(0)
    try:
        password=input("> Type your password:\n< ")
    except KeyboardInterrupt:
        pass
    if password=="winux-default-password":
        print("> Login: Log in "+user+": Log in PC. Not this user.")
        sleep(0)
        try:
            change=input("> It has been detected that you are in 中华人民共和国, 中国大陆. Would you like to switch to 简体中文?\n> (Y/N)or(True/False)\n< ")
        except KeyboardInterrupt:
            pass
        if change=="Y" or change=="y" or change=="True" or change=="true":
            print("> Languace change to 简体中文:")
            sleep(0)
            lang="zh_cn"
        elif change=="N" or change=="n" or change=="False" or change=="false":
            print("> Languace change to English(US):")
            sleep(0)
            lang="en_us"
        else:
            print("> Languace change to English(US):")
            sleep(0)
            lang="en_us"
        del change
    elif password==r"WU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUwpZT1UgU0hPVUxEIE5PVCBUWVBFIFRISVMKWU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUw==":
        print(r"> Login: Log in TypeError: password is incorrect: Log in KeyboardInterrupt. NameError: name 'D:\kl.py' is not defined.")
        sys.exit(1)
    else:
        print("> Login: Log in TypeError: password is incorrect: Log in SyntaxError: invalid syntax. NameError: name 'is_user_in_pc' is not defined.")
        sys.exit(1)
if lang=="zh_cn":
    print(r"""] sudo netpc is--open /value:no /active:yes from System /command:yes /active:no --system
> 请求的操作需要提升。

> 你要允许此应用对你的设备进行更改吗？
> 如果要继续，请输入管理员密码。
< ▯▯▯▯▯▯▯▯▯▯▯
} 执行了 sudo netpc is--open /value:no /active:yes from System /command:yes /active:no --system：来自 System 账户。
> 命令成功完成：命令成功完成。
] sudo netpc mainpc /value:{input} /active:yes from System /command:yes /active:no --system
> 请求的操作需要提升。

> 你要允许此应用对你的设备进行更改吗？
> 如果要继续，请输入管理员密码。
< ▯▯▯▯▯▯▯▯▯▯▯
} 执行了 sudo netpc mainpc /value:{input} /active:yes from System /command:yes /active:no --system：来自 System 账户。
> 命令成功完成：要求用户输入自定义内容。
> 命令行要求定义value的值。
< 25565
} 执行了 sudo netpc mainpc /value:{input} /active:yes from System /command:yes /active:no --system：来自 System 账户。
> 命令成功完成：命令成功完成。
] sudo netpc password /value:{input} /active:yes from System /command:yes /active:no --system
> 请求的操作需要提升。

> 你要允许此应用对你的设备进行更改吗？
> 如果要继续，请输入管理员密码。
< ▯▯▯▯▯▯▯▯▯▯▯
} 执行了 sudo netpc password /value:{input} /active:yes from System /command:yes /active:no --system：来自 System 账户。
> 命令成功完成：要求用户输入自定义内容。
> 命令行要求定义value的值。
< winux-default-password
} 执行了 sudo netpc password /value:{input} /active:yes from System /command:yes /active:no --system：来自 System 账户。
> 命令成功完成：命令成功完成。""")
else:
    print(r"""] sudo netpc is--open /value:no /active:yes from System /command:yes /active:no --system
> The requested operation requires elevation.

> Do you want to allow the following program to make changes to this computer?
> If you want to continue, please enter your Administrator password.
< ▯▯▯▯▯▯▯▯▯▯▯
} Running command sudo netpc is--open /value:no /active:yes from System /command:yes /active:no --system: From System.
> Command running complete: Command running complete.
] sudo pc mainpc /value:{input} /active:yes from System /command:yes /active:no --system
> The requested operation requires elevation.

> Do you want to allow the following program to make changes to this computer?
> If you want to continue, please enter your Administrator password.
< ▯▯▯▯▯▯▯▯▯▯▯
} Running command sudo pc mainpc /value:{input} /active:yes from System /command:yes /active:no --system: From System.
> Command running complete: Ask the user to enter custom content.
> The command line requires the definition of the "value".
< 25565
} Running command sudo pc mainpc /value:{input} /active:yes from System /command:yes /active:no --system: From System.
> Command running complete: Command running complete.
] sudo netpc maxpc /value:{input} /active:yes from System /command:yes /active:no --system
> The requested operation requires elevation.

> Do you want to allow the following program to make changes to this computer?
> If you want to continue, please enter your Administrator password.
< ▯▯▯▯▯▯▯▯▯▯▯
} Running command sudo netpc maxpc /value:{input} /active:yes from System /command:yes /active:no --system: From System.
> Command running complete: Ask the user to enter custom content.
> The command line requires the definition of the "value".
< winux-default-password
} Running command sudo netpc maxpc /value:{input} /active:yes from System /command:yes /active:no --system: From System.
> Command running complete: Command running complete.""")
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
while True:
    try:
        command=input("] ")
    except KeyboardInterrupt:
        if lang=="zh_cn":
            print("\n} 没有执行命令：无效键位：来自 "+user+" 账户。\n> 命令成功完成：不支持的键位。")
        else:
            print("\n} No running command: is invalid keys.: From "+user+".\n> Command running complete: Unsupported keys.")
        continue
    if command=="" or command==" " or "  " in command:
        if lang=="zh_cn":
            print("} 没有执行命令：输入的字符串没有值：来自 "+user+" 账户。\n> 命令成功完成：不支持空命令。")
        else:
            print("} No running command: type in str no value.: From "+user+".\n> Command running complete: No allow empty commands.")
    elif 'pc install /value{"' in command and '"}' in command and r"/command:yes" in command:
        if "ubuntu" in command:
            if lang=="zh_cn":
                uac=input("> 请求的操作需要提升。\n\n> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
            else:
                uac==input("> The requested operation requires elevation.\n\n> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
            if uac=="zyz20120418":
                if lang=="zh_cn":
                    print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> 开始安装：Ubuntu")
                else:
                    print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.\n> Starting to install: Ubuntu")
                seed()
                print("> [Mirror] Check the mirrors:\n> [Main] https://github.com/:",end="")
                print("done\n> [Mirror] https://www.github-zh.com/:",end="")
                print("bad\n> All mirrors are in there.\n> Start to install Ubuntu:")
                for i in range(randint(25,3000)):
                    print("> Get "+str(i+1)+r": [Mirror] "+choice(git.ubuntu)+": done"+"\n> Ign "+str(i+1)+r": [Mirror] "+choice(git.ubuntu)+": done")
                if lang=="zh_cn":
                    print("> Ubuntu 已经成功地安装到了您的计算机上。")
                else:
                    print("> Ubuntu is install in your PC successfully.")
        elif "arch" in command:
            # Uncomplete
            pass
    elif r"host server /value:{192.168.100.6:25565}" in command and r"/command:yes" in command:
        if lang=="zh_cn":
            print("> 正在访问服务器……")
        else:
            print("> Connecting the server...")
        connect=web(True)
        if connect:
            server=True
            if lang=="zh_cn":
                print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
            else:
                print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
        else:
            music(r"resource\__init__\music\tip.wav")
            if lang=="zh_cn":
                print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。")
            else:
                print("} Running command "+command+": From "+user+".\n> Command running complete: The connection attempt failed due to the connecting party not responding correctly after a period of time or the connected host not reacting.")
    elif r'host user /value:{"login-code-1429491716-zyz20120418":"zyz20120418"}' in command and "/command:yes" in command:
        if server:
            if lang=="zh_cn":
                print("> 正在验证第三方服务器……")
            else:
                print("> Validating 3rd-party server...")
            connect=web(True)
            if connect:
                login=True
                if lang=="zh_cn":
                    print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
                else:
                    print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
            else:
                music(r"resource\__init__\music\tip.wav")
                if lang=="zh_cn":
                    print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。")
                else:
                    print("} Running command "+command+": From "+user+".\n> Command running complete: The connection attempt failed due to the connecting party not responding correctly after a period of time or the connected host not reacting.")
        else:
            if lang=="zh_cn":
                print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：找不到服务器。")
            else:
                print("} Running command "+command+": From "+user+".\n> Command running complete: Cannot found the server.")
    elif r'host earn /value:{"' in command and r'"}' in command and r"/command:yes" in command:
        if lang=="zh_cn":
            print("> 正在验证第三方服务器……")
        else:
            print("> Validating 3rd-party server...")
        connect=web(True)
        if web:
            if server and login:
                if r"WU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUwpZT1UgU0hPVUxEIE5PVCBUWVBFIFRISVMKWU9VIFNIT1VMRCBOT1QgVFlQRSBUSElTCllPVSBTSE9VTEQgTk9UIFRZUEUgVEhJUw==" in command:
                    if lang=="zh_cn":
                        print("} 执行了 <ERROR:SyntaxError|invalid type>：来自 Linux 账户。\n> 命令成功完成：命令成功完成。\n> 完啦，系统要崩！")
                    else:
                        print("} Running command <ERROR:SyntaxError|invalid type>: From Linux.\n> Command running complete: Command running complete.\n> God, who crashed my pc?")
                elif r"Rk9VUlRZIFRXTwpGT1VSVFkgVFdPCkZPVVJUWSBUV08KRk9VUlRZIFRXTwpGT1VSVFkgVFdP" in command:
                    if lang=="zh_cn":
                        print("} 执行了 FOURTY TWO：来自 Universe 账户。\n> 命令成功完成：命令成功完成。\n> 宇宙的终极奥义！")
                    else:
                        print("} Running command FOURTY TWO: From Universe.\n> Command running complete: Command running complete.\n> The ultimate secret of the universe!")
                elif r"QWRtaW5pc3RyYXRvciBieSBBZ2UxMF9Nb3l1CkFjY291bnQgaXMgIjE0Mjk0OTE3MTYiClBhc3N3b3JkIGlzICJ6eXoyMDEyMDQxOCIKQVBJLUtleSBpcyAibG9naW4tY29kZS0xNDI5NDkxNzE2LXp5ejIwMTIwNDE4IgpTZXJ2ZXIgaXMgIlt7InNlcnZlciI6ImJhaWR1LmNvbSJ9LHsidGVzdCI6dHJ1ZX1dIgotLS0tLSBUaGlzIGlzIHRoZSBlbmQgbGluZSAtLS0tLQ==" in command:
                    admin=True #[1]
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。\n> 启用了管理员模式。")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.\n> Administration is enable.")
                else:
                    music(r"resource\__init__\music\tip.wav")
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：错误的兑换码。")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Incorrect earn code.")
            elif server:
                if lang=="zh_cn":
                    print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：错误的用户信息。")
                else:
                    print("} Running command "+command+": From "+user+".\n> Command running complete: Incorrect account information.")
            else:
                if lang=="zh_cn":
                    print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：找不到服务器。")
                else:
                    print("} Running command "+command+": From "+user+".\n> Command running complete: Cannot found the server.")
        else:
            music(r"resource\__init__\music\tip.wav")
            if lang=="zh_cn":
                print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。")
            else:
                print("} Running command "+command+": From "+user+".\n> Command running complete: The connection attempt failed due to the connecting party not responding correctly after a period of time or the connected host not reacting.")
    elif "sudo" in command and r" /active:yes " not in command:
        if lang=="zh_cn":
            print("} 执行了 "+command+r"：不能在没有/active₁时执行sudo：来自 "+user+" 账户。"+"\n> 命令成功完成：语法错误。")
        else:
            print("} Running "+command+r": Cannot execute sudo without /active₁: From "+user+"."+"\n> Command running complete: SyntaxError.")
    elif ("--rootin" in command or "--system" in command) and ("sudo" not in command):
        if lang=="zh_cn":
            input("> 请求的操作需要提升。\n")
            sleep(0)
            print(r"} 执行了 "+command+"：不能在没有sudo时执行超级用户后缀（--rootin、--system）：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
        else:
            input("> The requested operation requires elevation.\n")
            sleep(0)
            print(r"} Running command "+command+": Cannot execute superuser suffixes (--rootin, --system) without sudo: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")

    elif r"pc power /value:no" in command and r"/command:yes" in command:
        if lang=="zh_cn":
            print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
            sleep(0)
            print("> 来自 "+user+" 的命令：关机")
            sleep(2)
            print("> 卸载运行环境……")
            sleep(1)
            print("> 卸载运行时模块……")
            sleep(2)
            print("> 卸载可视化程序……")
            sleep(3)
            print("> 卸载语言……")
            sleep(0)
            print("> Uninstall languace...")
            sleep(1)
            print("> Uninstall user module...")
            sleep(2)
            print("> Uninstall user...")
            sleep(2)
            print("> Uninstall all program...")
            sleep(2)
            print("> Uninstall Winux...")
            sleep(3)
            print("> Power off.")
            sleep(2)
            print()
            break
            quit()
        else:
            print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
            sleep(0)
            print("> Command from "+user+": Shutdown")
            sleep(2)
            print("> Uninstall running environment...")
            sleep(1)
            print("> Uninstall runtime module...")
            sleep(2)
            print("> Uninstall visualizers...")
            sleep(3)
            print("> Uninstall languace...")
            sleep(1)
            print("> Uninstall user module...")
            sleep(2)
            print("> Uninstall user...")
            sleep(2)
            print("> Uninstall all program...")
            sleep(2)
            print("> Uninstall Winux...")
            sleep(3)
            print("> Power off.")
            sleep(2)
            print()
            break
            quit()
    elif "sudo" in command and r" /active:yes " not in command:
        if lang=="zh_cn":
            print("} 执行了 "+command+r"：不能在没有/active₁时执行sudo：来自 "+user+" 账户。"+"\n> 命令成功完成：语法错误。")
        else:
            print("} Running "+command+r": Cannot execute sudo without /active₁: From "+user+"."+"\n> Command running complete: SyntaxError.")
    elif ("--rootin" in command or "--system" in command) and ("sudo" not in command):
        if lang=="zh_cn":
            input("> 请求的操作需要提升。\n")
            sleep(0)
            print(r"} 执行了 "+command+"：不能在没有sudo时执行超级用户后缀（--rootin、--system）：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
        else:
            input("> The requested operation requires elevation.\n")
            sleep(0)
            print(r"} Running command "+command+": Cannot execute superuser suffixes (--rootin, --system) without sudo: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
    elif "--system" in command or "--rootin" in command:
        if lang=="zh_cn":
            input("> 请求的操作需要提升。\n")
            sleep(0)
            uac=input("> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
            if uac=="zyz20120418":
                if r"/value:{input}" in command:
                    if lang=="zh_cn":
                        value=input("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：要求用户输入自定义内容。\n> 命令行要求定义value的值。\n< ")
                        if value=="" or value==" " or "  " in value:
                            print("} 没有执行命令：输入的字符串没有值：来自 "+user+" 账户。\n> 命令成功完成：不支持空命令。")
                        else:
                            print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
                    else:
                        value=input('} Running command "+command+": From "+user+".\n> Command running complete: Ask the user to enter custom content.\n> The command line requires the definition of the "value".\n< ')
                        if value=="" or value==" " or "  " in value:
                            print("} No running command: type in str no value.: From "+user+".\n> Command running complete: No allow empty commands.")
                        else:
                            print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
                else:
                    print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
            else:
                    print("} 执行了 "+command+"：密码不正确：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
        else:
            input("> The requested operation requires elevation.\n")
            sleep(0)
            uac=input("> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
            if uac=="zyz20120418":
                print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
            else:
                print("} Running command "+command+": Password is incorrect: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
        del uac
    elif r"/value:{input}" in command:
        if lang=="zh_cn":
            value=input("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：要求用户输入自定义内容。\n> 命令行要求定义value的值。\n< ")
            if value=="" or value==" " or "  " in value:
                print("} 没有执行命令：输入的字符串没有值：来自 "+user+" 账户。\n> 命令成功完成：不支持空命令。")
            else:
                print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
        else:
            value=input('} Running command "+command+": From "+user+".\n> Command running complete: Ask the user to enter custom content.\n> The command line requires the definition of the "value".\n< ')
            if value=="" or value==" " or "  " in value:
                print("} No running command: type in str no value.: From "+user+".\n> Command running complete: No allow empty commands.")
            else:
                print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
    elif r" /localgroup:system " in command:
        if " --system" not in command:
            if lang=="zh_cn":
                print("} 执行了 "+command+"：权限不足：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
            else:
                print("} Running command "+command+": InsufficientPermissionsError: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
        else:
            if lang=="zh_cn":
                input("> 请求的操作需要提升。\n")
                sleep(0)
                uac=input("> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
                if uac=="zyz20120418":
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
                else:
                    print("} 执行了 "+command+"：密码不正确：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
            else:
                input("> The requested operation requires elevation.\n")
                sleep(0)
                uac=input("> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
                if uac=="zyz20120418":
                    print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
                else:
                    print("} Running command "+command+": Password is incorrect: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
            del uac
    elif r" /localgroup:root " in command:
        if " --rootin" not in command:
            if lang=="zh_cn":
                print("} 执行了 "+command+"：权限不足：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
            else:
                print("} Running command "+command+": InsufficientPermissionsError: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
        else:
            if lang=="zh_cn":
                input("> 请求的操作需要提升。\n")
                sleep(0)
                uac=input("> 你要允许此应用对你的设备进行更改吗？\n> 如果要继续，请输入管理员密码。\n< ")
                if uac=="zyz20120418":
                    if lang=="zh_cn":
                        print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
                    else:
                        print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
                else:
                    print("} 执行了 "+command+"：密码不正确：来自 "+user+" 账户。"+"\n> 命令成功完成：权限不足。")
            else:
                input("> The requested operation requires elevation.\n")
                sleep(0)
                uac=input("> Do you want to allow the following program to make changes to this computer?\n> If you want to continue, please enter your Administrator password.\n< ")
                if uac=="zyz20120418":
                    print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")
                else:
                    print("} Running command "+command+": Password is incorrect: From "+user+"."+"\n> Command running complete: InsufficientPermissionsError.")
            del uac
    else:
        if lang=="zh_cn":
            print("} 执行了 "+command+"：来自 "+user+" 账户。\n> 命令成功完成：命令成功完成。")
        else:
            print("} Running command "+command+": From "+user+".\n> Command running complete: Command running complete.")

#Footips
"""
[1]：其实我也没想好这个管理员权限可以干什么……先做了再说 =w=
"""
