from PyDictionary import PyDictionary


class Dict:
    def __init__(self):
        self.dictionary = PyDictionary()

    def lookup(self):
        try:
            fin = ''
            for syn in self.mean:
                fin += syn + " "
            return fin
        except TypeError:
            return "Invalid word"


class Definition(Dict):
    def __init__(self, word):
        super().__init__()
        self.name = "definition"
        self.mean = self.dictionary.meaning(word)
        self.find = self.lookup()

    def lookup(self):
        try:
            fin = ''
            for key in self.mean:
                fin += key + "\n"
                values, i = self.mean[key], 1
                while i <= len(values):
                    fin += "{}. {}\n".format(i, values[i - 1])
                    i += 1
                fin += "\n"
            return fin
        except TypeError:
            return "Invalid word"


class Synonym(Dict):
    def __init__(self, word):
        super().__init__()
        self.name = "synonym"
        self.mean = self.dictionary.synonym(word)
        self.find = self.lookup()


class Antonym(Dict):
    def __init__(self, word):
        super().__init__()
        self.name = "antonym"
        self.mean = self.dictionary.antonym(word)
        self.find = self.lookup()
