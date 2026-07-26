import os
import subprocess
import sys


def install_builder():

    print("\nInstalling Dara Builder...\n")

    required = [
        "main.py",
        "files.py",
        "rest.py",
        "final.py"
    ]

    missing = []

    for file in required:
        if not os.path.exists(file):
            missing.append(file)

    if missing:
        print("Missing files:")
        for item in missing:
            print("-", item)
    else:
        print("Dara Builder installed successfully.")
        print("Run: python main.py")



def add_to_repo():

    print("\nAdding files to Dara repository...\n")

    subprocess.run(
        "git add .",
        shell=True
    )

    message = input(
        "Commit message: "
    )

    subprocess.run(
        f'git commit -m "{message}"',
        shell=True
    )

    print(
        "Files added to repository."
    )



def connect_github():

    print("\nGitHub Connection\n")

    username = input(
        "GitHub username: "
    )

    repo = input(
        "Repository name: "
    )


    url = (
        f"https://github.com/"
        f"{username}/"
        f"{repo}.git"
    )


    print(
        "\nRepository:"
    )

    print(url)


    confirm = input(
        "Connect? (y/n): "
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
            "GitHub connected."
        )



def create_requirements():

    print(
        "\nCreating requirements.txt..."
    )


    content = """# Dara Studio Builder

# Uses Python standard library only
"""


    with open(
        "requirements.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)


    print(
        "requirements.txt created."
    )



def menu():

    while True:

        print(
"""
================================
       Dara Studio Setup
================================

1. Install Dara Builder
2. Add to Dara Repo
3. Connect GitHub
4. Create requirements.txt
5. Exit

"""
        )


        choice = input(
            "Choose: "
        )


        if choice == "1":
            install_builder()

        elif choice == "2":
            add_to_repo()

        elif choice == "3":
            connect_github()

        elif choice == "4":
            create_requirements()

        elif choice == "5":
            print("Exit")
            break

        else:
            print("Invalid option")



if __name__ == "__main__":
    menu()
