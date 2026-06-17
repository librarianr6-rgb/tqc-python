TITLE = "費氏數列"
INPUTS = ["num"]
INPUT_META = {
    "num": {
        "label": "整數 num",
        "placeholder": "請輸入 num (>=2)"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數num (num>=2)，並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。"
)
def solve(data: dict) -> dict:
    num = int(data["num"])
    # 建立費氏數列
    F = [0, 1]
    for i in range(2, num):
        F.append(F[i-1] + F[i-2])
    # 轉成字串輸出
    output = " ".join(str(x) for x in F)
    return {
        "output": output
    }