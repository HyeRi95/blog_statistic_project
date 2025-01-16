# # 파이썬 크롤링 연습 1 
# BeutifulSoup는 스크롤 동작이 추가 되어야 하면 안됨
# 첫 화면에 보이는 내용은 크롤링 가능 
import requests
from bs4 import BeautifulSoup

# 요청할 URL
url = 'https://m.blog.naver.com/11destiny3?categoryNo=14&tab=1'  # 여기에 실제 URL을 입력하세요.

# 헤더 추가 (브라우저처럼 보이게 하는 User-Agent)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 페이지 요청
response = requests.get(url, headers=headers)

# 페이지가 정상적으로 로드되었는지 확인
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # '날짜' 수 크롤링
    count_list = []
    count_elements = soup.find_all('div', class_='count__T3YO8')
    for count in count_elements:
        print(count.text)
    
    # '이웃수' 값 크롤링
    neighbor_elements = soup.find_all('span', class_='buddy__fw6Uo')
    for neighbor in neighbor_elements:
        # title_text = title.get_text(strip=True)
        print(neighbor.text)
    
    # # 결과 출력
    # print("날짜:", count_list)
    # print("제목:", title_list)
else:
    print("페이지 요청 실패:", response.status_code)
