import os
import sys
from datetime import datetime
from shared import lang_import
from shared import command_import
from shared import user_import

lang = lang_import()
user = user_import()
command = command_import()

def format_size(size):
    """格式化文件大小显示"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f}{unit}"
        size /= 1024.0

def format_time(timestamp):
