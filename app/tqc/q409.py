TITLE = "投票統計"
INPUTS = ["投票結果"]
OUTPUT_HINT = "某次選舉有兩位候選人，分別是No.1: Nami、No.2: Chopper。請撰寫一程式，輸入五張選票，輸入值如為1即表示針對1號候選人投票；輸入值如為2即表示針對2號候選人投票。如輸入其他值則視為廢票。每次投完後需印出目前每位候選人的得票數，最後印出最高票者為當選人；如最終計算有相同最高票數者或無法選出最高票者，顯示「=> No one won the election.」。"
def solve(data: dict) -> dict:
    votes_text = str(data["投票結果"]).strip()
    votes = votes_text.split()
    Nami = 0
    Chopper = 0
    null = 0
    results = []
    for item in votes[:5]:
        n = int(float(item))
        if n == 1:
            Nami += 1
        elif n == 2:
            Chopper += 1
        else:
            null += 1
        results.append(f"Total votes of No.1: Nami = {Nami}")
        results.append(f"Total votes of No.2: Chopper = {Chopper}")
        results.append(f"Total null votes = {null}")
    if Nami > Chopper:
        results.append("=> No.1 Nami won the election.")
    elif Chopper > Nami:
        results.append("=> No.2 Chopper won the election.")
    else:
        results.append("=> No one won the election.")
    return {
        "output": "\n".join(results)
    }