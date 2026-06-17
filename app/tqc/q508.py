TITLE = "最大公因數"
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
    "請撰寫一程式，讓使用者輸入兩個正整數x、y，並將x與y傳遞給名為compute()的函式，此函式回傳x和y的最大公因數。"
)
def solve(data: dict) -> dict:
    x = int(data["x"])
    y = int(data["y"])
    # 輾轉相除法（Euclidean Algorithm）
    while y != 0:
        x, y = y, x % y
    return {
        "output": str(x)
    }