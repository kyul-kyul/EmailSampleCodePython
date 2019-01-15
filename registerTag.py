import requests
import json

def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())

def RegisterTag(APP_KEY, apiFunction, tagName):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    data = {'tagName': tagName}
    Post(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    tagApi = 'tags'
    tagName = 'tagName'

    RegisterTag(APP_KEY, tagApi, tagName)