TITLE = "不定數迴圈（最小值）"
INPUTS = ["數列"]
INPUT_META = {
    "數列": {
        "label": "輸入多個整數（最後輸入9999結束）",
        "placeholder": "例如：29,100,948,377,-28,0,-388,9999"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入數字，輸入動作直到輸入值為9999才結束，"
    "然後找出其最小值並輸出。"
)
def solve(data: dict) -> dict:
    nums = data["數列"].split(",")
    values = []
    for n in nums:
        n = int(n.strip())
        if n == 9999:
            break
        values.append(n)
    if len(values) == 0:
        return {"output": "No data"}
    return {
        "output": str(min(values))
    }