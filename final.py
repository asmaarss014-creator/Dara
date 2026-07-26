"""
Dara Studio Builder
Additional source code storage

Contains remaining generated files.
"""


EXTRA_CODES = {


"lib/core/app.dart": """
import 'package:flutter/material.dart';

import '../workspace/workspace.dart';

import 'theme.dart';



class DaraStudioApp extends StatelessWidget {


  const DaraStudioApp({

    super.key,

  });



  @override

  Widget build(BuildContext context) {


    return MaterialApp(

      title: "Dara Studio",


      debugShowCheckedModeBanner: false,


      theme: AppTheme.dark,


      home: const Workspace(),


    );


  }


}
""",



"lib/workspace/workspace.dart": """
import 'package:flutter/material.dart';



class Workspace extends StatelessWidget {


  const Workspace({

    super.key,

  });



  @override

  Widget build(BuildContext context) {


    return Scaffold(

      body: Center(

        child: Text(

          "Dara Studio Workspace",

        ),

      ),

    );


  }


}
""",



"lib/workspace/explorer.dart": """
class Explorer {


  List<String> files = [];


  void addFile(String file){

    files.add(file);

  }


}
""",



"lib/editor/editor.dart": """
class CodeEditor {


  String content = "";


  void write(String value){

    content = value;

  }


  String read(){

    return content;

  }


}
""",



"lib/editor/tabs.dart": """
class EditorTabs {


  final List<String> tabs = [];


  void open(String file){

    tabs.add(file);

  }


}
""",



"lib/terminal/terminal.dart": """
class Terminal {


  List<String> history = [];


  void execute(String command){

    history.add(command);

  }


}
""",



"lib/terminal/output.dart": """
class TerminalOutput {


  final List<String> lines = [];


  void add(String text){

    lines.add(text);

  }


}
""",



"lib/settings/settings.dart": """
class Settings {


  bool darkMode = true;


  String fontFamily =
      "JetBrains Mono";


}
""",



"lib/templates/templates.dart": """
class Templates {


  List<String> available = [

    "Flutter",

    "Python",

    "HTML"

  ];


}
""",



"lib/extensions/extensions.dart": """
class Extensions {


  List<String> installed = [];


  void install(String name){

    installed.add(name);

  }


}
""",



"lib/shared/helpers.dart": """
class Helpers {


  static String cleanPath(
      String path
  ){

    return path.trim();

  }


}
""",



"lib/shared/widgets.dart": """
import 'package:flutter/material.dart';



class DaraCard extends StatelessWidget {


  final Widget child;


  const DaraCard({

    super.key,

    required this.child,

  });



  @override

  Widget build(BuildContext context){


    return Card(

      child: child,

    );


  }


}
"""

}