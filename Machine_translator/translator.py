from translate import Translator


class translation:

    def __init__(self, text):
        self.text = text

    def translate_word(self):
        translator = Translator(to_lang='hi', from_lang='en')
        translation = translator.translate(self.text)
        return translation
