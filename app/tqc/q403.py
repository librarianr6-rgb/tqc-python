TITLE = "倍數總和計算（4或9的倍數）"
INPUTS = ["a", "b"]
INPUT_META = {
    "a": {
        "label": "起始整數 a",
        "placeholder": "請輸入整數 a（a <= b）"
    },
    "b": {
        "label": "結束整數 b",
        "placeholder": "請輸入整數 b（a <= b）"
    }
}
OUTPUT_HINT = (
    "請輸出 a 到 b 之間所有 4 或 9 的倍數（每列10個，欄寬4靠左對齊），"
    "並輸出倍數個數與總和。"
)
def solve(data: dict) -> dict:
    a = int(data["a"])
    b = int(data["b"])
    nums = []
    for i in range(a, b + 1):
        if i % 4 == 0 or i % 9 == 0:
            nums.append(i)
    lines = []
    row = ""
    for idx, val in enumerate(nums, start=1):
        row += f"{val:<4d}"
        if idx % 10 == 0:
            lines.append(row.rstrip())
            row = ""
    if row:
        lines.append(row.rstrip())
    count = len(nums)
    total = sum(nums)
    lines.append(str(count))
    lines.append(str(total))
    result = "\n".join(lines)
    return {
        "output": result
    }