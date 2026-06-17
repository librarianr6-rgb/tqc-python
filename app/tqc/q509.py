import math
TITLE = "最簡分數"
INPUTS = ["x", "y", "m", "n"]
INPUT_META = {
    "x": {"label": "分子 x", "placeholder": "請輸入 x"},
    "y": {"label": "分母 y", "placeholder": "請輸入 y"},
    "m": {"label": "分子 m", "placeholder": "請輸入 m"},
    "n": {"label": "分母 n", "placeholder": "請輸入 n"}
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入二個分數，分別是x/y和m/n（其中x、y、m、n皆為正整數），計算這兩個分數的和為p/q，接著將p和q傳遞給名為compute()函式，此函式回傳p和q的最大公因數（Greatest Common Divisor, GCD）。再將p和q各除以其最大公因數，最後輸出的結果必須以最簡分數表示。"
)
def solve(data: dict) -> dict:
    x = int(data["x"])
    y = int(data["y"])
    m = int(data["m"])
    n = int(data["n"])
    # 通分
    p = x * n + m * y   # 分子
    q = y * n           # 分母
    # 約分
    g = math.gcd(p, q)
    p //= g
    q //= g
    output = f"{x}/{y} + {m}/{n} = {p}/{q}"
    return {
        "output": output
    }