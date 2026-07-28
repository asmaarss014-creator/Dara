elif query.data.startswith("repo:"):

    repo_name = (
        query.data
        .replace(
            "repo:",
            ""
        )
    )


    await downloader.show_files(
        update,
        repo_name
    )


elif query.data.startswith("file:"):

    data = query.data.split(":")

    repo_name = data[1]

    file_path = data[2]


    await downloader.send_file(
        update,
        repo_name,
        file_path
    )