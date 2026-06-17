TITLE = "等級判斷"
INPUTS = ["分數"]
INPUT_META = {
    "分數": {
        "label": "請輸入分數",
        "placeholder": "請輸入 0~100 的整數"
    }
}
OUTPUT_HINT = "(1111101)請使用選擇敘述撰寫一程式，根據使用者輸入的分數顯示對應的等級。80~100:A，70~79:B，60~69:C，其餘:F"
def solve(data: dict) -> dict:
    s = int(float(data["分數"]))
    if s >= 80:
        grade = "A"
    elif s >= 70:
        grade = "B"
    elif s >= 60:
        grade = "C"
    else:
        grade = "F"
    return {
        "output": grade
    }