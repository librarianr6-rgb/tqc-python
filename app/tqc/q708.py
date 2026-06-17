TITLE = "字典合併"

INPUTS = (
    [item for i in range(20) for item in (f"d1_key{i}", f"d1_value{i}")]
    +
    [item for i in range(20) for item in (f"d2_key{i}", f"d2_value{i}")]
)

INPUT_META = {
    **{
        f"d1_key{i}": {
            "label": f"dict1 Key {i+1}",
            "placeholder": "請輸入 Key，結束請輸入 end"
        }
        for i in range(20)
    },
    **{
        f"d1_value{i}": {
            "label": f"dict1 Value {i+1}",
            "placeholder": "請輸入 Value"
        }
        for i in range(20)
    },
    **{
        f"d2_key{i}": {
            "label": f"dict2 Key {i+1}",
            "placeholder": "請輸入 Key，結束請輸入 end"
        }
        for i in range(20)
    },
    **{
        f"d2_value{i}": {
            "label": f"dict2 Value {i+1}",
            "placeholder": "請輸入 Value"
        }
        for i in range(20)
    }
}

OUTPUT_HINT = (
    "請建立兩個字典 dict1 與 dict2，每筆資料包含 Key 與 Value。"
    "每個字典輸入 Key 時，若輸入 end 則結束該字典輸入。"
    "程式會將 dict2 合併到 dict1，若有相同 Key，dict2 的 Value 會取代 dict1 的 Value。"
    "最後依 Key 排序後，逐行輸出 key: value。"
)

def solve(data: dict) -> dict:
    def compute(prefix: str) -> dict:
        Dict = {}

        for i in range(20):
            key = data.get(f"{prefix}_key{i}", "").strip()

            if key == "" or key == "end":
                break

            value = data.get(f"{prefix}_value{i}", "").strip()
            Dict[key] = value

        return Dict

    dict1 = compute("d1")
    dict2 = compute("d2")

    dict1.update(dict2)

    results = []
    for key in sorted(dict1):
        results.append(f"{key}: {dict1[key]}")

    return {
        "output": "\n".join(results)
    }