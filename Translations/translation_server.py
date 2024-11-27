import csv
import locale
import warnings
import codecs

class Translate:
    def __init__(self, file_encoding: str = "utf-8") -> None:

        self.__messages: dict = {}
        self.__languages: list = []
        self.__default_language: str = "en"
        self.__use_dialects: bool = False

        with codecs.open("Translations/App - Translations.csv", mode='r', encoding=file_encoding) as file:
            reader = csv.reader(file)
            
            languages_definitions: list = next(reader)
            
            for lang in languages_definitions[1:]:
                if lang != "":
                    self.__languages.append(lang)

            for row in reader:
                self.__messages[row[0]] = tuple(row[1:])
        
        self.__current_language: str = self.get_suported_language(self.get_system_language())
        self.__current_language_index: int = self.__languages.index(self.__current_language)

    def get_system_language(self) -> str:
        iso_code: str = None
        try:
            iso_code = locale.locale_alias[locale.getlocale()[0].lower()]
        except Exception:
            warnings.warn("Default system language not found!\nRetuning Default Language...",)
            return self.__default_language
        
        system_language: str = iso_code.split(".")[0]
        if not self.__use_dialects:
            system_language = system_language.split("_")[0]
        
        return system_language

    def get_suported_language(self, language: str) -> str:
        if language in self.__languages:
            return language
        else:
            return self.__default_language

    def tr(self, msg_id:str) -> str:
        message = self.__messages.get(msg_id)
        if isinstance(message, tuple):
            return message[self.__current_language_index]
        else:
            return msg_id
    
    def set_language(self, language: str) -> None:
        if not isinstance(language, str):
            raise ValueError("Please enter the language code as an string value!\nInput: {lang}".format(lang=language))
        if not language in self.__languages:
            raise ValueError("This Language is not defined on the Translation file!")
        self.__current_language = language
        self.__current_language_index = self.__languages.index(self.__current_language)
        

    @property
    def messages(self) -> dict:
        return self.__messages
    
    @property
    def current_language(self) -> str:
        return self.__current_language
    
    @property
    def current_language_index(self) -> int:
        return self.__current_language_index


translate = Translate()
tr = translate.tr

if __name__ == "__main__":
    
    print("Messages found: {msg}".format(msg = translate.messages))
    print("Current Language: {lang} (index: {index})".format(lang=translate.current_language, index=translate.current_language_index))