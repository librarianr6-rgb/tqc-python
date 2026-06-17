TITLE = "分數對照GPA"
INPUTS = ["分數"]
OUTPUT_HINT = "請撰寫一程式，讓使用者以不定數迴圈的方式輸入一個正整數（代表分數），之後根據分數對照GPA的對照表，印出其所對應的GPA。假設此不定數迴圈輸入-9999則會結束此迴圈。"
def solve(data: dict) -> dict:
    scores_text = str(data["分數"]).strip()
    scores = scores_text.split()
    results = []
    for item in scores:
        n = int(float(item))
        if n == -9999:
            break
        elif n >= 90:
            results.append("A")
        elif n >= 80:
            results.append("B")
        elif n >= 70:
            results.append("C")
        elif n >= 60:
            results.append("D")
        else:
            results.append("E")
    return {
        "output": "\n".join(results)
    }