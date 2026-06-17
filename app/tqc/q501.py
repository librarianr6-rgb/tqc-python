TITLE = "訊息顯示"
INPUTS = ["系別", "學號", "姓名"]
OUTPUT_HINT = "請撰寫一程式，呼叫函式compute()，該函式功能為讓使用者輸入系別（Department）、學號（Student ID）和姓名（Name）並顯示這些訊息"
def solve(data: dict) -> dict:
    department = data["系別"]
    studentid = data["學號"]
    name = data["姓名"]
    output = (
        f"Department: {department}\n"
        f"Student ID: {studentid}\n"
        f"Name: {name}"
    )
    return {
        "output": output
    }