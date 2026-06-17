# 114111206_翁一
import math
TITLE = "正 n 邊形面積計算"
# 題庫輸入：正整數 n、正數 s
INPUTS = ["邊數", "邊長"]
#（# 題目輸出提示
OUTPUT_HINT = "請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）"
def solve(data: dict) -> dict:
    n = int(float(data["邊數"]))   # 邊數 n
    s = float(data["邊長"])        # 邊長 s
    # 正 n 邊形面積公式
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    # 完全對齊題庫輸出格式
    return {
        "output": f"正 n 邊形面積 = {area:.4f}"
    }