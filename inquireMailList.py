import requests
import json

def Get(url, params):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.get(url, params=params, headers=headers)
    print(request.json())

def InquireMailList(APP_KEY, apiFunction, requestId, startSendDate):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    params = {'requestId': requestId, 'startSendDate': startSendDate}
    Get(url, params)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    inquireMailListApi = 'mails'
    requestId = '2018121917070788070014'
    startSendDate = '2018-12-18 00:00:00'

    InquireMailList(APP_KEY, inquireMailListApi, requestId, startSendDate)
