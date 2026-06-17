TITLE = "數字總和與平均"

INPUTS = ["s"]

INPUT_META = {
    "s": {
        "label": "數字字串",
        "placeholder": "請輸入多個整數，數字之間以空白分隔"
    }
}

OUTPUT_HINT = (
    "請輸入多個整數，數字之間以空白分隔。"
    "程式會計算這些整數的總和與平均，並輸出結果。"
)

def solve(data: dict) -> dict:
    Str = data.get("s", "")

    List = [int(i) for i in Str.split()]

    total = sum(List)
    average = total / len(List)

    results = [
        "Total = %d" % total,
        "Average = %.1f" % average
    ]

    return {
        "output": "\n".join(results)
    }