TITLE = "數字排序"
INPUTS = [f"n{i}" for i in range(10)]
INPUT_META = {
    f"n{i}": {
        "label": f"第{i+1}個數",
        "placeholder": "請輸入整數"
    } for i in range(10)
}
OUTPUT_HINT = (
    "輸入10個數字，輸出由大到小的前3個數字。"
)
def solve(data: dict) -> dict:
    nums = [int(data[f"n{i}"]) for i in range(10)]
    # 由大到小排序
    nums.sort(reverse=True)
    # 取前三大
    result = nums[:3]
    return {
        "output": f"{result[0]} {result[1]} {result[2]}"
    }