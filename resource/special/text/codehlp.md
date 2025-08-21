<h2 id="head"></h2>  

## 前言  
如果您可以了解 Winux 的源代码，并且在 GD-OCL 的许可下进行修改，那么以下是我们的一些帮助。  
如果您的更改想提交到 GD Studio，这些帮助文档的指示将成为我们进行审核的一项重要指标。  

---
<h3 id="content"></h3>  

### 目录  <!--他X的目录好难搓啊啊啊啊啊 世界上不是有种东西叫做 https://markdown.cn/docs/tutorial-extras/hacks#%E7%9B%AE%E5%BD%95 吗-->

- <a href="#head" target="_self">前言</a>  
    - <a href="#php8" target="_self">1. PHP-8 标准</a>  
    - <a href="#footip" target="_self">2. 脚注</a>  
    - <a href="#syntax" target="_self">3. 语法</a>  
    - <a href="#code" target="_self">4. 代码</a>  
- <a href="#end" target="_self">后记</a>  

---
<h3 id="php8"></h3>  

### <sup><a href="#content" target="_self">¶</a></sup> 1. PHP-8 标准  
由 Python 相关社区发布的 PHP-8 标准是各大程序员编写 Python 程序的准则。为了使代码兼具可 I/O 性与社区性，您的修改可以遵循 PHP-8 标准。但如果您需要将您的代码递交到 GD Studio，那么我们不建议您遵循 PHP-8 的部分标准。例如：  
- 运算符号、关键词之间可选的空格、空行  
例如：  
- 数学运算 / 逻辑符号之间的可选空格<sub>（例如`a == 1`应该替换为`a==1`）</sub>；
- 关键字词之间的空白部分<sub>（例如`import ...`之后无需加入多余的空行）</sub>；
- 等等。  

---
<h3 id="footip"></h3>  

### <sup><a href="#content" target="_self">¶</a></sup> 2. 脚注  
脚注，在大部分帮助文档和维基中起到了不可或缺的作用。我们在`__init__.py`也引入了脚注规则。  
要使用脚注，您应该在代码中加入单独的一行“`# Footips`”，并且在后一行加入“`""""""`”，框架类似于  
``` Python
# Footips
"""
[1]: Something should be here...
[x]: Write something here...
"""
```  
这样。  
若要调用脚注，只需在行后添加“` #[x]`”即可。  
如果要得到脚注的完整支持，您应该在代码开头导入`.footips`，并且在需要启用脚注的文件前加入“`footips.global.enable(True)`”，框架类似于  

<details>  

``` Python
import ...
from ... import ...
import .footips
footips.global.enable(True)
...

@footips.function.enable(True)
def function(...): #[1]
    ...

...
function(...) #[1]
...

# Footips
"""
[1]: ...
"""
```  
</details>  

这样。  
---
<h3 id="syntax"></h3>  

### <sup><a href="#content" target="_self">¶</a></sup> 3. 语法  
在 Winux 中，我们使用了一种以注释和字符串为主的简易语法体系。如果要使用这些语法，您需要：  
- 1. 注释  
注释语法主要以方括号为逻辑符号主体，脚注与特殊标记的语法也以方括号为主体。如：  

<details>
<summary>展开……</summary>

``` Python
#[!SKIP] Untitle
"""
[!SKIP] skip[Untitle]
"""
#[!DEFINE] Untitle: json[i]
i = {
    "basic":"aarch64"
    "class":"build-in",
    "function":"instruction",
    "extension":
        [
            "json-basic",
            "python",
            "pylance",
            "python3-is-python"
        ],
    "extra":
        {
            "basic":
                {
                    "rawtext":
                        [{
                            "code":"utf-8"
                        },{
                            "text":"已虚拟化的UEFI固件"
                        }]
                },
            "class":"define",
            "function":
                {
                    "ColsoneType":"function",
                    "ColsoneEvent":
                        {
                            "function":
                                {
                                    "basic":"python3", #[!SKIP] Temp
                                    """
                                    If unknown to write it, use a empty list or "python3"
                                    """
                                    "class":"build-in",
                                    "function":"skip",
                                    "extension":
                                        [
                                            "json-basic",
                                            "python",
                                            "pylance",
                                            "python3-is-python"
                                        ],
                                    "extra":[] #[!SKIP] Temp
                                    """
                                    If unknown to write it, use a empty list
                                    """
                                }
                        },
                    "ColsoneExtra":
                        {
                            "basic":["json"],
                            "build-in":
                                [
                                    "python",
                                    "pylance",
                                    "python3-is-python"
                                ],
                            "extension":["json-basic"],
                            "extra":["skip"]
                        }
                },
            "extension":
                [
                    "json-basic",
                    "python",
                    "pylance",
                    "python3-is-python"
                ],
            "extra":[]
        }
}
```  
</details>

> [!TIP]
> 此语法的`extension`部分原生支持`Pylance`和`cSpell`。
> 这些插件通常已经伴随着`Python`的`venv`环境或 <a href="https://code.visualstudio.com">Visual Studio Code</a> 安装。
更详细的内容可以参见<a href="#">我们的教程网站</a>。  
- 2. 字符串  
字符串语法通常配合注释语法使用，以“`""""""`”为逻辑符号主体。如：  
``` Python
#[!BUILD-IN] Copyright
"""
Copyright 2025 GD Studio.
"""
#[!BUILD-IN] Instruction
"""
Write something here... 
"""
...
```  
通常来说，注释的“`[!BUILD-IN] `”部分可以忽略不写。  
`[!BUILD-IN]`的内容也包括前文提到的脚注。  
&nbsp;&nbsp;&nbsp;&nbsp;1. 以“`#[x]`”定义脚注，其中`x`填写<bold>正</bold>整数，从 1 开始；  
&nbsp;&nbsp;&nbsp;&nbsp;2. 在文件末尾添加“`#[!BUILD-IN] Footips`”与“`""""""`”，并在其中以“`[x]: ...`”来说明脚注内容，其中`x`填写整数<sub>（包含负数、0 与正数）</sub>，从 1 开始，并且这个脚注必须是已经被定义的脚注；  
&nbsp;&nbsp;&nbsp;&nbsp;3. 同一个脚注可以被定义多次，但只能被说明一次；如果所有的脚注均有被说明，则脚注定义位置不限<sub>（即，脚注`#[2]`可在脚注`#[1]`前）</sub>。  
### <sup><a href="#content" target="_self">¶</a></sup> 4. 代码 <h3 id="code"></h3>  

自 <a href="update.ipynb" target="_self">2025061304 版本</a>后，我们的编写惯例采用分散式编写<sub>（即，将一部分的代码转移到其它文件中，在使用时内联调用。此方法可以解决部分不稳定因素，但也有可能导致少量<a href="#2" target="_blank">令人疑惑的 Bug</a> 出现。）</sub>，所以您将要递交的代码尽量通过分文件或分`class`的方式编写。<center><code><font color="red">请注意，我们通常不会受理已经存在的文件 / 计划的的文件的毁灭性递交，如 \_\_init__.py 的递交。</font></code></center>  

---
<h3 id="end"></h3>  

## <sup><a href="#content" target="_self">¶</a></sup> 后记  
如果您想为 Winux 的开发工作做出贡献，您可以前往<a href="https://github.com/Age10-Moyu/Winux">此项目的 GitHub 页</a>。  
希望文档可以帮助到你！

---
&copy; 2025 <a href="https://github.com/GDStu">GD Studio</a>. All rights reserved.  
&nbsp;&nbsp;Write by <a href="https://github.com/Age10-Moyu">Age10_Moyu</a>.
~~<!--Fxxk Markdown-->~~