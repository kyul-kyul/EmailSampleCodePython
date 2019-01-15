import requests
import json

def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())

def RegisterBlockReceiver(APP_KEY, apiFunction, mailAddress, blockDate):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    blockReceiverList = [{'mailAddress': mailAddress, 'blockDate': blockDate}]
    data = {'blockReceiverList': blockReceiverList}
    Post(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    blockReceiverApi = 'block-receivers'
    mailAddress = 'vmfltm13@naver.com'
    blockDate = '2019-12-31 11:42:00'

    RegisterBlockReceiver(APP_KEY, blockReceiverApi, mailAddress, blockDate)