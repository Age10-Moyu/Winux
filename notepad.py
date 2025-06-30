import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from shared import lang_import,dynamic_import

if not dynamic_import():
    raise ImportError("Cannot found lib 'dynamics'. Are you installed it?")

class Notepad(tk.Tk):
    def __init__(self):
        super().__init__()
        self.lang = lang_import() or "zh_cn"
        self.title(self._tr("无标题 - 记事本", "Untited - Notepad"))
        self.geometry("800x600")
        self.icon_path = os.path.join(os.path.dirname(__file__), "resource", "notepad", "icons", "icon.png")
        try:
            self.iconphoto(True, tk.PhotoImage(file=self.icon_path))
        except Exception:
            pass
        self._create_widgets()
        self._create_menu()
        self.file_path = None
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        if self._confirm_unsaved():
            self.destroy()

    def _tr(self, zh, en):
        return zh if self.lang == "zh_cn" else en

    def _create_widgets(self):
        self.text = tk.Text(self, undo=True, wrap="word", font=("Microsoft YaHei UI", 11))
        self.text.pack(fill=tk.BOTH, expand=True)
        self.scroll = ttk.Scrollbar(self, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

    def _create_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label=self._tr("新建", "New"), command=self.new_file)
        filemenu.add_command(label=self._tr("打开...", "Open..."), command=self.open_file)
        filemenu.add_command(label=self._tr("保存", "Save"), command=self.save_file)
        filemenu.add_command(label=self._tr("另存为...", "Save As..."), command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label=self._tr("退出", "Exit"), command=self.quit)
        menubar.add_cascade(label=self._tr("文件", "File"), menu=filemenu)

        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label=self._tr("撤销", "Undo"), command=lambda: self.text.event_generate('<<Undo>>'))
        editmenu.add_command(label=self._tr("重做", "Redo"), command=lambda: self.text.event_generate('<<Redo>>'))
        editmenu.add_separator()
        editmenu.add_command(label=self._tr("剪切", "Cut"), command=lambda: self.text.event_generate('<<Cut>>'))
        editmenu.add_command(label=self._tr("复制", "Copy"), command=lambda: self.text.event_generate('<<Copy>>'))
        editmenu.add_command(label=self._tr("粘贴", "Paste"), command=lambda: self.text.event_generate('<<Paste>>'))
        editmenu.add_separator()
        editmenu.add_command(label=self._tr("全选", "Select All"), command=lambda: self.text.event_generate('<<SelectAll>>'))
        menubar.add_cascade(label=self._tr("编辑", "Edit"), menu=editmenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label=self._tr("关于", "About"), command=self.show_about)
        menubar.add_cascade(label=self._tr("帮助", "Help"), menu=helpmenu)

        self.config(menu=menubar)

    def new_file(self):
        if self._confirm_unsaved():
            self.text.delete(1.0, tk.END)
            self.file_path = None
            self.title(self._tr("无标题 - 记事本", "Untited - Notepad"))

    def open_file(self):
        if not self._confirm_unsaved():
            return
        path = filedialog.askopenfilename(filetypes=[(self._tr("Text Files", "Text Files"), "*.txt"), (self._tr("All Files", "All Files"), "*.*")])
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)
                self.file_path = path
                self.title(f"{os.path.basename(path)} - {self._tr('记事本', 'Notepad')}")
            except Exception as e:
                messagebox.showerror(self._tr("打开文件失败", "Open Failed"), str(e))

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, "w", encoding="utf-8") as f:
                    f.write(self.text.get(1.0, tk.END).rstrip("\n"))
                self.title(f"{os.path.basename(self.file_path)} - {self._tr('记事本', 'Notepad')}")
            except Exception as e:
                messagebox.showerror(self._tr("保存失败", "Save Failed"), str(e))
        else:
            self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[(self._tr("Text Files", "Text Files"), "*.txt"), (self._tr("All Files", "All Files"), "*.*")])
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self.text.get(1.0, tk.END).rstrip("\n"))
                self.file_path = path
                self.title(f"{os.path.basename(path)} - {self._tr('记事本', 'Notepad')}")
            except Exception as e:
                messagebox.showerror(self._tr("保存失败", "Save Failed"), str(e))

    def show_about(self):
        about = tk.Toplevel(self)
        about.title(self._tr("关于", "About"))
        about.geometry("400x260")
        about.resizable(False, False)
        # 图标（缩小显示）
        try:
            icon_img = tk.PhotoImage(file=self.icon_path)
            w, h = icon_img.width(), icon_img.height()
            scale = int(max(w // 64, h // 64, 1))
            if scale > 1:
                icon_img = tk.PhotoImage(file=self.icon_path).subsample(scale, scale)  # type: ignore
            icon_label = tk.Label(about, image=icon_img)
            icon_label.image = icon_img  # type: ignore
            icon_label.pack(pady=(18, 5))
        except Exception:
            pass
        # 标题
        title_label = tk.Label(about, text=self._tr("Winux 记事本", "Winux Notepad"), font=("Segoe UI", 15, "bold"))
        title_label.pack()
        # 描述
        desc_label = tk.Label(about, text=self._tr("仿 Windows 记事本风格\nBy GD Studio", "Windows Notepad Style\nBy GD Studio"), font=("Segoe UI", 11))
        desc_label.pack(pady=(5, 12))
        # 关闭按钮
        close_btn = ttk.Button(about, text=self._tr("关闭", "Close"), command=about.destroy)
        close_btn.pack(pady=(0, 12))
        about.transient(self)
        about.grab_set()
        self.wait_window(about)

    def _confirm_unsaved(self):
        if self.text.edit_modified():
            res = messagebox.askyesnocancel(self._tr("提示", "Notice"), self._tr("你想将更改保存到 无标题 吗？", "Do you want to save changes to Untitled?"))
            if res is None:
                return False
            if res:
                self.save_file()
        return True

def main():
    app = Notepad()
    app.mainloop()

if __name__ == "__main__":
    main()
