TITLE = "集合條件判斷"
INPUTS = [f"n{i}" for i in range(20)]
INPUT_META = {
    f"n{i}": {
        "label": f"第{i+1}個數",
        "placeholder": "輸入整數或-9999結束"
    } for i in range(20)
}
OUTPUT_HINT = (
    "請撰寫一程式，輸入數個整數並儲存至集合，以輸入-9999為結束點（集合中不包含-9999），最後顯示該集合的長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）。"
)
def solve(data: dict) -> dict:
    s = set()
    for i in range(20):
        val = int(data[f"n{i}"])
        if val == -9999:
            break
        s.add(val)
    output = (
        f"Length: {len(s)}\n"
        f"Max: {max(s)}\n"
        f"Min: {min(s)}\n"
        f"Sum: {sum(s)}"
    )
    return {
        "output": output
    }