import math
TITLE = "一元二次方程式"
INPUTS = ["a", "b", "c"]
INPUT_META = {
    "a": {
        "label": "係數 a",
        "placeholder": "請輸入 a"
    },
    "b": {
        "label": "係數 b",
        "placeholder": "請輸入 b"
    },
    "c": {
        "label": "係數 c",
        "placeholder": "請輸入 c"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，將使用者輸入的三個整數（代表一元二次方程式的三個係數a、b、c）作為參數傳遞給一個名為compute()的函式，該函式回傳方程式的解，如無解則輸出【Your equation has no root.】"
)
def solve(data: dict) -> dict:
    a = float(data["a"])
    b = float(data["b"])
    c = float(data["c"])
    d = b**2 - 4*a*c  # 判別式
    if d < 0:
        return {
            "output": "Your equation has no root."
        }
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    # 由大到小排序
    roots = sorted([root1, root2], reverse=True)
    return {
        "output": f"{roots[0]}, {roots[1]}"
    }