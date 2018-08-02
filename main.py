#!/usr/bin/env python3

from extractor import Extractor
from sender import Sender


def notify_me(recipient):
    """ sends me an email saying that I might miss a commit for today """
    
    Sender(recipient).send()


def has_valid_event():
    """ checks if there is a push event created by me today """
    
    return len(Extractor().events) != 0


def main():
    # do nothing if there is a pushed commit today
    if has_valid_event():
        return 

    # email me
    notify_me(Extractor().email)

    
if __name__ == '__main__':
    main()

