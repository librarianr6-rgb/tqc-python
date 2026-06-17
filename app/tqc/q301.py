TITLE = "迴圈整數連加"
INPUTS = ["起始值", "結束值"]
OUTPUT_HINT = "請使用迴圈敘述撰寫一程式，讓使用者輸入兩個正整數a、b（a < b），利用迴圈計算從a開始連加到b的總和。例如：輸入a=1、b=100，則輸出結果為5050（1 + 2 + … + 100 = 5050）"
def solve(data: dict) -> dict:
    a = int(float(data["起始值"]))
    b = int(float(data["結束值"]))
    total = 0
    for i in range(a, b + 1):
        total += i
    return {
        "output": str(total)
    }