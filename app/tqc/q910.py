TITLE = "統計男女人數"

INPUTS = ["content"]

INPUT_META = {
    "content": {
        "label": "資料內容",
        "placeholder": "每行格式：姓名 身高 性別(0女,1男)"
    }
}

OUTPUT_HINT = "輸出資料內容並統計男性與女性人數。"

def solve(data: dict) -> dict:
    content = data["content"]

    male = 0
    female = 0

    result = []

    for line in content.splitlines():
        result.append(line)

        gender = line.split()[2]

        if gender == "0":
            female += 1
        elif gender == "1":
            male += 1

    result.append(f"Number of males: {male}")
    result.append(f"Number of females: {female}")

    return {
        "output": "\n".join(result)
    }