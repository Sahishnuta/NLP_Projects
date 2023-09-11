from flashtext import KeywordProcessor

class SpanOfKeyExtract:
    def __init__(self, text, add_keyword):
        self.text = text
        self.add_keyword = add_keyword

    def keySpan(self):
        keyword_processor = KeywordProcessor()
        keyword_processor.add_keyword(self.add_keyword)
        keywords_found = keyword_processor.extract_keywords(self.text, span_info=True)
        return keywords_found

span = SpanOfKeyExtract('I left school yesterday at 5 in evening', "school")
words = span.keySpan()
print(words)