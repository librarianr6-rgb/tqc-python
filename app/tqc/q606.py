TITLE = "二維串列行列數"
INPUTS = ["rows", "cols"]
INPUT_META = {
    "rows": {
        "label": "列數 rows",
        "placeholder": "請輸入列數"
    },
    "cols": {
        "label": "行數 cols",
        "placeholder": "請輸入行數"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入兩個正整數rows、cols，分別表示二維串列lst 的「第一個維度大小」與「第二個維度大小」。串列元素[row][col]所儲存的數字，其規則為：row、col 的交點值 = 第二個維度的索引col – 第一個維度的索引row。接著以該串列作為參數呼叫函式compute()輸出串列。提示：欄寬為4。"
)
def solve(data: dict) -> dict:
    rows = int(data["rows"])
    cols = int(data["cols"])
    lines = []
    for row in range(rows):
        line = ""
        for col in range(cols):
            val = col - row
            line += f"{val:>4}"
        lines.append(line)
    return {
        "output": "\n".join(lines)
    }