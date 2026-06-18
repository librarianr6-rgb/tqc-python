TITLE = "二進位檔案寫入與讀取"

INPUTS = ["content"]

INPUT_META = {
    "content": {
        "label": "5筆資料",
        "placeholder": "每行一筆資料"
    }
}

OUTPUT_HINT = "模擬將資料以 UTF-8 編碼寫入二進位檔，再讀出顯示。"

def solve(data: dict) -> dict:
    lines = data["content"].splitlines()

    binary_data = b""

    for line in lines[:5]:
        binary_data += (line + "\n").encode("utf-8")

    result = ["The content of \"data.dat\":"]

    for line in binary_data.decode("utf-8").splitlines():
        result.append(line)

    return {
        "output": "\n".join(result)
    }