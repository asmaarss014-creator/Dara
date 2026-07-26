"""
Dara Studio Builder
Project structure definition

This file contains folders and file names only.
"""

PROJECT_NAME = "DaraStudio"


FOLDERS = [

    "lib",

    "lib/core",
    "lib/workspace",
    "lib/editor",
    "lib/terminal",
    "lib/settings",
    "lib/templates",
    "lib/extensions",
    "lib/shared",

    "assets",
    "assets/icons",
    "assets/images",
    "assets/fonts",

    "templates",
    "extensions",
    "projects",
    "storage",
    "docs"

]


FILES = [

    "pubspec.yaml",
    "README.md",

    "lib/main.dart",


    # Core

    "lib/core/app.dart",
    "lib/core/config.dart",
    "lib/core/theme.dart",
    "lib/core/controller.dart",
    "lib/core/state.dart",
    "lib/core/storage.dart",
    "lib/core/services.dart",
    "lib/core/constants.dart",


    # Workspace

    "lib/workspace/workspace.dart",
    "lib/workspace/explorer.dart",
    "lib/workspace/project.dart",
    "lib/workspace/file_manager.dart",


    # Editor

    "lib/editor/editor.dart",
    "lib/editor/tabs.dart",
    "lib/editor/document.dart",
    "lib/editor/syntax.dart",


    # Terminal

    "lib/terminal/terminal.dart",
    "lib/terminal/runner.dart",
    "lib/terminal/output.dart",


    # Settings

    "lib/settings/settings.dart",
    "lib/settings/preferences.dart",


    # Templates

    "lib/templates/templates.dart",
    "lib/templates/template_manager.dart",


    # Extensions

    "lib/extensions/extensions.dart",
    "lib/extensions/extension_manager.dart",


    # Shared

    "lib/shared/widgets.dart",
    "lib/shared/helpers.dart",
    "lib/shared/constants.dart"

]