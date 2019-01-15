import requests
import json

def Delete(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.delete(url, data=json.dumps(data), headers=headers)
    print(request.json())

def DeleteUID(APP_KEY, apiFunction, uid):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + uid
    data = {}
    Delete(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    uidApi = 'uids'
    uid = '3'

    DeleteUID(APP_KEY, uidApi, uid)
