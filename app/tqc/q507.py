TITLE = "質數判斷"
INPUTS = ["x"]
INPUT_META = {
    "x": {
        "label": "整數 x",
        "placeholder": "請輸入整數"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入一個整數x，並將x傳遞給名為compute()的函式，此函式將回傳x是否為質數（Prime number）的布林值，接著再將判斷結果輸出。如輸入值為質數顯示【Prime】，否則顯示【Not Prime】。"
)
def solve(data: dict) -> dict:
    x = int(data["x"])
    if x < 2:
        return {"output": "Not Prime"}
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return {"output": "Not Prime"}
    return {"output": "Prime"}