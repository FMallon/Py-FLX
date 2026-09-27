from flx.scripts.get_editor_data import Editor
from flx.scripts.validate_lua_config_data import validate_executable_entries


def set_editor_data() -> Editor:

    editor = Editor()

    editor.editor_name = set_editor_name(editor.get_editor_name())

    if editor.editor_name is not None:
        editor.editor_args = set_editor_args(editor.get_editor_args())

    return editor


def set_editor_name(editor_name: str) -> str | None:

    if editor_name == "" or editor_name == "nil":
        print("\n[INFO] Editor name is empty, resorting to defaults!\n")
        return None

    return_code = validate_executable_entries(editor_name)

    if return_code != 0:
        print("\n[INFO] Invalid Editor chosen, resorting to defaults!\n")
        return None

    return editor_name


def set_editor_args(editor_args: list[str]) -> list[str] | None:

    if len(editor_args) == 0:
        return None

    return editor_args