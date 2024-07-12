"""
BeautifulSoup Library
https://dad-rock.tistory.com/751

데이터분석 파이썬 정리_570문제 - BeautifulSoup 모듈
https://wikidocs.net/158070

BeautifulSoup 정규표현식을 이용하여 원하는 값 추출
https://data-soin.tistory.com/57

파이썬 Beutiful Soup의 한계와 셀레니움의 필요성
https://jerry-style.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80%EA%B3%BC-Beautiful-Soup%EC%9D%98-%EC%9A%A9%EB%8F%84%EB%B3%84-%EC%B0%A8%EC%9D%B4

정적 페이지만 크롤링 가능
자바스크립트로 생성된 페이지처럼 동적 페이지는 불가능
"""
import requests
from bs4 import BeautifulSoup

# 크롤링할 웹 페이지 URL
# url = 'https://m.market09.kr/'
url = 'https://example.com'
print(url)

# 웹 페이지 요청
response = requests.get(url)
print(response.status_code)

# 페이지 요청이 성공했는지 확인
if response.status_code == 200:
    # HTML 소스 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)

    # 예제: 뉴스 제목 추출 (HTML 구조에 따라 변경 필요)
    titles = soup.find_all('h1')
    # titles = soup.find_all('h2', class_='title')

    # 추출한 제목 출력
    for idx, title in enumerate(titles):
        print(f"{idx + 1}. {title.get_text()}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
