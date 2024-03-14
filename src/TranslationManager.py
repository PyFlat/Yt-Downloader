import os

class TranslationManager():
    def __init__(self, directory:str=None):
        self.directory = directory
        languages = []
        for dir in os.listdir(self.directory):
            language, name = self.parse_keystring(open(f"{self.directory}/{dir}", "r", encoding="utf-8").read(),return_name=True)
            languages.append(language)
        print(languages)


    def parse_keystring(self, strings, return_name = False):
        keymap = {}
        name = ""
        for line in strings.split("\n"):
            key=""
            content=""
            space_buffer = ""
            mode="search_key"
            skip_special_key = False
            for c in line:
                if mode=="end":
                    continue
                if mode=="search_key":
                    if c == " ":
                        continue
                    else:
                        mode="load_key"
                if mode =="search_data":
                    if c=='"':
                        mode="read_data"
                    continue
                if mode=="load_key":
                    if c == "=":
                        mode="search_data"
                        continue
                    if c != " ":
                        key += space_buffer
                        space_buffer = ""
                    if c == " ":
                        space_buffer += c
                        continue
                    key += c
                if mode=="read_data":
                    if c =='\\' and not skip_special_key:
                        skip_special_key=True
                        continue
                    if c == '"' and not skip_special_key:
                        mode="end"
                        continue
                    content += c
                    skip_special_key = False
            if key == "NAME" and return_name:
                name = content
            else:
                keymap[key] = content
        if return_name:
            return keymap, name
        return keymap