from flx.scripts.get_app_data import App
from flx.scripts.validate_lua_config_data import validate_executable_entries



def set_app_data(alias: str, quiet=False) -> App:

    app = App(alias)

    app.name = set_app_name(app)
    app.target = set_app_target(app, quiet)
    app.args = set_app_args(app)
    app.background = set_app_background(app)
    app.wrapper = set_app_wrapper(app, quiet)
    app.wrapper_args = set_app_wrapper_args(app)
    app.gui = set_app_gui(app)
    app.image = set_app_image(app)

    return app



def set_app_name(app: App) -> str:

    return app.get_app_name()



def set_app_target(app: App, quiet = False) -> str:

    target = app.get_app_target()

    return_code = validate_executable_entries(target)

    if return_code != 0:
        if not quiet:
            print(f"[ERROR] The target {target} is not a valid executable!")
        raise SystemExit(return_code)

    return target



def set_app_args(app: App) -> list[str] | None:

    args = app.get_app_args()

    if not args:
        return None

    return args



def set_app_background(app: App) -> bool:

    background = app.get_app_background()

    if background.lower() == "true":
        return True
    else:
        return False



def set_app_wrapper(app: App, quiet = False) -> str | None:

    wrapper = app.get_app_wrapper()

    if wrapper == "nil" or not wrapper:
        return None

    return_code = validate_executable_entries(wrapper)

    if return_code != 0:
        if not quiet:
            print(f"[ERROR] The wrapper {wrapper} is not a valid executable!")
        raise SystemExit(return_code)

    return wrapper



def set_app_wrapper_args(app: App) -> list[str] | None:

    wrapper_args = app.get_app_wrapper_args()

    if not wrapper_args:
        return None

    return wrapper_args



def set_app_gui(app: App) -> bool:

    gui = app.get_app_gui()

    if gui.lower() == "true":
        return True
    else:
        return False


def set_app_image(app: App) -> str | None:

    from pathlib import Path
    from flx.scripts.validation import Validation

    image = app.get_app_image()

    if not image or image == "nil":
        return None

    image = Path(image)

    if Validation.validate_image(image) != 0:
        return None

    return str(image)