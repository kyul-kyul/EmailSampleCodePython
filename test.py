import requests
import json
import base64


# JSON Pretty Print
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


# POST
def Post(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.post(url, data=json.dumps(data), headers=headers)
    print(request.json())


# GET
def Get(url, params):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.get(url, params=params, headers=headers)
    print(request.json())


# PUT
def Put(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.put(url, data=json.dumps(data), headers=headers)
    print(request.json())


# DELETE
def Delete(url, data):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.delete(url, data=json.dumps(data), headers=headers)
    print(request.json())


# 메일 발송 - 일반 메일, 개별 메일, 광고성 일반 메일, 광고성 개별 메일
def SendMail(APP_KEY, apiFunction, receiveMailAddr, receiveName, receiveType, senderAddress, title, body):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    receiver1 = {'receiveMailAddr': receiveMailAddr, 'receiveName': receiveName, 'receiveType': receiveType}
    receiverList = [receiver1]
    data = {'senderAddress': senderAddress, 'title': title, 'body': body, 'receiverList': receiverList}
    Post(url, data)


# 메일 발송 - 인증 메일
def SendAuthMail(APP_KEY, apiFunction, receiveMailAddr, receiveName, senderAddress, title, body):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    receiver = {'receiveMailAddr': receiveMailAddr, 'receiveName': receiveName}
    data = {'senderAddress': senderAddress, 'title': title, 'body': body, 'receiver': receiver}
    Post(url, data)


# 메일 발송 - 태그 메일
def SendAuthMail(APP_KEY, apiFunction, tagExpression, senderAddress, title, body):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    data = {'senderAddress': senderAddress, 'title': title, 'body': body, 'tagExpression': tagExpression}
    Post(url, data)


# 첨부파일 업로드
def UploadFile(APP_KEY, fileName, createUser, fileBody):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/attachfile/binaryUpload'
    fileBody = base64.standard_b64encode(fileBody)
    fileBody = fileBody.decode('UTF-8')
    data = {'fileName': fileName, 'createUser': createUser, 'fileBody': fileBody}
    Post(url, data)


# 첨부 메일
def SendMailWithFile(APP_KEY, apiFunction, receiveMailAddr, receiveName, receiveType, senderAddress, title, body,
                     attachFileIdList):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    receiver1 = {'receiveMailAddr': receiveMailAddr, 'receiveName': receiveName, 'receiveType': receiveType}
    receiverList = [receiver1]
    data = {'senderAddress': senderAddress, 'title': title, 'body': body, 'receiverList': receiverList,
            'attachFileIdList': attachFileIdList}
    Post(url, data)


# 템플릿 메일 (제목/본문 치환)
def TemplateMail(APP_KEY, apiFunction, receiveMailAddr, receiveName, receiveType, senderAddress, templateId,
                 templateParameter):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    receiver1 = {'receiveMailAddr': receiveMailAddr, 'receiveName': receiveName, 'receiveType': receiveType}
    receiverList = [receiver1]
    data = {'senderAddress': senderAddress, 'templateId': templateId, 'templateParameter': templateParameter,
            'receiverList': receiverList, 'attachFileIdList': attachFileIdList}
    Post(url, data)


# 메일 발송 리스트 조회
def InquireMailList(APP_KEY, apiFunction, requestId, startSendDate):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction
    params = {'requestId': requestId, 'startSendDate': startSendDate}
    Get(url, params)


# 메일 발송 상세 조회
def InquireMailDetail(APP_KEY, apiFunction, requestId, mailSeq):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/sender/' + apiFunction + '/' + requestId + '/' + mailSeq
    params = {}
    Get(url, params)


# 태그 메일 발송 요청 조회
def InquireTagMailRequest(APP_KEY, apiFunction, startSendDate, endSendDate):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {'startSendDate': startSendDate, 'endSendDate': endSendDate}
    Get(url, params)


# 태그 메일 발송 수신자 조회
def InquireTagMailReceiver(APP_KEY, apiFunction, requestId):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + requestId
    params = {}
    Get(url, params)


# 태그 메일 발송 상세 조회
def InquireTagMailDetail(APP_KEY, apiFunction, requestId, mailSequence):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + requestId + '/' + mailSequence
    params = {}
    Get(url, params)


# 템플릿 조회
def InquireTemplate(APP_KEY, apiFunction):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {}
    Get(url, params)


# 템플릿 상세 조회
def InquireTemplateDetail(APP_KEY, apiFunction, templateId):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + templateId
    params = {}
    Get(url, params)


# 태그 조회
def InquireTag(APP_KEY, apiFunction):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {}
    Get(url, params)


# 태그 등록
def RegisterTag(APP_KEY, apiFunction, tagName):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    data = {'tagName': tagName}
    Post(url, data)


# 태그 수정
def ModifyTag(APP_KEY, apiFunction, tagId, tagName):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + tagId
    data = {'tagName': tagName}
    Put(url, data)


# 태그 삭제
def DeleteTag(APP_KEY, apiFunction, tagId):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + tagId
    data = {}
    Delete(url, data)


# UID 조회
def InquireUID(APP_KEY, apiFunction):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {}
    Get(url, params)


# UID 단건 조회
def InquireOneUID(APP_KEY, apiFunction, uid):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {'uid': uid}
    Get(url, params)


# UID 등록
def RegisterUID(APP_KEY, apiFunction, uid, tagIds, contact):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    contacts = {'contactType': 'EMAIL_ADDRESS', 'contact': contact}
    data = {'uid': uid, 'tagIds': tagIds, 'contacts': contacts}
    Post(url, data)


# UID 삭제
def DeleteUID(APP_KEY, apiFunction, uid):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + uid
    data = {}
    Delete(url, data)


# 메일 주소 등록
def RegisterEmailAddress(APP_KEY, apiFunction, uid, emailAddress):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + uid + '/email-addresses'
    data = {'emailAddress': emailAddress}
    Post(url, data)


# 메일 주소 삭제
def DeleteEmailAddress(APP_KEY, apiFunction, uid, emailAddress):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction + '/' + uid + '/email-addresses/' + emailAddress
    data = {}
    Delete(url, data)


# 통계 조회
def InquireStatistics(APP_KEY, apiFunction, fromDate, toDate, searchType):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {'from': fromDate, 'to': toDate, 'searchType': searchType}
    Get(url, params)


# 수신 거부 조회
def InquireBlockReceiver(APP_KEY, apiFunction):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {}
    Get(url, params)


# 수신 거부 등록
def RegisterBlockReceiver(APP_KEY, apiFunction, mailAddress, blockDate):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    blockReceiverList = [{'mailAddress': mailAddress, 'blockDate': blockDate}]
    data = {'blockReceiverList': blockReceiverList}
    Post(url, data)


# 수신 거부 삭제
def DeleteBlockReceiver(APP_KEY, apiFunction, deleted, mailAddress):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    blockReceiverList = [{'mailAddress': mailAddress}]
    data = {'deleted': deleted, 'blockReceiverList': blockReceiverList}
    Put(url, data)


if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    standardMailApi = 'mail'
    eachMailApi = 'eachMail'
    adMailApi = 'ad-mail'
    adEachMailApi = 'ad-eachMail'
    authMailApi = 'auth-mail'
    tagMailApi = 'tagMail'
    inquireMailListApi = 'mails'
    inquireTagMailApi = 'tagMails'
    inquireTemplateApi = 'templates'
    tagApi = 'tags'
    uidApi = 'uids'
    statisticsApi = 'statistics/view'
    blockReceiverApi = 'block-receivers'

    receiveMailAddr = 'woodikol1258@gmail.com'
    receiveName = 'lee'
    receiveType = 'MRT0'
    senderAddress = 'woodikol1258@gmail.com'
    title = 'title'
    adTitle = '(광고)title'
    body = 'body'
    tagExpression = ['tag1', 'AND', 'tag2']
    attachFileIdList = [284]

    fileName = 'fileName'
    createUser = 'lee'
    fileBody = ''
    with open('./123.png', 'rb') as f:
        fileBody = f.read()

    templateId = 'id'
    templateParameter = {'title_name': '클라우드고객1', 'body_content': 'test1'}

    requestId = '2018121917070788070014'
    startSendDate = '2018-12-18 00:00:00'
    endSendDate = '2018-12-31 00:00:00'
    mailSeq = '0'
    tagMailRequestId = '2018121917070788070014'

    tagName = 'tagName'
    tagId = 'ODrn4sdH'
    newTagName = 'new_tagName'

    uid = '3'
    contact = 'woodikol1258@gmail.com'
    emailAddress = 'woodikol1258@gmail.com'

    fromDate = '2018-12-01 00:00'
    toDate = '2018-12-24 00:00'
    searchType = 'DATE'
    mailAddress = 'vmfltm13@naver.com'
    blockDate = '2019-12-31 11:42:00'
    deleted = True

    # 일반 메일
    # SendMail(APP_KEY, standardMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, title, body)
    # 개별 메일
    # SendMail(APP_KEY, eachMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, title, body)
    # 광고성 일반 메일
    # SendMail(APP_KEY, adMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, adTitle, body)
    # 광고성 개별 메일
    # SendMail(APP_KEY, adEachMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, adTitle, body)
    # 인증 메일
    # SendAuthMail(APP_KEY, authMailApi, receiveMailAddr, receiveName, senderAddress, title, body)
    # 태그 메일 (결과는 Success이나, 막상 메일이 안감)
    # SendTagMail(APP_KEY, tagMailApi, tagExpression, senderAddress, title, body)
    # 첨부 파일 업로드
    # UploadFile(APP_KEY, fileName, createUser, fileBody)
    # 첨부 메일
    # SendMailWithFile(APP_KEY, standardMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, title, body, attachFileIdList)
    # 탬플릿 메일 (제목/본문 치환)
    # TemplateMail(APP_KEY, standardMailApi, receiveMailAddr, receiveName, receiveType, senderAddress, templateId, templateParameter)

    # 메일 발송 리스트 조회
    # InquireMailList(APP_KEY, inquireMailListApi, requestId, startSendDate)
    # 메일 발송 상세 조회
    # InquireMailDetail(APP_KEY, standardMailApi, requestId, mailSeq)
    # 태그 메일 발송 요청 조회
    # InquireTagMailRequest(APP_KEY, inquireTagMailApi, startSendDate, endSendDate)
    # 태그 메일 발송 수신자 조회 (결과는 Success이나, data가 공백
    # InquireTagMailReceiver(APP_KEY, inquireTagMailApi, requestId)
    # 태그 메일 발송 상세 조회 (Not exist data 오류)
    # InquireTagMailDetail(APP_KEY, inquireTagMailApi, tagMailRequestId, mailSeq)

    # 템플릿 조회
    # InquireTemplate(APP_KEY, inquireTemplateApi)
    # 템플릿 상세 조회
    # InquireTemplateDetail(APP_KEY, inquireTemplateApi, templateId)

    # 태그 조회
    # InquireTag(APP_KEY,tagApi)
    # 태그 등록
    # RegisterTag(APP_KEY, tagApi, tagName)
    # 태그 수정
    # ModifyTag(APP_KEY, tagApi, tagId, newTagName)
    # 태그 삭제
    # DeleteTag(APP_KEY, tagApi, tagId)

    # UID 조회
    # InquireUID(APP_KEY, uidApi)
    # UID 단건 조회
    # InquireOneUID(APP_KEY, uidApi, uid)
    # UID 등록 (Internal Error)
    # RegisterUID(APP_KEY, uidApi, uid, tagId, contact)
    # UID 삭제
    # DeleteUID(APP_KEY, uidApi, uid)
    # 메일 주소 등록
    # RegisterEmailAddress(APP_KEY, uidApi, uid, emailAddress)
    # 메일 주소 삭제
    # DeleteEmailAddress(APP_KEY, uidApi, uid, emailAddress)
    # 통계 조회
    # InquireStatistics(APP_KEY, statisticsApi, fromDate, toDate, searchType)

    # 수신 거부 조회
    # InquireBlockReceiver(APP_KEY, blockReceiverApi)
    # 수신 거부 등록
    # RegisterBlockReceiver(APP_KEY, blockReceiverApi, mailAddress, blockDate)
    # 수신 거부 삭제
    # DeleteBlockReceiver(APP_KEY, blockReceiverApi, deleted, mailAddress)