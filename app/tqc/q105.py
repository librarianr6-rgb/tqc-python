# 114111206_翁一
TITLE = "矩形面積與周長計算"
INPUTS = ["高", "寬"]
OUTPUT_HINT = "請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）"
def solve(data: dict) -> dict:
    h = float(data["高"])
    w = float(data["寬"])
    perimeter = 2 * (h + w)
    area = h * w
    return {
        "output": (
            f"高 = {h:.2f}\n"
            f"寬 = {w:.2f}\n"
            f"周長 = {perimeter:.2f}\n"
            f"面積 = {area:.2f}"
        )
    }
