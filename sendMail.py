import requests
import json

def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())

def SendMail(APP_KEY, apiFunction, receiveMailAddr, receiveName, receiveType, senderAddress, title, body):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    receiver1 = {'receiveMailAddr': receiveMailAddr, 'receiveName': receiveName, 'receiveType': receiveType}
    receiverList = [receiver1]
    data = {'senderAddress': senderAddress, 'title': title, 'body': body, 'receiverList': receiverList}
    Post(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    standardMailApi = 'mail'
    receiveMailAddr = 'woodikol1258@gmail.com'
    receiveName = 'lee'
    receiveType = 'MRT0'
    senderAddress = 'woodikol1258@gmail.com'
    title = 'title'
    body = 'body'

    SendMail(APP_KEY, standardMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, title, body)