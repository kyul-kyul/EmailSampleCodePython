import requests
import json

def Get(url, params):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.get(url, params=params, headers=headers)
    print(request.json())

def InquireBlockReceiver(APP_KEY, apiFunction):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {}
    Get(url, params)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    blockReceiverApi = 'block-receivers'
    InquireBlockReceiver(APP_KEY, blockReceiverApi)