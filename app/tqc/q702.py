TITLE = "數組合併排序"
INPUTS = [f"a{i}" for i in range(20)] + [f"b{i}" for i in range(20)]
INPUT_META = {
    **{
        f"a{i}": {
            "label": f"tuple1 第{i+1}個",
            "placeholder": "輸入數字或-9999結束"
        } for i in range(20)
    },
    **{
        f"b{i}": {
            "label": f"tuple2 第{i+1}個",
            "placeholder": "輸入數字或-9999結束"
        } for i in range(20)
    }
}
OUTPUT_HINT = (
    "請撰寫一程式，輸入並建立兩組數組，各以-9999為結束點（數組中不包含-9999）。將此兩數組合併並從小到大排序之，顯示排序前的數組和排序後的串列。"
)
def solve(data: dict) -> dict:
    list1 = []
    list2 = []
    # 讀 tuple1
    for i in range(20):
        val = int(data[f"a{i}"])
        if val == -9999:
            break
        list1.append(val)
    # 讀 tuple2
    for i in range(20):
        val = int(data[f"b{i}"])
        if val == -9999:
            break
        list2.append(val)
    # 合併
    combined = list1 + list2
    combined_tuple = tuple(combined)
    # 排序
    sorted_list = sorted(combined)
    output = (
        f"Combined tuple before sorting: {combined_tuple}\n"
        f"Combined list after sorting: {sorted_list}"
    )
    return {
        "output": output
    }