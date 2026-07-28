"""
Dara Cloud Sync
GitHub Repository Manager
"""


class RepositoryManager:


    def __init__(self, github_client):

        self.github = github_client



    def list_repositories(self):

        repositories = []

        for repo in self.github.get_user().get_repos():

            repositories.append(
                {
                    "name": repo.name,
                    "full_name": repo.full_name
                }
            )

        return repositories



    def get_repository_files(
        self,
        repo_name,
        path=""
    ):

        repo = (
            self.github
            .get_user()
            .get_repo(repo_name)
        )


        contents = (
            repo
            .get_contents(path)
        )


        files = []


        for item in contents:

            files.append(
                {
                    "name": item.name,
                    "path": item.path,
                    "type": item.type
                }
            )


        return files