import requests

url = "https://api.telegram.org/bot{token}/{method}".format(
    token="5037172459:AAF1FDpL72U3rsGOSxtc9f6FGdhO6fmE61Y",
    method = "setWebhook"
    #method="getWebhookinfo"
    #method = "deleteWebhook"
)

data = {"url": "https://functions.yandexcloud.net/d4e29e4bbqpqmcbhl6dv"}

r = requests.post(url, data=data)
print(r.json())
