from flx.scripts.paths import FILE_LUA_CONFIG, FILE_LUA_QUERY

import subprocess


class App:


    def __init__(self, alias: str):
        self.alias = alias



    def get_app_name(self) -> str:

        result = subprocess.run(
        [
            "lua",
            str(FILE_LUA_QUERY),
            "get_app_name",
            str(FILE_LUA_CONFIG),
            self.alias
        ],
        capture_output=True,
        text=True
        )

        if result.returncode != 0:
            print(result.stderr)
            raise SystemExit(result.returncode)

        return result.stdout.strip()



    def get_app_target(self) -> str:
        
        return subprocess.run(
            [
                "lua",
                str(FILE_LUA_QUERY),
                "get_app_target",
                str(FILE_LUA_CONFIG),
                self.alias
            ],
            capture_output=True,
            text=True
        ).stdout.strip()



    def get_app_args(self) -> list[str]:

        output = subprocess.run(
            [
                "lua",
                str(FILE_LUA_QUERY),
                "get_app_args",
                str(FILE_LUA_CONFIG),
                self.alias
            ],
            capture_output=True,
            text=True
        ).stdout.strip()

        return output.splitlines()


    def get_app_background(self) -> str:

        output = subprocess.run(
            [
                "lua",
                str(FILE_LUA_QUERY),
                "get_app_background",
                str(FILE_LUA_CONFIG),
                self.alias
            ],
            capture_output=True,
            text=True
        ).stdout.strip()

        return output


    def get_app_wrapper(self) -> str:

        return subprocess.run(
            [
                "lua",
                str(FILE_LUA_QUERY),
                "get_app_wrapper",
                str(FILE_LUA_CONFIG),
                self.alias
            ],
            capture_output=True,
            text=True
        ).stdout.strip()


    def get_app_wrapper_args(self) -> list[str]:
        output = subprocess.run(
        [
            "lua",
            str(FILE_LUA_QUERY),
            "get_app_wrapper_args",
            str(FILE_LUA_CONFIG),
            self.alias
        ],
            capture_output=True,
            text=True
        ).stdout.strip()

        return output.splitlines()