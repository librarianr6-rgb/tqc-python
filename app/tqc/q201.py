TITLE = "偶數判斷"
INPUTS = ["整數"]
OUTPUT_HINT = "(1141111101)請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是否為偶數（even）"
def solve(data: dict) -> dict:
    n = int(float(data["整數"]))  # 輸入整數
    if n % 2 == 0:
        result = f"{n} 是偶數."
    else:
        result = f"{n} 是奇數."
    return {
        "output": result
    }