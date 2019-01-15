import requests
import json

def Get(url, params):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.get(url, params=params, headers=headers)
    print(request.json())

def InquireTagMailRequest(APP_KEY, apiFunction, startSendDate, endSendDate):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {'startSendDate': startSendDate, 'endSendDate': endSendDate}
    Get(url, params)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    inquireTagMailApi = 'tagMails'
    startSendDate = '2018-12-18 00:00:00'
    endSendDate = '2018-12-31 00:00:00'

    InquireTagMailRequest(APP_KEY, inquireTagMailApi, startSendDate, endSendDate)