import shared,sys

lang=shared.lang_import()
user=shared.user_import()
command=shared.command_import()

class about:
    __init__ = "The main program, Winux's root"
    __main__ = "Winux runner, running this program to start Winux"
    kl = "Keyboard locker, protect the main process"
    web = "Internet pinger"
    shell = "Running program tester, can block you if you running Winux by pythonw.exe"
    git = "Can help you install some packages"
    special = "Other things of the scripts"
    shared = "Shared functions and utilities for the program"
    restart = "Just a simple script to restart Winux"

@staticmethod
def help(func=None,type="get"):
    if type=="get":
        if func=="__init__":
            return "[<class:__init__.{self}>,<group:root>]\nHelp lib: program __init__\nMethods:\n    Externality: not support\n    Interior: use by shared.py -> *\nAttribute:\n    Class: __init__.{self}\n    Group: root"
        elif func=="__main__":
            return "[<class:__main__.{self}>,<group:main>]\nHelp lib: program __main__\nMethods:\n    Externality: not support\n    Interior: not support\nAttribute:\n    Class: __main__.{self}\n    Group: main"
        elif func=="kl":
            return "[<class:kl.kl>,<group:script>]\nHelp lib: script kl\nMethods:\n    Externality: not support\n    Interior: use by\n        import kl\n        kl.kl(muiti=True)\nAttribute:\n    Class: kl.kl\n    Group: script\n    Message: plan to deprecate"
        elif func=="web":
            return "[<class:web.connect>,<group:program>]\nHelp lib: program web\nMethods:\n    Externality: not support\n    Interior: use by\n        import web\n        web.connect(show=False)\nAttribute:\n    Class: web.{self}\n    Group: program"
        elif func=="shell":
            return "[<class:shell.__init__>,<group:program>]\nHelp lib: program shell\nMethods:\n    Externality: not support\n    Interior: use by\n        import shell\n        shell.__init__(run=True)\nAttribute:\n    Class: shell.{self}\n    Group: program"
        elif func=="git":
            return "[<class:git.install>,<group:program>]\nHelp lib: program git\nMethods:\n    Externality: use by\n        /git.py -m install [...]\n    Interior: use by\n        import git\n        git.install(\"...\")\nAttribute:\n    Class: git.{self}\n    Group: program"
        elif func=="special":
            return "[<class:special.{self}>,<group:script>]\nHelp lib: script special\nMethods:\n    Externality: use by\n        /special.py -m help [...]\n    Interior: use by\n        import special\n        special.[...]()\nAttribute:\n    Class: special.{self}\n    Group: script"
        elif func=="shared":
            return "[<class:shared.{self}>,<group:script>]\nHelp lib: script shared\nMethods:\n    Externality: not support\n    Interior: use by\n        import shared\n        shared.[...]()\nAttribute:\n    Class: shared.{self}\n    Group: script"
        elif func=="restart":
            return "[<class:restart.{self}>,<group:script>]\nHelp lib: script restart\nMethods:\n    Externality: not support\n    Interior: use by\n        import restart\nAttribute:\n    Class: restart.{self}\n    Group: script"
        else:
            raise TypeError(f"[<error:'not found [func] {func}'>]\nHelp lib: something was error\nUse by\n    import special\n    special.help(func=\"[\n        __init__ / __main__ / kl / web / shell / git / special / shared / restart\n    ]\",type=\"[\n        get / print\n    ]\")")
    elif type=="print":
        if lang=="zh_cn":
            print("} 正在使用外联输出。\n> 此程序或脚本没有配置输出符，将替换为空。\n")
        else:
            print("} Using external output.\n> This program or script has no output symbol configured, will replace with None.\n")
        if func=="__init__":
            print("[<class:__init__.{self}>,<group:root>]\nHelp lib: program __init__\nMethods:\n    Externality: not support\n    Interior: use by shared.py -> *\nAttribute:\n    Class: __init__.{self}\n    Group: root")
        elif func=="__main__":
            print("[<class:__main__.{self}>,<group:main>]\nHelp lib: program __main__\nMethods:\n    Externality: not support\n    Interior: not support\nAttribute:\n    Class: __main__.{self}\n    Group: main")
        elif func=="kl":
            print("[<class:kl.kl>,<group:script>]\nHelp lib: script kl\nMethods:\n    Externality: not support\n    Interior: use by\n        import kl\n        kl.kl(muiti=True)\nAttribute:\n    Class: kl.kl\n    Group: script\n    Message: plan to deprecate")
        elif func=="web":
            print("[<class:web.connect>,<group:program>]\nHelp lib: program web\nMethods:\n    Externality: not support\n    Interior: use by\n        import web\n        web.connect(show=False)\nAttribute:\n    Class: web.{self}\n    Group: program")
        elif func=="shell":
            print("[<class:shell.__init__>,<group:program>]\nHelp lib: program shell\nMethods:\n    Externality: not support\n    Interior: use by\n        import shell\n        shell.__init__(run=True)\nAttribute:\n    Class: shell.{self}\n    Group: program")
        elif func=="git":
            print("[<class:git.install>,<group:program>]\nHelp lib: program git\nMethods:\n    Externality: use by\n        /git.py -m install [...]\n    Interior: use by\n        import git\n        git.install(\"...\")\nAttribute:\n    Class: git.{self}\n    Group: program")
        elif func=="special":
            print("[<class:special.{self}>,<group:script>]\nHelp lib: script special\nMethods:\n    Externality: use by\n        /special.py -m help [...]\n    Interior: use by\n        import special\n        special.[...]()\nAttribute:\n    Class: special.{self}\n    Group: script")
        elif func=="shared":
            print("[<class:shared.{self}>,<group:script>]\nHelp lib: script shared\nMethods:\n    Externality: not support\n    Interior: use by\n        import shared\n        shared.[...]()\nAttribute:\n    Class: shared.{self}\n    Group: script")
        elif func=="restart":
            print("[<class:restart.{self}>,<group:script>]\nHelp lib: script restart\nMethods:\n    Externality: not support\n    Interior: use by\n        import restart\nAttribute:\n    Class: restart.{self}\n    Group: script")
        else:
            raise TypeError(f"[<error:'not found [func] {func}'>]\nHelp lib: something was error\nUse by\n    import special\n    special.help(func=\"[\n        __init__ / __main__ / kl / web / shell / git / special / shared / restart\n    ]\",type=\"[\n        get / print\n    ]\")")
    else:
        raise TypeError(f"[<class:{func}."+"{self}'>,<error:'not found [type] {"+type+"}'>]\nHelp lib: something was error\nUse by\n    import special\n    special.help(func=\""+str(func)+"\",type=\"[\n        get / print\n    ]\")")

class git:
    @staticmethod
    def empty(func=None):
        if func=="install":
            return "[<class:special.git>,<function:install>,<message:'poor for compacts'>]"
        elif not bool(func):
            return "[<class:special.git>,<error:'not rich function'>]"
        else:
            return f"[<class:special.git>,<function:{func}>,<error:'not found this function'>]"

if __name__=="__main__":
    if len(sys.argv)>=3 and sys.argv[1]=="-m" and sys.argv[2]=="help":
        func_name=sys.argv[3] if len(sys.argv)>3 else None
        try:
            help(func=func_name, type="print")
        except TypeError as e:
            print(str(e))
    else:
        print("} Using external output.\n> This program or script has no output symbol configured, will replace by default profile.\n")
        print("> Usage: python special.py -m help [function_name]")
        print("> Available function names: __init__, __main__, kl, web, shell, git, special, shared, restart")