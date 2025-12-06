import tkinter as tk
from tkinter import ttk,filedialog,messagebox
import os
import sys
import json
import configparser
import hashlib
import chardet
from shared import lang_import,dynamic_import
from time import sleep
from random import randint

skip=False
if "--without-dynamic" in sys.argv or "-wd" in sys.argv:
    skip=True
    if __name__ == "__main__":
        if "--no-output" in sys.argv or "-no" in sys.argv:
            pass
        else:
            sleep(1)
            print("[WARN] Winux/Kernel/System32/SysCheck: Standard library 'dynamic' is not found, will replace with LightDM.")
            sleep(randint(1,3))
            print("[INFO] Winux/Kernel/System64/SysLib/ApplicationEnv: Load 1 package(s) ['LightDM'] from <build-in function>")
            sleep(randint(1,3))

if not skip:
    if not dynamic_import():
        if lang_import()=="zh_cn":
            print("> 标准库系列“dynamic”未找到，将使用 LightDynamic 替代。")
        else:
            print("> Standard library 'dynamic' is not found, will replace with LightDM.")
    if __name__=="__main__":
        raise EnvironmentError("Not dynamic environment be installed.\nNotepad cannot run without dynamic environment.\nUse '--without-dynamic' to skip dynamic environment check and notepad will use build-in LightDM instead.")

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lang_ini_path=os.path.join(os.path.dirname(__file__),"resource","home","user","lang.ini")
        self.lang=self._load_language()
        self.title(self._tr("无标题 - 记事本","Untited - Notepad"))
        self.geometry("800x600")
        self.icon_path=os.path.join(os.path.dirname(__file__),"resource","notepad","icons","icon.png")
        self.config_path=os.path.join(os.path.dirname(__file__),"resource","home","user","config.json")
        try:
            self.iconphoto(True,tk.PhotoImage(file=self.icon_path))
        except Exception:
            pass
        self._load_config()
        self._create_widgets()
        self._create_menu()
        self.file_path=None
        self.file_lock=None  # 文件锁
        self.original_content_hash=None  # 原始文件内容的哈希值
        self.current_encoding="utf-8"  # 当前文件编码
        self.protocol("WM_DELETE_WINDOW",self.on_close)

    def on_close(self):
        if self._confirm_unsaved():
            self._release_file_lock()
            self.destroy()

    def _tr(self,zh,en):
        return zh if self.lang=="zh_cn" else en

    def _acquire_file_lock(self,filepath):
        """获取文件锁"""
        try:
            self._release_file_lock()  # 先释放之前的锁
            # 创建锁文件
            lock_path=filepath+".lock"
            self.file_lock=open(lock_path,"w")
            self.file_lock.write(f"locked by notepad at {os.getpid()}")
            self.file_lock.flush()
            return True
        except Exception:
            return False

    def _release_file_lock(self):
        """释放文件锁"""
        try:
            if self.file_lock:
                lock_path=self.file_lock.name
                self.file_lock.close()
                self.file_lock=None
                if os.path.exists(lock_path):
                    os.remove(lock_path)
        except Exception:
            pass

    def _calculate_content_hash(self,content):
        """计算内容的MD5哈希值"""
        return hashlib.md5(content.encode('utf-8')).hexdigest()

    def _has_content_changed(self):
        """检查内容是否改变（通过比对哈希值）"""
        if self.original_content_hash is None:
            return False
        current_content=self.text.get(1.0,tk.END).rstrip("\n")
        current_hash=self._calculate_content_hash(current_content)
        return current_hash!=self.original_content_hash

    def _detect_encoding(self,file_path):
        """自动检测文件编码"""
        try:
            with open(file_path,"rb") as f:
                raw_data=f.read()
            result=chardet.detect(raw_data)
            encoding=result['encoding']
            confidence=result['confidence']
            
            # 如果检测置信度高，返回检测到的编码
            if confidence>0.7:
                # 统一一些编码名称
                if encoding.lower() in ['gb2312','gbk','gb18030']:
                    return 'gbk'
                elif encoding.lower() in ['utf-8-sig']:
                    return 'utf-8-sig'
                elif encoding.lower().startswith('utf'):
                    return 'utf-8'
                return encoding
            return 'utf-8'
        except Exception:
            return 'utf-8'

    def _load_language(self):
        """从 lang.ini 加载语言配置"""
        try:
            if os.path.exists(self.lang_ini_path):
                config=configparser.ConfigParser()
                config.read(self.lang_ini_path,encoding="utf-8")
                lang_code=config.get("LANG","global_lang",fallback="zh_cn")
                # 将 en 映射为 en，cn/zh_cn 映射为 zh_cn
                if lang_code.lower() in ["en","english"]:
                    return "en"
                else:
                    return "zh_cn"
        except Exception:
            pass
        # 回退到 lang_import() 或默认值
        return lang_import() or "zh_cn"

    def _load_config(self):
        """从配置文件加载字体设置"""
        self.current_font_family="Microsoft YaHei UI"
        self.current_font_size=11
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path,"r",encoding="utf-8") as f:
                    config=json.load(f)
                    app_config=config.get("app_config",{})
                    self.current_font_family=app_config.get("font_family","Microsoft YaHei UI")
                    self.current_font_size=app_config.get("font_size",11)
        except Exception:
            pass

    def _save_config(self):
        """保存字体设置到配置文件"""
        try:
            os.makedirs(os.path.dirname(self.config_path),exist_ok=True)
            
            # 读取现有配置
            existing_config={"global_config":{},"app_config":{}}
            if os.path.exists(self.config_path):
                try:
                    with open(self.config_path,"r",encoding="utf-8") as f:
                        existing_config=json.load(f)
                except Exception:
                    pass
            
            # 更新 app_config
            if "app_config" not in existing_config:
                existing_config["app_config"]={}
            existing_config["app_config"]["reg_name"]="notepad"
            existing_config["app_config"]["font_family"]=self.current_font_family
            existing_config["app_config"]["font_size"]=self.current_font_size
            
            # 保存配置
            with open(self.config_path,"w",encoding="utf-8") as f:
                json.dump(existing_config,f,ensure_ascii=False,indent=2)
        except Exception:
            pass

    def _create_widgets(self):
        # 创建框架用于正确布局
        text_frame=tk.Frame(self)
        text_frame.pack(fill=tk.BOTH,expand=True)
        
        # 创建滚动条
        self.scroll=ttk.Scrollbar(text_frame,command=self._on_scroll)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)
        
        # 创建文本框，优化性能和清晰度
        self.text=tk.Text(
            text_frame,
            undo=True,
            wrap="word",
            font=(self.current_font_family,self.current_font_size),
            maxundo=-1,  # 无限撤销
            autoseparators=True,  # 自动分隔撤销操作
            relief=tk.FLAT,  # 扁平边框
            borderwidth=0,
            highlightthickness=0,
            insertwidth=2,  # 光标宽度
            selectbackground="#0078d4",  # 选中背景色
            selectforeground="white",  # 选中文字色
            yscrollcommand=self.scroll.set
        )
        self.text.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        
        # 创建右键菜单
        self._create_context_menu()
    
    def _on_scroll(self,*args):
        """滚动回调，优化大文件性能"""
        self.text.yview(*args)

    def _create_context_menu(self):
        """创建右键菜单"""
        self.context_menu=tk.Menu(self.text,tearoff=0)
        self.context_menu.add_command(label=self._tr("撤销","Undo"),command=lambda: self.text.event_generate('<<Undo>>'))
        self.context_menu.add_command(label=self._tr("重做","Redo"),command=lambda: self.text.event_generate('<<Redo>>'))
        self.context_menu.add_separator()
        self.context_menu.add_command(label=self._tr("剪切","Cut"),command=lambda: self.text.event_generate('<<Cut>>'))
        self.context_menu.add_command(label=self._tr("复制","Copy"),command=lambda: self.text.event_generate('<<Copy>>'))
        self.context_menu.add_command(label=self._tr("粘贴","Paste"),command=lambda: self.text.event_generate('<<Paste>>'))
        self.context_menu.add_command(label=self._tr("删除","Delete"),command=self._delete_selection)
        self.context_menu.add_separator()
        self.context_menu.add_command(label=self._tr("全选","Select All"),command=lambda: self.text.event_generate('<<SelectAll>>'))
        
        # 绑定右键事件
        self.text.bind("<Button-3>",self._show_context_menu)

    def _show_context_menu(self,event):
        """显示右键菜单"""
        try:
            # 更新菜单项状态
            has_selection=bool(self.text.tag_ranges("sel"))
            can_undo=self.text.edit_modified()
            
            # 根据状态启用/禁用菜单项
            self.context_menu.entryconfig(0,state="normal" if can_undo else "disabled")  # 撤销
            self.context_menu.entryconfig(3,state="normal" if has_selection else "disabled")  # 剪切
            self.context_menu.entryconfig(4,state="normal" if has_selection else "disabled")  # 复制
            self.context_menu.entryconfig(6,state="normal" if has_selection else "disabled")  # 删除
            
            # 显示菜单
            self.context_menu.tk_popup(event.x_root,event.y_root)
        finally:
            self.context_menu.grab_release()

    def _delete_selection(self):
        """删除选中的文本"""
        try:
            self.text.delete("sel.first","sel.last")
        except tk.TclError:
            pass

    def _create_menu(self):
        menubar=tk.Menu(self)
        filemenu=tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label=self._tr("新建","New"),command=self.new_file)
        filemenu.add_command(label=self._tr("打开...","Open..."),command=self.open_file)
        filemenu.add_command(label=self._tr("以指定编码打开...","Open with Encoding..."),command=self.open_file_with_encoding)
        filemenu.add_command(label=self._tr("保存","Save"),command=self.save_file)
        filemenu.add_command(label=self._tr("另存为...","Save As..."),command=self.save_as)
        filemenu.add_command(label=self._tr("以指定编码保存...","Save with Encoding..."),command=self.save_with_encoding)
        filemenu.add_separator()
        filemenu.add_command(label=self._tr("退出","Exit"),command=self.on_close)
        menubar.add_cascade(label=self._tr("文件","File"),menu=filemenu)

        editmenu=tk.Menu(menubar,tearoff=0)
        editmenu.add_command(label=self._tr("撤销","Undo"),command=lambda: self.text.event_generate('<<Undo>>'))
        editmenu.add_command(label=self._tr("重做","Redo"),command=lambda: self.text.event_generate('<<Redo>>'))
        editmenu.add_separator()
        editmenu.add_command(label=self._tr("剪切","Cut"),command=lambda: self.text.event_generate('<<Cut>>'))
        editmenu.add_command(label=self._tr("复制","Copy"),command=lambda: self.text.event_generate('<<Copy>>'))
        editmenu.add_command(label=self._tr("粘贴","Paste"),command=lambda: self.text.event_generate('<<Paste>>'))
        editmenu.add_separator()
        editmenu.add_command(label=self._tr("全选","Select All"),command=lambda: self.text.event_generate('<<SelectAll>>'))
        menubar.add_cascade(label=self._tr("编辑","Edit"),menu=editmenu)

        formatmenu=tk.Menu(menubar,tearoff=0)
        formatmenu.add_command(label=self._tr("字体设置...","Font Settings..."),command=self.change_font)
        formatmenu.add_separator()
        formatmenu.add_command(label=self._tr("查找...","Find..."),command=self.find_text)
        formatmenu.add_command(label=self._tr("替换...","Replace..."),command=self.replace_text)
        menubar.add_cascade(label=self._tr("格式","Format"),menu=formatmenu)

        helpmenu=tk.Menu(menubar,tearoff=0)
        helpmenu.add_command(label=self._tr("关于","About"),command=self.show_about)
        helpmenu.add_separator()
        helpmenu.add_command(label=self._tr("This is not my language","这不是我的语言"),command=self.change_language)
        menubar.add_cascade(label=self._tr("帮助","Help"),menu=helpmenu)

        self.config(menu=menubar)

    def _choose_encoding(self,default_encoding="utf-8"):
        """选择编码对话框"""
        encoding_win=tk.Toplevel(self)
        encoding_win.title(self._tr("选择编码","Choose Encoding"))
        encoding_win.geometry("350x450")
        encoding_win.resizable(False,False)
        encoding_win.transient(self)
        encoding_win.grab_set()
        
        # 居中显示
        encoding_win.update_idletasks()
        x=(encoding_win.winfo_screenwidth()//2)-(encoding_win.winfo_width()//2)
        y=(encoding_win.winfo_screenheight()//2)-(encoding_win.winfo_height()//2)
        encoding_win.geometry(f"+{x}+{y}")
        
        # 主框架
        main_frame=tk.Frame(encoding_win,bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH,expand=True)
        
        # 标题
        tk.Label(main_frame,text=self._tr("选择文件编码:","Select File Encoding:"),
                font=("Segoe UI",11,"bold"),bg="#f0f0f0").pack(anchor="w",padx=20,pady=(20,10))
        
        # 编码列表框架
        list_frame=tk.Frame(main_frame,bg="white",relief=tk.SOLID,borderwidth=1)
        list_frame.pack(padx=20,pady=(0,20),fill=tk.BOTH,expand=True)
        
        scrollbar=ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        
        encoding_list=tk.Listbox(list_frame,yscrollcommand=scrollbar.set,font=("Segoe UI",10),
                                activestyle="none",highlightthickness=0,borderwidth=0,
                                selectbackground="#0078d4",selectforeground="white")
        encoding_list.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        scrollbar.config(command=encoding_list.yview)
        
        # 常用编码列表
        encodings=[
            ("UTF-8","utf-8"),
            ("UTF-8 with BOM","utf-8-sig"),
            ("GBK (简体中文)","gbk"),
            ("GB2312 (简体中文)","gb2312"),
            ("GB18030 (简体中文)","gb18030"),
            ("Big5 (繁体中文)","big5"),
            ("ASCII","ascii"),
            ("Latin-1 (ISO-8859-1)","latin-1"),
            ("Windows-1252","cp1252"),
            ("Shift-JIS (日文)","shift_jis"),
            ("EUC-JP (日文)","euc_jp"),
            ("EUC-KR (韩文)","euc_kr"),
            ("UTF-16 LE","utf-16-le"),
            ("UTF-16 BE","utf-16-be"),
            ("UTF-32 LE","utf-32-le"),
            ("UTF-32 BE","utf-32-be")
        ]
        
        selected_encoding=[default_encoding]
        
        for display_name,encoding_name in encodings:
            encoding_list.insert(tk.END,display_name)
            if encoding_name==default_encoding:
                encoding_list.select_set(encodings.index((display_name,encoding_name)))
                encoding_list.see(encodings.index((display_name,encoding_name)))
        
        # 当前选中的编码显示
        current_label=tk.Label(main_frame,
                              text=self._tr(f"当前选中: {default_encoding}",f"Current: {default_encoding}"),
                              font=("Segoe UI",9),bg="#f0f0f0",fg="#666")
        current_label.pack(anchor="w",padx=20,pady=(0,15))
        
        def on_select(event):
            selection=encoding_list.curselection()
            if selection:
                idx=selection[0]
                selected_encoding[0]=encodings[idx][1]
                current_label.config(text=self._tr(f"当前选中: {encodings[idx][1]}",
                                                   f"Current: {encodings[idx][1]}"))
        
        encoding_list.bind("<<ListboxSelect>>",on_select)
        
        # 按钮
        btn_frame=tk.Frame(main_frame,bg="#f0f0f0")
        btn_frame.pack(pady=(0,15))
        
        result=[None]
        
        def on_ok():
            result[0]=selected_encoding[0]
            encoding_win.destroy()
        
        def on_cancel():
            result[0]=None
            encoding_win.destroy()
        
        ttk.Button(btn_frame,text=self._tr("确定","OK"),command=on_ok,width=12).pack(side=tk.LEFT,padx=5)
        ttk.Button(btn_frame,text=self._tr("取消","Cancel"),command=on_cancel,width=12).pack(side=tk.LEFT,padx=5)
        
        encoding_win.wait_window()
        return result[0]

    def new_file(self):
        if self._confirm_unsaved():
            self._release_file_lock()
            self.text.delete(1.0,tk.END)
            self.file_path=None
            self.original_content_hash=None
            self.current_encoding="utf-8"
            self.title(self._tr("无标题 - 记事本","Untited - Notepad"))

    def open_file(self):
        """使用自动检测编码打开文件"""
        self._open_file_internal(None)

    def open_file_with_encoding(self):
        """使用指定编码打开文件"""
        encoding=self._choose_encoding("utf-8")
        if encoding:
            self._open_file_internal(encoding)

    def _open_file_internal(self,encoding=None):
        """内部打开文件方法"""
        if not self._confirm_unsaved():
            return
        path=filedialog.askopenfilename(filetypes=[(self._tr("Text Files","Text Files"),"*.txt"),(self._tr("All Files","All Files"),"*.*")])
        if path:
            try:
                # 自动检测编码或使用指定编码
                if encoding is None:
                    detected_encoding=self._detect_encoding(path)
                    self.current_encoding=detected_encoding
                else:
                    self.current_encoding=encoding
                
                # 获取文件锁
                if not self._acquire_file_lock(path):
                    messagebox.showwarning(
                        self._tr("文件已锁定","File Locked"),
                        self._tr("该文件可能正在被其他程序使用。","The file may be in use by another program.")
                    )
                
                # 读取文件内容
                with open(path,"r",encoding=self.current_encoding,errors="ignore") as f:
                    content=f.read()
                
                # 保存原始内容的哈希值
                self.original_content_hash=self._calculate_content_hash(content)
                
                self.text.delete(1.0,tk.END)
                self.text.insert(1.0,content)
                self.text.mark_set(tk.INSERT,"1.0")
                self.text.see("1.0")
                self.text.edit_modified(False)
                
                self.file_path=path
                # 在标题栏显示编码信息
                self.title(f"{os.path.basename(path)} - {self._tr('记事本','Notepad')}")
            except Exception as e:
                self._release_file_lock()
                messagebox.showerror(self._tr("打开文件失败","Open Failed"),str(e))

    def save_file(self):
        """使用当前编码保存文件"""
        if self.file_path:
            self._save_file_internal(self.file_path,self.current_encoding)
        else:
            self.save_as()

    def save_with_encoding(self):
        """使用指定编码保存文件"""
        if self.file_path:
            encoding=self._choose_encoding(self.current_encoding)
            if encoding:
                self._save_file_internal(self.file_path,encoding)
        else:
            self.save_as()

    def _save_file_internal(self,path,encoding):
        """内部保存文件方法"""
        try:
            content=self.text.get(1.0,tk.END).rstrip("\n")
            with open(path,"w",encoding=encoding,errors="ignore") as f:
                f.write(content)
            self.text.edit_modified(False)  # 标记为已保存
            
            # 更新哈希值
            self.original_content_hash=self._calculate_content_hash(content)
            self.current_encoding=encoding
            
            self.title(f"{os.path.basename(path)} - {self._tr('记事本','Notepad')}")
        except Exception as e:
            messagebox.showerror(self._tr("保存失败","Save Failed"),str(e))

    def save_as(self):
        path=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[(self._tr("Text Files","Text Files"),"*.txt"),(self._tr("All Files","All Files"),"*.*")])
        if path:
            try:
                # 释放旧文件锁，获取新文件锁
                self._release_file_lock()
                self._acquire_file_lock(path)
                
                self.file_path=path
                # 保存时保持当前编码
                self._save_file_internal(path,self.current_encoding)
            except Exception as e:
                messagebox.showerror(self._tr("保存失败","Save Failed"),str(e))

    def show_about(self):
        about=tk.Toplevel(self)
        about.title(self._tr("关于“记事本”","About\"Notepad\""))
        about.geometry("400x260")
        about.resizable(False,False)
        try:
            icon_img=tk.PhotoImage(file=self.icon_path)
            w,h=icon_img.width(),icon_img.height()
            scale=int(max(w // 64,h // 64,1))
            if scale > 1:
                icon_img=tk.PhotoImage(file=self.icon_path).subsample(scale,scale)  # type: ignore
            icon_label=tk.Label(about,image=icon_img)
            icon_label.image=icon_img  # type: ignore
            icon_label.pack(pady=(18,5))
        except Exception:
            pass
        title_label=tk.Label(about,text=self._tr("Winux 记事本","Winux Notepad"),font=("Segoe UI",15,"bold"))
        title_label.pack()
        desc_label=tk.Label(about,text=self._tr("仿 Windows 记事本风格\nBy GD Studio.","Windows Notepad Style\nBy GD Studio."),font=("Segoe UI",11))
        desc_label.pack(pady=(5,12))
        close_btn=ttk.Button(about,text=self._tr("关闭","Close"),command=about.destroy)
        close_btn.pack(pady=(0,12))
        about.transient(self)
        about.grab_set()
        self.wait_window(about)

    def change_language(self):
        """语言切换功能"""
        if self.lang=="zh_cn":
            msg=f"Current Language: {self.lang}\n\nSwitch to en?\nApplication will restart after switching."
            title="Language Settings"
            new_lang="en"
        else:
            msg=f"当前语言：{self.lang}\n\n你确实要切换到zh_cn吗？\n语言切换后，应用将自动重启。"
            title="语言设置"
            new_lang="zh_cn"
        
        result=messagebox.askyesno(title,msg)
        if result:
            try:
                # 更新 lang.ini 文件
                os.makedirs(os.path.dirname(self.lang_ini_path),exist_ok=True)
                config=configparser.ConfigParser()
                config["LANG"]={"global_lang":new_lang}
                with open(self.lang_ini_path,"w",encoding="utf-8") as f:
                    config.write(f)
                
                # 提示重启
                if self.lang=="zh_cn":
                    messagebox.showinfo("Success","Language changed.\nTo apply the changes, please restart Notepad.")
                else:
                    messagebox.showinfo("成功","语言已更改。\n重新启动记事本以应用更改。")
                
                # 关闭应用
                self.destroy()
                import subprocess
                if getattr(sys,'frozen',False):
                    # 如果是打包后的exe
                    subprocess.Popen([sys.executable]+sys.argv)
                else:
                    # 如果是Python脚本
                    subprocess.Popen([sys.executable]+sys.argv)
            except Exception as e:
                if self.lang=="zh_cn":
                    messagebox.showerror("Error",f"Failed to change language: {str(e)}")
                else:
                    messagebox.showerror("错误",f"无法更改语言设置：{str(e)}")

    def _confirm_unsaved(self):
        """确认是否保存未保存的更改（通过哈希比对）"""
        if self.file_path:
            # 通过哈希比对检查是否有更改
            if self._has_content_changed():
                filename=os.path.basename(self.file_path)
                res=messagebox.askyesnocancel(
                    self._tr("提示","Notice"),
                    self._tr(f"你想将更改保存到 {filename} 吗？",f"Do you want to save changes to {filename}?")
                )
                if res is None:
                    return False
                if res:
                    self.save_file()
            return True
        else:
            # 新文件：使用 edit_modified 标记
            if self.text.edit_modified():
                res=messagebox.askyesnocancel(
                    self._tr("提示","Notice"),
                    self._tr("你想将更改保存到 无标题 吗？","Do you want to save changes to Untitled?")
                )
                if res is None:
                    return False
                if res:
                    self.save_file()
        return True

    def change_font(self):
        """字体设置窗口 - 字体和字号集中在一个窗口，带实时预览"""
        font_win=tk.Toplevel(self)
        font_win.title(self._tr("字体设置","Font Settings"))
        font_win.geometry("620x480")
        font_win.resizable(False,False)
        
        # 临时变量
        temp_family=tk.StringVar(value=self.current_font_family)
        temp_size=tk.IntVar(value=self.current_font_size)
        
        # 主框架
        main_frame=tk.Frame(font_win,bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH,expand=True)
        
        # 左侧 - 字体列表
        left_frame=tk.Frame(main_frame,bg="#f0f0f0")
        left_frame.place(x=15,y=15,width=280,height=320)
        
        tk.Label(left_frame,text=self._tr("字体:","Font:"),font=("Segoe UI",11,"bold"),bg="#f0f0f0",anchor="w").pack(fill=tk.X,pady=(0,8))
        
        font_list_frame=tk.Frame(left_frame,bg="white",relief=tk.SOLID,borderwidth=1)
        font_list_frame.pack(fill=tk.BOTH,expand=True)
        
        font_scrollbar=ttk.Scrollbar(font_list_frame)
        font_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        
        font_list=tk.Listbox(font_list_frame,yscrollcommand=font_scrollbar.set,font=("Segoe UI",10),
                            activestyle="none",highlightthickness=0,borderwidth=0,selectbackground="#0078d4",
                            selectforeground="white")
        font_list.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        font_scrollbar.config(command=font_list.yview)
        
        import tkinter.font as tkfont
        available_fonts=sorted(tkfont.families())
        for font in available_fonts:
            font_list.insert(tk.END,font)
        
        try:
            idx=available_fonts.index(self.current_font_family)
            font_list.select_set(idx)
            font_list.see(idx)
        except ValueError:
            pass
        
        # 右侧 - 字号列表
        right_frame=tk.Frame(main_frame,bg="#f0f0f0")
        right_frame.place(x=310,y=15,width=120,height=320)
        
        tk.Label(right_frame,text=self._tr("字号:","Size:"),font=("Segoe UI",11,"bold"),bg="#f0f0f0",anchor="w").pack(fill=tk.X,pady=(0,8))
        
        size_list_frame=tk.Frame(right_frame,bg="white",relief=tk.SOLID,borderwidth=1)
        size_list_frame.pack(fill=tk.BOTH,expand=True)
        
        size_scrollbar=ttk.Scrollbar(size_list_frame)
        size_scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        
        size_list=tk.Listbox(size_list_frame,yscrollcommand=size_scrollbar.set,font=("Segoe UI",10),
                            activestyle="none",highlightthickness=0,borderwidth=0,selectbackground="#0078d4",
                            selectforeground="white")
        size_list.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        size_scrollbar.config(command=size_list.yview)
        
        common_sizes=[8,9,10,11,12,14,16,18,20,22,24,26,28,36,48,72]
        for size in common_sizes:
            size_list.insert(tk.END,str(size))
        
        try:
            idx=common_sizes.index(self.current_font_size)
            size_list.select_set(idx)
            size_list.see(idx)
        except ValueError:
            size_list.insert(tk.END,str(self.current_font_size))
            size_list.select_set(len(common_sizes))
        
        # 预览区域
        preview_frame=tk.LabelFrame(main_frame,text=self._tr("  预览  ","  Preview  "),
                                   font=("Segoe UI",10,"bold"),bg="white",relief=tk.SOLID,borderwidth=1)
        preview_frame.place(x=15,y=345,width=590,height=80)
        
        preview_text=tk.Label(preview_frame,text=self._tr("微软雅黑 AaBbCc123","Microsoft YaHei AaBbCc123"),
                            font=(temp_family.get(),temp_size.get()),bg="white",anchor="center")
        preview_text.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)
        
        def update_preview(*args):
            """更新预览"""
            try:
                preview_text.config(font=(temp_family.get(),temp_size.get()))
            except Exception:
                pass
        
        def on_font_select(event):
            selection=font_list.curselection()
            if selection:
                temp_family.set(font_list.get(selection[0]))
                update_preview()
        
        def on_size_select(event):
            selection=size_list.curselection()
            if selection:
                try:
                    temp_size.set(int(size_list.get(selection[0])))
                    update_preview()
                except ValueError:
                    pass
        
        font_list.bind("<<ListboxSelect>>",on_font_select)
        size_list.bind("<<ListboxSelect>>",on_size_select)
        
        # 底部按钮
        btn_frame=tk.Frame(main_frame,bg="#f0f0f0")
        btn_frame.place(x=15,y=435,width=590,height=35)
        
        def apply_settings():
            self.current_font_family=temp_family.get()
            self.current_font_size=temp_size.get()
            self.text.config(font=(self.current_font_family,self.current_font_size))
            self._save_config()
            font_win.destroy()
        
        def reset_default():
            temp_family.set("Microsoft YaHei UI")
            temp_size.set(11)
            update_preview()
            try:
                idx=available_fonts.index("Microsoft YaHei UI")
                font_list.selection_clear(0,tk.END)
                font_list.select_set(idx)
                font_list.see(idx)
            except ValueError:
                pass
            try:
                idx=common_sizes.index(11)
                size_list.selection_clear(0,tk.END)
                size_list.select_set(idx)
                size_list.see(idx)
            except ValueError:
                pass
        
        ttk.Button(btn_frame,text=self._tr("确定","OK"),command=apply_settings,width=12).pack(side=tk.RIGHT,padx=5)
        ttk.Button(btn_frame,text=self._tr("取消","Cancel"),command=font_win.destroy,width=12).pack(side=tk.RIGHT,padx=5)
        ttk.Button(btn_frame,text=self._tr("恢复默认","Reset"),command=reset_default,width=12).pack(side=tk.LEFT,padx=5)
        
        font_win.transient(self)
        font_win.grab_set()

    def find_text(self):
        find_win=tk.Toplevel(self)
        find_win.title(self._tr("查找","Find"))
        find_win.geometry("400x150")
        find_win.resizable(False,False)
        
        tk.Label(find_win,text=self._tr("查找内容:","Find:"),font=("Segoe UI",10)).pack(anchor="w",padx=20,pady=(20,5))
        
        find_entry=ttk.Entry(find_win,font=("Segoe UI",10),width=40)
        find_entry.pack(padx=20,pady=(0,20))
        find_entry.focus()
        
        def do_find():
            keyword=find_entry.get()
            if not keyword:
                return
            
            self.text.tag_remove("found","1.0",tk.END)
            start="1.0"
            count=0
            while True:
                pos=self.text.search(keyword,start,tk.END,nocase=True)
                if not pos:
                    break
                end=f"{pos}+{len(keyword)}c"
                self.text.tag_add("found",pos,end)
                count+=1
                start=end
            
            self.text.tag_config("found",background="yellow",foreground="black")
            
            if count==0:
                messagebox.showinfo(self._tr("查找","Find"),self._tr(f"找不到\"{keyword}\"",f"Cannot find \"{keyword}\""),parent=find_win)
            else:
                first_pos=self.text.search(keyword,"1.0",tk.END,nocase=True)
                if first_pos:
                    self.text.see(first_pos)
                    self.text.mark_set(tk.INSERT,first_pos)
        
        btn_frame=tk.Frame(find_win)
        btn_frame.pack()
        ttk.Button(btn_frame,text=self._tr("查找","Find"),command=do_find).pack(side=tk.LEFT,padx=5)
        ttk.Button(btn_frame,text=self._tr("关闭","Close"),command=find_win.destroy).pack(side=tk.LEFT,padx=5)
        
        find_win.transient(self)
        find_win.grab_set()

    def replace_text(self):
        replace_win=tk.Toplevel(self)
        replace_win.title(self._tr("替换","Replace"))
        replace_win.geometry("400x220")
        replace_win.resizable(False,False)
        
        tk.Label(replace_win,text=self._tr("查找内容:","Find:"),font=("Segoe UI",10)).pack(anchor="w",padx=20,pady=(20,5))
        find_entry=ttk.Entry(replace_win,font=("Segoe UI",10),width=40)
        find_entry.pack(padx=20,pady=(0,10))
        find_entry.focus()
        
        tk.Label(replace_win,text=self._tr("替换为:","Replace with:"),font=("Segoe UI",10)).pack(anchor="w",padx=20,pady=(0,5))
        replace_entry=ttk.Entry(replace_win,font=("Segoe UI",10),width=40)
        replace_entry.pack(padx=20,pady=(0,20))
        
        def do_replace():
            find_text=find_entry.get()
            replace_text=replace_entry.get()
            if not find_text:
                return
            
            content=self.text.get("1.0",tk.END)
            new_content=content.replace(find_text,replace_text)
            count=content.count(find_text)
            
            if count>0:
                self.text.delete("1.0",tk.END)
                self.text.insert("1.0",new_content)
                messagebox.showinfo(self._tr("替换","Replace"),self._tr(f"已替换 {count} 处",f"Replaced {count} occurrence(s)"),parent=replace_win)
            else:
                messagebox.showinfo(self._tr("替换","Replace"),self._tr(f"找不到\"{find_text}\"",f"Cannot find \"{find_text}\""),parent=replace_win)
        
        btn_frame=tk.Frame(replace_win)
        btn_frame.pack()
        ttk.Button(btn_frame,text=self._tr("全部替换","Replace All"),command=do_replace).pack(side=tk.LEFT,padx=5)
        ttk.Button(btn_frame,text=self._tr("关闭","Close"),command=replace_win.destroy).pack(side=tk.LEFT,padx=5)
        
        replace_win.transient(self)
        replace_win.grab_set()

def main():
    app=Notepad()
    app.mainloop()

if __name__=="__main__":
    main()
