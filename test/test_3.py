"""
selenium 옵션 참조
https://jheaon.tistory.com/128

동적 페이지, 정적 페이지 크롤링
https://jheaon.tistory.com/127

파이썬을 활용한 업무 자동화 - selenium 4
https://wikidocs.net/177133
"""
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeOptions 설정
# options = webdriver.ChromeOptions()
# Chrome 브라우저 열기
driver = webdriver.Chrome()
# driver = webdriver.Chrome(options=options)

try:
    # 웹 페이지 열기
    driver.get('https://m.market09.kr/')
    print("사이트를 열었습니다.")

    # 페이지가 완전히 로드될 때까지 잠시 대기
    # time.sleep(3)  # 필요에 따라 시간을 조정하세요.
except Exception as e:
    # 요소가 존재하지 않는 경우
    print("사이트를 여는데 실패하였습니다.")
    print("오류 메시지:", str(e))

    # 브라우저 닫기
    if 'driver' in locals():
        driver.quit()

    # 프로그램 종료
    sys.exit(1)
    # exit()

finally:
    # 정상 처리, 오류 발생 관계없이 실행됨
    # 잠시 대기 (페이지가 완전히 로드될 시간을 줍니다)
    time.sleep(3)

try:
    # WebDriverWait를 사용하여 텍스트를 포함하는 요소가 나타날 때까지 대기
    wait = WebDriverWait(driver, 10)
    close_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "오늘 그만 보기")]')))
    # 모든 요소에서 텍스트 찾기
    # close_btn = driver.find_element(By.XPATH, '//*[text()="오늘 그만 보기"]')
    # a 태그에서 텍스트 찾기
    # close_btn = driver.find_element(By.XPATH, '//a[text()="오늘 그만 보기"]')
    # close_btn = driver.find_element(By.LINK_TEXT, '오늘 그만 보기')
    # print(close_btn)

    # 버튼 클릭
    close_btn.click()
    print("오늘 그만 보기 버튼을 클릭했습니다.")

except Exception as e:
    # 요소가 존재하지 않는 경우
    pass
    # print("오늘 그만 보기 버튼을 찾을 수 없습니다.")
    # print("오류 메시지:", str(e))
    #
    # # 브라우저 닫기
    # # driver 객체 존재 여부 확인
    # if 'driver' in locals():
    #     driver.quit()
    #
    # # 프로그램 종료
    # sys.exit(1)
    # # exit()

finally:
    # 정상 처리, 오류 발생 관계없이 실행됨
    # 잠시 대기 (페이지가 완전히 로드될 시간을 줍니다)
    time.sleep(3)

    # 브라우저 닫기
    # if 'driver' in locals():
    #     driver.quit()

try:
    # WebDriverWait를 사용하여 텍스트를 포함하는 요소가 나타날 때까지 대기
    wait = WebDriverWait(driver, 10)
    my_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "MY공구")]')))

    # 버튼 클릭
    my_btn.click()
    print("MY공구 버튼을 클릭했습니다.")

except Exception as e:
    # 요소가 존재하지 않는 경우
    print("MY공구 버튼을 찾을 수 없습니다.")
    print("오류 메시지:", str(e))

    # 브라우저 닫기
    if 'driver' in locals():
        driver.quit()

    # 프로그램 종료
    sys.exit(1)
    # exit()

finally:
    # 잠시 대기 (페이지가 완전히 로드될 시간을 줍니다)
    time.sleep(3)

try:
    # WebDriverWait를 사용하여 텍스트를 포함하는 요소가 나타날 때까지 대기
    wait = WebDriverWait(driver, 10)
    login_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "로그인&회원가입")]')))

    # 버튼 클릭
    login_btn.click()
    print("로그인&회원가입 버튼을 클릭했습니다.")

except Exception as e:
    # 요소가 존재하지 않는 경우
    print("로그인&회원가입 버튼을 찾을 수 없습니다.")
    print("오류 메시지:", str(e))

    # 브라우저 닫기
    if 'driver' in locals():
        driver.quit()

    # 프로그램 종료
    sys.exit(1)
    # exit()

finally:
    # 잠시 대기 (페이지가 완전히 로드될 시간을 줍니다)
    time.sleep(3)

try:
    # WebDriverWait를 사용하여 텍스트를 포함하는 요소가 나타날 때까지 대기
    wait = WebDriverWait(driver, 10)
    kakao_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "카카오로 시작하기")]')))

    # 버튼 클릭
    kakao_btn.click()
    print("카카오로 시작하기 버튼을 클릭했습니다.")

except Exception as e:
    # 요소가 존재하지 않는 경우
    print("카카오로 시작하기 버튼을 찾을 수 없습니다.")
    print("오류 메시지:", str(e))

    # 브라우저 닫기
    if 'driver' in locals():
        driver.quit()

    # 프로그램 종료
    sys.exit(1)
    # exit()

finally:
    # 잠시 대기 (페이지가 완전히 로드될 시간을 줍니다)
    time.sleep(3)

try:
    # 현재 열린 모든 창의 핸들을 가져오기
    # all_windows = driver.window_handles
    # main_window = driver.current_window_handle
    #
    # # 팝업창으로 전환
    # for window in all_windows:
    #     if window != main_window:
    #         driver.switch_to.window(window)
    #         break
    # 카카오 로그인 팝업 (자식창)
    driver.switch_to.window(driver.window_handles[1])

    # WebDriverWait를 사용하여 로그인 ID 입력 필드가 나타날 때까지 대기
    login_id_field = wait.until(EC.presence_of_element_located((By.NAME, 'loginId')))

    # 로그인 ID 입력 필드에 값 입력
    login_id_field.send_keys('aaaaa')
    print('로그인 ID 입력 필드에 "aaaaa"를 입력했습니다.')

    time.sleep(3)
    # WebDriverWait를 사용하여 로그인 ID 입력 필드가 나타날 때까지 대기
    login_pw_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

    # 로그인 ID 입력 필드에 값 입력
    login_pw_field.send_keys('bbbbb')
    print('로그인 PASSWORD 입력 필드에 "bbbbb"를 입력했습니다.')

    time.sleep(3)
    # WebDriverWait를 사용하여 type="submit" 버튼이 나타날 때까지 대기
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))

    # type="submit" 버튼 클릭
    submit_button.click()
    print('type="submit" 버튼을 클릭했습니다.')

    # # 작업이 끝난 후 팝업창 닫기
    # driver.close()
    #
    # # 메인 창으로 다시 전환
    # driver.switch_to.window(main_window)

except Exception as e:
    # 요소가 존재하지 않는 경우
    print("loginId 입력 필드를 찾을 수 없습니다.")
    print("오류 메시지:", str(e))

    # 브라우저 닫기
    if 'driver' in locals():
        driver.quit()

    # 프로그램 종료
    sys.exit(1)
    # exit()

finally:
    # 잠시 대기 (페이지가 완전히 로드될 시간을 줍니다)
    time.sleep(3)

# 잠시 대기 (페이지가 완전히 로드될 시간을 줍니다)
# time.sleep(3)

# 브라우저 닫기
if 'driver' in locals():
    driver.quit()
