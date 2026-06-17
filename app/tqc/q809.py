TITLE = "密碼檢查"

INPUTS = ["password"]

INPUT_META = {
    "password": {
        "label": "密碼",
        "placeholder": "請輸入密碼"
    }
}

OUTPUT_HINT = (
    "請輸入一個密碼字串，程式會檢查是否符合以下規則："
    "至少八個字元、只包含英文字母和數字、至少有一個大寫英文字母。"
    "若符合規則，輸出 Valid password；否則輸出 Invalid password。"
)

def solve(data: dict) -> dict:
    password = data.get("password", "")

    # a. 必須至少八個字元
    rule1 = len(password) >= 8

    # b. 只包含英文字母和數字
    rule2 = True
    for ch in password:
        if not (
            "A" <= ch <= "Z" or
            "a" <= ch <= "z" or
            "0" <= ch <= "9"
        ):
            rule2 = False
            break

    # c. 至少要有一個大寫英文字母
    rule3 = False
    for ch in password:
        if "A" <= ch <= "Z":
            rule3 = True
            break

    if rule1 and rule2 and rule3:
        result = "Valid password"
    else:
        result = "Invalid password"

    return {
        "output": result
    }