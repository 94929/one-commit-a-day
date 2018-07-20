import sys
import json
import requests

from datetime import datetime
from dateutil.parser import parse

from config import base
from config import headers


class Extractor:
    """ This class extracts github informations from the api server """

    ##################################
    # Constructor methods come below #
    ##################################

    def __init__(self):
        # init user info that are belong to me
        self.__user = self.__init_user('/user')
        self.__login = self.__user['login']
        self.__email = self.__user['email']

        # init repos that are owned by me
        self.__repos = self.__init_repos('/user/repos')

        # init push events that are owned by me
        self.__events = (
                self.__init_events('/users/{}/events'.format(self.__login))
            )

    def __init_user(self, url):
        """ Init all user informations of mine in Github """
        user = self.__get_contents_from(url)
        return user

    def __init_repos(self, url):
        """ Init all (public + private) repos owned by me """
        repos = self.__get_contents_from(url)
        repos_of_mine = (
                [r for r in repos if r['owner']['login'] == self.__login]
            )
        return repos_of_mine

    def __init_events(self, url):
        """ Init all recent events (push commit) owned by me """
        
        # create a container which will contain all recent push events by me
        recent_push_events_by_me = []

        # iterate for each events
        events = self.__get_contents_from(url)
        for event in events:

            # 1. is this created today
            if (parse(event['created_at']).date() != datetime.now().date()):
                continue
            
            # 2. is this a push event
            # 3. is this created by me
            if (event['type'] == 'PushEvent' 
                    and event['actor']['login'] == self.__login):

                # if all conditions satisfied, append to the container
                recent_push_events_by_me.append(event)

        return recent_push_events_by_me

    ###################################
    # HTTP Request methods come below #
    ###################################

    def __get(self, url):
        addr = base + url
        print('Performing GET HTTP request to:', addr)
        r = requests.get(base+url, headers=headers)
        if not r.ok:
            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print(e)
                sys.exit(1)
        print('Received GET HTTP response from:', addr)
        return r

    def __get_contents_from(self, url):
        r = self.__get(url)
        contents = json.loads(r.content)
        return contents

    #############################
    # Getter methods come below #
    #############################

    @property
    def login(self):
        return self.__login

    @property
    def email(self):
        return self.__email

    @property
    def repos(self):
        return self.__repos

    @property
    def events(self):
        return self.__events

    ##################################
    # Algorithmic methods come below #
    ##################################

    def get_repo_names(self):
        return [repo['name'] for repo in self.__repos]

    # testing method
    def f(self):
        contents = self.__get_contents_from('/user')
        print(json.dumps(contents, indent=4))

