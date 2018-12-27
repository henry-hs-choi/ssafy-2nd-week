from slacker import Slacker
from requests.sessions import Session
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import websocket
import json

token = 'xoxb-507380538243-508977950518-RLe2YmWWsHlSo9WS468u3lQ1'
driver = webdriver.Chrome("C:/Users/student/PycharmProjects/chromedriver.exe")





def run():
    slack = Slacker(token)

    res = slack.rtm.connect()
    endpoint = res.body['url']

    ws = websocket.create_connection(endpoint)
    ws.settimeout(60)

    while True:
        try:
            link = "https://scontent-icn1-1.cdninstagram.com/vp/876428c5f8437d27bff6b115af3f1a0a/5C1E0CBE/t51.2885-15/e15/38653880_1964556773637924_5085773437796876288_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com"
            # msg = json.loads(ws.recv())
            # print("https://scontent-icn1-1.cdninstagram.com/vp/876428c5f8437d27bff6b115af3f1a0a/5C1E0CBE/t51.2885-15/e15/38653880_1964556773637924_5085773437796876288_n.jpg?_nc_ht=scontent-icn1-1.cdninstagram.com")
            # if(('message' in msg['type']) and ('m_search' in msg['text'])):
            #     search = msg['text'].replace("m_search", "").strip()
            #     slack.chat.post_message("#general", "Searching <" + search + "> in YOUTUBE MUSIC NOW...")
            #     driver.get("https://music.youtube.com/search?q=" + search.replace(" ", "+"))
            #
            #     find_element = "play-button"
            #     WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.ID, find_element)))
            #     link = driver.find_element_by_id(find_element)
            #     link.click()
            #     slack.chat.post_message("#general", str(driver.current_url))
            slack.chat.post_message("#random", link)


        except websocket.WebSocketTimeoutException:
            print("websocket time out error")
            ws.send(json.dumps({'type': 'ping'}))

        except websocket.WebSocketConnectionClosedException:
            print("Connection closed")
            break

        except Exception as e:
            print(e)
            break

    driver.quit()
    ws.close()


run()

