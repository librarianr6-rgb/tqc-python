# 114111206_翁一
TITLE = "五個數值的總和與平均"
# 依題庫：輸入五個數字
INPUTS = ["數值1", "數值2", "數值3", "數值4", "數值5"]
# 題目輸出提示
OUTPUT_HINT = "請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。"
def solve(data: dict) -> dict:
    # 依序讀取五個輸入值
    l = [0] * 5
    l[0] = float(data["數值1"])
    l[1] = float(data["數值2"])
    l[2] = float(data["數值3"])
    l[3] = float(data["數值4"])
    l[4] = float(data["數值5"])
    total = sum(l)
    avg = total / len(l)
    # 完全對齊題庫輸出格式
    output_text = (
        f"{l[0]:.0f} {l[1]:.0f} {l[2]:.0f} {l[3]:.0f} {l[4]:.0f}\n"
        f"合計 = {total:.1f}\n"
        f"平均 = {avg:.1f}"
    )
    return {
        "output": output_text
    }