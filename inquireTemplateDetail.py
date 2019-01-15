import requests
import json

def Get(url, params):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.get(url, params=params, headers=headers)
    print(request.json())

def InquireTemplateDetail(APP_KEY, apiFunction, templateId):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + templateId
    params = {}
    Get(url, params)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    inquireTemplateApi = 'templates'
    templateId = 'id'

    InquireTemplateDetail(APP_KEY, inquireTemplateApi, templateId)