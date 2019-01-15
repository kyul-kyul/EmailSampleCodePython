import requests
import json

def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())

def TemplateMail(APP_KEY, apiFunction, receiveMailAddr, receiveName, receiveType, senderAddress, templateId,
                 templateParameter):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    receiver1 = {'receiveMailAddr': receiveMailAddr, 'receiveName': receiveName, 'receiveType': receiveType}
    receiverList = [receiver1]
    data = {'senderAddress': senderAddress, 'templateId': templateId, 'templateParameter': templateParameter,
            'receiverList': receiverList, 'attachFileIdList': attachFileIdList}
    Post(url, data)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    standardMailApi = 'mail'
    receiveMailAddr = 'woodikol1258@gmail.com'
    receiveName = 'lee'
    receiveType = 'MRT0'
    senderAddress = 'woodikol1258@gmail.com'
    templateId = 'id'
    templateParameter = {'title_name': '클라우드고객1', 'body_content': 'test1'}


    TemplateMail(APP_KEY, standardMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, templateId,
                 templateParameter)