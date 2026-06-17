# 114111206_翁一
import math
TITLE = "圓形面積與周長計算"
INPUTS = ["半徑"]
OUTPUT_HINT = "請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）"
def solve(data: dict) -> dict:
    r = float(data["半徑"])
    perimeter = 2 * math.pi * r
    area = math.pi * r * r
    return {
        "output": (
            f"半徑 = {r:.2f}\n"
            f"周長 = {perimeter:.2f}\n"
            f"面積 = {area:.2f}"
        )
    }