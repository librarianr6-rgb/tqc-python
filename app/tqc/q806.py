TITLE = "字元出現次數"

INPUTS = ["s", "ch"]

INPUT_META = {
    "s": {
        "label": "字串",
        "placeholder": "請輸入一個字串"
    },
    "ch": {
        "label": "字元",
        "placeholder": "請輸入要計算的字元"
    }
}

OUTPUT_HINT = (
    "請輸入一個字串和一個字元，程式會將字串與字元傳入 compute() 函式，"
    "計算該字元在字串中出現的次數，並輸出結果。"
)

def compute(Str: str, ch: str) -> int:
    count = 0

    for c in Str:
        if c == ch:
            count += 1

    return count

def solve(data: dict) -> dict:
    Str = data.get("s", "")
    ch = data.get("ch", "")

    result = compute(Str, ch)

    return {
        "output": str(result)
    }