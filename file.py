import os,shared

lang=shared.lang_import()

def file_dir(path="."):
    try:
        items=os.listdir(path)
        text="\n".join(items)
        return {"result": True, "text": text}
    except Exception as e:
        return {"result": False, "text": str(e)}

def file_ls(path="."):
    try:
        items=os.listdir(path)
        text="\n".join(items)
        return {"result": True, "text": text}
    except Exception as e:
        return {"result": False, "text": str(e)}
