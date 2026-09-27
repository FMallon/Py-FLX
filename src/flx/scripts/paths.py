from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "FLX"

FILE_LUA_CONFIG = CONFIG_DIR / "flx.lua"
FILE_LUA_QUERY = Path(__file__).parent / "flx_query.lua"