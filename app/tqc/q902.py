TITLE = "讀取檔案數字加總"

INPUTS = []

INPUT_META = {}

OUTPUT_HINT = (
    "程式會讀取 q902.txt 的內容，內容為多個以空白分隔的數字，"
    "將這些數字加總後輸出。檔案讀取完成後會關閉。"
)

def solve(data: dict) -> dict:
    f = open("q902.txt", "r", encoding="utf-8")

    content = f.read()

    f.close()

    nums = [int(i) for i in content.split()]

    total = sum(nums)

    return {
        "output": str(total)
    }