TITLE = "數字反轉"
INPUTS = ["n"]
INPUT_META = {
    "n": {
        "label": "正整數",
        "placeholder": "請輸入一個正整數"
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者輸入一個正整數，"
    "將此數值以反轉的順序輸出。"
)
def solve(data: dict) -> dict:
    n = str(data["n"])   # 用字串方式處理
    reversed_n = n[::-1]  # 切片反轉
    return {
        "output": reversed_n
    }