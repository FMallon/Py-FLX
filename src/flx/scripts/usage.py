def usage() -> int:

    print("\nFLX - App Launcher & Local Bin\n")

    print("Usage:\n")

    print("  flx <arg>")
    print("  flx <arg> <app_name>")
    print("  flx <arg> <app_name> <extra_args...>\n")

    print("General Options:\n")

    print(f"  {'-h, --help':<45} Show usage")

    print("\nConfig Options:\n")

    print(f"  {'--generate-default-config':<45} Generate a default config")
    print(f"  {'-vc, --validate-config':<45} Validate the Lua config")
    print(f"  {'-e, --edit':<45} Edit the config file")
    print(
        f"  {'-ed, --edit-defaults':<45} "
        "Edit the config file with default editor options"
    )

    print("\nDisplay Options:\n")

    print(
        f"  {'-da, --display-all-apps':<45} "
        "Display all apps in the Lua config with their info"
    )

    print(
        f"  {'-d, --display-app <app_name>':<45} "
        "Display information for the specified app"
    )

    print("\nExecution:\n")

    print(
        f"  {'-- <app_name> <optional_extra_args>':<45} "
        "Run the program, command, script or app"
    )

    print("\nDebug Options:\n")

    print(
        f"  {'--debug <app_name> <optional_extra_args>':<45} "
        "Print the args in array format for debugging"
    )

    print("\n")

    return 0