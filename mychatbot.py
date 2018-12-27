# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template

app = Flask(__name__)

slack_token = "xoxb-507380538243-508977950518-RLe2YmWWsHlSo9WS468u3lQ1"
slack_client_id = "507449810307.506951689729"
slack_client_secret = "57112cb61f6780a1612ded153727f30d"
slack_verification = "yWSrwJybU1PnkHfzLlDoKbsF"
sc = SlackClient(slack_token)


# 크롤링 함수 구현하기
def _crawl_naver_keywords(text):
    # 여기에 함수를 구현해봅시다.
    # URL 데이터를 가져올 사이트 url 입력

    url = "http://www.cgv.co.kr/movies/"
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")

    contents = []
    rank = 1

    for data in soup.find_all("div", class_="box-contents"):
        if len(contents) >= 5:
            break
        title = data.find("strong", class_="title")
        title = title.get_text().strip()

        percent = data.find("strong", class_="percent")
        percent = percent.get_text().strip().replace("예매율", "예매율 : ")

        open = data.find("span", class_="txt-info")
        open = open.get_text().strip().replace("  ","").replace("개봉","").strip()

        contents.append(str(rank)+ "위 : <"+ str(title) +"> "+ str(percent) + ", 개봉 : " + str(open))
        rank += 1




    # 한글 지원을 위해 앞에 unicode u를 붙혀준다.
    return u'\n'.join(contents)


# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]

        keywords = _crawl_naver_keywords(text)
        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords
        )

        return make_response("App mention message has been sent", 200, )

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                                 "application/json"
                                                             })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
