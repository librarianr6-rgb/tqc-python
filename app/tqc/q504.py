
TITLE = "函式－次方計算"
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
    "請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，此函式接收兩個參數a、b，並回傳 a、b的值。"
)
def solve(data: dict) -> dict:
    a = int(data["a"])
    b = int(data["b"])
    return {
        "output": str(a ** b)
    }