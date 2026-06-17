TITLE = "閏年判斷"
INPUTS = ["年份"]
OUTPUT_HINT = "請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，然後判斷它是否為閏年或平年。若輸入-9999則結束此迴圈。"
def solve(data: dict) -> dict:
    years_text = str(data["年份"]).strip()
    years = years_text.split()
    results = []
    for item in years:
        year = int(float(item))
        if year == -9999:
            break
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            results.append(f"{year} is a leap year.")
        else:
            results.append(f"{year} is not a leap year.")
    return {
        "output": "\n".join(results)
    }