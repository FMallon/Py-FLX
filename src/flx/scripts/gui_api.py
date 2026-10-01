from flx.scripts.get_app_data import App
from flx.scripts.set_app_data import set_app_data


class Gui_API:

    # Get all app aliases/names - this is a list[str] from display_all_apps.py/get_all_app_names()
    # @staticmethod
    # def get_all_app_names() -> list[str]:
    #     from flx.scripts.display_all_apps import get_all_app_names

    #     return get_all_app_names()

    @staticmethod
    def get_all_gui_app_names() -> list[str]:

        from flx.scripts.display_all_apps import get_all_gui_app_names

        return get_all_gui_app_names()

        



    # Get all populated App objects
    @staticmethod
    def get_apps() -> list[App]:

        apps = Gui_API.get_all_gui_app_names()

        gui_apps = []

        # So if I try/except to catch a bad one, then it should set valid ones, and I will to if the app.gui = true, then append 
        for alias in apps:

            try:
                app = set_app_data(alias, quiet=True)

            except SystemExit:
                continue            
            
            if app.gui:
                gui_apps.append(app)
                

        return gui_apps


    @staticmethod
    def return_valid_apps() -> list[App]:

        apps = Gui_API.get_apps()

        return apps


    @staticmethod
    def pass_apps_info_to_typescript():


        apps = Gui_API.get_apps()


        apps.sort(key=lambda app: app.name)

        return [
            {
                "alias": app.alias,
                "name": app.name,
                "image": app.image
            }
            for app in apps
        ]


    @staticmethod
    def close_window() -> None:

        import webview, threading

        def destroy_window() -> None:
            webview.windows[0].destroy()

        threading.Timer(0.1, destroy_window).start()


    @staticmethod
    def run_app(alias: str) -> None:
        from flx.scripts.run_command import run_command
        print(f"App call requested: {alias}")
        run_command(alias, [], from_gui=True)
        Gui_API.close_window()