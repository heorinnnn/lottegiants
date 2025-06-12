import requests
from bs4 import BeautifulSoup
from datetime import datetime
import webbrowser # 웹 브라우저를 열기 위한 모듈

def show_kbo_intro():
    """KBO에 대한 간략한 소개를 출력합니다."""
    print("\n[KBO란?]")
    print("KBO는 'Korea Baseball Organization'의 약자로, 한국 프로야구를 총괄하는 기구입니다.")

def show_kbo_teams():
    """KBO 소속 구단 목록과 연고지를 출력합니다."""
    print("\n[KBO 소속 구단 목록 (구단 - 지역)]")
    teams = {
        "SSG 랜더스": "인천",
        "LG 트윈스": "서울",
        "두산 베어스": "서울",
        "KT 위즈": "수원",
        "삼성 라이온즈": "대구",
        "롯데 자이언츠": "부산",
        "기아 타이거즈": "광주",
        "한화 이글스": "대전",
        "NC 다이노스": "창원",
        "키움 히어로즈": "고척(서울)"
    }
    for team, city in teams.items():
        print(f"{team} - {city}")

def show_team_websites():
    """KBO 구단별 공식 홈페이지 링크를 출력합니다."""
    print("\n[KBO 구단별 홈페이지 (구단 - 링크)]")
    websites = {
        "SSG 랜더스": "https://www.ssglanders.com",
        "LG 트윈스": "https://www.lgtwins.com",
        "두산 베어스": "https://www.doosanbears.com",
        "KT 위즈": "https://www.ktwiz.co.kr",
        "삼성 라이온즈": "https://www.samsunglions.com",
        "롯데 자이언츠": "https://www.giantsclub.com",
        "기아 타이거즈": "https://www.tigers.co.kr",
        "한화 이글스": "https://www.hanwhaeagles.co.kr",
        "NC 다이노스": "https://www.ncdinos.com",
        "키움 히어로즈": "https://www.heroesbaseball.co.kr"
    }
    for team, url in websites.items():
        print(f"{team} - {url}")

def display_kbo_info_menu():
    """KBO 정보 메뉴 옵션을 출력합니다."""
    print("\n[KBO 정보]")
    print("1-1. KBO란?")
    print("1-2. KBO 구단 목록")
    print("1-3. KBO 구단 홈페이지")


def show_lottegiants_info():
    """롯데 자이언츠에 대한 간략한 소개를 출력합니다."""
    print("\n[롯데 자이언츠 소개]")
    print("1982년 창단된 롯데 자이언츠는 부산을 연고로 한 KBO 프로야구 구단입니다.")
    print("두 차례(1984, 1992) 한국시리즈 우승 경험이 있으며, 열정적인 팬덤과 사직야구장으로 유명합니다.")

def show_lottegiants_achievements():
    """롯데 자이언츠의 주요 성과를 출력합니다."""
    print("\n[롯데 자이언츠 주요 성과]")
    print("1984년: 후기리그 우승 및 한국시리즈 첫 우승 달성.")
    print("1992년: 정규시즌 3위에서 한국시리즈 우승.")
    print("1995년 / 1999년: 한국시리즈 준우승.")
    print("2008~2012년: 5년 연속 포스트시즌 진출.")
    print("2017년: 준플레이오프 진출.")

def show_pitchers():
    """롯데 자이언츠 투수 명단을 출력합니다."""
    print("\n[투수 명단]")
    print("No.15 김진욱, No.19 김강현, No.22 구승민, No.24 김상수, No.32 감보아, No.34 김원중")
    print("No.66 김태현, No.101 김현우, No.107 김태균, No.124 김도규, No.125 박세현")
    print("No.126 이영재, No.127 조영우, No.128 진승현, No.129 정성종, No.130 정현수")
    print("No.131 박진, No.132 박진형, No.133 심재민, No.134 박시영, No.135 최이준")
    print("No.136 이승헌, No.137 전미르, No.138 이민석, No.139 송재영, No.140 정우준")
    print("No.141 윤성빈, No.142 박영완, No.143 홍민기, No.144 박로건, No.145 하혜성")

def show_catchers():
    """롯데 자이언츠 포수 명단을 출력합니다."""
    print("\n[포수 명단]")
    print("No.20 정보근, No.27 윤태현, No.44 강태율, No.146 유강남")
    print("No.147 백두산, No.148 박건우, No.149 박재엽, No.150 손성빈")

