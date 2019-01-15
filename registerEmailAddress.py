import requests
import json

def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())

def RegisterEmailAddress(APP_KEY, apiFunction, uid, emailAddress):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + uid + '/email-addresses'
    data = {'emailAddress': emailAddress}
    Post(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    uidApi = 'uids'
    uid = '3'
    emailAddress = 'woodikol1258@gmail.com'

    RegisterEmailAddress(APP_KEY, uidApi, uid, emailAddress)