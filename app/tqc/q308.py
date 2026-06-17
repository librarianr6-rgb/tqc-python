TITLE = "迴圈位數加總"
INPUTS = ["筆數", "數列"]
INPUT_META = {
    "筆數": {
        "label": "測試資料筆數",
        "placeholder": "請輸入測試資料數量"
    },
    "數列": {
        "label": "測試整數（每行一筆）",
        "placeholder": "請輸入多個整數，用逗號分隔，例如：98765,32412,0"
    }
}
OUTPUT_HINT = (
    "請使用迴圈敘述撰寫一程式，讓使用者輸入一個數字，"
    "此數字代表後面測試資料的數量。每一筆測試資料是一個正整數，"
    "將此正整數的每個數字全部加總起來。"
)
def solve(data: dict) -> dict:
    count = int(data["筆數"])
    # 取得輸入數列（用逗號分隔）
    numbers = data["數列"].split(",")
    lines = []
    for i in range(count):
        num = int(numbers[i].strip())
        temp = num
        ans = 0
        while temp != 0:
            ans += temp % 10
            temp //= 10
        lines.append(f"Sum of all digits of {num} is {ans}")
    result = "\n".join(lines)
    return {
        "output": result
    }