TITLE = "數字反轉判斷"
INPUTS = ["數字"]
INPUT_META = {
    "數字": {
        "label": "正整數",
        "placeholder": "請輸入正整數（輸入 0 則輸出 0）"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入一個正整數，"
    "將此正整數以反轉的順序輸出，並判斷如輸入為 0，則輸出為 0。"
)
def solve(data: dict) -> dict:
    n = data["數字"].strip()
    if n == "0":
        return {
            "output": "0"
        }
    return {
        "output": n[::-1]
    }