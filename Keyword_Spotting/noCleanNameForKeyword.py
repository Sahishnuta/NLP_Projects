from flashtext import KeywordProcessor

class noCleanName:

    def __init__(self, text, add_keyword):
        self.text = text
        self.add_keyword = add_keyword

    def Findkeywords(self):
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keyword(self.add_keyword)
        keywords_found = keyword_processor.extract_keywords(self.text)
        return keywords_found

Extract = noCleanName("In my Childhood, i love to eat apple pie." , "Apple pie")
result = Extract.Findkeywords()
print(result)