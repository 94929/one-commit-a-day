#!/usr/bin/env python3

from github import Github
from config import access_token


def main():
    g = Github(access_token)

    # type(user) == AuthenticatedUser
    user = g.get_user()

    total_number_of_commits_by_me = 0
    repos = user.get_repos()
    for repo in repos:
        # ignore if curr_repo is not owned by me
        if repo.owner.login != user.login:
            continue
        
        number_of_commits_by_me = 0
        commits = repo.get_commits()
        for c in commits:
            author = c.author

            # github account that no longer exists tends to have none author
            if author is not None and author.login == user.login:
                number_of_commits_by_me += 1
                # type(author) == NamedUser
                #print('author.name:', author.name)
                #print('author.email:', author.email)

        print('For repo: {}, number_of_commits_by_me: {}'.format(
                repo.name, number_of_commits_by_me
            )
        )

        total_number_of_commits_by_me += number_of_commits_by_me
    print('total_number_of_commits_by_me:', total_number_of_commits_by_me)


if __name__ == '__main__':
    main()

