TITLE = "全字母句"
INPUTS = ["k"] + [f"s{i}" for i in range(20)]
INPUT_META = {
    "k": {"label": "測試筆數", "placeholder": "請輸入整數"},
    **{
        f"s{i}": {"label": f"句子{i+1}", "placeholder": "請輸入句子"}
        for i in range(20)
    }
}
OUTPUT_HINT = (
    "全字母句（Pangram）是英文字母表所有的字母都出現至少一次（最好只出現一次）的句子。請撰寫一程式，要求使用者輸入一正整數k（代表有k筆測試資料），每一筆測試資料為一句子，程式判斷該句子是否為Pangram，並印出對應結果True（若是）或False（若不是）。"
)
def solve(data: dict) -> dict:
    k = int(data["k"])
    results = []
    for i in range(k):
        s = data[f"s{i}"].lower()
        # 只保留英文字母
        letters = {ch for ch in s if ch.isalpha()}
        results.append(str(len(letters) == 26))
    return {
        "output": "\n".join(results)
    }