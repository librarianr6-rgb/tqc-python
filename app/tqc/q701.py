TITLE = "串列數組轉換"
INPUTS = ["數值1", "數值2", "數值3", "數值4", "數值5", "數值6", "數值7"]
OUTPUT_HINT = "請撰寫一程式，輸入數個整數並儲存至串列中，以輸入-9999為結束點（串列中不包含-9999），再將此串列轉換成數組，最後顯示該數組以及其長度（Length）、最大值（Max）、最小值（Min）、總和（Sum）"
def solve(data: dict) -> dict:
    LIST = []
    # 依序讀取輸入，遇到 -9999 即停止（不加入）
    for key in data:
        num = int(float(data[key]))
        if num == -9999:
            break
        LIST.append(num)
    TUPLE = tuple(LIST)
    output = (
        f"{TUPLE}\n"
        f"Length: {len(TUPLE)}\n"
        f"Max: {max(TUPLE)}\n"
        f"Min: {min(TUPLE)}\n"
        f"Sum: {sum(TUPLE)}"
    )
    return {
        "output": output
    }