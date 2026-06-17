# 114111206_翁一
TITLE = "座標距離計算"
# 依題庫：輸入四個數字 x1, y1, x2, y2
INPUTS = ["x1", "y1", "x2", "y2"]
# 題目輸出提示
OUTPUT_HINT = "請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。"
def solve(data: dict) -> dict:
    # 讀取輸入
    x1 = float(data["x1"])
    y1 = float(data["y1"])
    x2 = float(data["x2"])
    y2 = float(data["y2"])
    # 計算歐式距離
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    # 完全對齊題庫輸出格式
    output_text = (
        f"( {x1:g} , {y1:g} )\n"
        f"( {x2:g} , {y2:g} )\n"
        f"距離 = {distance:.4f}"
    )
    return {
        "output": output_text
    }