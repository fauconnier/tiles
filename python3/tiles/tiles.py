import os
import vim
from typing import Dict

WINDOW_CODE = "code"
WINDOW_CONSOLE = "console"
WINDOW_OUTPUT = "output"
WINDOW_SHELL = "shell"
WINDOW_STACK = "stack"
WINDOW_VARIABLE = "variables"
WINDOW_UNKNOWN = "unknown"

class Tiles:

    def _append_dict(self, index: Dict, name: str, window_number: int):
        var = index.get(name, [])
        var.append(window_number)
        index[name] = var
        return index

    def _equalize_code_windows(self):
        name_to_numbers, numbers_to_name = self.index_window()
        code_windows = name_to_numbers.get(WINDOW_CODE, [])


    def index_window(self) -> Dict:
        name_to_numbers = dict()
        numbers_to_name = dict()

        # Indexing Vimspector window
        for w in vim.windows:
            if "Variables" in str(w.buffer):
                name_to_numbers = self._append_dict(name_to_numbers, WINDOW_VARIABLE, w.number)
                numbers_to_name[w.number] = WINDOW_VARIABLE
            elif "StackTrace" in str(w.buffer):
                name_to_numbers = self._append_dict(name_to_numbers, WINDOW_STACK, w.number)
                numbers_to_name[w.number] = WINDOW_STACK
            elif "Console" in str(w.buffer):
                name_to_numbers = self._append_dict(name_to_numbers, WINDOW_CONSOLE, w.number)
                numbers_to_name[w.number] = WINDOW_CONSOLE
            elif "miniconda3" in str(w.buffer) or "bin/dlv" in str(w.buffer):
                name_to_numbers = self._append_dict(name_to_numbers, WINDOW_OUTPUT, w.number)
                numbers_to_name[w.number] = WINDOW_OUTPUT
            elif "bin/zsh" in str(w.buffer):
                name_to_numbers = self._append_dict(name_to_numbers, WINDOW_SHELL, w.number)
                numbers_to_name[w.number] = WINDOW_SHELL

        # Indexing code windows
        stack_number = name_to_numbers.get(WINDOW_STACK, [0])[0]
        output_number = name_to_numbers.get(WINDOW_OUTPUT, [0])[0]
        for w in vim.windows:
            if w.number > stack_number and w.number < output_number:
                name_to_numbers = self._append_dict(name_to_numbers, WINDOW_CODE, w.number)
                numbers_to_name[w.number] = WINDOW_CODE

        return name_to_numbers, numbers_to_name

    def show_display(self) -> None:
        number_of_lines = int(vim.eval("&lines"))
        print(f"number of lines: {number_of_lines}")
        name_to_numbers, numbers_to_name = self.index_window()
        print(name_to_numbers)
        print(numbers_to_name)
        for w in vim.windows:
            name = numbers_to_name.get(w.number, WINDOW_UNKNOWN)
            print(f"name: {name}")
            print(f"buf: {w.buffer}")
            print(f"height: {w.height}")
            print(f"width: {w.width}")

    def vimspector_base_display(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
            return None

        name_to_numbers, numbers_to_name = self.index_window()
        number_of_lines = int(vim.eval("&lines"))
        if number_of_lines < 60:
            # Small display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 34
                    w.width = 40
                elif name is WINDOW_STACK:
                    w.height = 10
                    w.width = 40
                elif name is WINDOW_OUTPUT:
                    w.height = 35
                    w.width = 80
                elif name is WINDOW_CONSOLE:
                    w.height = 10
                    w.width = 92
                elif name is WINDOW_SHELL:
                    w.height = 11
                    w.width = 80
        else:
            # larger display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 59
                    w.width = 55
                elif name is WINDOW_STACK:
                    w.height = 14
                    w.width = 55
                elif name is WINDOW_OUTPUT:
                    w.height = 60
                    w.width = 144
                elif name is WINDOW_CONSOLE:
                    w.height = 14
                    w.width = 163
                elif name is WINDOW_SHELL:
                    w.height = 15
                    w.width = 144

    def vimspector_code_focus(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
            return None

        name_to_numbers, numbers_to_name = self.index_window()
        number_of_lines = int(vim.eval("&lines"))
        if number_of_lines < 60:
            # Small display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 38
                    w.width = 32
                elif name is WINDOW_STACK:
                    w.height = 6
                    w.width = 32
                elif name is WINDOW_OUTPUT:
                    w.height = 39
                    w.width = 59
                elif name is WINDOW_CONSOLE:
                    w.height = 6
                    w.width = 121
                elif name is WINDOW_SHELL:
                    w.height = 7
                    w.width = 59
        else:
            # larger display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 59
                    w.width = 35
                elif name is WINDOW_STACK:
                    w.height = 14
                    w.width = 35
                elif name is WINDOW_OUTPUT:
                    w.height = 60
                    w.width = 93
                elif name is WINDOW_CONSOLE:
                    w.height = 14
                    w.width = 234
                elif name is WINDOW_SHELL:
                    w.height = 15
                    w.width = 93

    def vimspector_code_big_focus(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
            return None

        name_to_numbers, numbers_to_name = self.index_window()
        number_of_lines = int(vim.eval("&lines"))
        if number_of_lines < 60:
            # Small display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 40
                    w.width = 12
                elif name is WINDOW_STACK:
                    w.height = 4
                    w.width = 12
                elif name is WINDOW_OUTPUT:
                    w.height = 41
                    w.width = 42
                elif name is WINDOW_CONSOLE:
                    w.height = 4
                    w.width = 158
                elif name is WINDOW_SHELL:
                    w.height = 5
                    w.width = 42
        else:
            # Larger display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 67
                    w.width = 19
                elif name is WINDOW_STACK:
                    w.height = 6
                    w.width = 19
                elif name is WINDOW_OUTPUT:
                    w.height = 68
                    w.width = 77
                elif name is WINDOW_CONSOLE:
                    w.height = 6
                    w.width = 256
                elif name is WINDOW_SHELL:
                    w.height = 7
                    w.width = 76

    def vimspector_variable_focus(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
            return None

        name_to_numbers, numbers_to_name = self.index_window()
        number_of_lines = int(vim.eval("&lines"))
        if number_of_lines < 60:
            # Small display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 34
                    w.width = 67
                elif name is WINDOW_STACK:
                    w.height = 10
                    w.width = 67
                elif name is WINDOW_OUTPUT:
                    w.height = 35
                    w.width = 80
                elif name is WINDOW_CONSOLE:
                    w.height = 10
                    w.width = 65
                elif name is WINDOW_SHELL:
                    w.height = 11
                    w.width = 80
        else:
            # Larger display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 59
                    w.width = 94
                elif name is WINDOW_STACK:
                    w.height = 14
                    w.width = 94
                elif name is WINDOW_OUTPUT:
                    w.height = 60
                    w.width = 126
                elif name is WINDOW_CONSOLE:
                    w.height = 14
                    w.width = 143
                elif name is WINDOW_SHELL:
                    w.height = 15
                    w.width = 125


    def vimspector_stack_focus(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
            return None

        name_to_numbers, numbers_to_name = self.index_window()
        number_of_lines = int(vim.eval("&lines"))
        if number_of_lines < 60:
            # Small display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 6
                    w.width = 67
                elif name is WINDOW_STACK:
                    w.height = 38
                    w.width = 67
                elif name is WINDOW_OUTPUT:
                    w.height = 35
                    w.width = 80
                elif name is WINDOW_CONSOLE:
                    w.height = 10
                    w.width = 65
                elif name is WINDOW_SHELL:
                    w.height = 11
                    w.width = 80
        else:
            # Larger display
            for w in vim.windows:
                name = numbers_to_name.get(w.number, WINDOW_UNKNOWN + "_" + str(w.buffer))
                if name is WINDOW_VARIABLE:
                    w.height = 19
                    w.width = 94
                elif name is WINDOW_STACK:
                    w.height = 54
                    w.width = 94
                elif name is WINDOW_OUTPUT:
                    w.height = 60
                    w.width = 126
                elif name is WINDOW_CONSOLE:
                    w.height = 14
                    w.width = 143
                elif name is WINDOW_SHELL:
                    w.height = 15
                    w.width = 125
