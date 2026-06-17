TITLE = "字串大小寫轉換"

INPUTS = ["s"]

INPUT_META = {
    "s": {
        "label": "字串",
        "placeholder": "請輸入一個字串"
    }
}

OUTPUT_HINT = (
    "請輸入一個字串，程式會先輸出全部轉成大寫的結果，"
    "再輸出每個單字字首轉成大寫的結果。"
)

def solve(data: dict) -> dict:
    Str = data.get("s", "")

    results = [
        Str.upper(),
        Str.title()
    ]

    return {
        "output": "\n".join(results)
    }