import requests
import json

def Get(url, params):
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    request = requests.get(url, params=params, headers=headers)
    print(request.json())

def InquireStatistics(APP_KEY, apiFunction, fromDate, toDate, searchType):
    url = 'https://api-mail.cloud.toast.com/email/v1.4/appKeys/' + APP_KEY + '/' + apiFunction
    params = {'from': fromDate, 'to': toDate, 'searchType': searchType}
    Get(url, params)

if __name__ == "__main__":
    APP_KEY = '{APP_KEY}'

    statisticsApi = 'statistics/view'
    fromDate = '2018-12-01 00:00'
    toDate = '2018-12-24 00:00'
    searchType = 'DATE'

    InquireStatistics(APP_KEY, statisticsApi, fromDate, toDate, searchType)
