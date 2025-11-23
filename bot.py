import os
import requests
from datetime import date

# --- [여기만 수정하면 됩니다] ---
START_DATE = date(1997, 4, 7) # 목표 시작 날짜 (년, 월, 일)
# -----------------------------

def send_message():
    # 1. GitHub 비밀 금고에서 열쇠 꺼내기
    token = os.environ.get('APP_TOKEN')
    chat_id = os.environ.get('MY_ID')

    if not token or not chat_id:
        print("토큰이나 아이디가 없습니다! Settings에서 설정을 확인해주세요.")
        return

    # 2. 날짜 계산 (오늘 날짜 - 시작 날짜)
    today = date.today()
    d_day = (today - START_DATE).days + 1
    year = today.year
    end_of_year = date(year, 12, 31)
    days_left = (end_of_year - today).days # 오늘부터 남은 일수
    total_days_in_year = (end_of_year - date(year, 1, 1)).days + 1 # 올해의 총 일수
    day_of_year = (today - date(year, 1, 1)).days + 1 # 오늘이 올해에서 몇 번째 날인지

    # 3. 보낼 메시지 내용 (원하는 대로 수정하세요)
    # \n은 '줄바꿈'입니다.
    message_text = f"Lv: {d_day:,} / 36,525 ({round(d_day*100/36525)}%)\n" \
                   f"Days left : {days_left} ({day_of_year}, {round(day_of_year*100/total_days_in_year)}%)\n" \
                   f"Todays left : {2097 - today.year:,}\n" \

    # 4. 텔레그램으로 전송
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message_text}
    
    response = requests.post(url, data=data)
    # print("메시지 전송 결과:", response.json())

if __name__ == "__main__":
    send_message()
