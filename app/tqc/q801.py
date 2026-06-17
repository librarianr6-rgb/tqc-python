TITLE = "字元索引"

INPUTS = ["s"]

INPUT_META = {
    "s": {
        "label": "字串",
        "placeholder": "請輸入一個字串"
    }
}

OUTPUT_HINT = (
    "請輸入一個字串，程式會逐一印出每個字元及其所在的索引位置。"
)

def solve(data: dict) -> dict:
    Str = data.get("s", "")

    results = []

    for i in range(len(Str)):
        results.append("Index of '%s': %d" % (Str[i], i))

    return {
        "output": "\n".join(results)
    }