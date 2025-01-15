from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd 

# 웹드라이버 초기화
driver = webdriver.Chrome()

# 원하는 URL로 이동
# url = "https://m.blog.naver.com/11destiny3?categoryNo=13&tab=1"
url = 'https://m.blog.naver.com/11destiny3?categoryNo=15&tab=1'
driver.get(url)



# 페이지가 로드될 때까지 충분히 대기
time.sleep(1)  # 페이지가 로드되도록 3초 대기

# 페이지 끝까지 스크롤하여 콘텐츠 로드하기
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)  # 페이지가 로드되도록 3초 대기

date_lst=[]
comments_lst = []
likes_lst=[]
photos_lst=[]
title_lst=[]

# 2. 글 제목 크롤링
try:
    read_date_elements = driver.find_elements(By.CLASS_NAME, "time__mHZOn")
    if read_date_elements:
        for read_count in read_date_elements:
            date_lst.append(read_count.text)    
    else:
        print("등록일 요소가 없습니다.")

    read_comment_elements = driver.find_elements(By.CLASS_NAME, "comment_btn__LZkE_")
    if read_comment_elements:
        for read_count in read_comment_elements:
            comments_lst.append(read_count.text)
    else:
        print("댓글 수 요소가 없습니다.")

    read_like_elements = driver.find_elements(By.CLASS_NAME, "u_cnt")
    if read_like_elements:
        for read_count in read_like_elements:
            likes_lst.append(read_count.text)
    else:
        print("공감 수 요소가 없습니다.")

    read_photo_elements = driver.find_elements(By.CLASS_NAME, "num__dAt36")
    if read_photo_elements:
        for read_count in read_photo_elements:
            photos_lst.append(read_count.text)
    else:
        print("사진 수 요소가 없습니다.")

    title_elements = driver.find_elements(By.CLASS_NAME, "title__UUn4H")
    if title_elements:
        for title in title_elements:
            title_lst.append(read_count.text)
    else:
        print("글 제목 요소가 없습니다.")
except Exception as e:
    print("제목 크롤링 실패:", e)

# 브라우저 종료
driver.quit()