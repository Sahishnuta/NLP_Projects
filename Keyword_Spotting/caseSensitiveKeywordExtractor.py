from flashtext import KeywordProcessor

class CaseSensitiveKey:
    def __init__(self, text, add_keyword):
        self.text = text
        self.add_keyword = add_keyword

    def keysense(self):
        keyword_processor = KeywordProcessor(case_sensitive=True)
        keyword_processor.add_keyword(self.add_keyword)
        keywords_found = keyword_processor.extract_keywords(self.text)
        return keywords_found

sense = CaseSensitiveKey("913 deaths because of corona virus in a day in Italy, and China have lost 5 today.", 'Italy')
result = sense.keysense()
print(result)

