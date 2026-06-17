# 114111206_翁一
TITLE = "字串格式化輸出"
# 四個字串
INPUTS = ["字串1", "字串2", "字串3", "字串4"]
INPUT_META = {
    "字串1": {"label": "第一個字串", "placeholder": "請輸入字串 a"},
    "字串2": {"label": "第二個字串", "placeholder": "請輸入字串 b"},
    "字串3": {"label": "第三個字串", "placeholder": "請輸入字串 c"},
    "字串4": {"label": "第四個字串", "placeholder": "請輸入字串 d"},
}
OUTPUT_HINT = "請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。"
def solve(data: dict) -> dict:
    a = str(data["字串1"])
    b = str(data["字串2"])
    c = str(data["字串3"])
    d = str(data["字串4"])
    # 使用舊式 % 格式化，完全對齊題庫
    output_text = (
        "|%10s %10s|\n" % (a, b) +
        "|%10s %10s|\n" % (c, d) +
        "|%-10s %-10s|\n" % (a, b) +
        "|%-10s %-10s|" % (c, d)
    )
    return {
        "output": output_text
    }