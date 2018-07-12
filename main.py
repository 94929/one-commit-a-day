#!/usr/bin/env python3

from github import Github
from config import access_token


def main():
    g = Github(access_token)
    user = g.get_user()  # auth-ed user
    repos = user.get_repos()

    total_number_of_commits_by_me = 0
    for idx, repo in enumerate(repos):
        # ignore if curr_repo is not owned by me
        #if repo.author != me:
        #    continue
        
        #print('repo.name:', repo.name)
        #print('repo.description:', repo.description)

        commits = repo.get_commits()
        number_of_commits_by_me = 0
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

