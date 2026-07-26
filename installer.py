import os
import subprocess
import sys


def run_builder():
    print("\nStarting Dara Builder...\n")

    subprocess.run(
        [sys.executable, "main.py"]
    )


def github_connect():

    print("\nGitHub Setup")

    username = input(
        "GitHub username: "
    )

    repo = input(
        "Repository name: "
    )

    branch = input(
        "Branch name (default main): "
    )

    if branch.strip() == "":
        branch = "main"


    url = (
        f"https://github.com/"
        f"{username}/"
        f"{repo}.git"
    )


    print("\nRemote URL:")
    print(url)


    confirm = input(
        "\nAdd this remote? (y/n): "
    )


    if confirm.lower() == "y":

        subprocess.run(
            [
                "git",
                "remote",
                "add",
                "origin",
                url
            ]
        )

        print(
            "GitHub remote added."
        )


def check_requirements():

    print(
        "\nChecking Python..."
    )

    print(
        sys.version
    )


    if os.path.exists(
        "requirements.txt"
    ):

        print(
            "requirements.txt found"
        )

    else:

        print(
            "requirements.txt missing"
        )



def menu():

    while True:

        print(
"""
================================
       Dara Studio Setup
================================

1. Install / Run main.py
2. Connect GitHub Repo
3. Check Requirements
4. Exit

"""
        )


        choice = input(
            "Choose: "
        )


        if choice == "1":

            run_builder()


        elif choice == "2":

            github_connect()


        elif choice == "3":

            check_requirements()


        elif choice == "4":

            print(
                "Goodbye"
            )

            break


        else:

            print(
                "Invalid option"
            )



if __name__ == "__main__":

    menu()
