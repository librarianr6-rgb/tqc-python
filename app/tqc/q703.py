TITLE = "數組條件判斷"
INPUTS = [f"s{i}" for i in range(20)]
INPUT_META = {
    f"s{i}": {
        "label": f"第{i+1}個字串",
        "placeholder": "輸入字串或 end 結束"
    } for i in range(20)
}
OUTPUT_HINT = (
    "請撰寫一程式，輸入一些字串至數組（至少輸入五個字串），以字串”end”為結束點（數組中不包含字串”end”）。接著輸出該數組，再分別顯示該數組的第一個元素到第三個元素和倒數三個元素。"
)
def solve(data: dict) -> dict:
    lst = []
    for i in range(20):
        s = data[f"s{i}"]
        if s == "end":
            break
        lst.append(s)
    tup = tuple(lst)
    first3 = tup[:3]
    last3 = tup[-3:]
    output = f"{tup}\n{first3}\n{last3}"
    return {
        "output": output
    }