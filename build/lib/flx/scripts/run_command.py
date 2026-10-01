from flx.scripts.build_command import build_command

import subprocess


def run_command(alias: str, extra_args: list[str], from_gui: bool = False) -> int:

    cmd, background = build_command(alias, extra_args)

    print("\n")
    print("┌─ PyFLX ──────────────────────────────────────────────────────┐")
    print("│ ✓ Launch completed successfully.                             │")
    print("│   Application output and errors are handled by the target.   │")
    print("└──────────────────────────────────────────────────────────────┘")
    print()

    try:

        if background or from_gui: #or gui, then when gui uses this, it will always be background

            subprocess.Popen(
                cmd,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )

            return 0

        result = subprocess.run(cmd)
        raise SystemExit(result.returncode)

    except OSError as error:

        print(f"\n[ERROR] Failed to execute command: {cmd[0]}")
        print(f"[ERROR] {error}\n")

        raise SystemExit(16)
