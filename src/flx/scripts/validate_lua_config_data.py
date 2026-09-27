from flx.scripts.validation import Validation


# Editor name, wrapper, target

def validate_executable_entries(executable: str) -> int:

    if not executable:
        return 16

    if Validation.is_a_command(executable) == 0:
        return 0

    return 16