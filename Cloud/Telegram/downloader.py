from github.download import GitHubDownloader


class TelegramDownloader:

    def __init__(
        self,
        repository_manager,
        github_client
    ):

        self.repo_manager = repository_manager
        self.file_downloader = GitHubDownloader(
            github_client
        )


    async def send_file(
        self,
        update,
        repo_name,
        file_path
    ):

        query = update.callback_query

        await query.edit_message_text(
            "Preparing file..."
        )


        try:

            file = (
                self.file_downloader
                .download_file(
                    repo_name,
                    file_path
                )
            )


            await query.message.reply_document(
                document=open(
                    file,
                    "rb"
                )
            )


        except Exception as error:

            await query.message.reply_text(
                "Download failed.\n"
                "Please try again."
            )

            print(error)