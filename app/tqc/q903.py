TITLE = "模擬附加資料到檔案"

INPUTS = ["content", "names"]

INPUT_META = {
    "content": {
        "label": "原始檔案內容",
        "placeholder": "data.txt 原有內容"
    },
    "names": {
        "label": "新增的5個名字",
        "placeholder": "以空白分隔"
    }
}

def solve(data: dict) -> dict:
    content = data["content"]
    names = data["names"].split()

    for name in names[:5]:
        content += "\n" + name

    return {
        "output": content
    }