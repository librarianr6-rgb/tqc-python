TITLE = "迴圈數值相乘（三角形）"
INPUTS = ["n"]
INPUT_META = {
    "n": {
        "label": "整數 n",
        "placeholder": "請輸入整數（<100）"
    }
}
OUTPUT_HINT = (
    "請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數（<100），"
    "然後以三角形的方式依序輸出此數的相乘結果。"
    "提示：輸出欄寬為4，且需靠右對齊。"
)
def solve(data: dict) -> dict:
    n = int(data["n"])
    lines = []
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += f"{j * i:4d}"
        lines.append(row)
    result = "\n".join(lines)
    return {
        "output": result
    }