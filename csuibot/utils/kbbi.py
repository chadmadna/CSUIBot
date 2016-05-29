import requests
import json


class WordDefinition:

    def __init__(self, word):
        self.word = word
        self.definisi = None
        self.json_data = None

    def url_data(self):
        api_url = 'http://kateglo.com/api.php'
        r = requests.get(api_url, params={
            'format': 'json', 'phrase': self.word})
        try:
            self.json_data = r.json()
            return self.json_data
        except json.JSONDecodeError:
            return 'Oooopss, It looks like you type the wrong word!'

    @staticmethod
    def format_def(data):
        def_texts = ['({}){}'.format(i+1, data[i]['def_text']) for i in range(len(data))]
        return '\n'.join(def_texts)

    def definition(self):
        try:
            all_definisi = self.url_data()["kateglo"]["definition"]
            self.definisi = self.format_def(all_definisi)
            return self.definisi
        except TypeError:
            return self.url_data()
