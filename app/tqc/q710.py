TITLE = "字典搜尋"

INPUTS = [item for i in range(20) for item in (f"key{i}", f"value{i}")] + ["search"]

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
    },
    "search": {
        "label": "Search key",
        "placeholder": "請輸入要搜尋的 Key"
    }
}

OUTPUT_HINT = (
    "請建立一個字典，每筆資料包含 Key 與 Value。"
    "輸入 Key 時，若輸入 end 則結束字典輸入。"
    "接著輸入一個要搜尋的 Key，程式會判斷該 Key 是否存在於字典中，"
    "若存在輸出 True，否則輸出 False。"
)

def solve(data: dict) -> dict:
    Dict = {}

    for i in range(20):
        key = data.get(f"key{i}", "").strip()

        if key == "" or key == "end":
            break

        value = data.get(f"value{i}", "").strip()
        Dict[key] = value

    search = data.get("search", "").strip()

    return {
        "output": str(search in Dict)
    }