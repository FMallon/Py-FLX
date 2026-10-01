import webview

from flx.scripts.gui_api import Gui_API
from flx.scripts.paths import HTML_INDEX


def gui_run():

    
    webview.create_window(
        "FLX",
        HTML_INDEX.as_uri(),
        js_api=Gui_API(),
        width=600,
        height=400,
    )
    
    webview.start(debug=False)


if __name__ == "__main__":
    gui_run()