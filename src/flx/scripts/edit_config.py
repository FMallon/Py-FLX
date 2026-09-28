from flx.scripts.set_editor_data import set_editor_data
from flx.scripts.validation import Validation
from flx.scripts.paths import FILE_LUA_CONFIG
from pathlib import Path

import subprocess

def check_config_exists(file: Path) -> int:

    return_code = Validation.file_exists(file)

    if return_code != 0:

        print("\nYou can generate a default config using --generate-default-config\n")
        raise SystemExit(11)

    return 0


def edit_config_user() -> int:

    editor = set_editor_data()

    if editor.editor_name is None:
        return 1

    cmd_run_editor: list[str] = []

    cmd_run_editor.append(editor.editor_name)

    if editor.editor_args is not None:
        cmd_run_editor.extend(editor.editor_args)

    cmd_run_editor.append(FILE_LUA_CONFIG)

    cmd = subprocess.run(cmd_run_editor)

    if cmd.returncode != 0:
        return 19

    return 0
    

    

def edit_config_default(check_config: bool = True) -> int:

    if check_config:
        check_config_exists(FILE_LUA_CONFIG)

    editors = [
        "nano", 
        "nvim", 
        "neovim",
        "emacs",
        "vim"
        "vi",
        ]

    editor_to_use: str | None = None

    for editor in editors:

        if Validation.is_a_command(editor) == 0:
            editor_to_use = editor
            break


    if editor_to_use is None:
        print("\n[ERROR] No supported editor found !\n")
        raise SystemExit(18)

    cmd_run_editor: list[str] = []

    cmd_run_editor.append(editor_to_use)
    cmd_run_editor.append(FILE_LUA_CONFIG)

    cmd = subprocess.run(cmd_run_editor)

    if cmd.returncode != 0:
        return 19

    return 0
    



def edit_config():

    check_config_exists(FILE_LUA_CONFIG)
    
    return_code = edit_config_user()

    if return_code != 0:
        edit_config_default(check_config = False)