TITLE = "最大最小值索引"
INPUTS = [f"n{i}" for i in range(9)]
INPUT_META = {
    f"n{i}": {
        "label": f"第{i+1}個數",
        "placeholder": "請輸入整數"
    } for i in range(9)
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者建立一個3*3的矩陣，其內容為從鍵盤輸入的整數（不重複），接著輸出矩陣最大值與最小值的索引。"
)
def solve(data: dict) -> dict:
    nums = [int(data[f"n{i}"]) for i in range(9)]
    # 最大值
    max_val = max(nums)
    max_idx = nums.index(max_val)
    max_row = max_idx // 3
    max_col = max_idx % 3
    # 最小值
    min_val = min(nums)
    min_idx = nums.index(min_val)
    min_row = min_idx // 3
    min_col = min_idx % 3
    output = (
        f"Index of the largest number {max_val} is: ({max_row}, {max_col})\n"
        f"Index of the smallest number {min_val} is: ({min_row}, {min_col})"
    )
    return {
        "output": output
    }