import requests
import json
import base64

def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())

def UploadFile(APP_KEY, fileName, createUser, fileBody):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/attachfile/binaryUpload'
    fileBody = base64.standard_b64encode(fileBody)
    fileBody = fileBody.decode('UTF-8')
    data = {'fileName': fileName, 'createUser': createUser, 'fileBody': fileBody}
    Post(url, data)

def SendMailWithFile(APP_KEY, apiFunction, receiveMailAddr, receiveName, receiveType, senderAddress, title, body,
                     attachFileIdList):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    receiver1 = {'receiveMailAddr': receiveMailAddr, 'receiveName': receiveName, 'receiveType': receiveType}
    receiverList = [receiver1]
    data = {'senderAddress': senderAddress, 'title': title, 'body': body, 'receiverList': receiverList,
            'attachFileIdList': attachFileIdList}
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
    attachFileIdList = [284]
    fileName = 'fileName'
    createUser = 'lee'
    fileBody = ''
    with open('./123.png', 'rb') as f:
        fileBody = f.read()

    UploadFile(APP_KEY, fileName, createUser, fileBody)
    SendMailWithFile(APP_KEY, standardMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, title, body,
                     attachFileIdList)
