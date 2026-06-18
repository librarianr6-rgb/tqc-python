TITLE = "找出指定出現次數的單字"

INPUTS = ["content", "n"]

INPUT_META = {
    "content": {
        "label": "文字內容",
        "placeholder": "請輸入文字資料"
    },
    "n": {
        "label": "出現次數",
        "placeholder": "請輸入整數"
    }
}

OUTPUT_HINT = "輸出所有出現次數剛好等於 n 的單字，依字母順序排列。"

def solve(data: dict) -> dict:
    content = data["content"]
    n = int(data["n"])

    count_dict = {}

    for line in content.splitlines():
        for word in line.split():
            count_dict[word] = count_dict.get(word, 0) + 1

    result = []

    for word in count_dict:
        if count_dict[word] == n:
            result.append(word)

    result.sort()

    return {
        "output": "\n".join(result)
    }