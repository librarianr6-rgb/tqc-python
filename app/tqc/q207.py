TITLE = "折扣方案"
INPUTS = ["購物金額"]
INPUT_META = {
    "購物金額": {
        "label": "請輸入購物金額",
        "placeholder": "請輸入金額（整數或浮點數）"
    }
}
OUTPUT_HINT = "(1111101)請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於8,000（含）以上，並顯示折扣優惠後的實付金額。8,000（含）以上	9.5折，18,000（含）以上	9折，28,000（含）以上	8折，38,000（含）以上	7折"
def solve(data: dict) -> dict:
    m = float(data["購物金額"])
    if m >= 38000:
        total = m * 0.7
    elif m >= 28000:
        total = m * 0.8
    elif m >= 18000:
        total = m * 0.9
    elif m >= 8000:
        total = m * 0.95
    else:
        total = m
    return {
        "output": str(total)
    }