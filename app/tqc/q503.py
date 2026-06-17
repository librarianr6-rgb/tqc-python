TITLE = "函式－區間加總"
INPUTS = ["a", "b"]
INPUT_META = {
    "a": {
        "label": "整數 a",
        "placeholder": "請輸入整數 a"
    },
    "b": {
        "label": "整數 b",
        "placeholder": "請輸入整數 b"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳從a連加到b的和。"
)
def compute(a, b):
    total = 0
    for i in range(a, b + 1):
        total += i
    return total
def solve(data: dict) -> dict:
    a = int(data["a"])
    b = int(data["b"])
    result = compute(a, b)
    return {
        "output": str(result)
    }