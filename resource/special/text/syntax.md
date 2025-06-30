## 前言
对于任何一种终端，都需要有一种严格且规范的语法来保证终端的正常运作。Winux 也不例外。  
因此，我们制订了一套适用于 Winux 的语法。  
掌握它们，您将可以在使用 Winux 的过程中如鱼得水。

---
## 语法
#### 以下是 Winux 的命令行语句模板：  
_sudo_  `group`  `command`  /value:[ yes | no | \{"`text`"} ]  _/active:[ yes | no ]_  _[ from | by ]  `username`_  /command:[ yes | no ]  _/active:[ yes | no ]  <ins>**`oldpassword`  `newpassword`**</ins>  <ins>/group:[ users | devlopers | administrators | "Super Users" | root | system ]</ins>  --[ rootin | system ]_  
- _sudo_：选填。证明此命令以管理员权限运行。  
- `group`：必填。`command`所在的命令组空间。  
需要手动填写，即需要根据语境自行填写相关的内容，而并非照搬。  
- `command`：必填。需要执行的命令名称。  
需要手动填写。  
- /value：必填。规定了传递给 Winux 的附加值。  
当跟随的值是\{"`text`"}时，需要手动填写[^1]。  
- _/active<sub>1</sub>_：选填。证明此命令以开发者权限运行，通常与 _sudo_ 搭配使用。
- _[ from | by ] `username`_：选填。规定以什么用户的名义执行此命令。默认为当前登录的账户。  
`username`需要手动填写。  
- /command：必填。规定了是否执行此命令，在某些时候是二次确认。  
- _/active<sub>2</sub>_：选填。决定是否要更改此账户的某些信息。  
当此项存在且跟随值为yes时，_**`oldpassword`  `newpassword`**_ 与 _/group_ 至少存在一项或同时存在。  
- **_`oldpassword`_**：当 _/active<sub>2</sub>_ 存在时必填，反之不填。当前账户的旧密码。  
- **_`newpassword`_**：当 _/active<sub>2</sub>_ 与 _`oldpassword`_ 存在时必填，反之不填。当前账户意愿的新密码。  
- _/group_：当 _/active<sub>2</sub>_ 存在时必填，反之不填。更改当前账户的用户组，权限自左至右逐级递增。  
“"Super Users"”与“root”同级。  
- _--[ rootin | system ]_：选填。证明此命令以超级用户或系统权限运行，通常与 _sudo_ 及 _/active<sub>1</sub>_ 搭配使用。

很复杂，对吧？那么让我们看几个实例吧。  <del><sub>这里是后期的Caviar，我感觉我的眼睛被强健了，默鱼你看看你自己写的什么β玩意</sub></del>  
- sudo pc install /value:{"dynamic"} /active:yes from Age10_Moyu /command:yes /active:no --system  
意为以系统权限安装标准着色器。  
- pc power /value:no /command:yes  
意为关机。

## 后记
好的命令可以帮助你高效完成工作，希望这篇文章可以帮助到你！