TITLE = "最小值"
INPUTS = ["數值1", "數值2", "數值3", "數值4", "數值5",
          "數值6", "數值7", "數值8", "數值9", "數值10"]
OUTPUT_HINT = "請撰寫一程式，由使用者輸入十個數字，然後找出其最小值，最後輸出最小值"
def solve(data: dict) -> dict:
    nums = [
        float(data["數值1"]),
        float(data["數值2"]),
        float(data["數值3"]),
        float(data["數值4"]),
        float(data["數值5"]),
        float(data["數值6"]),
        float(data["數值7"]),
        float(data["數值8"]),
        float(data["數值9"]),
        float(data["數值10"]),
    ]
    return {
        "output": str(min(nums))
    }