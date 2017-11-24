import sublime, sublime_plugin

import os

class FindCppHeaderSourceCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        current_file = self.view.file_name()

        if current_file is None:
            return

        filename, file_extension = os.path.splitext(current_file)

        go_to_file = None

        if file_extension == '.cpp' or file_extension == '.c':
            go_to_file = filename + '.h'
        elif file_extension == '.h':
            go_to_file = filename + '.cpp'
            if not os.path.isfile(go_to_file):
                go_to_file = filename + '.c'

        where_to_search = current_file

        if not go_to_file is None:
            where_to_search = where_to_search + ',' + go_to_file

        self.view.window().run_command("show_panel", {"panel": "find_in_files", "where": where_to_search})

class SwitchHeaderSourceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        current_file = self.view.file_name()

        if current_file is None:
            return
        
        filename, file_extension = os.path.splitext(current_file)

        go_to_file = None

        if file_extension == '.cpp' or file_extension == '.c':
            go_to_file = filename + '.h'
        elif file_extension == '.h':
            go_to_file = filename + '.cpp'
            if not os.path.isfile(go_to_file):
                go_to_file = filename + '.c'

        if go_to_file is None or not os.path.isfile(go_to_file):
            return

        print("SwitchHeaderSourceCommand  " + str(go_to_file))
        self.view.window().open_file(go_to_file)



