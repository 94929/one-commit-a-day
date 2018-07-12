#!/usr/bin/env python3

from github import Github
from config import access_token


def main():
    # type(g) == GithubObject
    gh = Github(access_token)

    # type(user) == AuthenticatedUser
    user = gh.get_user()

    total_number_of_commits_by_me = 0
    repos = user.get_repos()
    for repo in repos:
        # ignore if curr_repo is not owned by me
        if repo.owner.login != user.login: continue
        #print('repo.name:', repo.name)
        
        number_of_commits_by_me = 0
        commits = repo.get_commits()

        # type(commit) == Commit
        for commit in commits:
            #print('commit:', commit)

            # github account that no longer exists tends to have none author
            # accummulate commits that owned by me
            author = commit.author  # type(author) == NamedUser
            if author is not None and author.login == user.login:
                number_of_commits_by_me += 1

        print('For repo: {}, number_of_commits_by_me: {}'.format(
                repo.name, number_of_commits_by_me
            )
        )

        total_number_of_commits_by_me += number_of_commits_by_me
    print('Total_number_of_commits_by_me:', total_number_of_commits_by_me)


if __name__ == '__main__':
    main()

