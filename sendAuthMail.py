import requests
import json

def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())

def SendAuthMail(APP_KEY, apiFunction, receiveMailAddr, receiveName, senderAddress, title, body):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    receiver = {'receiveMailAddr': receiveMailAddr, 'receiveName': receiveName}
    data = {'senderAddress': senderAddress, 'title': title, 'body': body, 'receiver': receiver}
    Post(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    authMailApi = 'auth-mail'
    receiveMailAddr = 'woodikol1258@gmail.com'
    receiveName = 'lee'
    receiveType = 'MRT0'
    senderAddress = 'woodikol1258@gmail.com'
    title = 'title'
    body = 'body'

    SendAuthMail(APP_KEY, authMailApi, receiveMailAddr, receiveName, senderAddress, title, body)