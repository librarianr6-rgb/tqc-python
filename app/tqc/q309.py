TITLE = "每月存款總額"
INPUTS = ["存款金額", "年利率", "月數"]
OUTPUT_HINT = "請使用迴圈敘述撰寫一程式，提示使用者輸入金額、年收益率，以及經過的月份數，接著顯示每個月的存款總額。輸出浮點數到小數點後第二位。"
def solve(data: dict) -> dict:
    total = float(data["存款金額"])
    y = float(data["年利率"])
    m = int(float(data["月數"]))
    lines = []
    lines.append("%s \t  %s" % ("Month", "Amount"))
    for i in range(1, m + 1):
        total += total * y / 1200
        lines.append("%3d \t %.2f" % (i, total))
    return {
        "output": "\n".join(lines)
    }