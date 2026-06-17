TITLE = "迴圈乘法表"
INPUTS = ["整數n"]
OUTPUT_HINT = "請使用迴圈敘述撰寫一程式，要求使用者輸入一個正整數n（n < 10），顯示n*n乘法表。每個運算子及運算元輸出的欄寬為2，而每項乘積輸出的欄寬為4，皆靠左對齊且不斷行。"
def solve(data: dict) -> dict:
    n = int(float(data["整數n"]))
    lines = []
    for i in range(1, n + 1):
        line = ""
        for j in range(1, n + 1):
            line += "%-2d* %-2d= %-4d" % (j, i, j * i)
        lines.append(line)
    return {
        "output": "\n".join(lines)
    }