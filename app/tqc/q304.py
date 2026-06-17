TITLE = "迴圈倍數總和"
INPUTS = ["a"]
INPUT_META = {
    "a": {
        "label": "整數 a",
        "placeholder": "請輸入正整數"
    }
}
OUTPUT_HINT = (
    "請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數 a，"
    "利用迴圈計算從 1 到 a 之間，所有 5 之倍數數字的總和。"
)
def solve(data: dict) -> dict:
    a = int(data["a"])
    total = 0
    for i in range(1, a + 1):
        if i % 5 == 0:
            total += i
    return {
        "output": str(total)
    }