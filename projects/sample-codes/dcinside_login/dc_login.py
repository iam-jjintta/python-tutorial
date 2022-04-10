
import json

from requests_html import HTMLSession


def get_login_data():
    "로그인에 필요한 정보"

    with open('account.json') as file:
        account = json.load(file)
    with open('data.json') as file:
        data = json.load(file)
        data.update(account)
    return data


def get_hash_data(html):
    "로그인 시 필요한 HASH 데이터 가져오기"

    selector = '#login_process > input[type=hidden]:nth-child(3)'
    attrs = html.find(selector, first=True).attrs
    return attrs['name'], attrs['value']


def get_user_name(html):
    "고닉 정보 가져오기"

    selector = '#login_box > div.user_info > div.user_inr > div.user_name.otp_width > strong'
    tag = html.find(selector, first=True)
    return tag.text


if __name__ == '__main__':
    # 로그인 시 필요한 헤더와 데이터를 가져온다.
    with open('headers.json') as file:
        headers = json.load(file)
        data = get_login_data()

    url = 'https://www.dcinside.com/'
    login_url = 'https://sign.dcinside.com/login/member_check'

    session = HTMLSession()

    dcinside_main = session.get(url, headers=headers)
    main_page = dcinside_main.html
    # 로그인 시 필요한 HASH 데이터를 가져온다.
    hash_data = get_hash_data(main_page)
    data[hash_data[0]] = hash_data[1]

    # 로그인 시 POST 방식으로 요청한다.
    # POST 방식은 GET 방식과는 달리 URL에 파라미터를 넘기는 방식이 아닌, Body에 데이터를 담아서 전송하는 방식이다.
    session.post(login_url, headers=headers, data=data)

    # 로그인을 한 다음, 로그인한 계정의 고정닉 정보를 가져온다.
    dcinside_main = session.get(url, headers=headers)
    main_page = dcinside_main.html
    user_name = get_user_name(main_page)

    # 고정닉 정보 출력
    print(user_name)
