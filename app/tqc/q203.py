TITLE = "閏年判斷"
INPUTS = ["年份"]
OUTPUT_HINT = "(114111101)請使用選擇敘述撰寫一程式，讓使用者輸入一個西元年份，然後判斷它是否為閏年（leap year）或平年。其判斷規則為：每四年一閏，每百年不閏，但每四百年也一閏"
def solve(data: dict) -> dict:
    n = int(float(data["年份"]))  # 輸入年份
    if n % 4 == 0 and (n % 400 == 0 or n % 100 != 0):
        result = f"{n} 是閏年."
    else:
        result = f"{n} 不是閏年."
    return {
        "output": result
    }