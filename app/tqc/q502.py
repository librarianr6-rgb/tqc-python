TITLE = "函式－乘積計算"
INPUTS = ["x", "y"]
INPUT_META = {
    "x": {
        "label": "整數 x",
        "placeholder": "請輸入整數 x"
    },
    "y": {
        "label": "整數 y",
        "placeholder": "請輸入整數 y"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，將使用者輸入的兩個整數作為參數傳遞給一個名為compute(x, y)的函式，此函式將回傳x和y的乘積。"
)
def compute(x, y):
    return x * y
def solve(data: dict) -> dict:
    x = int(data["x"])
    y = int(data["y"])
    result = compute(x, y)
    return {
        "output": str(result)
    }