TITLE = "字串取代"

INPUTS = ["content", "old", "new"]

INPUT_META = {
    "content": {
        "label": "檔案內容",
        "placeholder": "請輸入檔案內容"
    },
    "old": {
        "label": "原字串",
        "placeholder": "欲被取代的字串"
    },
    "new": {
        "label": "新字串",
        "placeholder": "取代後的字串"
    }
}

OUTPUT_HINT = "顯示取代前後的內容。"

def solve(data: dict) -> dict:
    content = data["content"]
    old = data["old"]
    new = data["new"]

    result = []
    result.append("=== Before the replacement")
    result.append(content)

    result.append("=== After the replacement")
    result.append(content.replace(old, new))

    return {
        "output": "\n".join(result)
    }