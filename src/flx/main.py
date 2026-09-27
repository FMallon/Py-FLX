#########################################################################################################################
#                                                                                                                       # 
#                                                     FLX                                                               #
#
#   [DESCRIPTION] FLX (Python) is a lightweight App Launcher & Local Bin written in Lua to run Scripts, Commands, Programs and Apps
#
#   [Dependencies]
#       Lua
#       Python
#
#                                                                                                                       
#                                                                                                    [AUTHOR] F. Mallon #
#                                                                                                 COPYRIGHT © F. Mallon #
#########################################################################################################################

####       Exit Codes        ####

# Exit 2  - Error: Unmet dependency
# Exit 3  - Error: Invalid arg
# Exit 4  - Error: Invalid no. of args
#
###########-From flx_query.lua-#############
#
# Exit 5  - Config file does not exist
# Exit 6  - Invalid config file format
# Exit 7  - Application name not found
# Exit 8  - Invalid query
#
###################################################################################################
#
# Exit 11 - Error: Lua Config doesn't exist - From validate_lua.py
# Exit 16 - Error: The target/wrapper is not a valid executable path/command
# Exit 18 - Error: No supported editor found on User's System
# Exit 19 - Error: Failed running the editor to edit the Config File
# Exit 20 - Error: Failure to create Config Directory
# Exit 21 - Error: Failure to Generate Default Config
#
###################################################################################################


import sys


def validate_args_length(operator: str, no_of_args: int) -> None:

    length = len(sys.argv)


    match operator:
        case "-eq":
            if length != no_of_args:
                print("\n[ERROR] Invalid number of args\n")
                raise SystemExit(4)


        case "-ne":
            if length == no_of_args:
                print("\n[ERROR] Invalid number of args\n")
                raise SystemExit(4)


        case "-gt":
            if length <= no_of_args:
                print("\n[ERROR] Invalid number of args\n")
                raise SystemExit(4)


        case "-ge":
            if length < no_of_args:
                print("\n[ERROR] Invalid number of args\n")
                raise SystemExit(4)


        case "-lt":
            if length >= no_of_args:
                print("\n[ERROR] Invalid number of args\n")
                raise SystemExit(4)


        case "-le":
            if length > no_of_args:
                print("\n[ERROR] Invalid number of args\n")
                raise SystemExit(4)


        case _:
            print("\n[ERROR] Invalid comparison operator\n")
            raise SystemExit(3)



def parse_args():

    if len(sys.argv) < 2:

        print("\n[ERROR] No option provided\n")
        raise SystemExit(3)


    match sys.argv[1]:


        # Run Command
        case "--":
            
            from flx.scripts.run_command import run_command

            validate_args_length("-ge", 3)

            alias: str = sys.argv[2]
            extra_args: list[str] = sys.argv[3:]

            run_command(alias, extra_args) 



        case "-e" | "--edit":

            validate_args_length("-eq", 2)

            from flx.scripts.edit_config import edit_config

            edit_config()

        
        case "-ed" | "--edit-defaults":

            validate_args_length("-eq", 2)

            from flx.scripts.edit_config import edit_config_default

            edit_config_default()


        # Display App 
        case "-d" | "--display-app":

            validate_args_length("-eq", 3)
            from flx.scripts.display_app import display_app
            alias = sys.argv[2]

            display_app(alias)

        case "-da" | "--display-all-app":

            validate_args_length("-eq", 2)
            from flx.scripts.display_all_apps import display_all_apps

            display_all_apps()

        

        # Usage
        case "-h" | "--help":

            validate_args_length("-eq", 2)

            from flx.scripts.usage import usage

            usage()
        

        
        # Verify Config
        case "-vc" | "--validate-config":

            validate_args_length("-eq", 2)

            from flx.scripts.validate_lua import validate_lua_option

            validate_lua_option()


        #Generate Default Config
        case "--generate-default-config":

            validate_args_length("-eq", 2)

            from flx.scripts.generate_default_config import generate_default_config

            generate_default_config()
        

        # Debug
        case "--debug":

            from flx.scripts.debug import debug

            validate_args_length("-ge", 3)

            alias: str = sys.argv[2]
            extra_args: list[str] = sys.argv[3:]

            debug(alias, extra_args)



        # Invalid
        case _:

            print("\n[ERROR] Invalid Option\n")
            raise SystemExit(3)



def main() -> None:

    from flx.scripts.validate_lua import validate_lua_dependency_exists
    validate_lua_dependency_exists()
    parse_args()



if __name__ == "__main__":
    main()