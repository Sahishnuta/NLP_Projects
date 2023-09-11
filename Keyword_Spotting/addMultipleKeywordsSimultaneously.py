from flashtext import KeywordProcessor

class addMultikeywords:

    def __init__(self, text, keyword_dict):
        self.text = text
        self.keyword_dict = keyword_dict

    def addkey(self):
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keywords_from_dict(self.keyword_dict)
        extractedKeyword = keyword_processor.extract_keywords(self.text)
        return extractedKeyword

adding = addMultikeywords("I am a SD and my speciality is python programming." , {"python": ["python", "python programing"],"senior developer": ["SD", "python developer"]})
result = adding.addkey()
print(result)