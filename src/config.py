from ConfigParser import SafeConfigParser
from trello import util


class Config(object):
    def __init__(self, path):
        self._path = path
        self._cp = SafeConfigParser()
        self._cp.read(path)
        self._boards = []
        self._load_boards()
        self._dirty = False

    def _load_boards(self):
        for _section in self._cp.sections():
            if _section.startswith("BOARD:"):
                self._boards.append({
                    "name": _section.split(':', 1)[1],
                    "board_id": self._cp.get(_section, "board_id"),
                    "list_id": self._cp.get(_section, "list_id")
                })

    def save(self):
        if not self._dirty:
            return

        with open(self._path, 'w') as fid:
                self._cp.write(fid)

    def get_trello_key(self):
        return self._cp.get("DEFAULT", "trello_key")

    def set_trello_key(self, value):
        self._cp.set("DEFAULT", "trello_key", value)
        self._dirty = True

    def get_trello_key_secret(self):
        return self._cp.get("DEFAULT", "trello_key_secret")

    def set_trello_key_secret(self, value):
        self._cp.set("DEFAULT", "trello_key_secret", value)
        self._dirty = True

    def get_trello_oauth_key(self):
        return self._cp.get("DEFAULT", "trello_oauth_key")

    def set_trello_oauth_key(self, value):
        self._cp.set("DEFAULT", "trello_oauth_key", value)
        self._dirty = True

    def get_trello_oauth_secret(self):
        return self._cp.get("DEFAULT", "trello_oauth_secret")

    def set_trello_oauth_secret(self, value):
        self._cp.set("DEFAULT", "trello_oauth_secret", value)
        self._dirty = True

    def get_google_key(self):
        return self._cp.get("DEFAULT", "google_key")

    def set_google_key(self, value):
        self._cp.set("DEFAULT", "google_key", value)
        self._dirty = True

    def get_google_key_secret(self):
        return self._cp.get("DEFAULT", "google_key_secret")

    def set_google_key_secret(self, value):
        self._cp.set("DEFAULT", "google_key_secret", value)
        self._dirty = True

    def get_google_oauth_key(self):
        return self._cp.get("DEFAULT", "google_oauth_key")

    def set_google_oauth_key(self, value):
        self._cp.set("DEFAULT", "google_oauth_key", value)
        self._dirty = True

    def get_google_oauth_secret(self):
        return self._cp.get("DEFAULT", "google_oath_secret")

    def set_google_oauth_secret(self, value):
        self._cp.set("DEFAULT", "google.oauth.secret", value)
        self._dirty = True

    def get_drive_path(self):
        return self._cp.get("DEFAULT", "drive_path")

    def set_drive_path(self, value):
        self._cp.set("DEFAULT", "drive_path", value)
        self._dirty = True

    def init_trello(self, key, secret):
        _ret = util.create_oauth_token(
            "1day",
            "read",
            key,
            secret,
            "trell-complete-report"
        )

        self.set_trello_key(key)
        self.set_trello_key_secret(secret)
        self.set_trello_oauth_key(_ret.get('oauth_token'))
        self.set_trello_oauth_secret(_ret.get('oauth_token_secret'))
        self.save()
