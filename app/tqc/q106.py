# 114111101王大明
TITLE = "平均速度計算"
INPUTS = ["分", "秒", "公里"]
OUTPUT_HINT = "假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）。"
def solve(data: dict) -> dict:
    x = float(data["分"])  # 分
    y = float(data["秒"])  # 秒
    z = float(data["公里"])  # 公里
    # 總時間（小時）
    time_hour = (60 * x + y) / 3600
    # 公里轉英里
    mile = z / 1.6
    speed = mile / time_hour
    return {
        "output": f"平均速度 = {speed:.1f}"
    }