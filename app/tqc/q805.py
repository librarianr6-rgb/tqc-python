TITLE = "字串對齊"

INPUTS = ["s"]

INPUT_META = {
    "s": {
        "label": "長度為6的字串",
        "placeholder": "請輸入長度為6的字串"
    }
}

OUTPUT_HINT = (
    "請輸入一個長度為6的字串，程式會將此字串分別置於寬度為10的欄位中，"
    "並依序顯示靠左、置中、靠右三種結果，左右皆以直線 | 作為邊界。"
)

def solve(data: dict) -> dict:
    Str = data.get("s", "")

    results = [
        "|" + Str.ljust(10) + "|",
        "|" + Str.center(10) + "|",
        "|" + Str.rjust(10) + "|"
    ]

    return {
        "output": "\n".join(results)
    }