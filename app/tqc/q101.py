# 114111206_翁一
TITLE = "整數格式化輸出"

# 四個整數
INPUTS = ["整數1", "整數2", "整數3", "整數4"]

INPUT_META = {
    "整數1": {"label": "第一個整數", "placeholder": "請輸入整數 a"},
    "整數2": {"label": "第二個整數", "placeholder": "請輸入整數 b"},
    "整數3": {"label": "第三個整數", "placeholder": "請輸入整數 c"},
    "整數4": {"label": "第四個整數", "placeholder": "請輸入整數 d"},
}

OUTPUT_HINT = "請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。"

def solve(data: dict) -> dict:
    a = int(float(data["整數1"]))
    b = int(float(data["整數2"]))
    c = int(float(data["整數3"]))
    d = int(float(data["整數4"]))

    # 使用舊式 % 格式化（與題庫完全一致）
    output_text = (
        "|%5d %5d|\n" % (a, b) +
        "|%5d %5d|\n" % (c, d) +
        "|%-5d %-5d|\n" % (a, b) +
        "|%-5d %-5d|" % (c, d)
    )

    return {
        "output": output_text
    }