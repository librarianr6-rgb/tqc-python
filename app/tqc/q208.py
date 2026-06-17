TITLE = "十進位轉十六進位"
INPUTS = ["十進位數"]
INPUT_META = {
    "十進位數": {
        "label": "請輸入 0~15 的整數",
        "placeholder": "例如：13"
    }
}
OUTPUT_HINT = "(1111101)請使用選擇敘述撰寫一程式，讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，將num轉換成十六進位值。轉換規則 = 十進位0~9的十六進位值為其本身，十進位10~15的十六進位值為A~F。"
def solve(data: dict) -> dict:
    num = int(float(data["十進位數"]))
    if num <= 9:
        result = str(num)
    elif num == 10:
        result = "A"
    elif num == 11:
        result = "B"
    elif num == 12:
        result = "C"
    elif num == 13:
        result = "D"
    elif num == 14:
        result = "E"
    elif num == 15:
        result = "F"
    else:
        result = "輸入超出範圍!"
    return {
        "output": result
    }