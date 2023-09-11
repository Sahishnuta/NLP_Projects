from flashtext import KeywordProcessor

class removeKey:
    def __init__(self, text, keyword_dict, remove_keyword):
        self.text = text
        self.keyword_dict = keyword_dict
        self.remove_keyword = remove_keyword

    def remove(self):
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keywords_from_dict(self.keyword_dict)
        keyword_processor.remove_keywords_from_dict(self.remove_keyword)
        extractedKeyword = keyword_processor.extract_keywords(self.text)
        return extractedKeyword

remove_extract = removeKey("I am a product manager for a java_2e platform", {
     "java": ["java_2e", "java programing"],
     "product management": ["PM", "product manager"]
 } ,{"product management": ["PM"]})

result = remove_extract.remove()
print(result)