def show_infielders():
    """롯데 자이언츠 내야수 명단을 출력합니다."""
    print("\n[내야수 명단]")
    print("No.1 김민수, No.3 한동희, No.5 노진혁, No.8 정훈, No.13 황성빈")
    print("No.38 안치홍, No.96 조세진, No.99 이학주, No.151 나승엽, No.152 고승민")
    print("No.153 손호영, No.154 박승욱, No.155 한태양, No.156 전민재, No.157 이호준, No.158 최민규")

def show_outfielders():
    """롯데 자이언츠 외야수 명단을 출력합니다."""
    print("\n[외야수 명단]")
    print("No.7 전준우, No.9 김주현, No.17 나승엽, No.53 고승민, No.97 윤민석")
    print("No.159 레이예스, No.160 윤동희, No.161 김동현, No.162 한승현")

def display_lottegiants_roster_menu():
    """롯데 자이언츠 선수단 메뉴 옵션을 출력합니다."""
    print("\n[롯데 자이언츠 선수단]")
    print("4-1. 투수")
    print("4-2. 포수")
    print("4-3. 내야수")
    print("4-4. 외야수")

def show_kbo_top10():
    """현재 날짜 기준으로 KBO 실시간 순위 TOP 10을 스크래핑하여 출력합니다."""
    today = datetime.today()
    weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    day_of_week = weekdays[today.weekday()]
    formatted_date = today.strftime(f"%m월 %d일 {day_of_week}")
    print(f"\n[{formatted_date}] 실시간 KBO 순위")
    url = "https://www.koreabaseball.com/record/teamrank/teamrankdaily.aspx"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="tData")
        if table:
            rows = table.find_all("tr")[1:]
            for i, row in enumerate(rows[:10]):
                cols = row.find_all("td")
                if cols:
                    team = cols[1].get_text(strip=True)
                    print(f"{i+1}등 {team}")
        else:
            print("⚠️ 순위 테이블을 찾을 수 없습니다. 웹사이트 구조가 변경되었을 수 있습니다.")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ 웹사이트에 연결할 수 없습니다. 인터넷 연결을 확인해주세요: {e}")
    except Exception as e:
        print(f"⚠️ 순위 정보를 불러오는 중 예상치 못한 오류가 발생했습니다: {e}")

