TITLE = "成績計算"
INPUTS = [f"s{i}" for i in range(10)]
INPUT_META = {
    f"s{i}": {
        "label": f"第{i+1}個成績",
        "placeholder": "請輸入成績"
    } for i in range(10)
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入十個成績，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。提示：平均值輸出到小數點後第二位。"
)
def solve(data: dict) -> dict:
    scores = [int(data[f"s{i}"]) for i in range(10)]
    scores.sort()
    total = sum(scores) - scores[0] - scores[-1]
    avg = total / 8
    return {
        "output": f"{total}\n{avg:.2f}"
    }