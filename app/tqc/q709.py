TITLE = "字典排序"

INPUTS = [item for i in range(20) for item in (f"key{i}", f"value{i}")]

INPUT_META = {
    **{
        f"key{i}": {
            "label": f"Key {i+1}",
            "placeholder": "請輸入 Key，結束請輸入 end"
        }
        for i in range(20)
    },
    **{
        f"value{i}": {
            "label": f"Value {i+1}",
            "placeholder": "請輸入 Value"
        }
        for i in range(20)
    }
}

OUTPUT_HINT = (
    "請建立一個字典，每筆資料包含 Key 與 Value。"
    "輸入 Key 時，若輸入 end 則結束輸入。"
    "程式會依照 Key 排序後，逐行輸出 key: value。"
)

def solve(data: dict) -> dict:
    color_dict = {}

    for i in range(20):
        key = data.get(f"key{i}", "").strip()

        if key == "" or key == "end":
            break

        value = data.get(f"value{i}", "").strip()
        color_dict[key] = value

    results = []

    for key in sorted(color_dict):
        results.append(f"{key}: {color_dict[key]}")

    return {
        "output": "\n".join(results)
    }