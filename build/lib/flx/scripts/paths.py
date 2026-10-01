from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "FLX"

FILE_LUA_CONFIG = CONFIG_DIR / "flx.lua"
FILE_LUA_QUERY = Path(__file__).parent / "flx_query.lua"

SOURCE_FILE = Path(__file__)
SOURCE_DIR = SOURCE_FILE.parent.parent

GUI_DIR = SOURCE_DIR / "gui"

HTML_DIR = GUI_DIR / "HTML"
CSS_DIR = GUI_DIR / "CSS"
TS_DIR = GUI_DIR / "TS"

HTML_INDEX = HTML_DIR / "index.html"