from csuibot import app
from json import loads
from requests import get
# Bot to get 5 latest news releveant to user request.
# Implemented by Bimo Prabowo R.


def search_news(query):
    search = ""
    for i in query:
        search += i + "+"
    search = search[:-1]
    header = {"Ocp-Apim-Subscription-Key": "{}".format(app.config['MICROSOFT_SEARCH_TOKEN'])}
    url = 'https://bingapis.azure-api.net/api/v5/news/search?q={}&count=5'.format(search)
    resp = get(url, headers=header)
    return loads(resp.text)
