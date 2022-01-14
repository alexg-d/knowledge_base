import requests
import json

url = "https://homepay-dev.homecredit.ru/auth/v1/send-otp"

phone = "9906323254"
body = '{ "phone" : ' + phone + ' }'
headers = {'Content-Type' : 'application/json', 'x-app-version' : '1.0'}
response = str(requests.post(url, headers = headers, data = body).text)

profile = '{  "registrationAddress" : {    "addressString" : "Тюменская обл,  г Тюмень, ул Александра Логунова, д 77, кв 1",
    "fiasId" : "35d05cd5-9428-4bcd-b4f3-45d89c387e6e",
    "postalCode" : "625016",
    "fiasLevel" : "8",
    "flat" : "1"  },
  "residentialAddress" : {
    "addressString" : "Тюменская обл,  г Тюмень, ул Александра Логунова, д 77, кв 1",
    "fiasId" : "35d05cd5-9428-4bcd-b4f3-45d89c387e6e",
    "postalCode" : "625016",
    "fiasLevel" : "8",
    "flat" : "1"  },  "email" : "ss@test.ru",
  "birthDate" : "1984-01-19",
  "birthPlace" : "Москва",
  "name" : "Александр",
  "orgIssue" : "ОТДЕЛЕНИЕМ ПО РАЙОНУ НОВО-ПЕРЕДЕЛКИНО ОУФМС РОССИИ ПО Г. МОСКВЕ В ЗАО",
  "passportNumber" : {{passport}},
  "sex" : "MALE",
  "patronymic" : "БЕЗНМД",
  "codeIssue" : "770-001",
  "income" : 90000,
  "surname" : "Хомяков",
  "occupationTypeCode" : "OMAY_Businessman",
  "dateIssue" : "2021-01-17",
  "advertisingMailing" : true
}'

response_dict = json.loads(response)

if response_dict.get('otpId') != None:
    otpId = response_dict.get('otpId')
    print('200 OK, ' + otpId)
else:
    print(response)


url = 'https://homepay-dev.homecredit.ru/auth/v1/check-otp'

body = '{ "phone" : ' + phone + ', "otpId" : ' + otpId + ', "code" : ' + phone[-4:] + ' }'

response = str(requests.post(url, headers = headers, data = body).text)

response_dict = json.loads(response)

if response_dict.get('access') != None:
    accessToken = response_dict.get('access')
    print('200 OK, ' + accessToken)
else:
    print(response)


url = 'https://homepay-dev.homecredit.ru/customer/v1/consent'
headers = {'Content-Type' : 'application/json', 'x-app-version' : '1.0', 'Authorization' : 'Bearer ' + accessToken}

response = requests.post(url, headers = headers)

print(response)


url = 'https://homepay-dev.homecredit.ru/customer/v1/get-sumsub-access'

response = requests.get(url, headers = headers).text

print(response)


url = 'https://homepay-dev.homecredit.ru/customer/v1/request-documents-data'

response = requests.get(url, headers = headers).text

print(response)


url = 'https://homepay-dev.homecredit.ru/customer/v1/send-otp'

body = '{ "phone" : ' + phone + ' }'

response = str(requests.post(url, headers = headers, data = body).text)

response_dict = json.loads(response)

if response_dict.get('otpId') != None:
    otpId = response_dict.get('otpId')
    print('200 OK, ' + otpId)
else:
    print(response)


url = 'https://homepay-dev.homecredit.ru/customer/v1/check-otp'

body = '{ "phone" : ' + phone + ', "otpId" : ' + otpId + ', "code" : ' + phone[-4:] + ' }'

response = requests.post(url, headers = headers, data = body)

print(response)