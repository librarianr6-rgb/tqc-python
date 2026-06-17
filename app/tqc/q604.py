TITLE = "眾數"
INPUTS = [f"n{i}" for i in range(10)]
INPUT_META = {
    f"n{i}": {
        "label": f"第{i+1}個數",
        "placeholder": "請輸入整數"
    } for i in range(10)
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入十個整數作為樣本數，輸出眾數（樣本中出現最多次的數字）及其出現的次數。"+
    "提示：假設樣本中只有一個眾數。"
)
def solve(data: dict) -> dict:
    nums = [int(data[f"n{i}"]) for i in range(10)]
    freq = {}
    # 計數
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    # 找最大出現次數
    mode = max(freq, key=freq.get)
    count = freq[mode]
    return {
        "output": f"{mode}\n{count}"
    }