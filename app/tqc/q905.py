TITLE = "刪除字串"

INPUTS = ["content", "target"]

INPUT_META = {
    "content": {
        "label": "檔案內容",
        "placeholder": "請輸入檔案內容"
    },
    "target": {
        "label": "欲刪除字串",
        "placeholder": "請輸入要刪除的字串"
    }
}

OUTPUT_HINT = "顯示刪除前後的內容。"

def solve(data: dict) -> dict:
    content = data["content"]
    target = data["target"]

    result = []
    result.append("=== Before the deletion")
    result.append(content)

    result.append("=== After the deletion")
    result.append(content.replace(target, ""))

    return {
        "output": "\n".join(result)
    }