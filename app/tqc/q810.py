TITLE = "最大值與最小值的差"

INPUTS = ["k"] + [f"s{i}" for i in range(100)]

INPUT_META = {
    "k": {
        "label": "測試筆數",
        "placeholder": "請輸入正整數 k，1 <= k <= 100"
    },
    **{
        f"s{i}": {
            "label": f"第{i+1}筆數字",
            "placeholder": "請輸入一串數字，數字之間以空白分隔"
        }
        for i in range(100)
    }
}

OUTPUT_HINT = (
    "請先輸入正整數 k，代表有 k 筆測試資料。"
    "每一筆測試資料是一串數字，數字之間以空白分隔。"
    "程式會找出每一筆資料中最大值與最小值的差，"
    "並將結果輸出到小數點後第二位。"
)

def solve(data: dict) -> dict:
    k = int(data.get("k", 0))

    results = []

    for i in range(k):
        Str = data.get(f"s{i}", "")

        nums = [float(x) for x in Str.split()]

        diff = max(nums) - min(nums)

        results.append("%.2f" % diff)

    return {
        "output": "\n".join(results)
    }