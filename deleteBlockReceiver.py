import requests
import json

def Put(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.put(url, data=json.dumps(data), headers=headers)
    print(request.json())

def DeleteBlockReceiver(APP_KEY, apiFunction, deleted, mailAddress):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    blockReceiverList = [{'mailAddress': mailAddress}]
    data = {'deleted': deleted, 'blockReceiverList': blockReceiverList}
    Put(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    blockReceiverApi = 'block-receivers'
    mailAddress = 'vmfltm13@naver.com'
    deleted = True

    DeleteBlockReceiver(APP_KEY, blockReceiverApi, deleted, mailAddress)
