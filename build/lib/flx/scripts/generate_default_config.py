def default_config_template() -> str:

    return """
    
apps = {


    hello = {

        target = "echo",

        args = {

            "Hello",

        },

        background = false,

    }

}
"""

def generate_default_config() -> None:

    from flx.scripts.validation import Validation
    from flx.scripts.paths import CONFIG_DIR, FILE_LUA_CONFIG

    if Validation.directory_exists(CONFIG_DIR) != 0:

        print("\n[INFO] Config Directory doesn't exist, creating now...\n")

        try:
            CONFIG_DIR.mkdir(parents=True, exist_ok=True)

        except OSError as error:
            print(
                f"\n[ERROR] An error occurred trying to create "
                f"the Config Directory {CONFIG_DIR}\n"
            )
            print(f"[ERROR] {error}\n")
            raise SystemExit(20)

    try:
        FILE_LUA_CONFIG.write_text(default_config_template())

    except OSError as error:
        print(
            f"\n[ERROR] An error occurred while generating "
            f"the Default Lua Config {FILE_LUA_CONFIG}\n"
        )
        print(f"[ERROR] {error}\n")
        raise SystemExit(21)

    print("\n[SUCCESS] The Default Config has been generated!\n")