"""
Dara Cloud Sync
GitHub Authentication
"""

from github import Github
from config import GITHUB_TOKEN


class GitHubAuth:

    def __init__(self):
        self.client = None
        self.user = None


    def connect(self):

        if not GITHUB_TOKEN:
            raise Exception(
                "GitHub token is missing. Add it in config.py"
            )

        try:
            self.client = Github(
                GITHUB_TOKEN
            )

            self.user = (
                self.client
                .get_user()
            )

            return True

        except Exception as error:

            print(
                "GitHub connection failed:",
                error
            )

            return False


    def username(self):

        if self.user:
            return self.user.login

        return None