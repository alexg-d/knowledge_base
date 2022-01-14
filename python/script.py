import requests

url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_iam_token = "t1.9euelZqWzc7MysfPlouZyc6YnYudke3rnpWaz5yUys2XicbOmpzOipSSjZzl8_cBFFZ7-e8QTjd4_d3z90FCU3v57xBON3j9._pzMwJTG6wvqpziU6O6yJ2v-6H9jr3KqUtdtn9uIHGyg3kBsfKo7QrXTaMbjzR9-yC3iz1FS0TAq1GwamQSUDw"

params = dict(key=API_iam_token, text='More info for me', lang='en-ru')
res = requests.get(url, params=params)


print(res.text)