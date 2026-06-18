TITLE = "統計行數、單字數與字元數"

INPUTS = ["content"]

INPUT_META = {
    "content": {
        "label": "檔案內容",
        "placeholder": "請輸入檔案內容"
    }
}

OUTPUT_HINT = "統計行數、單字數及字元數（不含空白與換行）。"

def solve(data: dict) -> dict:
    content = data["content"]

    lines = content.splitlines()

    f_line = 0
    f_word = 0
    f_char = 0

    for line in lines:
        f_line += 1
        words = line.split()
        f_word += len(words)
        f_char += sum(len(word) for word in words)

    return {
        "output":
            f"{f_line} line(s)\n"
            f"{f_word} word(s)\n"
            f"{f_char} character(s)"
    }