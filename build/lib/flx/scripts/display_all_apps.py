from flx.scripts.paths import FILE_LUA_CONFIG, FILE_LUA_QUERY
from flx.scripts.validation import Validation
import subprocess


def get_all_app_names() -> list[str] | None:

    if Validation.file_exists(FILE_LUA_CONFIG) != 0:
        print("\n")
        raise SystemExit(11)

    output = subprocess.run(
        [
            "lua",
            FILE_LUA_QUERY,
            "get_all_app_names",
            FILE_LUA_CONFIG
        ],
        capture_output=True,
        text=True
    ).stdout.strip()


    output = output.splitlines()

    if len(output) == 0:
        print("\n[INFO] There are no apps in the Config to display\n")
        return None

    return output


def get_all_gui_app_names():

    if Validation.file_exists(FILE_LUA_CONFIG) != 0:
            print("\n")
            raise SystemExit(11)

    output = subprocess.run(
        [
            "lua",
            FILE_LUA_QUERY,
            "get_all_gui_app_names",
            FILE_LUA_CONFIG
        ],
        capture_output=True,
        text=True
    ).stdout.strip()


    output = output.splitlines()

    if len(output) == 0:
        print("\n[INFO] There are no apps in the Config to display\n")
        return []

    return output


def display_all_apps() -> int:

    from flx.scripts.display_app import display_app

    apps = get_all_app_names()

    if apps is None:
        return 0

    for app in apps:

        try:
            display_app(app)

        except SystemExit:
            print(f"[INFO] Skipping invalid app: {app}")

    return 0