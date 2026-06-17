TITLE = "迴圈偶數連加"
INPUTS = ["a", "b"]
INPUT_META = {
    "a": {"label": "起始整數 a", "placeholder": "請輸入整數 a（a < b）"},
    "b": {"label": "結束整數 b", "placeholder": "請輸入整數 b（a < b）"},
}
OUTPUT_HINT = (
    "請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數 a、b（a < b），"
    "利用迴圈計算從 a 開始的偶數連加到 b 的總和。"
)
def solve(data: dict) -> dict:
    a = int(data["a"])
    b = int(data["b"])
    total = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            total += i
    return {
        "output": str(total)
    }