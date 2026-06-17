TITLE = "子集合與超集合"
INPUTS = (
    [f"a{i}" for i in range(5)] +
    [f"b{i}" for i in range(3)] +
    [f"c{i}" for i in range(9)]
)
INPUT_META = {
    **{f"a{i}": {"label": f"set1 第{i+1}個", "placeholder": "請輸入整數"} for i in range(5)},
    **{f"b{i}": {"label": f"set2 第{i+1}個", "placeholder": "請輸入整數"} for i in range(3)},
    **{f"c{i}": {"label": f"set3 第{i+1}個", "placeholder": "請輸入整數"} for i in range(9)},
}
OUTPUT_HINT = (
    "請撰寫一程式，依序輸入五個、三個、九個整數，並各自儲存到集合set1、set2、set3中。接著回答：set2是否為set1的子集合（subset）？set3是否為set1的超集合（superset）？"
)
def solve(data: dict) -> dict:
    set1 = {int(data[f"a{i}"]) for i in range(5)}
    set2 = {int(data[f"b{i}"]) for i in range(3)}
    set3 = {int(data[f"c{i}"]) for i in range(9)}
    result1 = set2.issubset(set1)
    result2 = set3.issuperset(set1)
    output = (
        f"set2 is subset of set1: {result1}\n"
        f"set3 is superset of set1: {result2}"
    )
    return {
        "output": output
    }