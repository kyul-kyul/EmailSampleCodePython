import requests
import json

def Delete(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.delete(url, data=json.dumps(data), headers=headers)
    print(request.json())

def DeleteEmailAddress(APP_KEY, apiFunction, uid, emailAddress):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + uid + '/email-addresses/' + emailAddress
    data = {}
    Delete(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    uidApi = 'uids'
    emailAddress = 'woodikol1258@gmail.com'

    DeleteEmailAddress(APP_KEY, uidApi, uid, emailAddress)
