import json
import requests

from config import base
from config import headers
from config import username


class Extractor:
    """ This class extracts github informations from the api server """

    ##################################
    # Constructor methods come below #
    ##################################

    def __init__(self):
        # init repos that are owned by me
        self.__repos = self.__init_repos()

    def __init_repos(self):
        """ Init all (public + private) repos owned by me """
        repos = self.__get_contents_from('/user/repos')
        repos_of_mine = [r for r in repos if r['owner']['login'] == username]
        return repos_of_mine

    ###################################
    # HTTP Request methods come below #
    ###################################

    def __get(self, url):
        addr = base + url
        #print('Performing GET HTTP request to:', addr)
        r = requests.get(base+url, headers=headers)
        if not r.ok:
            raise ValueError('Cannot perform HTTP request, GET')
        #print('Received GET HTTP response from:', addr)
        return r

    def __get_contents_from(self, url):
        r = self.__get(url)
        contents = json.loads(r.content)
        return contents

    #############################
    # Getter methods come below #
    #############################

    def get_repo_names(self):
        return [repo['name'] for repo in self.__repos]

    def get_repo_stats_this_week(self):
        stats = []
        for reponame in self.get_repo_names():
            # get weekly commit count for the repo owner, total 52 weeks
            url = '/repos/{}/{}/stats/participation'.format(username, reponame)
            weekly_commit_count = self.__get_contents_from(url)['owner']
            
            # get commit count for this week
            commit_count_this_week = weekly_commit_count[-1]
            if commit_count_this_week > 0:
                stats.append((reponame, commit_count_this_week))

        return stats


def main():
    e = Extractor()
    stats = e.get_repo_stats_this_week()
    print(stats)


if __name__ == '__main__':
    main()

