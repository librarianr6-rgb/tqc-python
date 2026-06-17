TITLE = "三角形判斷"
INPUTS = ["邊長1", "邊長2", "邊長3"]
INPUT_META = {
    "邊長1": {"label": "第一邊長", "placeholder": "請輸入邊長1"},
    "邊長2": {"label": "第二邊長", "placeholder": "請輸入邊長2"},
    "邊長3": {"label": "第三邊長", "placeholder": "請輸入邊長3"},
}
OUTPUT_HINT = (
    "(1111101)請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，"
    "檢查這三個邊長是否可以組成一個三角形。"
    "若可以，則輸出該三角形之周長；否則顯示【Invalid】。"
)
def solve(data: dict) -> dict:
    side1 = float(data["邊長1"])
    side2 = float(data["邊長2"])
    side3 = float(data["邊長3"])
    if (side1 + side2 > side3 and
        side2 + side3 > side1 and
        side3 + side1 > side2):
        perimeter = side1 + side2 + side3
        result = str(perimeter)
    else:
        result = "Invalid"
    return {
        "output": result
    }