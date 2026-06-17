TITLE = "撲克牌總和"
INPUTS = ["牌1", "牌2", "牌3", "牌4", "牌5"]
OUTPUT_HINT = "請撰寫一程式，讓使用者輸入52張牌中的5張，計算並輸出其總和。（J=11, Q=12, K=13, A=1）"
def solve(data: dict) -> dict:
    total = 0
    cards = [
        data["牌1"],
        data["牌2"],
        data["牌3"],
        data["牌4"],
        data["牌5"],
    ]
    for n in cards:
        n = str(n)
        if n == "J":
            total += 11
        elif n == "Q":
            total += 12
        elif n == "K":
            total += 13
        elif n == "A":
            total += 1
        else:
            total += int(n)
    return {
        "output": str(total)
    }
