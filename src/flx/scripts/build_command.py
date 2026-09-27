from flx.scripts.set_app_data import set_app_data

def build_command(alias: str, extra_args: list[str]) -> tuple[list[str], bool]:

    app = set_app_data(alias)

    cmd: list[str] = []

    # Wrapper - Optional
    if app.wrapper is not None:
        cmd.append(app.wrapper)

    # Wrapper Arguments
    if app.wrapper_args is not None:
        cmd.extend(app.wrapper_args)

    # Target - Required
    cmd.append(app.target)

    # Target Args - Optional
    if app.args is not None:
        cmd.extend(app.args)

    # Extra Args  - Optional: args defined during runtime
    if len(extra_args) > 0:

        cmd.extend(extra_args)


    return cmd, app.background