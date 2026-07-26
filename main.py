"""
Dara Studio Builder v1.0

Main project generator.
Works with Termux, Linux and Windows.
"""


import os


from files import (
    PROJECT_NAME,
    FOLDERS,
    FILES
)


from rest import CODES


from final import EXTRA_CODES




def create_folder(path):

    os.makedirs(
        path,
        exist_ok=True
    )




def write_file(path, content):

    folder = os.path.dirname(path)


    if folder:

        create_folder(folder)


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)




def prepare_project():


    print()

    print(
        "Creating folders..."
    )


    for folder in FOLDERS:


        create_folder(

            os.path.join(

                PROJECT_NAME,

                folder

            )

        )



    print(
        "Folders complete"
    )




def generate_files():


    print()

    print(
        "Writing files..."
    )


    all_codes = {}


    all_codes.update(
        CODES
    )


    all_codes.update(
        EXTRA_CODES
    )



    for file_name in FILES:


        content = all_codes.get(

            file_name,

            "// File created by Dara Studio Builder"

        )


        write_file(

            os.path.join(

                PROJECT_NAME,

                file_name

            ),

            content

        )



        print(

            "[+]",

            file_name

        )




def main():


    print("""
================================

       Dara Studio Builder

              v1.0

================================
""")


    prepare_project()


    generate_files()



    print()

    print(
        "Dara Studio project created successfully."
    )


    print(
        "Location:",
        PROJECT_NAME
    )




if __name__ == "__main__":

    main()