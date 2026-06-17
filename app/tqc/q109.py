# 114111101王大明
import math
TITLE = "正五邊形面積計算"
# 依題庫：輸入一個正數 s
INPUTS = ["邊長"]
# 題目輸出提示
OUTPUT_HINT = "請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）"
def solve(data: dict) -> dict:
    s = float(data["邊長"])
    # 正五邊形面積公式
    area = (5 * s ** 2) / (4 * math.tan(math.pi / 5))
    # 完全對齊題庫輸出格式
    return {
        "output": f"正五邊形面積 = {area:.4f}"
    }