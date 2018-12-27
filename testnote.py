import urllib.request
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





def main():
    # url = "http://www.kweather.co.kr/air/air_forecast.html"

    # Chrome WebDriver를 이용해 Chrome을 실행합니다.
    driver = webdriver.Chrome("C:/Users/student/PycharmProjects/chromedriver.exe")

    # www.google.com으로 이동합니다.
    driver.get("https://music.youtube.com/search?q=dance+the+night+away")

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "play-button"))
        )
    except:
        time.sleep(5)


    continue_link = driver.find_element_by_id('play-button')

    # 해당 링크를 클릭합니다.
    continue_link.click()
    print(driver.current_url)
    # WebDriver를 종료합니다. (브라우저 닫기)
    driver.quit()


    # url = "http://www.cgv.co.kr/movies/"
    # soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
    # driver = webdriver.Chrome('C:\Users\student\PycharmProjects')
    # driver.get('http://www.nfds.go.kr/fr_base_0001.jsf')
    #
    #
    # contents = []
    # rank = 1
    #
    # for data in soup.find_all("div", class_="box-contents"):
    #     if len(contents) >= 5:
    #         break
    #     title = data.find("strong", class_="title")
    #     title = title.get_text().strip()
    #
    #     percent = data.find("strong", class_="percent")
    #     percent = percent.get_text().strip()
    #
    #     open = data.find("span", class_="txt-info")
    #     open = open.get_text().strip().replace("  ","").replace("개봉","").strip()
    #
    #     contents.append(str(rank)+ "위 : "+ str(title) +" : "+ str(percent) + ", 개봉 : " + str(open))
    #     rank += 1
    #
    # print(contents)

if __name__ == "__main__":
    main()
