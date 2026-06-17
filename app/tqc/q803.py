TITLE = "取出最後三個字"

INPUTS = ["s"]

INPUT_META = {
    "s": {
        "label": "字串",
        "placeholder": "請輸入一串文字"
    }
}

OUTPUT_HINT = (
    "請輸入一串文字，程式會將字串依空白切割成串列，"
    "並輸出最後三個單字。"
)

def solve(data: dict) -> dict:
    Str = data.get("s", "")

    List = Str.split()

    result = " ".join(List[-3:])

    return {
        "output": result
    }