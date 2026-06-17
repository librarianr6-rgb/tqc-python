TITLE = "平均溫度"
INPUTS = [f"t{i}" for i in range(12)]
INPUT_META = {
    f"t{i}": {
        "label": f"第{i+1}筆溫度",
        "placeholder": "請輸入溫度"
    } for i in range(12)
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入四週各三天的溫度，接著計算並輸出這四週的平均溫度及最高、最低溫度。提示1：平均溫度輸出到小數點後第二位。提示2：最高溫度及最低溫度的輸出，如為31時，則輸出31，如為31.1時，則輸出31.1。"
)
def solve(data: dict) -> dict:
    temps = [float(data[f"t{i}"]) for i in range(12)]
    avg = sum(temps) / 12
    highest = max(temps)
    lowest = min(temps)
    # 處理整數顯示（31.0 → 31）
    def fmt(x):
        return str(int(x)) if x.is_integer() else str(x)
    output = (
        f"Average: {avg:.2f}\n"
        f"Highest: {fmt(highest)}\n"
        f"Lowest: {fmt(lowest)}"
    )
    return {
        "output": output
    }