lotte_schedule = {
    "6": [
        ("6월 7일", "토", "두산", "롯데", "잠실", "17:00"),
        ("6월 8일", "일", "두산", "롯데", "잠실", "17:00"),
        ("6월 10일", "화", "KT", "롯데", "수원", "18:30"),
        ("6월 11일", "수", "KT", "롯데", "수원", "18:30"),
        ("6월 12일", "목", "KT", "롯데", "수원", "18:30"),
        ("6월 13일", "금", "SSG", "롯데", "문학", "18:30"),
        ("6월 14일", "토", "SSG", "롯데", "문학", "17:00"),
        ("6월 15일", "일", "SSG", "롯데", "문학", "17:00"),
        ("6월 17일", "화", "롯데", "한화", "사직", "18:30"),
        ("6월 18일", "수", "롯데", "한화", "사직", "18:30"),
        ("6월 19일", "목", "롯데", "한화", "사직", "18:30"),
        ("6월 20일", "금", "롯데", "삼성", "사직", "18:30"),
        ("6월 21일", "토", "롯데", "삼성", "사직", "17:00"),
        ("6월 22일", "일", "롯데", "삼성", "사직", "17:00"),
        ("6월 24일", "화", "NC", "롯데", "창원", "18:30"),
        ("6월 25일", "수", "NC", "롯데", "창원", "18:30"),
        ("6월 26일", "목", "NC", "롯데", "창원", "18:30"),
        ("6월 27일", "금", "롯데", "KT", "사직", "18:30"),
        ("6월 28일", "토", "롯데", "KT", "사직", "17:00"),
        ("6월 29일", "일", "롯데", "KT", "사직", "17:00"),
    ],
    "7": [
        ("7월 1일", "화", "롯데", "LG", "사직", "18:30"),
        ("7월 2일", "수", "롯데", "LG", "사직", "18:30"),
        ("7월 3일", "목", "롯데", "LG", "사직", "18:30"),
        ("7월 4일", "금", "KIA", "롯데", "광주", "18:30"),
        ("7월 5일", "토", "KIA", "롯데", "광주", "17:00"),
        ("7월 6일", "일", "KIA", "롯데", "광주", "17:00"),
        ("7월 8일", "화", "롯데", "두산", "사직", "18:30"),
        ("7월 9일", "수", "롯데", "두산", "사직", "18:30"),
        ("7월 10일", "목", "롯데", "두산", "사직", "18:30"),
        ("7월 17일", "목", "LG", "롯데", "잠실", "18:30"),
        ("7월 18일", "금", "LG", "롯데", "잠실", "18:30"),
        ("7월 19일", "토", "LG", "롯데", "잠실", "17:00"),
        ("7월 20일", "일", "LG", "롯데", "잠실", "17:00"),
        ("7월 22일", "화", "키움", "롯데", "고척", "18:30"),
        ("7월 23일", "수", "키움", "롯데", "고척", "18:30"),
        ("7월 24일", "목", "키움", "롯데", "고척", "18:30"),
        ("7월 25일", "금", "롯데", "NC", "사직", "18:30"),
        ("7월 26일", "토", "롯데", "NC", "사직", "17:00"),
        ("7월 27일", "일", "롯데", "NC", "사직", "17:00"),
        ("7월 29일", "화", "롯데", "SSG", "사직", "18:30"),
        ("7월 30일", "수", "롯데", "SSG", "사직", "18:30"),
        ("7월 31일", "목", "롯데", "SSG", "사직", "18:30"),
    ],
    "8": [
        ("8월 1일", "금", "키움", "롯데", "고척", "18:30"),
        ("8월 2일", "토", "키움", "롯데", "고척", "17:00"),
        ("8월 3일", "일", "키움", "롯데", "고척", "17:00"),
        ("8월 5일", "화", "롯데", "KIA", "사직", "18:30"),
        ("8월 6일", "수", "롯데", "KIA", "사직", "18:30"),
        ("8월 7일", "목", "롯데", "KIA", "사직", "18:30"),
        ("8월 8일", "금", "롯데", "SSG", "사직", "18:30"),
        ("8월 9일", "토", "롯데", "SSG", "사직", "17:00"),
        ("8월 10일", "일", "롯데", "SSG", "사직", "17:00"),
        ("8월 12일", "화", "한화", "롯데", "대전", "18:30"),
        ("8월 13일", "수", "한화", "롯데", "대전", "18:30"),
        ("8월 14일", "목", "한화", "롯데", "대전", "18:30"),
        ("8월 15일", "금", "롯데", "삼성", "사직", "18:30"),
        ("8월 16일", "토", "롯데", "삼성", "사직", "17:00"),
        ("8월 17일", "일", "롯데", "삼성", "사직", "17:00"),
        ("8월 19일", "화", "LG", "롯데", "잠실", "18:30"),
        ("8월 20일", "수", "LG", "롯데", "잠실", "18:30"),
        ("8월 21일", "목", "LG", "롯데", "잠실", "18:30"),
        ("8월 22일", "금", "NC", "롯데", "창원", "18:30"),
        ("8월 23일", "토", "NC", "롯데", "창원", "17:00"),
        ("8월 24일", "일", "NC", "롯데", "창원", "17:00"),
        ("8월 26일", "화", "롯데", "KT", "사직", "18:30"),
        ("8월 27일", "수", "롯데", "KT", "사직", "18:30"),
        ("8월 28일", "목", "롯데", "KT", "사직", "18:30"),
        ("8월 29일", "금", "롯데", "두산", "사직", "18:30"),
        ("8월 30일", "토", "롯데", "두산", "사직", "17:00"),
        ("8월 31일", "일", "롯데", "두산", "사직", "17:00"),
    ]
}

def show_lotte_schedule_by_month(month):
    """특정 월의 롯데 자이언츠 남은 경기 일정을 출력합니다."""
    today = datetime(2025, 6, 7) # 현재 시간을 2025년 6월 7일 14:27:17 KST로 설정
    print(f"\n[2025년 {month}월 롯데 자이언츠 남은 경기 일정]")
    found_games = False
    current_year = today.year
    for date_str, weekday, team1, team2, stadium, time in lotte_schedule.get(month, []):
        try:
            date_obj = datetime.strptime(f"{current_year}년 {date_str}", "%Y년 %m월 %d일")
        except ValueError:
            print(f"⚠️ 유효하지 않은 날짜 형식입니다: {date_str}. 스킵합니다.")
            continue
        
        if date_obj >= today.replace(hour=0, minute=0, second=0, microsecond=0):
            print(f"{date_str}({weekday}) {team1} vs {team2} ({stadium} {time})")
            found_games = True
    if not found_games:
        print(f"해당 월에 남은 경기 일정이 없습니다.")

