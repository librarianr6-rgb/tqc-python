TITLE = "社會安全碼檢查"

INPUTS = ["s"]

INPUT_META = {
    "s": {
        "label": "SSN",
        "placeholder": "請輸入社會安全碼，例如 123-45-6789"
    }
}

OUTPUT_HINT = (
    "請輸入一組社會安全碼 SSN，格式中可使用 - 分隔。"
    "程式會將字串依 - 切割，並檢查每一段是否皆為數字。"
    "若每一段都是數字，輸出 Valid SSN；否則輸出 Invalid SSN。"
)

def solve(data: dict) -> dict:
    Str = data.get("s", "")

    List = Str.split("-")

    for i in List:
        if not i.isdigit():
            return {
                "output": "Invalid SSN"
            }

    return {
        "output": "Valid SSN"
    }