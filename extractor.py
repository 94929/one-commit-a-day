import json
import requests

from config import base
from config import headers


class Extractor:

    def __init__(self):
        pass

    def get(url, headers={}):
        r = requests.get(url, headers=headers)
        if not r.ok:
            raise ValueError('Cannot perform HTTP request, GET')
        return r

    def get_contents_from(self, url):
        r = get(base + url, headers)
        contents = json.loads(r.content)
        return contents


def main():
    e = Extractor()


if __name__ == '__main__':
    e = Extractor()

