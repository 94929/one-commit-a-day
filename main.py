#!/usr/bin/env python3

from github import Github
from config import access_token

from config import base

def notify_me(me, result):
    """
    Notify current user by email regarding the result

    :param me: AuthenticatedUser
    :param result: int
    """

    pass


def get_total_number_of_commits_by_me(me):
    """
    Returns total number of commits by a given user

    :param me: AuthenticatedUser
    :rtype: int
    """

    total_number_of_commits_by_me = 0
    for repo in me.get_repos():

        # ignore if curr_repo is not owned by me
        if repo.owner.login != me.login:
            continue

        number_of_commits_by_me = 0
        for commit in repo.get_commits():

            # github account that no longer exists tends to have none author
            # accummulate commits that owned by me
            if commit.author is not None and commit.author.login == me.login:
                number_of_commits_by_me += 1

        print('For repo: {}, number_of_commits_by_me: {}'.format(
                repo.name, number_of_commits_by_me
            )
        )

        total_number_of_commits_by_me += number_of_commits_by_me

    return total_number_of_commits_by_me


def main():
    # type(g) == GithubObject
    gh = Github(access_token)

    # type(user) == AuthenticatedUser
    user = gh.get_user()

    total_number_of_commits_by_me = get_total_number_of_commits_by_me(user)
    print('total_number_of_commits_by_me:', total_number_of_commits_by_me)


if __name__ == '__main__':
    main()

