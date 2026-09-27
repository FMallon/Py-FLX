from flx.scripts.paths import FILE_LUA_CONFIG, FILE_LUA_QUERY
import subprocess

class Editor:

    def get_editor_name(self) -> str:

        return subprocess.run(
            [
                "lua",
                str(FILE_LUA_QUERY),
                "get_editor_name",
                str(FILE_LUA_CONFIG),
            ],
            capture_output=True,
            text=True
        ).stdout.strip()



    def get_editor_args(self) -> list[str]:

        output =  subprocess.run(
            [
                "lua",
                str(FILE_LUA_QUERY),
                "get_editor_args",
                str(FILE_LUA_CONFIG),
            ],
            capture_output=True,
            text=True
        ).stdout.strip()

        return output.splitlines()
