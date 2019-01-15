import requests
import json


def Get(url, params):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.get(url, params=params, headers=headers)
    print(request.json())

def InquireMailDetail(APP_KEY, apiFunction, requestId, mailSeq):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction + '/' + requestId + '/' + mailSeq
    params = {}
    Get(url, params)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    inquireMailListApi = 'mails'
    requestId = '2018121917070788070014'
    mailSeq = '0'

    InquireMailDetail(APP_KEY, standardMailApi, requestId, mailSeq)
