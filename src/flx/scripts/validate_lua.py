from flx.scripts.paths import FILE_LUA_CONFIG, FILE_LUA_QUERY
import subprocess



def verify_lua_config_exists() -> int:

    from flx.scripts.validation import Validation


    if Validation.file_exists(FILE_LUA_CONFIG) != 0:
        print(f"\n[ERROR] Lua Config {FILE_LUA_CONFIG} doesn't exist")
        print("\tYou can generate a default config with --generate-default-config\n")
        raise SystemExit(11)

    return 0


def validate_lua() -> int:


    
    verify_lua_config_exists()

    try:
        output = subprocess.run(
            [
                "lua",
                str(FILE_LUA_QUERY),
                "validate_lua",
                str(FILE_LUA_CONFIG)
            ],
            capture_output=True,
            text=True,
            timeout=7
        )

    except subprocess.TimeoutExpired:
        print("\n[ERROR] Lua Validation timed out after 7 seconds!\n")
        print("[INFO] The Config may contain an operation that is not completing.")
        print("       This could be caused by a bad function, blocked file I/O,")
        print("       or an operation waiting for input.\n")

        raise SystemExit(12)


    if output.returncode != 0:

        print("\n[ERROR] There is an error in the Config:\n")
        print(output.stderr)
        raise SystemExit(output.returncode)
    
    return 0



def validate_lua_option() -> int:

    if validate_lua() == 0:
        print("\n[SUCCESS] The Lua Config passed the validation check!\n")
        return 0



def validate_lua_dependency_exists() -> None:

    from flx.scripts.validation import Validation

    if Validation.is_a_command("lua") != 0:

        print("\n[INFO]\tThis Application requires Lua to work, which appears to not be installed on this System!")
        print("\tLua can be installed using your distro's Package Manager!\n")
        raise SystemExit(2)