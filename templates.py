# templates.py

TEMPLATES = {
    "README.md": """# Dara Studio

A lightweight, high-performance Android code editor.
""",

    ".gitignore": """
.gradle/
build/
.idea/
*.iml
local.properties
""",

    "settings.gradle.kts": """
rootProject.name = "DaraStudio"
include(":app")
""",

    "build.gradle.kts": """
plugins {
    id("com.android.application") version "8.0.0" apply false
    id("org.jetbrains.kotlin.android") version "2.0.0" apply false
}
""",

    "app/src/main/AndroidManifest.xml": """
<?xml version="1.0" encoding="utf-8"?>
<manifest package="com.darastudio"/>
""",

    "app/src/main/kotlin/com/darastudio/MainActivity.kt": """
package com.darastudio

import androidx.activity.ComponentActivity

class MainActivity : ComponentActivity()
""",
}