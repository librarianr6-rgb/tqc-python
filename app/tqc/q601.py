TITLE = "偶數索引值加總"
INPUTS = [f"n{i}" for i in range(12)]
INPUT_META = {
    f"n{i}": {
        "label": f"第{i+1}個數",
        "placeholder": "請輸入1~99整數"
    } for i in range(12)
}
OUTPUT_HINT = (
    "顯示12個數（每列3個、寬度3靠右），並輸出偶數索引的總和。"
)
def solve(data: dict) -> dict:
    nums = [int(data[f"n{i}"]) for i in range(12)]
    # 偶數索引加總（0,2,4,...）
    total = sum(nums[i] for i in range(0, 12, 2))
    # 排版輸出（每列3個，寬度3，靠右）
    lines = []
    for i in range(0, 12, 3):
        line = f"{nums[i]:>3}{nums[i+1]:>3}{nums[i+2]:>3}"
        lines.append(line)
    lines.append(str(total))
    return {
        "output": "\n".join(lines)
    }