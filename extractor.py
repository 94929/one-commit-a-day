import json
import requests

from config import base
from config import headers
from config import login


class Extractor:
    """ This class extracts github informations from the api server """

    ##################################
    # Constructor methods come below #
    ##################################

    def __init__(self):
        self.__repos = self.__init_repos()

    def __init_repos(self):
        """ Init all (public + private) repos owned by me """
        repos = self.__get_contents_from('/user/repos')
        repos_owned_by_me = [r for r in repos if r['owner']['login'] == login]
        return repos_owned_by_me

    ###################################
    # HTTP Request methods come below #
    ###################################

    def __get(self, url):
        addr = base + url
        print('Performing GET HTTP request to:', addr)
        r = requests.get(base+url, headers=headers)
        if not r.ok:
            raise ValueError('Cannot perform HTTP request, GET')
        print('Received GET HTTP response from:', addr)
        return r

    def __get_contents_from(self, url):
        r = self.__get(url)
        contents = json.loads(r.content)
        return contents

    #############################
    # Getter methods come below #
    #############################

    def get_repo_names(self):
        return [repo['name'] for repo in self.repos]


def main():
    e = Extractor()


if __name__ == '__main__':
    main()

