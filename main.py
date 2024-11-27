from Translations.translation_server import translate
from app import App


if __name__ == "__main__":
    # translate.set_language("en")
    # print(translate.tr("settings"))
    
    app = App()
    app.run()