def display_lotte_schedule_menu():
    """롯데 자이언츠 경기 일정 메뉴 옵션을 출력합니다."""
    print("\n[롯데 자이언츠 경기 일정 보기]")
    print("6-1. 6월 경기 일정")
    print("6-2. 7월 경기 일정")
    print("6-3. 8월 경기 일정")

def open_ticket_website():
    """롯데 자이언츠 경기 예매 홈페이지를 웹 브라우저로 엽니다."""
    ticket_url = "https://ticket.giantsclub.com/loginForm.do"
    print(f"\n[경기 예매 홈페이지로 이동] {ticket_url}")
    webbrowser.open(ticket_url)

def open_official_shop():
    """롯데 자이언츠 온라인 쇼핑몰을 웹 브라우저로 엽니다."""
    shop_url = "https://www.lotteon.com/p/display/sellㅔer/sellerShop/lottegiants?ch_no=101509&ch_dtl_no=1049592"
    print(f"\n[롯데 자이언츠 온라인 쇼핑몰로 이동] {shop_url}")
    webbrowser.open(shop_url)

def open_kbo_streaming():
    """KBO 중계 페이지를 웹 브라우저로 엽니다."""
    streaming_url = "https://www.tving.com/sports/kbo"
    print(f"\n[KBO 중계 페이지로 이동] {streaming_url}")
    webbrowser.open(streaming_url)

def open_lotte_highlights():
    """롯데 자이언츠 하이라이트 페이지를 웹 브라우저로 엽니다."""
    highlights_url = "https://www.tving.com/kbo/more/curation/CR3501"
    print(f"\n[롯데 자이언츠 하이라이트 페이지로 이동] {highlights_url}")
    webbrowser.open(highlights_url)

def main():
    """메인 프로그램 함수입니다. 사용자 메뉴를 반복적으로 표시하고 선택에 따라 함수를 호출합니다."""
    while True:
        print("\n========== KBO 메뉴 ==========")
        print("1. KBO 정보")
        print("2. 롯데 자이언츠 소개")
        print("3. 롯데 자이언츠 주요 성과")
        print("4. 롯데 자이언츠 선수단")
        print("5. 실시간 KBO 순위 (TOP 10)")
        print("6. 롯데 자이언츠 경기 일정")
        print("7. 경기 예매 홈페이지 바로가기")
        print("8. 롯데 자이언츠 온라인 쇼핑몰")
        print("9. KBO 중계 페이지 바로가기")
        print("10. 롯데 자이언츠 하이라이트")
        print("q. 종료")

        command = input("원하는 메뉴 번호를 입력하세요: ").strip().lower()

        if command == "1":
            display_kbo_info_menu() # 1번 선택 시 세부 메뉴 옵션만 보여줍니다.
        elif command == "1-1":
            show_kbo_intro()
        elif command == "1-2":
            show_kbo_teams()
        elif command == "1-3":
            show_team_websites()
        elif command == "2":
            show_lottegiants_info()
        elif command == "3":
            show_lottegiants_achievements()
        elif command == "4":
            display_lottegiants_roster_menu() # 4번 선택 시 세부 메뉴 옵션만 보여줍니다.
        elif command == "4-1":
            show_pitchers()
        elif command == "4-2":
            show_catchers()
        elif command == "4-3":
            show_infielders()
        elif command == "4-4":
            show_outfielders()
        elif command == "5":
            show_kbo_top10()
        elif command == "6":
            display_lotte_schedule_menu() # 6번 선택 시 세부 메뉴 옵션만 보여줍니다.
        elif command == "6-1":
            show_lotte_schedule_by_month("6")
        elif command == "6-2":
            show_lotte_schedule_by_month("7")
        elif command == "6-3":
            show_lotte_schedule_by_month("8")
        elif command == "7":
            open_ticket_website()
        elif command == "8":
            open_official_shop()
        elif command == "9":
            open_kbo_streaming()
        elif command == "10":
            open_lotte_highlights()
        elif command == "q":
            print("프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 입력입니다. 메뉴에 해당하는 번호를 입력해주세요.")

if __name__ == "__main__":
    main()