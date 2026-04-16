from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import re
 
# 사용자 설정
USER_ID = "nitori"
DRIVER_PATH = "C:/Users/ION/Downloads/chromedriver-win64/chromedriver.exe"
REPO_PATH = "./Algo-main/백준"

# 드라이버 주소 (path를 버전에 맞게 설정)
# chrome://settings/help
# https://storage.googleapis.com/chrome-for-testing-public/141.0.7390.54/win64/chromedriver-win64.zip

# 크롬 드라이버 실행 (확장 프로그램 포함)
service = Service(DRIVER_PATH)
options = Options()
driver = webdriver.Chrome(options=options, service=service)

def get_boj_solved_list(url):
    print("백준에서 데이터 가져오는 중...")
    driver.get(url)
    time.sleep(5)
 
    # 2. problem-list 내의 모든 문제 번호 수집
    problem_elements = driver.find_elements(By.CSS_SELECTOR, ".problem-list a[href^='/problem/']")
    problems = [el.text.strip() for el in problem_elements if el.text.strip()]
 
    print(f"✅ 총 {len(problems)} 문제 발견")
    # print(problems)
    return problems

def get_local_solve_list(path):
    print(f"로컬 폴더 {path} 스캔 중...")
    local_numbers = set()
    for root, dirs, files in os.walk(path):
         for directory in dirs:
              # No.name 형식에서 No추출
              match = re.match(r'^(\d+)\.', directory)
              if match:
                   local_numbers.add(match.group(1))
    print(f"✅ 총 {len(local_numbers)} 문제 발견")
    # print(local_numbers)
    return local_numbers
     

try:
    # # 1. 내 유저 페이지 접속
    url = f"https://www.acmicpc.net/user/{USER_ID}"
    boj_set = set(get_boj_solved_list(url))

    # 2. 로컬 문제 번호 추출
    local_set = get_local_solve_list(REPO_PATH)
    
    # 누락된 문제 (백준 set - 로컬 set)
    missing = sorted(list(boj_set - local_set), key=int)
    print("-" * 27)
    print(f"누락된 문제 수 {len(missing)}")
    if missing:
         print("누락된 번호 목록")
         print(", ".join(missing))

finally:
        driver.quit()

# commit수와 solved 문제 수가 달라서 몇몇 문제가 누락되었다고 판단,
# boj_past_upload를 응용해서 만든 누락 문제 검사기
# 이후 백준 허브 스크립트를 통해 누락된 문제에 대해 순회 가능