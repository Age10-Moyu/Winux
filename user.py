import os
import json
from pathlib import Path
from shared import lang_import, user_import, command_import



def encode(text):
    CIPHER_CODE = "hdelbkj73y24adb2b6nadbbkj77z3jadbbkj7f79aadbbkj7dc2kcg"
    result = []
    for i, char in enumerate(text.lower()):
        if not char.isalpha():
            result.append(char)
            continue
        shifted = ord(char) + 3
        if shifted > ord('z'):
            shifted -= 26
        num = ord(chr(shifted)) - ord('a') + 1
        if (i+1) % 2 == 1:
            num += 1
        else:
            num -= 1
        cipher_char = CIPHER_CODE[num % len(CIPHER_CODE)]
        result.append(cipher_char)
    return ''.join(result)

def decode(text):
    CIPHER_CODE = "hdelbkj73y24adb2b6nadbbkj77z3jadbbkj7f79aadbbkj7dc2kcg"
    result = []
    for i, char in enumerate(text):
        if not char.isalpha():
            result.append(char)
            continue
        try:
            num = CIPHER_CODE.index(char)
        except ValueError:
            result.append(char)
            continue
        if (i+1) % 2 == 1:
            num -= 1
        else:
            num += 1
        if num <= 0:
            num += 26
        letter = chr(num + ord('a') - 1)
        shifted = ord(letter) - 3
        if shifted < ord('a'):
            shifted += 26
        result.append(chr(shifted))
    return ''.join(result)

def ensure_dir_exists(path):
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path, exist_ok=True)

lang_path = "resource/home/user/lang.ini"
ensure_dir_exists(lang_path)
with open(lang_path, "w", encoding="utf-8") as f:
    f.write(lang_import())

account_path = "resource/home/user/account.json"
ensure_dir_exists(account_path)
username = user_import()
password = "zyz20120418" if username in ["Age10_Moyu", "System"] else "winux-default-password"
with open(account_path, "w", encoding="utf-8") as f:
    json.dump({
        "account": username,
        "password": encode(password)
    }, f, ensure_ascii=False, indent=2)

history_path = "resource/home/user/history.txt"
ensure_dir_exists(history_path)
with open(history_path, "a", encoding="utf-8") as f:
    f.write(command_import() + "\n")