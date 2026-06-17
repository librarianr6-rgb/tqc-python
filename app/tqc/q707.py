TITLE = "集合運算"

INPUTS = [f"x{i}" for i in range(20)] + [f"y{i}" for i in range(20)]

INPUT_META = {
    **{
        f"x{i}": {
            "label": f"X組科目{i+1}",
            "placeholder": "請輸入科目，結束請輸入 end"
        }
        for i in range(20)
    },
    **{
        f"y{i}": {
            "label": f"Y組科目{i+1}",
            "placeholder": "請輸入科目，結束請輸入 end"
        }
        for i in range(20)
    }
}

OUTPUT_HINT = (
    "請輸入兩組科目資料 X 與 Y，每一組輸入多個科目，並以 end 表示該組輸入結束。"
    "程式會依序輸出：X與Y的聯集、交集、Y減X、對稱差集，且結果皆會排序後輸出。"
)

def solve(data: dict) -> dict:
    X = set()
    Y = set()

    # 讀取 X 組
    for i in range(20):
        subject = data.get(f"x{i}", "").strip()

        if subject == "" or subject == "end":
            break

        X.add(subject)

    # 讀取 Y 組
    for i in range(20):
        subject = data.get(f"y{i}", "").strip()

        if subject == "" or subject == "end":
            break

        Y.add(subject)

    results = [
        str(sorted(X | Y)),
        str(sorted(X & Y)),
        str(sorted(Y - X)),
        str(sorted(X ^ Y))
    ]

    return {
        "output": "\n".join(results)
    }