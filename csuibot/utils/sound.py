import soundcloud
from requests.exceptions import HTTPError

from csuibot import app


class Sound:
    def __init__(self, action, keyword):
        self.client = soundcloud.Client(client_id=app.config['CLIENT_ID'],
                                        client_secret=app.config['CLIENT_SECRET'])
        self.action = action
        self.keyword = keyword
        try:
            self.trx = self.get_tracks(self.action, self.keyword)
            self.lookup = self._parse_tracks()
        except HTTPError:
            self.lookup = "Tracks not found"

    def get_tracks(self, act, key):
        if act == 'sound_composer':
            user = self.client.get('/resolve', url='http://soundcloud.com/{}'.format(key))
            tracks = self.client.get('/users/{}/tracks'.format(user.id), limit=5)
        return tracks

    def _parse_tracks(self):
        track_str = ""
        for track in self.trx:
            track_str += """TRACK NAME {}
DURATION {}
COMPOSER {}
URL {}

""".format(track.title, self._parse_duration(track.duration),
                track.user['username'], track.permalink_url)
        return track_str

    def _parse_duration(self, ms):
        s = float(ms) // 1000
        m, s = divmod(s, 60)
        return "%02d:%02d" % (m, s)
