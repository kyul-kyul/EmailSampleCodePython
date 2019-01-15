import requests
import json

def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())

def RegisterUID(APP_KEY, apiFunction, uid, tagIds, contact):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    contacts = {'contactType': 'EMAIL_ADDRESS', 'contact': contact}
    data = {'uid': uid, 'tagIds': tagIds, 'contacts': contacts}
    Post(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    uidApi = 'uids'
    tagId = 'ODrn4sdH'
    uid = '3'
    contact = 'woodikol1258@gmail.com'

    RegisterUID(APP_KEY, uidApi, uid, tagId, contact)