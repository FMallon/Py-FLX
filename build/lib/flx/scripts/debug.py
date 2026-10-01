from flx.scripts.build_command import build_command

def debug(alias: str, extra_args: list[str]) -> None:

    cmd, background = build_command(alias, extra_args)
    
    i: int = 0


    print(f"\n[COMMAND]\t{" ".join(cmd)} ")
    
    print(f"[BACKGROUND]\t{background}")
    
    print("\n")

    for arg in cmd:
        print(f"[arg{i}] {arg}")
        i=i+1
    print("\n")