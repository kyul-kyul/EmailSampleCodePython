import requests
import json

def Delete(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.delete(url, data=json.dumps(data), headers=headers)
    print(request.json())

def DeleteTag(APP_KEY, apiFunction, tagId):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + tagId
    data = {}
    Delete(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    tagApi = 'tags'
    tagId = 'ODrn4sdH'

    DeleteTag(APP_KEY, tagApi, tagId)
