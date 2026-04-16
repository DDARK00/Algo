from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
 
# 사용자 설정
USER_ID = "nitori"
DRIVER_PATH = "C:/Users/ION/Downloads/chromedriver-win64/chromedriver.exe"
WAIT_TIME = 10   # 각 묶음을 열고 기다릴 시간 (초)
BATCH_SIZE = 1  # 동시에 열 탭 개수
 
# 드라이버 주소 (path를 버전에 맞게 설정)
# https://storage.googleapis.com/chrome-for-testing-public/141.0.7390.54/win64/chromedriver-win64.zip

# 크롬 드라이버 실행 (확장 프로그램 포함)
service = Service(DRIVER_PATH)
options = Options()
options.add_argument("--user-data-dir=C:/selenium_profiles/bjhubprofile")
options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(options=options, service=service)
 
try:
    # 1. 내 유저 페이지 접속
    url = f"https://www.acmicpc.net/user/{USER_ID}"
    driver.get(url)
    time.sleep(5)
 
    # 2. problem-list 내의 모든 문제 번호 수집
    problem_elements = driver.find_elements(By.CSS_SELECTOR, ".problem-list a[href^='/problem/']")
    problems = [el.text.strip() for el in problem_elements if el.text.strip()]
 
    print(f"✅ 총 {len(problems)} 문제 발견")
    print(problems)
 
    # 3. 20개씩 나누어 처리
    for start in range(0, len(problems), BATCH_SIZE):
        batch = problems[start:start + BATCH_SIZE]
        print(f"▶️ {start+1} ~ {start+len(batch)} 번째 문제 탭 열기...")
 
        # (1) 각 문제의 '내 제출' 페이지 탭 열기
        for pid in batch:
            status_url = f"https://www.acmicpc.net/status?from_mine=1&problem_id={pid}&user_id={USER_ID}"
            driver.execute_script(f"window.open('{status_url}', '_blank');")
            time.sleep(0.3)  # 탭 열기 간격
 
        # (2) 대기 (백준허브가 커밋 처리할 시간)
        print(f"⏳ {WAIT_TIME}초 대기 중...")
        time.sleep(WAIT_TIME)
 
        # (3) 새로 연 탭들 닫기 (첫 번째 탭 제외)
        while len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
 
        # 다시 메인 탭으로 전환
        driver.switch_to.window(driver.window_handles[0])
 
    print("🎉 모든 문제 순회 완료!")
 
finally:
    driver.quit()

# from https://div4u.tistory.com/entry/%EB%B0%B1%EC%A4%80%ED%97%88%EB%B8%8C-%EB%B0%B1%EC%A4%80-%EC%9D%B4%EC%A0%84-%EC%A0%9C%EC%B6%9C-%EC%BB%A4%EB%B0%8B-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8