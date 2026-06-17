TITLE = "矩陣相加"
INPUTS = [
    "a11", "a12", "a21", "a22",
    "b11", "b12", "b21", "b22"
]
INPUT_META = {
    "a11": {"label": "Matrix 1 [1,1]", "placeholder": "請輸入整數"},
    "a12": {"label": "Matrix 1 [1,2]", "placeholder": "請輸入整數"},
    "a21": {"label": "Matrix 1 [2,1]", "placeholder": "請輸入整數"},
    "a22": {"label": "Matrix 1 [2,2]", "placeholder": "請輸入整數"},
    "b11": {"label": "Matrix 2 [1,1]", "placeholder": "請輸入整數"},
    "b12": {"label": "Matrix 2 [1,2]", "placeholder": "請輸入整數"},
    "b21": {"label": "Matrix 2 [2,1]", "placeholder": "請輸入整數"},
    "b22": {"label": "Matrix 2 [2,2]", "placeholder": "請輸入整數"}
}
OUTPUT_HINT = (
    "請撰寫一程式，讓使用者建立兩個2*2的矩陣，其內容為從鍵盤輸入的整數，接著輸出這兩個矩陣的內容以及它們相加的結果。"
)
def solve(data: dict) -> dict:
    matrix1 = [
        [int(data["a11"]), int(data["a12"])],
        [int(data["a21"]), int(data["a22"])]
    ]
    matrix2 = [
        [int(data["b11"]), int(data["b12"])],
        [int(data["b21"]), int(data["b22"])]
    ]
    result = [
        [matrix1[0][0] + matrix2[0][0], matrix1[0][1] + matrix2[0][1]],
        [matrix1[1][0] + matrix2[1][0], matrix1[1][1] + matrix2[1][1]]
    ]
    lines = []
    lines.append("Matrix 1:")
    for row in matrix1:
        lines.append(f"{row[0]} {row[1]}")
    lines.append("Matrix 2:")
    for row in matrix2:
        lines.append(f"{row[0]} {row[1]}")
    lines.append("Sum of 2 matrices:")
    for row in result:
        lines.append(f"{row[0]} {row[1]}")
    return {
        "output": "\n".join(lines)
    }