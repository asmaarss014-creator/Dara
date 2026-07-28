"""
Dara Cloud Sync
GitHub File Downloader
"""

import os
import tempfile


class GitHubDownloader:

    def __init__(self, github_client):
        self.github = github_client


    def download_file(
        self,
        repo_name,
        file_path
    ):

        repo = (
            self.github
            .get_user()
            .get_repo(repo_name)
        )

        content = (
            repo
            .get_contents(file_path)
        )

        temp_dir = tempfile.gettempdir()

        file_location = os.path.join(
            temp_dir,
            content.name
        )

        with open(
            file_location,
            "wb"
        ) as file:

            file.write(
                content.decoded_content
            )

        return file_location