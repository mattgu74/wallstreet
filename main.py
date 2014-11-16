import configparser
import os
import payutcli
import pprint

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

class WallStreet:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read([
            os.path.join(ROOT_DIR, 'defaults.ini'),
            os.path.join(ROOT_DIR, 'local_settings.ini'),
        ])
        self.client = payutcli.Client(**dict(self.config.items('client')))
        self.auth()

    def auth(self):
        self.client.call("ADMINRIGHT", "loginApp", key=self.config.get("rights", "key"))
        self.client.call("POSS3", "loginBadge", badge_id=self.config.get("rights", "badge_id"), pin=self.config.get("rights", "pin"))

    def get_price(self):
        return self.client.call("GESARTICLE", "getProducts", fun_id=2)

    def run(self):
        pprint.pprint(self.get_price())



if __name__ == '__main__':
    w = WallStreet()
    w.run()
