TITLE = "算術運算"
INPUTS = ["a", "b", "運算子"]
OUTPUT_HINT = "(1111101)請使用選擇敘述撰寫一程式，讓使用者輸入兩個整數a、b，然後再輸入一算術運算子 (+、-、*、/、//、%） ，輸出經過運算後的結果"
def solve(data: dict) -> dict:
    a = float(data["a"])
    b = float(data["b"])
    c = str(data["運算子"])
    if c == "+":
        result = a + b
    elif c == "-":
        result = a - b
    elif c == "*":
        result = a * b
    elif c == "/":
        result = a / b
    elif c == "//":
        result = a // b
    elif c == "%":
        result = a % b
    else:
        result = "無效運算子"
    return {
        "output": str(result)
    }