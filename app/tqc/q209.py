import math
TITLE = "距離判斷"
INPUTS = ["x座標", "y座標"]
INPUT_META = {
    "x座標": {
        "label": "請輸入 x 座標",
        "placeholder": "例如：7"
    },
    "y座標": {
        "label": "請輸入 y 座標",
        "placeholder": "例如：20"
    }
}
OUTPUT_HINT = "(1111101)請使用選擇敘述撰寫一程式，讓使用者輸入一個點的平面座標x和y值，判斷此點是否與點(5, 6)的距離小於或等於15，如距離小於或等於15顯示【Inside】，反之顯示【Outside】。"
def solve(data: dict) -> dict:
    x = float(data["x座標"])
    y = float(data["y座標"])
    # 計算與 (5, 6) 的距離
    distance = math.sqrt((x - 5) ** 2 + (y - 6) ** 2)
    if distance <= 15:
        result = "Inside"
    else:
        result = "Outside"
    return {
        "output": result
    }