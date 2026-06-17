# 114111101王大明
TITLE = "浮點數格式化輸出"
# 四個浮點數
INPUTS = ["浮點數1", "浮點數2", "浮點數3", "浮點數4"]
INPUT_META = {
    "浮點數1": {"label": "第一個浮點數", "placeholder": "請輸入浮點數 a"},
    "浮點數2": {"label": "第二個浮點數", "placeholder": "請輸入浮點數 b"},
    "浮點數3": {"label": "第三個浮點數", "placeholder": "請輸入浮點數 c"},
    "浮點數4": {"label": "第四個浮點數", "placeholder": "請輸入浮點數 d"},
}
OUTPUT_HINT = "請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。"
def solve(data: dict) -> dict:
    a = float(data["浮點數1"])
    b = float(data["浮點數2"])
    c = float(data["浮點數3"])
    d = float(data["浮點數4"])
    # 使用舊式 % 格式化，完全對齊題庫
    output_text = (
        "|%7.2f %7.2f|\n" % (a, b) +
        "|%7.2f %7.2f|\n" % (c, d) +
        "|%-7.2f %-7.2f|\n" % (a, b) +
        "|%-7.2f %-7.2f|" % (c, d)
    )
    return {
        "output": output_text
    }
