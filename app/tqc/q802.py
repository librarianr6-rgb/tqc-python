TITLE = "ASCII碼"

INPUTS = ["s"]

INPUT_META = {
    "s": {
        "label": "字串",
        "placeholder": "請輸入一個字串"
    }
}

OUTPUT_HINT = (
    "請輸入一個字串，程式會逐一輸出每個字元的 ASCII code，"
    "最後輸出所有字元 ASCII code 的總和。"
)

def solve(data: dict) -> dict:
    Str = data.get("s", "")
    Sum = 0
    results = []

    for i in range(len(Str)):
        ascii_code = ord(Str[i])
        results.append("ASCII code for '%s' is %d" % (Str[i], ascii_code))
        Sum += ascii_code

    results.append(str(Sum))

    return {
        "output": "\n".join(results)
    }