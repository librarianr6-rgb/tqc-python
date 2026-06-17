TITLE = "成績計算（多學生）"
INPUTS = [f"s{i}_{j}" for i in range(3) for j in range(5)]
INPUT_META = {
    f"s{i}_{j}": {
        "label": f"第{i+1}位學生 第{j+1}科",
        "placeholder": "請輸入成績"
    }
    for i in range(3) for j in range(5)
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。提示：平均分數輸出到小數點後第二位。"
)
def solve(data: dict) -> dict:
    lines = []
    for i in range(3):
        scores = [int(data[f"s{i}_{j}"]) for j in range(5)]
        total = sum(scores)
        avg = total / 5
        lines.append(f"Student {i+1}")
        lines.append(f"#Sum {total}")
        lines.append(f"#Average {avg:.2f}")
    return {
        "output": "\n".join(lines)
    }