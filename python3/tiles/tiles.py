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
            elif "miniconda3" in str(w.buffer):
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
        name_to_numbers, numbers_to_name = self.index_window()
        print(name_to_numbers)
        print(numbers_to_name)
        for w in vim.windows:
            name = numbers_to_name.get(w.number, WINDOW_UNKNOWN)
            print(f"name: {name}")
            print(f"height: {w.height}")
            print(f"width: {w.width}")

    def vimspector_base_display(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
        
        name_to_numbers, numbers_to_name = self.index_window()
        for w in vim.windows:
            name = numbers_to_name.get(w.number, WINDOW_UNKNOWN)
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

    def vimspector_code_focus(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
        
        name_to_numbers, numbers_to_name = self.index_window()
        for w in vim.windows:
            name = numbers_to_name.get(w.number, WINDOW_UNKNOWN)
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


    def vimspector_code_big_focus(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
        
        name_to_numbers, numbers_to_name = self.index_window()
        for w in vim.windows:
            name = numbers_to_name.get(w.number, WINDOW_UNKNOWN)
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
                w.width = 141
            elif name is WINDOW_SHELL:
                w.height = 5
                w.width = 59


    def vimspector_variable_focus(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
        
        name_to_numbers, numbers_to_name = self.index_window()
        for w in vim.windows:
            name = numbers_to_name.get(w.number, WINDOW_UNKNOWN)
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


    def vimspector_stack_focus(self) -> None:
        if len(vim.windows) < 5:
            print("Nothing to re-tiles")
        
        name_to_numbers, numbers_to_name = self.index_window()
        for w in vim.windows:
            name = numbers_to_name.get(w.number, WINDOW_UNKNOWN)
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
