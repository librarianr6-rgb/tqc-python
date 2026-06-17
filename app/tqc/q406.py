TITLE = "不定數迴圈－BMI 計算"
INPUTS = ["資料序列"]
INPUT_META = {
    "資料序列": {
        "label": "輸入身高(cm)、體重(kg)，以 -9999 結束",
        "placeholder": "例如：176,80,170,100,-9999"
    }
}
OUTPUT_HINT = (
    "請使用不定數迴圈輸入身高與體重，計算 BMI 並判斷狀態："+
    "BMI < 18.5 → under weight，"+
    "18.5 <= BMI < 25 → normal，"+
    "25 <= BMI < 30 → over weight，"+
    "BMI >= 30 → fat。"
)
def solve(data: dict) -> dict:
    nums = data["資料序列"].split(",")
    lines = []
    i = 0
    while i < len(nums):
        cm = float(nums[i].strip())
        if cm == -9999:
            break
        kg = float(nums[i + 1].strip())
        i += 2
        bmi = kg / (cm / 100) ** 2
        lines.append(f"BMI: {bmi:.2f}")
        if bmi >= 30:
            lines.append("State: fat")
        elif bmi >= 25:
            lines.append("State: over weight")
        elif bmi >= 18.5:
            lines.append("State: normal")
        else:
            lines.append("State: under weight")
    result = "\n".join(lines)
    return {
        "output": result
    }