from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 웹드라이버 초기화
driver = webdriver.Chrome()

# 원하는 URL로 이동
url = 'https://m.blog.naver.com/11destiny3?categoryNo=15&tab=1'
driver.get(url)

# 페이지가 로드될 때까지 충분히 대기
time.sleep(1)  # 페이지가 로드되도록 1초 대기

# 페이지 끝까지 스크롤하여 콘텐츠 로드하기
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # 페이지가 로드되도록 2초 대기

# 데이터 수집
data = {
    '날짜': [elem.text for elem in driver.find_elements(By.CLASS_NAME, "time__mHZOn")],
    '댓글수': [elem.text for elem in driver.find_elements(By.CLASS_NAME, "comment_btn__LZkE_")],
    '공감수': [elem.text for elem in driver.find_elements(By.CLASS_NAME, "u_cnt")],
    '사진수': [elem.text.replace("사진 개수", "").strip() 
                for elem in driver.find_elements(By.CLASS_NAME, "num__dAt36")],
    '제목': [elem.text for elem in driver.find_elements(By.CLASS_NAME, "title__UUn4H")]
}

# 데이터 프레임 생성
df = pd.DataFrame(data)

# 브라우저 종료
driver.quit()

# 결과 확인
print(df)
