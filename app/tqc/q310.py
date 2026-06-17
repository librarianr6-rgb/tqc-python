import math
TITLE = "迴圈公式計算（根號分式總和）"
INPUTS = ["n"]
INPUT_META = {
    "n": {
        "label": "正整數 n",
        "placeholder": "請輸入正整數 (n > 1)"
    }
}
OUTPUT_HINT = (
    "請使用迴圈敘述撰寫一程式，讓使用者輸入正整數 n (1 < n)，"
    "計算以下公式的總和："
    "1/(1+√2) + 1/(√2+√3) + ... + 1/(√(n-1)+√n)，"
    "並輸出結果至小數點後四位。"
)
def solve(data: dict) -> dict:
    num = int(data["n"])
    total = 0.0
    for n in range(2, num + 1):
        total += 1 / (math.sqrt(n - 1) + math.sqrt(n))
    return {
        "output": f"{total:.4f}"
    }