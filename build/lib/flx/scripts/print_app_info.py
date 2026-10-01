from flx.scripts.set_app_data import set_app_data


def print_app_info(alias: str) -> None:

    app = set_app_data(alias)

    # -------------------------------------------------------------------------
    # Format normal arguments
    # -------------------------------------------------------------------------

    formatted_args = ""

    if app.args is not None:

        for i, arg in enumerate(app.args):

            if i > 0:

                formatted_args += ", "

            formatted_args += f'"{arg}"'

    # -------------------------------------------------------------------------
    # Format wrapper arguments
    # Only display them when a wrapper actually exists.
    # -------------------------------------------------------------------------

    formatted_wrapper_args = ""

    if app.wrapper is not None and app.wrapper_args is not None:

        for i, arg in enumerate(app.wrapper_args):

            if i > 0:

                formatted_wrapper_args += ", "

            formatted_wrapper_args += f'"{arg}"'

    # -------------------------------------------------------------------------
    # Format background
    # -------------------------------------------------------------------------

    background = str(app.background)

    if app.gui:

        background += " (overridden by GUI to True)"

    # -------------------------------------------------------------------------
    # Format image
    # -------------------------------------------------------------------------

    image = app.image if app.image is not None else "None"

    # -------------------------------------------------------------------------
    # Calculate table width
    # -------------------------------------------------------------------------

    label_width = 14
    value_width = 59
    total_width = label_width + value_width + 5

    line = "─" * total_width

    # -------------------------------------------------------------------------
    # Application header
    # -------------------------------------------------------------------------

    print()

    print(f"╭{line}╮")

    header_left = (total_width + 12) // 2
    header_right = (total_width - 12) // 2

    print(f"│{'APPLICATION':>{header_left}}{'':>{header_right}}│")

    print(f"├{line}┤")

    # -------------------------------------------------------------------------
    # Application data
    # -------------------------------------------------------------------------

    print(
        f"│ {'Name':<{label_width}} │ "
        f"{app.name:<{value_width}} │"
    )


    if app.target:

        print(
            f"│ {'Target':<{label_width}} │ "
            f"{app.target:<{value_width}} │"
        )


    if formatted_args:

        print(
            f"│ {'Args':<{label_width}} │ "
            f"{formatted_args:<{value_width}} │"
        )

    print(
        f"│ {'Background':<{label_width}} │ "
        f"{background:<{value_width}} │"
    )


    if app.wrapper is not None:

        print(
            f"│ {'Wrapper':<{label_width}} │ "
            f"{app.wrapper:<{value_width}} │"
        )


    if formatted_wrapper_args:

        print(
            f"│ {'Wrapper Args':<{label_width}} │ "
            f"{formatted_wrapper_args:<{value_width}} │"
        )


    if app.gui is not None:

        print(
            f"│ {'GUI':<{label_width}} │ "
            f"{str(app.gui):<{value_width}} │"
        )


    if app.image is not None:

        print(
            f"│ {'Image':<{label_width}} │ "
            f"{image:<{value_width}} │"
        )

    print(f"╰{line}╯")

    print()