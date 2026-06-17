TITLE = "依參數格式化輸出"
INPUTS = ["a", "x", "y"]
INPUT_META = {
    "a": {
        "label": "字元 a",
        "placeholder": "請輸入字元"
    },
    "x": {
        "label": "每列數量 x",
        "placeholder": "請輸入整數 x"
    },
    "y": {
        "label": "列數 y",
        "placeholder": "請輸入整數 y"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，將使用者輸入的三個參數，變數名稱分別為a（代表字元character）、x（代表個數）、y（代表列數），作為參數傳遞給一個名為compute()的函式，該函式功能為：一列印出x個a字元，總共印出y列。提示：輸出的每一個字元後方有一空格。"
)
def solve(data: dict) -> dict:
    a = data["a"]
    x = int(data["x"])
    y = int(data["y"])
    lines = []
    for i in range(y):
        line = (a + " ") * x
        lines.append(line.rstrip())  # 去掉最後一個空格
    return {
        "output": "\n".join(lines)
    }