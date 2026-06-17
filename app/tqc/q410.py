TITLE = "繪製等腰三角形"
INPUTS = ["n"]
INPUT_META = {
    "n": {
        "label": "三角形高度",
        "placeholder": "請輸入正整數，例如 7"
    }
}
OUTPUT_HINT = (
    "請依照輸入的 n，繪製對應的等腰三角形（由 * 組成）。"
)
def solve(data: dict) -> dict:
    n = int(data["n"])
    lines = []
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (i * 2 + 1)
        lines.append(spaces + stars)
    result = "\n".join(lines)
    return {
        "output": result
    }