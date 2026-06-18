TITLE = "身高體重統計"

INPUTS = ["s"]

INPUT_META = {
    "s": {
        "label": "資料內容",
        "placeholder": "每行格式：姓名 身高 體重"
    }
}

OUTPUT_HINT = "計算平均身高、平均體重、最高者與最重者。"

def solve(data: dict) -> dict:
    rows = [line.split() for line in data["s"].strip().split("\n")]

    name = [row[0] for row in rows]
    height = [float(row[1]) for row in rows]
    weight = [float(row[2]) for row in rows]

    result = []
    result.append("Average height: %.2f" % (sum(height) / len(height)))
    result.append("Average weight: %.2f" % (sum(weight) / len(weight)))
    result.append(
        "The tallest is %s with %.2fcm"
        % (name[height.index(max(height))], max(height))
    )
    result.append(
        "The heaviest is %s with %.2fkg"
        % (name[weight.index(max(weight))], max(weight))
    )

    return {
        "output": "\n".join(result)
    }