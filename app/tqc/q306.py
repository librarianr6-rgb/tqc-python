TITLE = "迴圈整數連乘"
INPUTS = ["整數n"]
OUTPUT_HINT = "請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數n，利用迴圈計算並輸出n!的值。例如：輸入n=15，則輸出結果為1307674368000。"
def solve(data: dict) -> dict:
    n = int(float(data["整數n"]))
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return {
        "output": str(ans)
    }