TITLE = "資料寫入檔案"

INPUTS = [f"line{i}" for i in range(5)]

INPUT_META = {
    **{
        f"line{i}": {
            "label": f"第{i+1}筆資料",
            "placeholder": "請輸入學生名字和期末總分，例如 Amy 90"
        }
        for i in range(5)
    }
}

OUTPUT_HINT = (
    "請輸入五筆資料，每一筆資料包含學生名字和期末總分，兩者以空白隔開。"
    "程式會將五筆資料寫入 q901.txt，每一筆資料為一行。"
)

def solve(data: dict) -> dict:
    f = open("q901.txt", "w", encoding="utf-8")

    for i in range(5):
        line = data.get(f"line{i}", "")
        f.write(line + "\n")

    f.close()

    return {
        "output": ""
    }