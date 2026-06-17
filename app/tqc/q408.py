TITLE = "奇偶數個數計算"
INPUTS = ["數列"]
INPUT_META = {
    "數列": {
        "label": "輸入10個整數",
        "placeholder": "例如：1,2,3,4,5,6,7,8,9,10"
    }
}
OUTPUT_HINT = (
    "請輸入10個整數，統計其中偶數與奇數的個數。"
)
def solve(data: dict) -> dict:
    nums = data["數列"].split(",")
    even = 0
    odd = 0
    for i in range(10):
        n = int(nums[i].strip())
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
    result = f"Even numbers: {even}\nOdd numbers: {odd}"
    return {
        "output": result
    }