TITLE = "字元判斷"
INPUTS = ["字元"]
INPUT_META = {
    "字元": {
        "label": "請輸入一個字元",
        "placeholder": "例如：P、a、9、$"
    }
}
OUTPUT_HINT = "(1111101)請使用選擇敘述撰寫一程式，讓使用者輸入一個字元，判斷它是包括大、小寫的英文字母（alphabet）、數字（number）、或者其它字元（symbol）。例如：a為英文字母、9為數字、$為其它字元"
def solve(data: dict) -> dict:
    s = str(data["字元"])
    # 只取第一個字元（避免使用者輸入多個字）
    if len(s) == 0:
        return {"output": "輸入是空值."}
    ch = s[0]
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        result = f"{ch} 是一個字元."
    elif '0' <= ch <= '9':
        result = f"{ch} 是一個數字."
    else:
        result = f"{ch} 是一個符號(其它字元)."
    return {
        "output": result
    }