from csuibot.config import TELEGRAM_BOT_TOKEN, COMPUTER_VISION_KEY

import requests
import json

API_URL = 'https://api.projectoxford.ai/vision/v1.0/analyze' \
          '?visualFeatures=Categories%2CTags%2CDescription' \
          '%2CFaces%2CImageType%2CColor%2CAdult'
HEADERS = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': COMPUTER_VISION_KEY,
}
FILE_URL = 'https://api.telegram.org/file/bot{0}/{1}'


class ImgRequest:

    def __init__(self, imginfo):
        self.imgfile = self.get_file(imginfo)
        self.request = self.request_features()
        self._data = json.loads(self.request.text)
        self.init_features()

    @staticmethod
    def get_file(fileinfo):
        file_path = fileinfo.file_path.replace('\\', '')
        response = requests.get(FILE_URL.format(TELEGRAM_BOT_TOKEN, file_path))
        return response.content

    def request_features(self):
        return requests.post(API_URL, headers=HEADERS, data=self.imgfile)

    def init_features(self):
        if self.request.status_code == 200:
            self._categories = self._fetch_categories()
            self._tags = self._fetch_tags()
            self._description = self._fetch_description()
            self._faces = self._fetch_faces()
            self._image_type = self._fetch_image_type()
            self._color = self._fetch_color()
            self._is_adult = self._fetch_is_adult()
        else:
            self.request.raise_for_status()

    @property
    def categories(self):
        return self._categories

    @property
    def tags(self):
        return self._tags

    @property
    def description(self):
        return self._description

    @property
    def faces(self):
        return self._faces

    @property
    def image_type(self):
        return self._image_type

    @property
    def color(self):
        return self._color

    @property
    def is_adult(self):
        return self._is_adult

    def _fetch_categories(self):
        try:
            data = self._data['categories']
        except KeyError:
            return "Uncategorized"
        category_list = sorted(data, key=lambda x: x['score'])
        categories = [" > ".join(
            [c.title() for c in cat['name'].split('_') if c != '']
        ) for cat in category_list]
        ret = categories[-1]  # pick most confident category

        return ret

    def _fetch_tags(self):
        data = self._data['tags']
        tag_list = sorted(data, key=lambda x: x['confidence'], reverse=True)[:5]
        ret = ", ".join([tag['name'].replace('_', ' ') for tag in tag_list])

        return ret

    def _fetch_description(self):
        data = self._data['description']
        captions = sorted(data['captions'], key=lambda x: x['confidence'])
        ret = captions[-1]['text']  # pick most confident caption
        ret = ret[0].upper() + ret[1:]

        return ret

    def _fetch_faces(self):
        data = self._data['faces']
        ret = []
        for face in data:
            d = {k: face[k] for k in ('gender', 'age')}
            ret.append(d)

        return ret

    def _fetch_image_type(self):
        data = self._data['imageType']
        imgtype = []
        if data['clipArtType']:
            imgtype.append('Clipart')
        if data['lineDrawingType']:
            imgtype.append('Line drawing')
        ret = ", ".join(imgtype)

        return ret

    def _fetch_color(self):
        ret = {}
        data = self._data['color']
        ret['dominant'] = data['dominantColors']
        ret['fg'] = data['dominantColorForeground']
        ret['bg'] = data['dominantColorBackground']
        ret['accent'] = data['accentColor']
        ret['is_bw'] = data['isBWImg']

        return ret

    def _fetch_is_adult(self):
        return (self._data['adult']['isAdultContent'],
                self._data['adult']['isRacyContent'])
