#!/usr/bin/env python3

from github import Github
from config import access_token


def main():
    g = Github(access_token)


if __name__ == '__main__':
    main()

